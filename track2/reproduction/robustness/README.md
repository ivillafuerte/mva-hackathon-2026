# Bounded exploratory robustness audit — 24 October 2026

**Result:** the stated directional conclusions survive the specified finite-set sensitivity checks. This does **not** establish biological validation or justify promoting a treatment. The important wording correction is **12 nearest measured variant rows spanning 8 distinct six-base contexts**, not 12 independent contexts.

This is an additive **post-hoc exploratory analysis**, designed after the original results were known. [Protocol](protocol.json) was frozen before these new calculations; [amendment 01](protocol_amendment_01.json) was recorded before execution after design review. The amendment omitted a potentially misleading shared-denominator genome-wide correlation and added a separate equal-context-weighted PTC summary. This is not a prospective preregistration. No competitor code/data, private patient-genomic files or new experiments were used.

## What is stable, what changes, what remains insufficient

| Check | Actual result | Bounded interpretation |
|---|---|---|
| PTC paired median, full nearest set | +0.0165 percentage points (pp); 11 positive and 1 negative individual paired differences | Small source-table median; not universal response or BUB1B efficacy |
| Leave one measured variant row out | 12 deletions; paired-median range +0.014–+0.019 pp | Median stays positive within this finite row set |
| Leave one whole six-base context group out | 8 deletions, 9–11 rows retained; range +0.0135–+0.0285 pp | Direction retained after removing duplicate-context groups; magnitude changes |
| Equal-context-weighted summary | Median of 8 within-context median paired differences = +0.0160 pp | Separate estimand, not an independent replication |
| Marginal versus paired median | Gentamicin median 0.1985%; untreated median 0.1745%; difference of medians +0.0240 pp | +0.0240 is **not** the median paired increment +0.0165 |
| GSE feature-choice grid | 95%, 97.5%, 99% and 99.5% reciprocal overlap all select the same 3 near-duplicate features; Rap/Pro 0.585706364–0.585706426 | Technical selection stability, not independent biological confirmation |
| Exact-span threshold | 100% reciprocal overlap: **no eligible feature** | Insufficient, not zero expression; no silent fallback |
| GSE arithmetic versus geometric condition means | Primary Rap/Pro 0.585706 versus 0.584998 | Direction unchanged; no pseudocount |
| GSE leave one sample out | Primary Rap/Pro 0.542241–0.629171 | All remain below 1; deleting a sample leaves 1 in one condition and 2 in each other condition |
| GSE all cross-condition sample ratios | Four Rap/Pro ratios: 0.513663–0.666239 | Unpaired sample-dependence diagnostic, **not four biological replicates** |
| Quiescence comparison | Primary Qui/Pro 0.186191; Rap/Qui 3.145731 | Both conditions are lower than proliferative control, with different magnitudes; not cell-cycle-matched and not a causal adjustment |

**All deletion and cross-sample ranges are diagnostic ranges, not confidence intervals.** Analyses are deterministic and exhaustive; there is no random seed to vary, no bootstrap and no new p-value. The shuffle seed in one test checks order-invariance only.

### Interpretation

- **Stable:** no row/context deletion reverses the PTC paired-median sign; all specified eligible GSE feature/estimator/sample diagnostics retain Rap/Pro below 1. The existing candidate decisions are unchanged: no new promotion; gentamicin/mefloquine stays a low-priority experimental branch, and this GSE evidence does not support an RNA-abundance-increase rationale for sirolimus.
- **Changes:** clarify the 12-row/8-context denominator; expose context multiplicities, the one negative individual PTC difference (`RP1_S542X`, −0.003 pp), and the effect of aggregation/deletion on magnitude. Do not conflate differences of marginal medians with median paired differences.
- **Insufficient:** no exact six-base context measurement; no exact-span GSE feature; no direct BUBR1 protein, exact-genotype functional rescue, clinical efficacy or causal proliferation-adjusted drug effect. Serum-restricted quiescence is not a cell-cycle-matched control. The cell-state contrasts flag interpretive ambiguity but cannot separate treatment effects from proliferation effects.

GSE remains **n=2 samples per condition in one normal fibroblast cell line**. The 3 overlapping features, 4 ratios and 6 deletions do not increase n. Near-identical feature ratios are redundant locus views. The original 149122-versus-149135 row discrepancy remains unresolved. Processed, unstranded genomic-span RPKM features are not validated mature isoform estimates.

## Reproduce from the repository root

Use the pinned original Python/dependency setup in [the parent README](../README.md). First fetch and hash-verify the public source inputs, then run the new analysis and tests:

```bash
python track2/reproduction/fetch_inputs.py
python track2/reproduction/robustness/run_sensitivity.py
python track2/reproduction/robustness/test_sensitivity.py

# Optional: independent second output directory; every result file should match.
python track2/reproduction/robustness/run_sensitivity.py --outdir /tmp/mva-robustness-rerun
diff -rq track2/reproduction/robustness/results /tmp/mva-robustness-rerun
```

`--input-root` can point to another intact `track2/reproduction` directory. A source-hash mismatch, modified original scientific script, malformed track or coordinate inconsistency is a stop condition, not permission to substitute input data. Censored/missing nearest PTC observations are not treated as exact values. Empty feature sets and nonpositive geometric-mean inputs are marked insufficient.

## Evidence and output files

- [Full machine-readable result](results/sensitivity_results.json): source inventory, hashes, exact Excel row IDs, contexts, source values, every deletion, feature coordinates, contrasts and `stable` / `changes` / `insufficient` interpretation.
- [PTC measured rows](results/ptc_nearest_measured_rows.csv), [row deletions](results/ptc_leave_one_variant_row_out.csv), [context-group deletions](results/ptc_leave_one_context_group_out.csv).
- [GSE threshold grid](results/gse_feature_thresholds.csv), [estimators](results/gse_feature_estimators.csv), [sample deletions](results/gse_leave_one_sample_out.csv), [all 18 locus overlaps, annotation audit only](results/gse_locus_overlap_audit.csv).
- [Result SHA-256 inventory](results/artifact_hashes.json), [11-test run log](verification/test_sensitivity.log), [separate four-analysis replay check](verification/deterministic_replay_check_20261024.json).

The complete PTC worksheet has **5837 populated source rows plus 5837 blank formatted rows**; 2724 populated valid UGA rows enter six-base-distance selection. The nearest subset has 12 fully observed, uncensored paired measurements, 8 unique contexts and Hamming distance 1. Its exact six-base match count is 0. Group multiplicities are emitted, rather than assuming independent contexts.

### Execution provenance and preserved historical artifacts

The 24 October run verified all 14 source/reference SHA-256 values against the unchanged original manifest. It used **previously downloaded public cached bytes**, not a fresh network download, and the existing Python 3.12.14 environment with the pinned packages, **not a newly created isolated environment**. The four original analyses were rerun in a separate directory; all four historical comparator hashes matched. The new sensitivity was run twice into separate directories; all nine output files were byte-identical. Eleven unit/integration tests and Python compilation passed.

The original four scientific scripts, original input/script manifests, historical `execution_check.json` and original submission report remain byte-identical. Their deterministic replay is separate from this new sensitivity analysis. NMD published permutation values are still reused rather than rerun; the checkpoint's displayed cells still belong to one representative replicate, not independent biological replicates. These checks do not close the exact-genotype, functional, exposure or eligibility gaps.

Public source attribution remains in [input_manifest.json](../input_manifest.json): [Toledano et al.](https://www.nature.com/articles/s41588-024-01878-5), [GSE65145](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE65145), [Gillespie et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC4915505/), and archived UCSC hg19 RefSeq annotation. No full source workbook or whole article is added to the repository by this audit.
