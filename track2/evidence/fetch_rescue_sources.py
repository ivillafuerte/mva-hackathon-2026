"""Refresh public bibliographic metadata; never reads patient files.

Run: python track2/evidence/fetch_rescue_sources.py
Requires only the Python standard library. No abstracts are redistributed.
"""
import concurrent.futures
import datetime
import json
from pathlib import Path
import urllib.parse
import urllib.request

PMIDS = ['20516114', '23242215', '33523869', '36844366',
         '39445691', '36351280', '37118121']


def fetch(pmid):
    query = urllib.parse.urlencode({
        'query': f'EXT_ID:{pmid} AND SRC:MED', 'format': 'json',
        'resultType': 'core', 'pageSize': 1,
    })
    url = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?' + query
    with urllib.request.urlopen(url, timeout=40) as response:
        data = json.load(response)
    rows = data['resultList']['result']
    if len(rows) != 1 or rows[0]['id'] != pmid:
        raise ValueError(f'Unexpected bibliographic match: {pmid}')
    row = rows[0]
    return {key: row.get(key) for key in
            ['id', 'pmcid', 'doi', 'title', 'authorString', 'firstPublicationDate']} | {
                'source_url': url, 'pubmed_url': f'https://pubmed.ncbi.nlm.nih.gov/{pmid}/'}


if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        records = list(pool.map(fetch, PMIDS))
    output = Path(__file__).with_name('rescue_sources.json')
    output.write_text(json.dumps({
        'retrieved_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'scope': 'Public bibliography; metadata matching does not validate efficacy.',
        'records': records,
    }, ensure_ascii=False, indent=2) + '\n')
    print(f'Validated {len(records)} PMID matches; wrote {output}')
