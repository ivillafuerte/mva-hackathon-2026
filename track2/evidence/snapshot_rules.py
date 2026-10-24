"""Record hashes and extract fields from public official challenge materials.

Fetch only public Space code/template files, never the gated patient dataset.
Use --cache to reuse a downloaded snapshot; --refresh fetches a new live version.
"""
import argparse
import concurrent.futures
import datetime
import hashlib
import json
from pathlib import Path
import urllib.request
import xml.etree.ElementTree as ET
import zipfile

PATHS = ['config.py', 'tabs/rules.py', 'tabs/faq.py', 'tabs/about.py',
         'tabs/submit_track2.py', 'static/templates/methods_description_form.xlsx']
BASE = 'https://huggingface.co/spaces/SageBio/rare-disease-real-kid-mva-hackathon-2026/resolve/main/'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cache', type=Path, required=True)
    parser.add_argument('--refresh', action='store_true')
    parser.add_argument('--acquired-on', help='Operator-recorded acquisition date for a cached snapshot (YYYY-MM-DD).')
    args = parser.parse_args()
    args.cache.mkdir(parents=True, exist_ok=True)

    def fetch(path):
        local = args.cache / Path(path).name
        if args.refresh or not local.exists():
            with urllib.request.urlopen(BASE + path, timeout=40) as response:
                local.write_bytes(response.read())
        data = local.read_bytes()
        return {'source_url': BASE + path, 'filename': local.name,
                'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        sources = list(pool.map(fetch, PATHS))
    ns = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
    with zipfile.ZipFile(args.cache / 'methods_description_form.xlsx') as archive:
        strings = [''.join(node.itertext()) for node in ET.fromstring(
            archive.read('xl/sharedStrings.xml')).findall('s:si', ns)] if 'xl/sharedStrings.xml' in archive.namelist() else []
        sheet = ET.fromstring(archive.read('xl/worksheets/sheet2.xml'))
        fields = {}
        for cell in sheet.findall('.//s:c', ns):
            address = cell.get('r')
            value = cell.find('s:v', ns)
            inline = cell.find('s:is', ns)
            text = strings[int(value.text)] if cell.get('t') == 's' and value is not None else ''.join(inline.itertext()) if inline is not None else value.text if value is not None else ''
            if address.startswith('A') and text:
                fields[address] = text
    result = {'recorded_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'source_mode': 'live refresh' if args.refresh else 'existing downloaded snapshot; acquisition date recorded by operator',
              'operator_acquisition_date': args.acquired_on if not args.refresh else None,
              'sources': sources, 'track2_template_fields': fields,
              'community_sources': [BASE.replace('/resolve/main/', '/discussions/2'),
                                    BASE.replace('/resolve/main/', '/discussions/5')]}
    out = Path(__file__).with_name('rules_manifest.json')
    out.write_text(json.dumps(result, indent=2) + '\n')
    print(f'Recorded {len(sources)} sources and {len(fields)} template fields: {out}')


if __name__ == '__main__':
    main()
