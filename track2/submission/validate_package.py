"""Audit local submission artifacts without asserting human-dependent readiness.

This is a packaging/consistency check, not biological or privacy certification.
It never opens private patient directories and does not submit or publish files.
"""
from pathlib import Path
import csv
import datetime
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    'README.md', 'requirements.txt', 'LICENSE.md',
    'report/ivillafuerte_track2_report.md', 'drugs/candidate_assessment.md',
    'experiments/development_plan.md', 'submission/methods.md',
    'submission/readiness.md', 'submission/pitch_script.md',
    'structure/results/metrics.json', 'structure/results/residue_summary.tsv',
    'structure/results/rotamer_summary.tsv', 'evidence/rules_manifest.json',
]


def main():
    errors = [f'Missing: {p}' for p in REQUIRED if not (ROOT / p).is_file()]
    files = [p for p in ROOT.rglob('*') if p.is_file()
             and '__pycache__' not in p.parts and p.suffix not in {'.zip', '.pyc'}
             and p.name not in {'domain_750_1045.pdb', 'lys_rotamers.json', 'lys_rotamers_jitter.json'}]
    for path in files:
        if re.search(r'\.(vcf|bcf|bam|bai|cram|crai|fastq|fq|tbi|csi)(\.(gz|bgz))?($|\.)', path.name, re.I):
            errors.append(f'Genomic file type must not be packaged: {path.relative_to(ROOT)}')
        if path.suffix == '.md':
            text = path.read_text()
            for target in re.findall(r'\]\(([^)]+)\)', text):
                if '://' in target or target.startswith(('#', 'mailto:')):
                    continue
                if not (path.parent / target.split('#')[0]).exists():
                    errors.append(f'Broken local link in {path.relative_to(ROOT)}: {target}')
    metrics = json.loads((ROOT / 'structure/results/metrics.json').read_text())
    with (ROOT / 'structure/results/rotamer_summary.tsv').open() as f:
        rows = list(csv.DictReader(f, delimiter='\t'))
    jitter = [x for x in rows if x['set'] == 'jitter']
    passing = sum(int(x['clashes_overlap_gt_0_4A']) == 0 for x in jitter)
    if len(jitter) != metrics['rotamer_jitter_summary']['count']:
        errors.append('Rotamer table count differs from metrics.')
    if passing != metrics['rotamer_jitter_summary']['zero_clashes_gt_0_4A']:
        errors.append('Rotamer clash count differs from metrics.')
    if metrics['transcript']['variants']['737']['mut_codon_DNA'] != 'TGA':
        errors.append('Unexpected L737* codon.')
    if metrics['residues']['1002']['residue'] != 'ASN':
        errors.append('Unexpected WT residue at position 1002.')
    pitch = (ROOT / 'submission/pitch_script.md').read_text().split('<!-- SPOKEN_START -->')[1].split('<!-- SPOKEN_END -->')[0]
    words = len(pitch.split())
    methods = (ROOT / 'submission/methods.md').read_text()
    abstract = methods.split('## Method abstract')[1].split('\n', 1)[1]
    abstract_words = len(abstract.split())
    if abstract_words > 500:
        errors.append('Methods abstract exceeds 500 words.')
    for row in range(7, 18):
        if f'row {row}' not in methods:
            errors.append(f'Missing official methods row {row}.')
    if not 300 <= words <= 450:
        errors.append('Pitch outside planned 300–450 spoken-word range; review timing.')
    output = {
        'checked_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'technical_checks_pass': not errors,
        'submission_ready': False,
        'errors': errors,
        'pitch_spoken_words': words,
        'words_per_minute_for_three_minutes': round(words / 3, 1),
        'actual_video_duration_verified': False,
        'methods_abstract_words': abstract_words,
        'rotamer_table_rows_jitter': len(jitter),
        'rotamers_below_clash_criterion': passing,
        'limitations': 'Local links and file-type/consistency checks are not exhaustive privacy, scientific or account certification.',
        'open_items': ['Participant-confirmed AI provider/tier/settings',
                       'Final submission identity and live quota',
                       'Reviewed repository publication',
                       'Recorded three-minute video and accessible URL',
                       'Final participant review and actual upload'],
        'file_sha256': {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                        for p in sorted(files) if p.name != 'validation.json'},
    }
    (ROOT / 'submission/validation.json').write_text(json.dumps(output, indent=2) + '\n')
    print(json.dumps({k: v for k, v in output.items() if k != 'file_sha256'}, indent=2))
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
