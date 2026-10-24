"""Recalculate published BUBR1 control data. No biological simulation."""
import argparse
import hashlib
import json
import platform
import statistics
import urllib.request
import warnings
from pathlib import Path
import openpyxl

URL = 'https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs42003-026-10384-9/MediaObjects/42003_2026_10384_MOESM5_ESM.xlsx'
SHA256 = 'd793bc309981fefad4a7bc5a8de852054563b0c29b1212d0221519674f9f5f90'
# One-based columns; each comparison uses the WT from its own figure panel.
PANELS = [('Figure 3D', 22, 23, 25, 'V200A/L205A'),
          ('Figure 4B', 27, 28, 30, 'D137R'),
          ('Figure 4F', 46, 47, 49, 'C132E')]

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--input', type=Path, default=Path('cache/source_data.xlsx'))
    p.add_argument('--output', type=Path, default=Path('results.json'))
    p.add_argument('--fetch', action='store_true')
    a = p.parse_args()
    if a.fetch and not a.input.exists():
        a.input.parent.mkdir(parents=True, exist_ok=True)
        with urllib.request.urlopen(URL, timeout=60) as response:
            a.input.write_bytes(response.read())
    actual = hashlib.sha256(a.input.read_bytes()).hexdigest()
    if actual != SHA256:
        raise ValueError('Source hash differs: review the new source before analysis')
    # The unsupported extension warning concerns a read-only load; input is never saved.
    with warnings.catch_warnings():
        warnings.filterwarnings('ignore', message='Unknown extension is not supported.*')
        w = openpyxl.load_workbook(a.input, read_only=True, data_only=True)
        rows = list(w['Sheet1'].values)
        w.close()
    output = []
    for figure, marker, wtcol, mutantcol, mutant in PANELS:
        assert rows[0][marker - 1] == figure
        assert rows[0][wtcol - 1] == 'Wild type'
        assert rows[0][mutantcol - 1] == mutant
        for col, label in [(wtcol, 'Wild type'), (mutantcol, mutant)]:
            cells = [(r+1, row[col-1]) for r, row in enumerate(rows[1:], 1)
                     if row[col-1] is not None]
            if not cells or any(type(v) not in (int, float) or v < 0 for _,v in cells):
                raise ValueError(f'Unexpected measurements: {figure} {label}')
            values = [v for _,v in cells]
            output.append({'figure':figure,'condition':label,'n_cells':len(values),
                           'median_NEBD_to_exit_min':statistics.median(values),
                           'source_column_1based':col,
                           'source_rows_1based':[r for r,_ in cells]})
    result = {'analysis':'Published single-cell mitotic-arrest duration reanalysis',
              'classification':'COMPUTATIONAL reanalysis of DIRECT-BUBR1 experiments',
              'source_url':URL,'source_sha256':actual,
              'software':{'python':platform.python_version(),'openpyxl':openpyxl.__version__},
              'random_seed':None,'random_seed_reason':'Deterministic extraction and medians',
              'biological_replicate_unit':'Representative replicate per displayed panel; cell counts are not independent biological replicates',
              'drug_treatment_rescue_tested':False,'N1002K_tested':False,
              'activation_rate_measured':False,
              'comparisons':output}
    a.output.write_text(json.dumps(result,indent=2)+'\n')
    for r in output:print(r['figure'],r['condition'],r['n_cells'],round(r['median_NEBD_to_exit_min'],2))

if __name__ == '__main__':main()
