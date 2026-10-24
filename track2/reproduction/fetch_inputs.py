"""New 2026-10-22 retrieval wrapper; original scientific analyses are unchanged.

Downloads only public source inputs; refuses changed bytes rather than silently
substituting them. No credentials, private genomic files, or result snapshots.
"""
import hashlib
import json
from pathlib import Path
import urllib.request

ROOT = Path(__file__).resolve().parent
manifest = json.loads((ROOT / 'input_manifest.json').read_text())
for item in manifest['inputs']:
    dest = ROOT / item['path']
    if not dest.resolve().is_relative_to(ROOT):
        raise ValueError('Input destination escapes analysis directory')
    if dest.exists():
        data = dest.read_bytes()
    else:
        request = urllib.request.Request(item['url'], headers={'User-Agent': 'Track2-reproduction-audit/2026-10-22'})
        with urllib.request.urlopen(request, timeout=90) as response:
            data = response.read()
    if hashlib.sha256(data).hexdigest() != item['sha256']:
        raise ValueError(f"Source hash changed for {item['path']}; review source, do not alter expected data")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(data)
    print('VERIFIED', item['path'], len(data), flush=True)
for reference in manifest['bundled_public_references']:
    if hashlib.sha256((ROOT / reference['path']).read_bytes()).hexdigest() != reference['sha256']:
        raise ValueError(f"Bundled source hash differs: {reference['path']}")
    print('VERIFIED', reference['path'])
