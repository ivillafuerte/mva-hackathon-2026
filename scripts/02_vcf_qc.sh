#!/usr/bin/env bash

set -euo pipefail

VCF=$(find /data/private/variants -maxdepth 1 -name "*.vcf.gz" | head -1)

if [ -z "${VCF}" ]; then
    echo "ERROR: No .vcf.gz file found."
    exit 1
fi

mkdir -p /results/qc

echo "Generating bcftools statistics..."

bcftools stats \
    "${VCF}" \
    > /results/qc/vcf_stats.txt

echo "Counting variants..."

TOTAL=$(bcftools view -H "${VCF}" | wc -l | tr -d ' ')

SNPS=$(bcftools view \
    -v snps \
    -H "${VCF}" \
    | wc -l \
    | tr -d ' ')

INDELS=$(bcftools view \
    -v indels \
    -H "${VCF}" \
    | wc -l \
    | tr -d ' ')

echo "Total variants: ${TOTAL}"
echo "SNPs:           ${SNPS}"
echo "Indels:         ${INDELS}"

cat > /results/qc/summary.txt <<SUMMARY
MVA Hackathon - Initial VCF QC

Total variants: ${TOTAL}
SNPs: ${SNPS}
Indels: ${INDELS}
SUMMARY

echo
echo "Results written to:"
echo "/results/qc/"
