# Four October reanalyses: reproducible source pipeline

Recovered original analysis scripts, plus explicitly new retrieval/check wrappers dated October 22, 2026. The frozen website JSON is an output comparator, **never an input to these analyses**. No wet-laboratory result, clinical efficacy, raw-read realignment or exact-genotype rescue is produced.

## From a clean checkout

Use Python **3.12.14** and the pinned versions below. From the repository root:

```bash
python3.12 -m venv .venv-track2
. .venv-track2/bin/activate
python -m pip install -r track2/reproduction/requirements.txt
python track2/reproduction/fetch_inputs.py && python track2/reproduction/run_reanalyses.py
```

Run the fetch to successful completion **before** starting the reanalyses. It retrieves approximately 21 MB from GEO/NCBI, Elsevier and Springer Nature and verifies every input SHA-256. A changed hash is a stop condition requiring source review, not permission to overwrite the expected value. Network failure is not a successful reproduction. Generated files are ignored; the public annotation input and eight-row prediction extract are versioned, with provenance below. `execution_check.json` records the actual interpreter and four artifact comparisons. The expected hashes are checks, not injected measured values.

| Analysis | Actual calculation | Input and per-analysis command (run inside indicated subdirectory) | Expected result; scope |
|---|---|---|---|
| `gse65145` | Parse all six processed tracks; validate coordinate arrays; select by >=99% reciprocal overlap and boundary distance before reading condition ratios | GEO GSE65145 archive, six sample metadata files, archived UCSC hg19 RefSeq response. `python reanalyse_gse65145.py` | 149122 rows per track, 18 locus-overlapping rows, 3 qualifying features; primary Rap/Pro 0.585706364. Normal fibroblast RNA feature, not BUBR1 protein or rescue |
| `nmd` | Recalculate three isoform ratios, screen-wide Z/Fisher and BH calculations; audit spreadsheet formulas | Zhao supplementary tables S1/S2/S4. `python reanalyze.py` | 704 drugs + control. Montelukast ratios 1.3153820850896314, 3.406494677098417, 1.7654686351224798. Published permutation q 0.02115 is reused, **not a rerun of the stochastic permutation procedure** |
| `ptc` | Read complete Supplementary Table 3, select nearest six-base UGA contexts, calculate medians and paired increments | Toledano workbook; archived prediction extract. `python analyze.py --workbook supp_tables.xlsx --predictions prediction_extracts.tsv --outdir results` then `python test_analysis.py` | No exact six-base match; 12 nearest contexts, untreated median 0.1745%, gentamicin 0.1985%, paired increment 0.0165 percentage points. Not a prediction of BUB1B efficacy |
| `checkpoint` | Validate workbook hash/panel labels, extract individual displayed cell measurements and calculate panel-specific medians | Zhang supplementary source data, Sheet1. `python reanalyze.py --input cache/source_data.xlsx --output results.json` | Figure 4B WT 650 min (27 cells), D137R 60 min (39). Representative replicate; cells are not independent biological replicates. No drug or N1002K experiment |

The Python scripts inside the four analysis subdirectories are recovered unchanged from the original October packages. `original_script_hashes.json` identifies their bytes. `fetch_inputs.py` and `run_reanalyses.py` are new orchestration only. Python 3.12.14, pandas 2.2.3, numpy 2.3.5, scipy 1.17.0 and openpyxl 3.1.5 were used. The final October 22 check created a brand-new isolated virtual environment, installed the pinned dependencies, started with no downloaded inputs or generated analysis outputs, fetched all 12 remote inputs sequentially, and reran all four analyses. All four checked artifacts matched their archived SHA-256 values; `execution_check.json` records the successful run at 18:59:19 UTC and confirms the isolated virtual environment. This is a successful clean computational reproduction under the stated input boundaries, not biological validation.

## Provenance, exclusions and remaining reproduction limits

- **GSE65145:** [GEO](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE65145); [Gillespie primary paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC4915505/). Only public normal-cell processed tracks are downloaded. The UCSC response includes changing `downloadTime` metadata, so the archived October 10 public annotation is versioned to preserve exact bytes. This is an annotation input, not an analysis result. The 149122-versus-149135 row discrepancy remains unresolved.
- **NMD:** [Zhao primary paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC8718828/) and publisher workbooks linked in `input_manifest.json`. The original full article HTML is intentionally omitted: it is unused in calculations. Therefore the new `summary.json` input inventory omits that HTML, while all calculated CSV artifacts remain comparable. Individual Ct replicates are unavailable, so no replicate uncertainty or original permutation-process replication is claimed.
- **PTC:** [Toledano primary paper](https://www.nature.com/articles/s41588-024-01878-5) and [RTDetective dataset](https://doi.org/10.6084/m9.figshare.23708901), observed version 2, CC BY 4.0. `prediction_extracts.tsv` is the unchanged eight-row public coordinate extract from the original package. Reproduction of the **measured nearest-context chart** comes from the freshly downloaded whole workbook. Whole-genome Figshare prediction-file extraction and upstream transcript-to-genome mapping are **not rerun** here; the bundled prediction rows are not independent new evidence and are not necessary for interpreting the measured chart.
- **Checkpoint:** [Zhang primary paper/source data](https://www.nature.com/articles/s42003-026-10384-9); source SHA-256 and cell row/column references are emitted by the original script. Version-only output changes must be distinguished from numerical changes rather than forcing a hash match.
- Source workbooks are fetched directly, not silently reconstructed from chart summaries. No private genomic inputs, credentials, participant records, or complete papers are redistributed in this folder. Existing historical report data are unchanged.

## Reading the check

An archived `execution_check.json` describes a past run, not an assurance that a future network fetch will succeed. Rerun both commands above. Four matching artifacts demonstrate deterministic computation from these public processed sources; they do not validate a treatment, reproduce the authors' biological experiments, or fill the exact-genotype rescue/exposure/eligibility gaps.
