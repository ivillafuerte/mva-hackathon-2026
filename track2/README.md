# Track 2: Functional BUBR1 Rescue Windows

English documentation edition, September 10, 2026. Research proposal with completed public-reference computations and proposed biological validation. No submission, clinical treatment or fetal experiment has occurred.

## Read the proposal

- [Main Track 2 report](report/ivillafuerte_track2_report.md)
- [Approved-drug assessment](drugs/candidate_assessment.md)
- [Experimental development plan](experiments/development_plan.md)
- [Official methods-template answers](submission/methods.md)
- [Requirements and open submission items](submission/readiness.md)
- [Three-minute pitch script](submission/pitch_script.md)

The main report is the current scientific narrative. Earlier notes below are retained as English technical records; historical prioritization is not the final drug decision.

- [Structural and mechanism audit](report/research_status_audit_2026-09-08.md)
- [Anakinra hypothesis record](report/alternative_anakinra_2026-09-08.md)
- [Temporal rescue concept](report/functional_rescue_windows_2026-09-09.md)

## Reproduce public computations

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

The package validation command checks local links, required artifacts, metric/table agreement, pitch length, template coverage and prohibited genomic file types. Passing technical checks does not close human-dependent submission items. Its output explicitly records outstanding account settings, video and remote publication.

## Scope and license

Approved medications are evaluated as conditional hypotheses. WT BUBR1 is a proposed experimental reference; prenatal mRNA is a future extension outside the nominated repurposed intervention. No universal therapeutic threshold, measured drug response or cancer cure is claimed. See [license](LICENSE.md) and the main report's required acknowledgment. Use only permitted findings and public references; do not add patient-scale genomic files or logs to Git.

## Final reproduction audit

The September 10 repeat execution reproduced `metrics.json`, `residue_summary.tsv` and `rotamer_summary.tsv` exactly. The initial native environment failed; a clean dependency installation and recovery of a truncated public PAE cache file resolved the repeat execution. All public reference hashes matched the audited manifest before analysis. This is computational reproducibility, not biological validation. See [reproduction audit](submission/reproduction_check.json).
