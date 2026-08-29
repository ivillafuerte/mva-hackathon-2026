#!/usr/bin/env bash

set -euo pipefail

VCF=$(find /data/private/variants -maxdepth 1 -name "*.vcf.gz" -print -quit)

if [ -z "${VCF}" ]; then
    echo "ERROR: No .vcf.gz file found in /data/private/variants"
    exit 1
fi

echo "======================================"
echo " MVA Hackathon - VCF Inspection"
echo "======================================"

echo
echo "VCF:"
echo "${VCF}"

echo
echo "File size:"
ls -lh "${VCF}"

echo
echo "Samples:"
bcftools query -l "${VCF}"

echo
echo "VCF format/version:"
bcftools view -h "${VCF}" | grep '^##fileformat' || true

echo
echo "Reference:"
bcftools view -h "${VCF}" | grep '^##reference=' || true

echo
echo "Source / variant caller:"
bcftools view -h "${VCF}" | grep -E '^##(source|GATKCommandLine|SentieonCommandLine|DRAGEN|DeepVariant)' | sed -n '1,20p' || true

echo
echo "Contigs:"
bcftools view -h "${VCF}" \
    | grep '^##contig=' \
    | sed -n '1,10p'

echo
echo "FILTER definitions:"
bcftools view -h "${VCF}" \
    | grep '^##FILTER=' \
    | sed -n '1,30p'

echo
echo "INFO fields:"
bcftools view -h "${VCF}" \
    | grep '^##INFO=' \
    | sed -n '1,50p'

echo
echo "FORMAT fields:"
bcftools view -h "${VCF}" \
    | grep '^##FORMAT=' \
    | sed -n '1,50p'

echo
echo "Column header:"
bcftools view -h "${VCF}" | grep '^#CHROM'

echo
echo "Index check:"
bcftools index -n "${VCF}"

echo
echo "First 5 variants:"
bcftools view -H "${VCF}" | sed -n '1,5p'

echo
echo "======================================"
echo " Inspection completed"
echo "======================================"
