#!/usr/bin/env python3
"""Download only public references pinned in the manifest; never upload data."""
import argparse
import hashlib
import json
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ap=argparse.ArgumentParser();ap.add_argument('--cache',type=Path,default=Path('data/reference/track2'));args=ap.parse_args()
manifest=Path(__file__).parents[1]/'evidence/public_references.json'
args.cache.mkdir(parents=True,exist_ok=True)
def fetch(item):
    path=args.cache/item['filename']
    if path.exists() and hashlib.sha256(path.read_bytes()).hexdigest()==item['sha256']:
        return f'Cache OK: {path.name}'
    with urllib.request.urlopen(item['url'],timeout=45) as response: body=response.read()
    observed=hashlib.sha256(body).hexdigest()
    if observed!=item['sha256']:
        raise RuntimeError(f'{path.name}: reference changed; expected {item["sha256"]}, received {observed}. The validated version is not overwritten.')
    path.write_bytes(body)
    return f'Verified download: {path.name}'
with ThreadPoolExecutor(max_workers=4) as pool:
    for future in as_completed([pool.submit(fetch,item) for item in json.loads(manifest.read_text())['files']]):
        print(future.result())
