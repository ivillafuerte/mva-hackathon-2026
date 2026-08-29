#!/usr/bin/env bash
set -euo pipefail

fail=0

printf '%s\n' '=== MVA public-repository safety audit ==='

forbidden_regex='(^data/private/|^results/private/|^results/annotated/|\.(vcf|vcf\.gz|vcf\.bgz|bcf|tbi|csi|bam|bai|cram|crai|fastq|fastq\.gz|fq|fq\.gz)$)'

tracked_forbidden="$(git ls-files | grep -E "$forbidden_regex" || true)"
if [[ -n "$tracked_forbidden" ]]; then
  printf '%s\n' 'ERROR: forbidden challenge/genomic files are tracked:'
  printf '%s\n' "$tracked_forbidden"
  fail=1
else
  printf '%s\n' 'OK: no forbidden genomic/private file patterns are tracked.'
fi

tracked_data_docs="$(git ls-files 'data/**' | grep -Ei '\.(doc|docx|pdf)$' || true)"
if [[ -n "$tracked_data_docs" ]]; then
  printf '%s\n' 'ERROR: document(s) under data/ are tracked:'
  printf '%s\n' "$tracked_data_docs"
  fail=1
else
  printf '%s\n' 'OK: no challenge source documents under data/ are tracked.'
fi

large_files=''
while IFS= read -r f; do
  [[ -f "$f" ]] || continue
  size=$(wc -c < "$f")
  if (( size > 50000000 )); then
    large_files+="$f ($size bytes)"$'\n'
  fi
done < <(git ls-files)

if [[ -n "$large_files" ]]; then
  printf '%s\n' 'WARNING: tracked files larger than 50 MB:'
  printf '%s' "$large_files"
else
  printf '%s\n' 'OK: no tracked files exceed 50 MB.'
fi

if (( fail != 0 )); then
  printf '%s\n' 'AUDIT FAILED. Remove sensitive files from Git history/index before publishing.'
  exit 1
fi

printf '%s\n' 'AUDIT PASSED.'
