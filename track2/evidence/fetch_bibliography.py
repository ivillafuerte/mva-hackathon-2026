"""Refresh PMID metadata cited in English Markdown documentation.

Uses only public bibliographic identifiers, not patient data or full abstracts.
"""
import datetime
import json
from pathlib import Path
import re
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]


def main():
    identifiers = set()
    for path in ROOT.rglob('*.md'):
        identifiers.update(re.findall(r'PMID\s*:?\s*([0-9]{7,8})', path.read_text()))
    if not identifiers:
        raise ValueError('No PMIDs found.')
    query = 'SRC:MED AND (' + ' OR '.join('EXT_ID:' + x for x in sorted(identifiers)) + ')'
    url = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?' + urllib.parse.urlencode({
        'query': query, 'format': 'json', 'resultType': 'core', 'pageSize': 100})
    with urllib.request.urlopen(url, timeout=40) as response:
        data = json.load(response)
    rows = [{key: row.get(key) for key in ['id', 'doi', 'pmcid', 'title',
             'authorString', 'firstPublicationDate']} for row in data['resultList']['result']]
    missing = sorted(identifiers - {row['id'] for row in rows})
    output = {'retrieved_date': datetime.datetime.now(datetime.timezone.utc).date().isoformat(),
              'query_url': url, 'records': rows, 'missing_pmids': missing,
              'scope': 'Metadata check only; does not certify mechanistic claims.'}
    (ROOT / 'evidence/bibliography.json').write_text(json.dumps(output, indent=2) + '\n')
    print(f'{len(rows)} references matched; missing: {missing}')
    return 1 if missing else 0


if __name__ == '__main__':
    raise SystemExit(main())
