# Challenge Data Handling

This repository is structured so that code and small publishable findings can be public while genome-scale patient data remain controlled.

## Never commit

- VCF/gVCF files and indexes
- BAM/CRAM files and indexes
- FASTQ files
- Any copy, subset, slice, or reformat containing genotype-scale patient data
- Annotated genome-wide or large per-variant tables derived from the challenge genome
- Notebook state/caches containing genotype-scale data
- Challenge clinical source documents
- Stored prompts/logs containing pasted blocks of genome-scale variant data

## May be retained as challenge findings

Per the organizer's published clarification, small ranked candidate lists, HPO terms, gene/pathway findings, code, reports, and leaderboard entries can be retained as research outputs, provided they do not reconstruct a meaningful portion of the genome.

## Local directory policy

Private inputs and genotype-scale intermediates should remain under ignored paths such as:

```text
data/private/
results/private/
results/annotated/
```

Public references can also remain local because of size:

```text
data/reference/clinvar/
data/reference/gnomad/
data/reference/vep/
```

## LLM/service policy

Follow the challenge organizer's processor-vs-recipient test for third-party services. The project methods report documents the provider/tier used for LLM assistance and the applicable no-training policy. Avoid submitting feedback/rating on challenge-related model outputs when that could change data-use treatment.

## Deletion

At the challenge deletion milestone, remove controlled genomic data and genotype-scale derived material from all systems under participant control, then complete the organizer's required deletion attestation. Retain only the challenge-permitted findings and code.
