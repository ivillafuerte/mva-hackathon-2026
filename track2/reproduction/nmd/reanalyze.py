"""Reanalyze public Zhao et al. NMD screening summary tables; no patient data.
Run: python reanalyze.py. Requires pandas, numpy, scipy, openpyxl (read only).
"""
from pathlib import Path
import hashlib, json, platform
import numpy as np
import pandas as pd
import scipy
import openpyxl
from scipy.stats import chi2, norm

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results'
OUT.mkdir(exist_ok=True)
GENES = ['Ptbp2', 'Hnrnpl', 'Tra2b']

def bh(p):
    p = np.asarray(p, dtype=float)
    order = np.argsort(p)
    out = np.empty(len(p))
    out[order] = np.minimum(1, np.minimum.accumulate((p[order]*len(p)/np.arange(1,len(p)+1))[::-1])[::-1])
    return out

raw = pd.read_excel(ROOT/'inputs/table_S2.xlsx', sheet_name='Raw data all', header=None)
d = pd.DataFrame({'Drug':raw.iloc[2:,0].str.strip()}).reset_index(drop=True)
for gene, f, n in zip(GENES,[1,9,17],[5,13,21]):
    for role, col in [('nonNMD',f),('NMD',n)]:
        for off, suffix in [(0,'RQ'),(1,'low'),(2,'high')]:
            d[f'{gene}_{role}_{suffix}'] = pd.to_numeric(raw.iloc[2:,col+off],errors='raise').to_numpy()
    d[f'{gene}_ratio'] = d[f'{gene}_NMD_RQ']/d[f'{gene}_nonNMD_RQ']
    d[f'{gene}_log2_ratio'] = np.log2(d[f'{gene}_ratio'])
assert len(d)==705 and d.Drug.is_unique
assert np.isfinite(d[[f'{g}_ratio' for g in GENES]]).all().all()
d['is_control'] = d.Drug.eq('Thapsigargin')
q = pd.read_excel(ROOT/'inputs/table_S4.xlsx',sheet_name='NMD inhibitors')
q['Drug'] = q.Drug.str.strip()
d = d.merge(q,on='Drug',validate='one_to_one')
assert len(d)==705
for pcol in ['p_Fisher','p_permutation']:
    qcol = 'FDR_'+pcol[2:]
    d[f'{qcol}_BH_recomputed_705'] = bh(d[pcol])
    d.loc[~d.is_control,f'{qcol}_BH_excluding_control_704'] = bh(d.loc[~d.is_control,pcol])
with np.errstate(divide='ignore'):
    d['p_Fisher_recomputed_from_published_gene_p'] = chi2.sf(-2*np.log(d[['p_'+g for g in GENES]]).sum(axis=1),6)

# Reproduce the screen-wide standardized log-ratio model, not a replicate test.
zchecks = {}
for include_control in [True,False]:
    base = d if include_control else d[~d.is_control]
    for ddof in [0,1]:
        p = pd.DataFrame(index=d.index)
        for g in GENES:
            x = base[f'{g}_log2_ratio']
            p[g] = norm.sf((d[f'{g}_log2_ratio']-x.mean())/x.std(ddof=ddof))
        zchecks[f'include_control={include_control},ddof={ddof}'] = float(np.max(np.abs(p.to_numpy()-d[['p_'+g for g in GENES]].to_numpy())))
        if include_control and ddof==1:
            reconstructed_p = p.copy()
with np.errstate(divide='ignore'):
    d['p_Fisher_from_reconstructed_z'] = chi2.sf(-2*np.log(reconstructed_p).sum(axis=1),6)
d['q_Fisher_from_reconstructed_z_705'] = bh(d.p_Fisher_from_reconstructed_z)
assert abs(d.FDR_Fisher-d.q_Fisher_from_reconstructed_z_705).max() < 1e-6, 'Published Fisher model mismatch'

# Leave-one-reporter-out sensitivity uses reconstructed unrounded p values.
# Standardization includes the positive control to match the published model.
# These are exploratory recombinations, not independent validation or new biological tests.
for omit in GENES:
    cols = [g for g in GENES if g!=omit]
    with np.errstate(divide='ignore'):
        pp = chi2.sf(-2*np.log(reconstructed_p[cols]).sum(axis=1),4)
    d.loc[~d.is_control,'LOO_without_'+omit+'_q704'] = bh(pp[~d.is_control])

ratio_cols=[g+'_ratio' for g in GENES]
n_cols=[g+'_NMD_RQ' for g in GENES]
f_cols=[g+'_nonNMD_RQ' for g in GENES]
d['minimum_ratio']=d[ratio_cols].min(axis=1)
d['median_ratio']=d[ratio_cols].median(axis=1)
d['reporters_ratio_gt1']=(d[ratio_cols]>1).sum(axis=1)
d['reporters_ratio_ge1_5']=(d[ratio_cols]>=1.5).sum(axis=1)
d['reporters_ratio_ge2']=(d[ratio_cols]>=2).sum(axis=1)
d['NMD_increases_gt1']=(d[n_cols]>1).sum(axis=1)
d['nonNMD_all_within_0_5_to_2']=((d[f_cols]>=.5)&(d[f_cols]<=2)).all(axis=1)
d['both_published_q_le0_05']=(d.FDR_Fisher<=.05)&(d.FDR_permutation<=.05)
d['both_published_q_le0_01']=(d.FDR_Fisher<=.01)&(d.FDR_permutation<=.01)

# Audit published ratio summaries. Do not propagate suspect ratio bounds/SEM.
audits=[]
for g in GENES:
    r=pd.read_excel(ROOT/'inputs/table_S2.xlsx',sheet_name=g,header=None).iloc[2:].copy()
    r.columns=['Drug','F','F_low','F_high','N','N_low','N_high','ratio','ratio_low','ratio_high','SEM']
    r.Drug=r.Drug.str.strip()
    for c in r.columns[1:]: r[c]=pd.to_numeric(r[c])
    r['gene']=g
    r['calculated_ratio']=r.N/r.F
    r['ratio_abs_error']=abs(r.ratio-r.calculated_ratio)
    r['bounds_reversed']=r.ratio_low>r.ratio_high
    r['low_matches_Nlow_div_Flow']=np.isclose(r.ratio_low,r.N_low/r.F_low,rtol=1e-8,atol=1e-10)
    r['high_matches_Nhigh_div_Fhigh']=np.isclose(r.ratio_high,r.N_high/r.F_high,rtol=1e-8,atol=1e-10)
    audits.append(r)
a=pd.concat(audits,ignore_index=True)
wf=openpyxl.load_workbook(ROOT/'inputs/table_S2.xlsx',read_only=True,data_only=False)
sem_formula_records=[]
for g in GENES:
    for row in wf[g].iter_rows(min_row=3):
        f=row[10].value
        sem_formula_records.append({'gene':g,'Drug':row[0].value,'cell':row[10].coordinate,'formula':f,
          'SEM_uses_central_and_bounds':isinstance(f,str) and 'STDEV.S(H' in f and ':J' in f and 'SQRT(COUNT(H' in f})
wf.close()
pd.DataFrame(sem_formula_records).to_csv(OUT/'published_SEM_formula_audit.csv',index=False)
a.to_csv(OUT/'published_ratio_bounds_audit.csv',index=False)
d.to_csv(OUT/'all_drugs_reanalysis.csv',index=False)
selected=d[d.both_published_q_le0_05|d.Drug.str.contains('Mefloquine|Nicotinic acid|Naloxone',case=False)]
selected.to_csv(OUT/'selected_candidates.csv',index=False)

drugs=d[~d.is_control]
summary={
 'source':{'PMID':'35024243','DOI':'10.1016/j.omtn.2021.12.003','model':'Neuro-2a mouse cells','screen_exposure':'5 uM, 5 h; not a treatment recommendation'},
 'n_drugs':len(drugs),'n_controls':int(d.is_control.sum()),
 'S1_n_rows':len(pd.read_excel(ROOT/'inputs/table_S1.xlsx')),
 'published_q_both_le_0_05_drugs':drugs.loc[drugs.both_published_q_le0_05,'Drug'].tolist(),
 'published_q_both_le_0_01_drugs':drugs.loc[drugs.both_published_q_le0_01,'Drug'].tolist(),
 'Fisher_recompute_max_abs_error':float(abs(d.p_Fisher-d.p_Fisher_recomputed_from_published_gene_p).max()),
 'BH_max_abs_error':{k:float(abs(d[k]-d[k+'_BH_recomputed_705']).max()) for k in ['FDR_Fisher','FDR_permutation']},
 'z_model_max_abs_errors':zchecks,
 'Fisher_from_reconstructed_z_max_abs_error':float(abs(d.p_Fisher-d.p_Fisher_from_reconstructed_z).max()),
 'Fisher_q_from_reconstructed_z_max_abs_error':float(abs(d.FDR_Fisher-d.q_Fisher_from_reconstructed_z_705).max()),
 'ratio_audit':{'n_rows':len(a),'n_reversed_bounds':int(a.bounds_reversed.sum()),'n_low_matches_same_side_division':int(a.low_matches_Nlow_div_Flow.sum()),'n_high_matches_same_side_division':int(a.high_matches_Nhigh_div_Fhigh.sum()),'max_ratio_error':float(a.ratio_abs_error.max()),'n_SEM_formulas_using_central_and_bounds':sum(x['SEM_uses_central_and_bounds'] for x in sem_formula_records)},
 'descriptive_threshold_sensitivity':{},
 'screen_log2_ratio_correlation':drugs[[g+'_log2_ratio' for g in GENES]].corr().to_dict(),
 'limitations':['Table S2 provides normalized RQ summaries and marginal intervals, not individual Ct replicates.','No BUB1B measurement or exact-genotype rescue.','AS-NMD ratios do not isolate decay from alternative splicing and differential isoform regulation.','Published permutation p values are reused; the stochastic permutation algorithm is not independently reproduced.','Zero published permutation p values are finite-sampling outputs, not zero biological uncertainty.','LOO analysis and effect thresholds are exploratory; they do not yield clinical rescue probabilities.'],
 'software':{'python':platform.python_version(),'pandas':pd.__version__,'numpy':np.__version__,'scipy':scipy.__version__,'openpyxl_read_only':openpyxl.__version__},
 'inputs':[]
}
for threshold in [1,1.5,2]:
    mask=(drugs[ratio_cols]>=threshold).all(axis=1)
    summary['descriptive_threshold_sensitivity'][str(threshold)]={
     'all_three_ratios_ge_threshold':int(mask.sum()),
     'also_both_published_q_le_0_05':drugs.loc[mask&drugs.both_published_q_le0_05,'Drug'].tolist(),
     'also_nonNMD_within_0_5_to_2':drugs.loc[mask&drugs.both_published_q_le0_05&drugs.nonNMD_all_within_0_5_to_2,'Drug'].tolist()}
for f in sorted((ROOT/'inputs').iterdir()):
    summary['inputs'].append({'file':str(f.relative_to(ROOT)),'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()})
(OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
print(selected[['Drug']+ratio_cols+['FDR_Fisher','FDR_permutation','nonNMD_all_within_0_5_to_2']+['LOO_without_'+g+'_q704' for g in GENES]].to_string(index=False))
