# Rare Disease, Real Kid: MVA Hackathon 2026

Reproducible genomic analysis pipeline for the MVA Hackathon 2026.

## Objectives

- Whole Genome Sequencing variant analysis
- Variant annotation
- Rare variant prioritization
- Phenotype/genotype correlation
- Compound heterozygous candidate detection
- Candidate ranking
- Reproducible genomic workflow

## Security

Patient genomic and clinical data are restricted.

The following data must never be committed to this repository:

- FASTQ
- VCF / BCF
- BAM / CRAM
- Clinical documents
- Patient-specific derived datasets

Restricted data are stored locally under:

    data/private/

and mounted read-only inside the analysis container.

## Build

    make build

## Check environment

    make check

## Inspect VCF

    make inspect

## Run initial QC

    make qc

## Interactive shell

    make shell

