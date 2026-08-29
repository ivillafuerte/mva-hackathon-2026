#!/usr/bin/env bash

set -euo pipefail

VCF=$(find /data/private/variants -maxdepth 1 -name "*.vcf.gz" -print -quit)

if [ -z "${VCF}" ]; then
    echo "ERROR: No VCF found."
    exit 1
fi

REGION="15:40161069-40221123"

mkdir -p /results/private/bub1b

ALL="/results/private/bub1b/bub1b.all.vcf.gz"
PASS="/results/private/bub1b/bub1b.pass.vcf.gz"
HET="/results/private/bub1b/bub1b.pass.het.vcf.gz"
TSV="/results/private/bub1b/bub1b.pass.het.tsv"

echo "======================================"
echo " BUB1B targeted extraction"
echo "======================================"
echo
echo "Region: ${REGION}"
echo

echo "[1/4] Extracting all BUB1B-region variants..."

bcftools view \
    -r "${REGION}" \
    -Oz \
    -o "${ALL}" \
    "${VCF}"

bcftools index -f "${ALL}"

echo "[2/4] Keeping PASS variants..."

bcftools view \
    -f PASS \
    -Oz \
    -o "${PASS}" \
    "${ALL}"

bcftools index -f "${PASS}"

echo "[3/4] Keeping PASS heterozygous variants..."

bcftools view \
    -i 'GT="het"' \
    -Oz \
    -o "${HET}" \
    "${PASS}"

bcftools index -f "${HET}"

echo "[4/4] Creating local candidate table..."

bcftools query \
    -f '%CHROM\t%POS\t%ID\t%REF\t%ALT\t%QUAL\t%FILTER[\t%GT\t%AD\t%DP\t%GQ]\n' \
    "${HET}" \
    > "${TSV}"

ALL_COUNT=$(bcftools view -H "${ALL}" | wc -l | tr -d ' ')
PASS_COUNT=$(bcftools view -H "${PASS}" | wc -l | tr -d ' ')
HET_COUNT=$(bcftools view -H "${HET}" | wc -l | tr -d ' ')

echo
echo "======================================"
echo " Summary"
echo "======================================"
echo "All region variants:          ${ALL_COUNT}"
echo "PASS variants:                ${PASS_COUNT}"
echo "PASS heterozygous variants:   ${HET_COUNT}"
echo
echo "Private candidate table:"
echo "${TSV}"
echo
echo "Do not commit or redistribute this file."
