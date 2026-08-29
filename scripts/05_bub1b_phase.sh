#!/usr/bin/env bash

set -euo pipefail

VCF="/results/private/bub1b/bub1b.pass.het.vcf.gz"
OUT="/results/private/bub1b/bub1b.phase.tsv"

if [ ! -f "${VCF}" ]; then
    echo "ERROR: BUB1B heterozygous VCF not found."
    exit 1
fi

echo "======================================"
echo " BUB1B phase/genotype inspection"
echo "======================================"

bcftools query \
    -f '%CHROM\t%POS\t%ID\t%REF\t%ALT\t%QUAL[\t%GT\t%AD\t%DP\t%GQ\t%PGT\t%PID]\n' \
    "${VCF}" \
    > "${OUT}"

COUNT=$(wc -l < "${OUT}" | tr -d ' ')

PHASED_GT=$(awk -F '\t' '$7 ~ /\|/ {c++} END {print c+0}' "${OUT}")
WITH_PGT=$(awk -F '\t' '$11 != "." && $11 != "" {c++} END {print c+0}' "${OUT}")
WITH_PID=$(awk -F '\t' '$12 != "." && $12 != "" {c++} END {print c+0}' "${OUT}")

echo
echo "Heterozygous variants:          ${COUNT}"
echo "Explicitly phased GT (0|1):     ${PHASED_GT}"
echo "Variants with PGT:              ${WITH_PGT}"
echo "Variants with PID:              ${WITH_PID}"

echo
echo "Private output:"
echo "${OUT}"
