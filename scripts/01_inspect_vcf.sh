#!/usr/bin/env bash

set -euo pipefail

VCF=$(find /data/private/variants -maxdepth 1 -name "*.vcf.gz" | head -1)

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
bcftools view -h "${VCF}" | grep '^##fileformat'

echo
echo "Reference:"
bcftools view -h "${VCF}" | grep -E '^##reference=' || true

echo
echo "Contigs:"
bcftools view -h "${VCF}" \
    | grep '^##contig=' \
    | head -10

echo
echo "INFO fields:"
bcftools view -h "${VCF}" \
    | grep '^##INFO=' \
    | head -30

echo
echo "FORMAT fields:"
bcftools view -h "${VCF}" \
    | grep '^##FORMAT=' \
    | head -30

echo
echo "First 5 variants:"
bcftools view -H "${VCF}" | head -5 || true
