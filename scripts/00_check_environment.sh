#!/usr/bin/env bash

set -euo pipefail

echo "======================================"
echo " MVA Hackathon - Environment Check"
echo "======================================"

echo
echo "Architecture:"
uname -m

echo
echo "Operating system:"
cat /etc/os-release | grep PRETTY_NAME

echo
echo "Python:"
python3 --version

echo
echo "bcftools:"
bcftools --version | head -1

echo
echo "samtools:"
samtools --version | head -1

echo
echo "bedtools:"
bedtools --version

echo
echo "pysam:"
python3 -c "import pysam; print(pysam.__version__)"

echo
echo "pandas:"
python3 -c "import pandas; print(pandas.__version__)"

echo
echo "Environment OK"
