# Track 2: BUB1B Virtual Lab — Evidence-Guided Drug Repurposing

The dated October 24 report is the latest prepared update. The original Submission 1 report stays frozen. The October 17 scientific snapshot is unchanged; separately identified sensitivity diagnostics add no wet-lab experiment or exact-genotype rescue. Amlexanox remains eligibility HOLD; montelukast requires useful exact-truncation function; gentamicin + mefloquine remains experimental. Prior product and Figure 6 source checks are already public in main commit `0cb71c4946fd71d0c0b5b1589026a2ed9e8a33b6`. Repository publication is not official resubmission.

## Read the proposal

- [Latest prepared dated report](report/ivillafuerte_track2_report_revision_20261024.md)
- [One-page candidate decision matrix](drugs/candidate_decision_matrix_20261024.md)
- [Frozen original Submission 1 report](report/ivillafuerte_track2_report.md)
- [Earlier public documentary revision](report/ivillafuerte_track2_report_postsubmission_proposed.md)
- [Product/formulation and experimental-to-human exposure fiche](drugs/product_exposure_fiche.md)
- [Historical drug assessment and current eligibility cautions](drugs/candidate_assessment.md)
- [Experimental development plan](experiments/development_plan.md)
- [Official methods-template answers](submission/methods.md)
- [Requirements and open submission items](submission/readiness.md)
- [Pitch video on YouTube — 2:57](https://youtu.be/u527j7tO0OA)
- [Current BUB1B web laboratory](https://www.stackfire.com/labs/biolab/mvabub1b)
- [BioLab overview](https://www.stackfire.com/labs/biolab)
- [Pitch script (planning record)](submission/pitch_script.md)

The dated revised report is the latest prepared scientific narrative, not proof of a replacement upload. The September sirolimus-first ranking is superseded, not erased from historical notes. The October snapshot has 4 reanalyses, 6 evidence audits, 1 synthetic software test and 4 quantitative charts. A frozen [public snapshot](evidence/mva-results-2026-10-17.json) preserves record-level sources and limitations. Earlier notes below are retained as English technical records; historical prioritization is not the final drug decision.

- [Structural and mechanism audit](report/research_status_audit_2026-09-08.md)
- [Anakinra hypothesis record](report/alternative_anakinra_2026-09-08.md)
- [Temporal rescue concept](report/functional_rescue_windows_2026-09-09.md)

## Reproduce the September public allele computations

From the repository root, use Python 3.12 and a C compiler if FreeSASA has no compatible wheel:

```bash
python -m venv .venv-track2
source .venv-track2/bin/activate
python -m pip install -r track2/requirements.txt
python track2/structure/fetch_public_references.py --cache data/reference/track2
python track2/structure/analyze_bubr1.py --cache data/reference/track2 --out track2/structure/results
python track2/structure/conservation_panel.py --cache data/reference/track2 --out track2/structure/results
python track2/evidence/fetch_rescue_sources.py
python track2/evidence/fetch_bibliography.py
python track2/evidence/snapshot_rules.py --cache data/reference/track2/rules --refresh
python track2/submission/validate_package.py
```

On Linux, if FreeSASA compilation selects an unavailable compiler, use `CC=gcc python -m pip install -r track2/requirements.txt` with GCC installed.

The reference fetcher checks audited SHA-256 hashes and fails if a live input has changed; do not silently overwrite audited references. Review and document a new snapshot if that occurs. Large public model files remain outside Git. No private VCF is needed.

`metrics.json` contains sequence/transcript checks, model confidence, SASA, contacts, geometry, software and input hashes. Compact residue/rotamer tables and the conservation panel are included. Full exploratory geometry is regenerated locally. The rotamer search does not model energies or probabilities; hydrogen bonds are candidates and secondary structure is a Phi/Psi description, not a DSSP result. Synthetic helix self-tests are not biological results.

The package validation command checks local links, required artifacts, metric/table agreement, pitch length, template coverage and prohibited genomic file types. Passing technical checks does not close human-dependent submission items. Its September-generated output is historical, not evidence that the October package is complete. The current [readiness checklist](submission/readiness.md) controls outstanding publication, account and video checks.

## Scope and license

Repurposing candidates are evaluated as conditional hypotheses; current product-level eligibility, especially amlexanox, is not inferred from historical approval. WT BUBR1 is a proposed experimental reference; prenatal mRNA is a future extension outside the nominated repurposed intervention. No universal therapeutic threshold, exact-genotype pharmacological rescue or cancer cure is claimed. Published model-specific drug responses are not patient or exact-genotype results. See [license](LICENSE.md) and the main report's required acknowledgment. Use only permitted findings and public references; do not add patient-scale genomic files or logs to Git.

## Final reproduction audit

The September 10 repeat execution reproduced `metrics.json`, `residue_summary.tsv` and `rotamer_summary.tsv` exactly. The initial native environment failed; a clean dependency installation and recovery of a truncated public PAE cache file resolved the repeat execution. All public reference hashes matched the audited manifest before analysis. This is computational reproducibility, not biological validation. See [reproduction audit](submission/reproduction_check.json).

## Reproduce the four October reanalyses

Use the [clean-checkout guide](reproduction/README.md), recovered original scripts, pinned dependencies and new explicit retrieval/check wrappers. Four deterministic output artifacts were reproduced from public processed inputs; this does not rerun biological experiments, sequencing-read alignment, the NMD paper's original stochastic permutation test or complete Figshare prediction extraction. The guide identifies the archived public annotation and small prediction extract, source hashes and per-analysis limits. The website snapshot is an output comparator, never an analysis input.

The [frozen original report](report/ivillafuerte_track2_report.md) and [spoken script](submission/pitch_script.md) retain the October 17 snapshot (SHA-256 `678706bf000be1d358af6317af5a03136291ae35889e6fccbbeeb8ce9f66d1e3`). No historical measurements were changed. Follow the recorded execution audit rather than interpreting a package validator as biological validation.

The earlier documentary revision was merged into main at `0cb71c4946fd71d0c0b5b1589026a2ed9e8a33b6`. The dated prepared report and [methods](submission/methods.md) distinguish that snapshot from the executed October 24 exploratory sensitivity audit in [robustness](reproduction/robustness/README.md). Original measurements, four original analysis scripts and the original Submission 1 report are preserved. No new biological replication, causal proliferation adjustment or clinical prediction is claimed. A revised report must be uploaded through the official process before it becomes a revised submission; no such receipt is asserted here. Video availability and displayed duration do not certify full audiovisual quality.
