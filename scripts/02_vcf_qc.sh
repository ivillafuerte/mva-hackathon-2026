#!/usr/bin/env bash

set -euo pipefail

VCF=$(find /data/private/variants -maxdepth 1 -name "*.vcf.gz" -print -quit)

if [ -z "${VCF}" ]; then
    echo "ERROR: No VCF found."
    exit 1
fi

mkdir -p /results/qc

echo "======================================"
echo " MVA Hackathon - Initial VCF QC"
echo "======================================"

echo
echo "Generating bcftools statistics..."

bcftools stats "${VCF}" > /results/qc/bcftools_stats.txt

echo
echo "Counting variants..."

TOTAL=$(bcftools view -H "${VCF}" | wc -l | tr -d ' ')
PASS=$(bcftools view -H -f PASS "${VCF}" | wc -l | tr -d ' ')

SNPS=$(bcftools view -H -v snps "${VCF}" | wc -l | tr -d ' ')
INDELS=$(bcftools view -H -v indels "${VCF}" | wc -l | tr -d ' ')

BIALLELIC=$(bcftools view -H -m2 -M2 "${VCF}" | wc -l | tr -d ' ')
MULTI=$(bcftools view -H -m3 "${VCF}" | wc -l | tr -d ' ')

HET=$(bcftools view -H -i 'GT="het"' "${VCF}" | wc -l | tr -d ' ')
HOM=$(bcftools view -H -i 'GT="hom"' "${VCF}" | wc -l | tr -d ' ')

PASS_HET=$(bcftools view -H -f PASS -i 'GT="het"' "${VCF}" | wc -l | tr -d ' ')

echo "Total variants:        ${TOTAL}"
echo "PASS variants:         ${PASS}"
echo "SNPs:                  ${SNPS}"
echo "Indels:                ${INDELS}"
echo "Biallelic variants:    ${BIALLELIC}"
echo "Multiallelic variants: ${MULTI}"
echo "Heterozygous calls:    ${HET}"
echo "Homozygous calls:      ${HOM}"
echo "PASS heterozygous:     ${PASS_HET}"

cat > /results/qc/summary.txt <<SUMMARY
MVA Hackathon - Initial VCF QC

Reference: GRCh38
Sample: WGS_EX2312012

Total variants:        ${TOTAL}
PASS variants:         ${PASS}
SNPs:                  ${SNPS}
Indels:                ${INDELS}
Biallelic variants:    ${BIALLELIC}
Multiallelic variants: ${MULTI}
Heterozygous calls:    ${HET}
Homozygous calls:      ${HOM}
PASS heterozygous:     ${PASS_HET}
SUMMARY

echo
echo "QC completed."
echo "Results written to /results/qc/"
