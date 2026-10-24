# MVA Hackathon 2026 - Track 1 Variant Prioritization

## Track 2 research proposal

The [latest prepared Track 2 report](track2/report/ivillafuerte_track2_report_revision_20261024.md) is the dated October 24 update, with a [one-page decision matrix](track2/drugs/candidate_decision_matrix_20261024.md) and executed public-data sensitivity diagnostics. The [original Submission 1 report](track2/report/ivillafuerte_track2_report.md) remains frozen. Product-status and Figure 6 evidence were already incorporated into public main at `0cb71c4946fd71d0c0b5b1589026a2ed9e8a33b6`; the new audit does not relabel them as new experiments. Amlexanox is on eligibility HOLD, montelukast depends on useful exact-truncation function, and gentamicin + mefloquine remains experimental. No exact-genotype pharmacological rescue is established. The [research package](track2/README.md) preserves methods, source limits and the [published pitch video](https://youtu.be/u527j7tO0OA) (displayed duration 2:57). A prepared or published revision is not an official resubmission; do not infer a revised-PDF receipt. Product eligibility, the prescribed dataset citation and the video review status remain tracked in [readiness](track2/submission/readiness.md).

Reproducible local pipeline for the **Rare Disease, Real Kid: MVA Hackathon 2026**, Track 1 (Variant Prediction).

## Primary result

The highest-ranked hypothesis is a **BUB1B compound-heterozygous pair** on GRCh38:

- `chr15:40209701 T>G` - `NM_001211.6:c.2210T>G`, `p.Leu737Ter`
- `chr15:40220612 T>G` - `NM_001211.6:c.3006T>G`, `p.Asn1002Lys`

The first allele is a known pathogenic MVA1 allele. The second is an ultra-rare missense candidate with population, computational, and protein-domain evidence. Independent trans-phase confirmation remains a limitation.

## Design goals

- Keep challenge genomic data local and private.
- Make software and public-reference acquisition reproducible.
- Separate private inputs/intermediates from publishable code and findings.
- Use containerized command-line tooling for deterministic analysis.
- Produce a challenge-compatible ranked CSV without publishing genotype-scale data.

## Environment

The analysis was developed on Apple Silicon using Docker with Ubuntu 24.04 ARM64. Core tools include Python, bcftools, samtools, bedtools, pysam, NCBI Datasets CLI, ClinVar, gnomAD, and Ensembl VEP-compatible annotations.

## Repository layout

```text
config/                     configuration
pipeline/                   analysis modules
scripts/                    reproducible command-line workflows
data/private/               AUTHORIZED CHALLENGE DATA - NEVER COMMIT
data/reference/             downloaded public references - local only
results/private/            genotype-scale derived data - NEVER COMMIT
results/qc/                 local QC outputs
results/annotated/          local annotation outputs
results/ranked/             local ranked outputs
results/submission/         final small candidate CSV/report staging
Dockerfile
compose.yaml
requirements.txt
Makefile
```

## Quick start

Build and verify the container:

```bash
make build
make check
```

Place authorized challenge inputs under `data/private/` according to the local configuration. Do not publish or commit those files.

Run the core workflow:

```bash
make qc
make bub1b
make bub1b-phase
```

Public reference datasets such as ClinVar and gnomAD should be downloaded locally and excluded from Git because of size. The pipeline documentation should record the exact release/version used.

## Evidence workflow

1. Validate the supplied GRCh38 callset and sample structure.
2. Review challenge HPO phenotype terms.
3. Prioritize mechanistically relevant MVA genes.
4. Extract and QC candidate variants in the BUB1B locus.
5. Map variants to the MANE Select transcript `NM_001211.6`.
6. Cross-reference ClinVar for clinical assertions.
7. Query gnomAD v4.1 for population frequency and homozygote counts.
8. Review VEP consequence, CADD, REVEL, SIFT, PolyPhen-2, SpliceAI, and conserved domains.
9. Rank a minimal set of causal hypotheses.
10. Explicitly track unresolved phase/segregation limitations.

## Data safety

This repository must contain **no raw or genotype-scale challenge data**. Before making the repository public, run:

```bash
bash scripts/prepublish_audit.sh
```

See [DATA_HANDLING.md](DATA_HANDLING.md) for the challenge-specific handling policy used by this project.

## Reproducibility note

The public repository reproduces the computational method but intentionally does not bundle the controlled challenge inputs. An authorized participant must obtain the dataset through the official challenge access flow and place it in the documented local private paths.

## Disclaimer

This project is a hackathon research submission and is not a clinical diagnostic report. Variant interpretation and compound-heterozygous phase require appropriate clinical validation before medical use.
