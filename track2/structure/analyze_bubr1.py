#!/usr/bin/env python3
"""Reproducible WT BUBR1 geometry; does not predict ΔΔG or pathogenicity.

Uses public references only. Residue numbering follows UniProt O60566.
Rotamers form an unweighted geometric grid, without relaxation or energy estimates.
"""
import argparse
import csv
import hashlib
import itertools
import json
from pathlib import Path

import Bio
import freesasa
import numpy as np
from Bio import SeqIO
from Bio.Data.PDBData import protein_letters_3to1, residue_sasa_scales
from Bio.PDB import MMCIFParser, PDBParser

BB = {'N', 'CA', 'C', 'O', 'OXT'}
VDW = {'C': 1.70, 'N': 1.55, 'O': 1.52, 'S': 1.80}


def rounded(x):
    if isinstance(x, dict): return {k: rounded(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)): return [rounded(v) for v in x]
    if isinstance(x, np.ndarray): return rounded(x.tolist())
    if isinstance(x, (float, np.floating)): return round(float(x), 5)
    if isinstance(x, np.integer): return int(x)
    return x


def unit(v):
    return v / np.linalg.norm(v)


def dihedral(a, b, c, d):
    b0=-(b-a); b1=unit(c-b); b2=d-c
    v=b0-np.dot(b0,b1)*b1; w=b2-np.dot(b2,b1)*b1
    return float(np.degrees(np.arctan2(np.dot(np.cross(b1,v),w),np.dot(v,w))))


def place(a, b, c, length, angle, torsion):
    """Internal coordinates; the torsion convention is checked at runtime."""
    bc = unit(c - b)
    normal = unit(np.cross(b - a, bc))
    tangent = np.cross(normal, bc)
    theta, phi = np.radians([angle, torsion])
    return c + length * (-bc*np.cos(theta) + np.sin(theta)*(tangent*np.cos(phi)+normal*np.sin(phi)))


def label(a):
    return f'{a.parent.resname}{a.parent.id[1]}:{a.name}'


def asa_dict(path, algorithm=freesasa.LeeRichards, resolution=100):
    s = freesasa.Structure(str(path))
    params = {'algorithm': algorithm, 'probe-radius': 1.4, 'n-threads': 1}
    params['n-slices' if algorithm == freesasa.LeeRichards else 'n-points'] = resolution
    result = freesasa.calc(s, freesasa.Parameters(params))
    atoms = {(s.chainLabel(i).strip(), int(s.residueNumber(i)), s.atomName(i).strip()): result.atomArea(i) for i in range(s.nAtoms())}
    return result, atoms


def residue_metrics(chain, position, areas, atom_areas, pae):
    r = chain[position]
    coords = np.array([a.coord for a in r])
    sc = [a for a in r if a.name not in BB]
    nonseq = []
    for q in chain:
        if q.id[1] == position: continue
        d = min(float(a-b) for a in r for b in q)
        nonseq.append({'residue': f'{q.resname}{q.id[1]}', 'number': q.id[1], 'min_heavy_distance_A': d,
                       'sequence_separation': abs(q.id[1]-position), 'plddt': float(q['CA'].bfactor),
                       'pae_both_directions_A': [pae[position-1, q.id[1]-1], pae[q.id[1]-1, position-1]]})
    neighbors = {str(c): sorted([x for x in nonseq if x['min_heavy_distance_A'] <= c], key=lambda x:x['min_heavy_distance_A']) for c in [4,5,8]}
    ar = vars(areas['A'][str(position)])
    polar = []
    # ASN amide donors/acceptors: geometric candidates only.
    if r.resname == 'ASN':
        for a_name in ['OD1','ND2']:
            a = r[a_name]
            for q in chain:
                if q == r: continue
                for b in q:
                    # Backbone carbonyls and amide nitrogen have defined chemical roles.
                    if not ((a_name == 'ND2' and b.name == 'O') or (a_name == 'OD1' and b.name == 'N' and q.resname != 'PRO')): continue
                    d = float(a-b)
                    if 2.5 <= d <= 3.5:
                        v1, v2 = unit(r['CG'].coord-a.coord), unit(b.coord-a.coord)
                        polar.append({'asparagine_atom': a_name, 'partner': label(b), 'distance_A': d,
                                      'angle_CG_AsnAtom_partner_deg': float(np.degrees(np.arccos(np.clip(v1@v2,-1,1)))),
                                      'status': 'candidate; no explicit hydrogens or energetic validation'})
    phi = dihedral(chain[position-1]['C'].coord,r['N'].coord,r['CA'].coord,r['C'].coord)
    psi = dihedral(r['N'].coord,r['CA'].coord,r['C'].coord,chain[position+1]['N'].coord)
    # Explicit geometric description, not a DSSP assignment.
    ss = 'alpha-like' if -100 <= phi <= -30 and -80 <= psi <= -5 else 'non-alpha/turn-or-loop; no DSSP assignment'
    center = np.mean([q['CA'].coord for q in chain if 750 <= q.id[1] <= 1045],axis=0)
    side_axis = unit(np.mean([a.coord for a in sc],axis=0)-r['CA'].coord)
    radial = unit(r['CA'].coord-center)
    charged = []
    charge_names={'ASP':{'OD1','OD2'},'GLU':{'OE1','OE2'},'LYS':{'NZ'},'ARG':{'NE','NH1','NH2'},'HIS':{'ND1','NE2'}}
    for q in chain:
        for b in q:
            if b.name in charge_names.get(q.resname,set()):
                d=min(float(a-b) for a in sc)
                if d<=8:charged.append({'atom':label(b),'min_sidechain_distance_A':d,'histidine_charge_uncertain':q.resname=='HIS'})
    return {'residue':r.resname,'position':position,'plddt':r['CA'].bfactor,
            'sasa_A2':ar['total'],'backbone_sasa_A2':ar['mainChain'],'sidechain_sasa_A2':ar['sideChain'],
            'rsa_percent_Tien2013':100*ar['total']/residue_sasa_scales['Wilke'][r.resname],
            'rsa_percent_Miller1987':100*ar['total']/residue_sasa_scales['Miller'][r.resname],
            'rsa_percent_FreeSASA_builtin':100*ar['relativeTotal'],
            'rsa_FreeSASA_reference_total_A2':ar['total']/ar['relativeTotal'] if ar['relativeTotal'] else None,
            'atom_sasa_A2':{a.name:atom_areas[('A',position,a.name)] for a in r},
            'phi_deg':phi,'psi_deg':psi,'secondary_structure_proxy':ss,
            'neighbors_heavy_atoms_inclusive':neighbors,
            'nonlocal_residue_counts':{c:len([x for x in v if x['sequence_separation']>2]) for c,v in neighbors.items()},
            'hbond_candidates':polar,'charged_atoms_within_8A_of_sidechain':charged,
            'sidechain_vs_domain_radial_cosine':float(side_axis@radial),
            'orientation_warning':'centroid proxy is not a solvent-accessibility measurement'}


def rotamers(chain, angle_sets=None):
    r = chain[1002]
    n,ca,cb = [r[x].coord.astype(float) for x in ['N','CA','CB']]
    env=[a for a in chain.get_atoms() if a.parent!=r]
    env += [r[x] for x in BB if x in r] + [r['CB']]
    # Exclude pairs separated by 1–2 bonds; include nonbonded CB–CE/NZ.
    ecoords=np.array([a.coord for a in env]); radii=np.array([VDW[a.element] for a in env])
    rows=[]
    if angle_sets is None: angle_sets=itertools.product([-60.,60.,180.],repeat=4)
    for angles in angle_sets:
        points=[n,ca,cb]
        for j,ang in enumerate(angles): points.append(place(*points[-3:],1.49 if j==3 else 1.52,111.0,ang))
        new=points[3:]
        # Check actual bond lengths and angles, not only expected output values.
        for j,a in enumerate(angles):
            observed=dihedral(*points[j:j+4])
            err=abs((observed-a+180)%360-180)
            assert err<1e-5,(a,observed)
        cl=[]; max_overlap=0.
        for j,p in enumerate(new):
            ds=np.linalg.norm(ecoords-p,axis=1)
            overlap=radii+(1.55 if j==3 else 1.70)-ds
            valid=np.array([not(a.parent==r and ((j==0 and a.name=='CA') or (j<=1 and a.name=='CB'))) for a in env])
            max_overlap=max(max_overlap,float(np.max(overlap[valid])))
            for k in np.where((overlap>0.4)&valid)[0]:
                cl.append({'new_atom':['CG','CD','CE','NZ'][j],'partner':label(env[k]),'distance_A':ds[k],'overlap_A':overlap[k]})
        # Within-residue clashes between new atoms separated by >=3 bonds.
        internal_distance=np.linalg.norm(new[0]-new[3]);max_overlap=max(max_overlap,3.25-internal_distance)
        if internal_distance<1.70+1.55-0.4:
            cl.append({'new_atom':'NZ','partner':'LYS1002:CG','distance_A':internal_distance,'overlap_A':3.25-internal_distance})
        near=[]
        for a in env:
            if a.parent.resname in ['ASP','GLU'] and a.name in ['OD1','OD2','OE1','OE2']:
                d=float(np.linalg.norm(new[3]-a.coord))
                if d<=4:near.append({'partner':label(a),'distance_A':d})
        # NZ sphere fraction accessible to a 1.4 Å probe, using Bondi radii.
        # Geometric proxy only; no probabilities or energy calculation.
        count=960; idx=np.arange(count); z=1-2*(idx+.5)/count
        phi=idx*np.pi*(3-np.sqrt(5));rr=np.sqrt(1-z*z)
        sphere=new[3]+2.95*np.column_stack([rr*np.cos(phi),rr*np.sin(phi),z])
        obs=np.vstack([ecoords,*new[:3]]);rad=np.r_[radii,1.7,1.7,1.7]+1.4
        close=np.linalg.norm(obs-new[3],axis=1)<7
        accessible=np.all(np.linalg.norm(sphere[:,None,:]-obs[None,close,:],axis=2)>=rad[close],axis=1)
        rows.append({'chi1':angles[0],'chi2':angles[1],'chi3':angles[2],'chi4':angles[3],
                     'clashes_overlap_gt_0_4A':len(cl),'max_overlap_A':max_overlap,
                     'interresidue_clashes_gt_0_4A':sum(not x['partner'].startswith(('ASN1002:','LYS1002:')) for x in cl),
                     'NZ_accessible_sphere_fraction':float(accessible.mean()),'salt_bridge_candidates':near,
                     'clashes':sorted(cl,key=lambda x:-x['overlap_A']),'new_atom_coordinates_A':new})
    rows.sort(key=lambda x:(x['clashes_overlap_gt_0_4A'],x['max_overlap_A'],-x['NZ_accessible_sphere_fraction']))
    return rows


def transcript_audit(path):
    record=SeqIO.read(path,'genbank');cds=next(f for f in record.features if f.type=='CDS');exons=[f for f in record.features if f.type=='exon']
    variants={}
    for aa,expected,mut in [(737,'TTA','TGA'),(1002,'AAT','AAG')]:
        start=int(cds.location.start)+(aa-1)*3
        assert str(record.seq[start:start+3])==expected
        context=str(record.seq[start-12:start]+mut+record.seq[start+3:start+15]).replace('T','U')
        exon=next((i+1,f) for i,f in enumerate(exons) if start in f.location)
        variants[str(aa)]={'codon_rna_1based_start':start+1,'wt_codon_DNA':expected,'mut_codon_DNA':mut,
                          'mutant_mRNA_minus12_codon_plus12':context,'plus4_base':str(record.seq[start+3]).replace('T','U'),
                          'exon_number':exon[0], 'exon_rna_coordinates':[int(exon[1].location.start)+1,int(exon[1].location.end)],
                          'nt_between_codon_end_and_next_junction':int(exon[1].location.end)-(start+3) if exon[0]<len(exons) else None,
                          'nt_between_codon_end_and_last_junction':int(exons[-1].location.start)-(start+3) if exon[0]<len(exons) else None}
    return {'accession':record.id,'CDS_1based':[int(cds.location.start)+1,int(cds.location.end)],
            'exons_1based':[[int(f.location.start)+1,int(f.location.end)] for f in exons], 'variants':variants}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--cache',type=Path,required=True);ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();args.out.mkdir(parents=True,exist_ok=True)
    pdb=args.cache/'BUBR1_AF_v6.pdb';m=PDBParser(QUIET=True).get_structure('AF',pdb)[0];c=m['A']
    u=json.loads((args.cache/'uniprot.json').read_text());seq=''.join(protein_letters_3to1[r.resname] for r in c)
    assert seq==u['sequence']['value'] and len(seq)==1050
    assert c[1002].resname=='ASN' and c[1012].resname=='LEU'
    pae=np.array(json.loads((args.cache/'BUBR1_AF_v6.pae.json').read_text())[0]['predicted_aligned_error'])
    assert pae.shape==(1050,1050)
    result,atoms=asa_dict(pdb);ar=result.residueAreas()
    measurements={str(p):residue_metrics(c,p,ar,atoms,pae) for p in [1002,1012]}
    # Algorithm cross-check: Lee–Richards 100 slices versus S&R 960 points.
    check,_=asa_dict(pdb,freesasa.ShrakeRupley,960)
    # Sensitivity to hypothetical low-confidence interdomain interactions.
    cropped=args.out/'domain_750_1045.pdb'
    cropped.write_text('\n'.join(l for l in pdb.read_text().splitlines() if l.startswith('ATOM') and 750<=int(l[22:26])<=1045)+'\nEND\n')
    dom,_=asa_dict(cropped)
    for p in [1002,1012]:
        measurements[str(p)]['sasa_SR960_A2']=check.residueAreas()['A'][str(p)].total
        measurements[str(p)]['sasa_domain_only_A2']=dom.residueAreas()['A'][str(p)].total
    rots=rotamers(c)
    # Sensitivity to idealized rotamer centers: ±20 degrees around the best six.
    # No relaxation, energy optimization or evidence of biological stability.
    jitter=sorted(set(tuple((r[f'chi{i+1}']+offset[i]+180)%360-180 for i in range(4))
                      for r in rots[:6] for offset in itertools.product([-20.,0.,20.],repeat=4)))
    fine=rotamers(c,jitter)
    plddt=[c[p]['CA'].bfactor for p in range(985,1021)]
    exp={}
    for name,chainid in [('5KHU','Q'),('6TLJ','S')]:
        p=args.cache/f'{name}.cif'
        if not p.exists():continue
        s=MMCIFParser(QUIET=True).get_structure(name,p)[0][chainid]
        exp[name]={'chain':chainid,'observed_residues':len(s),'observed_min_max':[min(r.id[1] for r in s),max(r.id[1] for r in s)],'has_1002':(' ',1002,' ') in s,'has_1012':(' ',1012,' ') in s}
    output={'evidence':'COMPUTATIONAL','model':'AF-O60566-F1-model_v6','length':len(seq),
            'sequence_985_1020':seq[984:1020],'plddt_985_1020':{'mean':np.mean(plddt),'min':min(plddt),'max':max(plddt)},
            'residues':measurements,'N1002_L1012_CA_distance_A':float(c[1002]['CA']-c[1012]['CA']),
            'N1002_L1012_min_heavy_distance_A':min(float(a-b) for a in c[1002] for b in c[1012]),
            'experimental_coverage_check':exp,
            'rotamer_grid_summary':{'count':len(rots),'zero_clashes_gt_0_4A':sum(r['clashes_overlap_gt_0_4A']==0 for r in rots),
                                    'min_max_overlap_A':min(r['max_overlap_A'] for r in rots),
                                    'no_interresidue_clashes':sum(r['interresidue_clashes_gt_0_4A']==0 for r in rots),
                                    'note':'Not a Boltzmann ensemble; cannot convert counts to probability or ΔΔG.'},
            'rotamer_jitter_summary':{'count':len(fine),'zero_clashes_gt_0_4A':sum(r['clashes_overlap_gt_0_4A']==0 for r in fine),
                                     'max_NZ_accessible_fraction_among_zero_clash':max((r['NZ_accessible_sphere_fraction'] for r in fine if r['clashes_overlap_gt_0_4A']==0),default=None),
                                     'note':'±20 degrees in each chi around the 6 best coarse conformations. Exploratory geometric sensitivity.'},
            'transcript':transcript_audit(args.cache/'NM_001211.6.gb'),
            'software':{'biopython':Bio.__version__,'numpy':np.__version__,'freesasa':'2.2.1'},
            'parameters':{'probe_A':1.4,'sasa_algorithm':'Lee-Richards','n_slices':100,'crosscheck':'Shrake-Rupley 960 points','rotamer_angles_deg':[-60,60,180],'clash_overlap_cutoff_A':.4},
            'sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [pdb,args.cache/'uniprot.json',args.cache/'BUBR1_AF_v6.pae.json',args.cache/'NM_001211.6.gb']}}
    (args.out/'metrics.json').write_text(json.dumps(rounded(output),indent=2)+'\n')
    (args.out/'lys_rotamers.json').write_text(json.dumps(rounded(rots),indent=2)+'\n')
    (args.out/'lys_rotamers_jitter.json').write_text(json.dumps(rounded(fine),indent=2)+'\n')
    with (args.out/'rotamer_summary.tsv').open('w') as f:
        keys=['set','chi1','chi2','chi3','chi4','clashes_overlap_gt_0_4A','interresidue_clashes_gt_0_4A','max_overlap_A','NZ_accessible_sphere_fraction']
        w=csv.DictWriter(f,fieldnames=keys,delimiter='\t',lineterminator='\n',extrasaction='ignore');w.writeheader()
        for name,group in [('coarse',rots),('jitter',fine)]:
            w.writerows([{'set':name,**rounded(row)} for row in group])
    with (args.out/'residue_summary.tsv').open('w') as f:
        keys=['position','residue','plddt','sasa_A2','rsa_percent_Tien2013','rsa_percent_Miller1987','rsa_percent_FreeSASA_builtin','backbone_sasa_A2','sidechain_sasa_A2','phi_deg','psi_deg']
        w=csv.DictWriter(f,fieldnames=keys,delimiter='\t',lineterminator='\n',extrasaction='ignore');w.writeheader();w.writerows(rounded(measurements).values())
    print(json.dumps(rounded({'residues':{p:{k:v for k,v in x.items() if k in ['plddt','sasa_A2','rsa_percent_Tien2013','rsa_percent_Miller1987','rsa_percent_FreeSASA_builtin','sasa_SR960_A2','sasa_domain_only_A2','hbond_candidates']} for p,x in measurements.items()},'rotamers':output['rotamer_grid_summary'],'top_rotamers':rots[:3],'transcript':output['transcript']}),indent=2))


if __name__=='__main__': main()
