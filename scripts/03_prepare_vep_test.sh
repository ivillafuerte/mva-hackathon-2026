#!/usr/bin/env bash

set -euo pipefail

VCF=$(find /data/private/variants -maxdepth 1 -name "*.vcf.gz" -print -quit)

if [ -z "${VCF}" ]; then
    echo "ERROR: No VCF found."
    exit 1
fi

mkdir -p /results/private
mkdir -p /results/annotated

OUTPUT=/results/private/vep_test.vcf.gz

echo "======================================"
echo " Preparing VEP test dataset"
echo "======================================"

echo
echo "Input:"
echo "${VCF}"

echo
echo "Extracting:"
echo "Chromosome 22:20,000,000-20,100,000"
echo "PASS variants only"

bcftools view \
    -r 22:20000000-20100000 \
    -f PASS \
    -Oz \
    -o "${OUTPUT}" \
    "${VCF}"

bcftools index -f "${OUTPUT}"

COUNT=$(bcftools view -H "${OUTPUT}" | wc -l | tr -d ' ')

echo
echo "Variants prepared: ${COUNT}"
echo
echo "Output:"
echo "${OUTPUT}"
