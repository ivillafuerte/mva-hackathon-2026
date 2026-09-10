#!/usr/bin/env python3
"""Exploratory UniProt BUB1B homolog panel without phylogenetic weighting."""
import argparse
import csv
import hashlib
import json
import re
from pathlib import Path
from Bio import Align, SeqIO
from Bio.Align import substitution_matrices

ap=argparse.ArgumentParser();ap.add_argument('--cache',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);args=ap.parse_args()
human=json.loads((args.cache/'uniprot.json').read_text())['sequence']['value']
aligner=Align.PairwiseAligner();aligner.mode='global';aligner.substitution_matrix=substitution_matrices.load('BLOSUM62');aligner.open_gap_score=-10;aligner.extend_gap_score=-.5
rows=[]
for rec in SeqIO.parse(args.cache/'orthologs.fasta','fasta'):
    if len(rec.seq)<900: continue  # Exclude fragments from the full-length protein panel.
    al=aligner.align(human,str(rec.seq))[0];mapping={}
    for (s1,e1),(s2,e2) in zip(*al.aligned):
        mapping.update({int(i):int(j) for i,j in zip(range(s1,e1),range(s2,e2))})
    row={'accession':rec.id.split('|')[1],'taxid':int(re.search(r'OX=(\d+)',rec.description)[1]),
         'species':re.search(r'OS=(.*?) OX=',rec.description)[1],'reviewed':rec.id.startswith('sp|'),
         'protein_evidence':int(re.search(r'PE=(\d+)',rec.description)[1]),'length':len(rec.seq),
         'alignment_score':float(al.score),'coverage_of_human':len(mapping)/len(human)}
    for pos in [737,1002,1012]:
        j=mapping.get(pos-1); row[f'aa_{pos}']=str(rec.seq[j]) if j is not None else '-'
        row[f'position_{pos}']=j+1 if j is not None else None
        row[f'context_{pos}']=str(rec.seq[max(0,j-10):j+11]) if j is not None else ''
    rows.append(row)
# One representative per species: reviewed status, protein evidence, coverage, score.
selected=[]
for taxid in sorted({r['taxid'] for r in rows}):
    selected.append(sorted((r for r in rows if r['taxid']==taxid),key=lambda r:(not r['reviewed'],r['protein_evidence'],-r['coverage_of_human'],-r['alignment_score'],r['accession']))[0])
args.out.mkdir(parents=True,exist_ok=True)
payload={'evidence':'COMPUTATIONAL','date':'2026-09-08','source_sha256':hashlib.sha256((args.cache/'orthologs.fasta').read_bytes()).hexdigest(),
         'method':'pairwise global BLOSUM62, gap open -10, extension -0.5; exclude sequence length <900; one representative/species',
         'limitations':'Exploratory gene-name panel, not a curated phylogeny or pathogenicity calibration; most entries unreviewed. Species are not independent observations.',
         'selected':selected,'all_full_length_candidates':rows}
(args.out/'conservation_panel.json').write_text(json.dumps(payload,indent=2)+'\n')
with (args.out/'conservation_panel.tsv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=list(selected[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(selected)
print(json.dumps(selected,indent=2))
