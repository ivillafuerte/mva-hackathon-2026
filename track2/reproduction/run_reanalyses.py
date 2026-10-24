"""New 2026-10-22 runner/checker. Does not reconstruct or change original analyses."""
from pathlib import Path
import datetime
import hashlib
import json
import platform
import subprocess
import sys
from importlib.metadata import version

ROOT = Path(__file__).resolve().parent
manifest = json.loads((ROOT / 'input_manifest.json').read_text())
for item in manifest['inputs'] + manifest['bundled_public_references']:
    path = ROOT / item['path']
    if not path.is_file():
        raise FileNotFoundError(f"Missing {item['path']}; finish fetch_inputs.py successfully before running analyses")
    if hashlib.sha256(path.read_bytes()).hexdigest() != item['sha256']:
        raise ValueError(f"Input hash differs before execution: {item['path']}")
original_hashes = json.loads((ROOT / 'original_script_hashes.json').read_text())
for path, expected in original_hashes.items():
    if hashlib.sha256((ROOT / path).read_bytes()).hexdigest() != expected:
        raise ValueError(f'Original scientific script differs: {path}')
jobs = [
    ('gse65145', ['reanalyse_gse65145.py'], 'gse65145_bub1b_results.json', 'e71199b4f23c6315f02febfd18aac8b9bcd7e7f8bb05a7a7b624ad874d54d3b6'),
    ('nmd', ['reanalyze.py'], 'results/selected_candidates.csv', 'ad7fa784e6caf2f126c9730e4edaf7dc75f0ea2ad54208661de75555ede6ab9c'),
    ('ptc', ['analyze.py', '--workbook', 'supp_tables.xlsx', '--predictions', 'prediction_extracts.tsv', '--outdir', 'results'], 'results/results.json', '8d1f7ca32b05f9e85cedc5d025ea04efee60b581ae4effea8fd389e6f4afbcb9'),
    ('checkpoint', ['reanalyze.py', '--input', 'cache/source_data.xlsx', '--output', 'results.json'], 'results.json', 'd6be3833115ac368fffe185dfea0e42439e4c80e723b88c626ecb9b874073e6c'),
]
records = []
for folder, args, artifact, expected in jobs:
    subprocess.run([sys.executable, *args], cwd=ROOT / folder, check=True)
    actual = hashlib.sha256((ROOT / folder / artifact).read_bytes()).hexdigest()
    records.append({'analysis': folder, 'artifact': folder+'/'+artifact, 'sha256': actual, 'matches_archived_result': actual == expected})
    if actual != expected:
        raise RuntimeError(f'{folder}: output differs; inspect numerical and software differences, do not change source to force a match')
subprocess.run([sys.executable, 'test_analysis.py'], cwd=ROOT / 'ptc', check=True)
result = {'checked_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'python': platform.python_version(), 'dependencies': {name: version(name) for name in ['pandas', 'numpy', 'scipy', 'openpyxl']},
          'isolated_virtual_environment': sys.prefix != sys.base_prefix, 'records': records,
          'scope': 'Original deterministic reanalyses from processed public source data; not new biological validation or reanalysis from sequencing reads.',
          'limitations': ['NMD original stochastic permutation procedure is not rerun; published p values are reused.',
                         'PTC prediction_extracts.tsv is archived public Figshare-derived input; full prediction-file extraction is not rerun.',
                         'UCSC annotation input preserves its original retrieval timestamp; it is not a fresh live annotation response.',
                         'Checkpoint exact-byte result assumes pinned Python/library versions; inspect version-only differences separately.']}
(ROOT / 'execution_check.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
