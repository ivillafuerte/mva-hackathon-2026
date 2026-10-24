# Research status audit: allele mechanisms and actual structure

Analysis date: September 8, 2026. English technical edition: September 10, 2026. Base repository commit: `fec5404dd63e03896d43e9b258551657a2b7f0bd`. The current submission narrative and rules checklist supersede historical prioritization in this note.

## Decision

**Structure weakly supports N1002K destabilization.** A conserved, partly buried asparagine participates in a modeled polar environment, but some lysine conformations fit the fixed WT backbone and expose the charged terminus. Neither reduced stability nor normal stability in cells is established. Keep stabilization conditional on abundance/half-life measurements and matched-protein functional rescue.

## Evidence status

| Status | Finding | Limit |
|---|---|---|
| Public reference confirmation | Human O60566 has 1,050 residues; numbering matches RefSeq/model | WT model, not mutant experimental structure |
| Participant report | Track 1 score 100.0 / 1.000 | Individual leaderboard was not independently reauthenticated |
| Strong annotation evidence | L737* ClinVar pathogenic/likely pathogenic | Does not measure RNA/protein in this child |
| Related-variant evidence | Some BUBR1 variants show reduced abundance and rescue after equalization | Does not establish N1002K mechanism |
| Weak computational evidence | Conserved local polar environment | Cannot distinguish stability from interaction defects |
| Unresolved | Molecular trans phase | Requires direct segregation or suitable read-backed evidence |
| Unsupported | Universal 50% therapeutic cutoff | Different models/endpoints give different dose-response behavior |
| Missing | Allele-specific functional protein contribution | Cannot infer by adding total protein amounts |

No private genome was accessed. The prior Claude synthetic helix values are excluded. This code is an independent implementation, not a review or execution of Claude's original script.

## Variant annotations

L737*: NM_001211.6:c.2210T>G, TTA to TGA. ClinVar VCV000533901.9 is pathogenic/likely pathogenic; the MVA-specific RCV has a single-submitter pathogenic assertion. A historical population-quality concern in a ClinVar comment is not automatically resolved by currently empty API filters. Public gnomAD exomes reproduced AC 115 / AN 1,461,846. Read-level quality was not reviewed. [ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/variation/533901/), [gnomAD](https://gnomad.broadinstitute.org/variant/15-40209701-T-G?dataset=gnomad_r4).

N1002K: the T>G allele reproduced AC 1 / AN 1,461,878 in public gnomAD exomes. Predictor scores from the handoff were not recalculated. ClinVar VCV004600147.1 represents c.3006T>A, also producing N1002K, with a VUS assertion and no functional evidence identified. Do not merge genomic alleles or assume identical RNA effects. Literal Europe PMC retrieval found no exact-variant experimental paper; absence of retrieved results is not proof of absence. [ClinVar alternate DNA allele](https://www.ncbi.nlm.nih.gov/clinvar/variation/4600147/), [gnomAD T>G](https://gnomad.broadinstitute.org/variant/15-40220612-T-G?dataset=gnomad_r4).

## Structural results — COMPUTATIONAL

Model: AF-O60566-F1-model_v6, exact canonical sequence match. Residues 985–1020: `SELKDGELWNKFFVRILNANDEATVSVLGELAAEMN`. Mean/minimum/maximum pLDDT: 89.79389 / 77.25 / 95.69.

| Metric | N1002 | L1012 |
|---|---:|---:|
| pLDDT | 91.06 | 95.31 |
| Total SASA, Å² | 27.03844 | 0.00086 |
| RSA Tien, % | 13.86587 | 0.00043 |
| RSA Miller, % | 17.11294 | 0.00048 |
| RSA FreeSASA reference, % | 18.64592 | 0.00048 |
| Side-chain SASA, Å² | 16.34876 | 0.00086 |
| Backbone SASA, Å² | 10.68969 | 0 |
| Phi / Psi, degrees | -126.60 / 37.28 | -66.39 / -47.24 |
| Nonlocal residues at 4 / 5 / 8 Å | 4 / 6 / 23 | 10 / 11 / 29 |

FreeSASA 2.2.1: Lee–Richards, 1.4 Å probe, 100 slices. A 960-point Shrake–Rupley cross-check gave 26.67841 Å² for N1002 and zero for L1012. The isolated 750–1045 domain gave the same local SASA as full-length protein. RSA denominators differ by scale. N1002 is non-alpha by Phi/Psi; L1012 is alpha-like. DSSP was not run. PDB 5KHU/Q and 6TLJ/S observed coordinates do not cover these residues; deposited sequence is not observed atomic coverage. [AlphaFold](https://alphafold.ebi.ac.uk/entry/O60566), [UniProt](https://www.uniprot.org/uniprotkb/O60566/entry), [Tien reference](https://doi.org/10.1371/journal.pone.0080635).

Polar-contact candidates: N1002 OD1–W978 backbone N, 2.825 Å; ND2–W978 O, 2.948 Å; ND2–V998 O, 2.827 Å. No explicit hydrogens, water or energetic validation is included. No acidic charged atom was within 8 Å of the WT Asn side chain; Arg999 NH1 was approximately 6.95 Å away. No new salt bridge was established in the tested geometries. N1002–L1012 distances: Cα 12.31954 Å, closest heavy atoms 10.34879 Å.

The 81-conformation coarse lysine grid had clashes under a >0.4 Å overlap criterion, with minimum maximum overlap 0.42967 Å. Local chi perturbation produced 486 conformations, 22 below the clash criterion. A maximum NZ probe-sphere accessibility of 46.04% is not residue RSA or functional protein percentage. Counts are not equilibrium probabilities; no relaxation, folding energy or ΔΔG is claimed. This contradicts inevitable steric destruction, not every possible stability defect.

Seven selected vertebrate homologs conserved aligned N1002 and L1012. Most entries were unreviewed; the panel is not a curated phylogeny and species are not independent samples. The AlphaFold MSA download was unavailable. Selection and alignment rules are in the conservation script.

## Comparator evidence

Suijkerbuijk 2010, PMID 20516114, DOI [10.1158/0008-5472.CAN-09-4319](https://doi.org/10.1158/0008-5472.CAN-09-4319): patient cell lines and protein-replacement systems.

| Variant | Observation | Location |
|---|---|---|
| I909T | Preserved RNA, increased turnover, HSP90 dependence; checkpoint rescue after abundance matching | Fig. 3–4 |
| L1012P | Low protein and proteasome/HSP90-related instability; matched-abundance rescue | Fig. 2–4 |
| R727C | Preserved RNA and increased turnover | Fig. 3 |
| R814H | Low abundance; do not assign every I909T experiment to this variant | Fig. 2 |
| Q921H | WT-like results in reported assays | Fig. 4, supplement |
| Y155C | Stable in replacement experiments but checkpoint-defective | Fig. 2, 5 |
| 731X | Functional rescue in selected assays despite truncation | Fig. 5 |
| N1002K | No direct functional experiment retrieved | Unresolved |

731X is not identical to L737*. Mouse L1002P represents human L1012P, not human N1002K. Allelic phenotypes differ despite similar total abundance in some models: PMID 31738183, DOI [10.1172/JCI126863](https://www.jci.org/articles/view/126863), Fig. 6–9. Its corrigendum corrects Fig. 2E; that panel is not the stability basis here.

The kinase/pseudokinase region name does not settle human catalytic activity. Species and assay differences matter: PMID 22698286, DOI [10.1016/j.devcel.2012.03.009](https://doi.org/10.1016/j.devcel.2012.03.009); PMID 31201382, DOI [10.1038/s41422-019-0178-z](https://doi.org/10.1038/s41422-019-0178-z). Test relevant human functions rather than selecting a label for convenience.

## Nonsense and functional-dose findings

The L737* stop is in exon 17/23 at RNA positions 2361–2363; codon-end distances are 73 nt to the next junction and 746 nt to the last. Mutant context: `UCCCUACCAGAG-[UGA]-AGUGCCUCUGCA`. NMD susceptibility is inferred; the +4 A is not the favorable +4 C reported elsewhere. Full-length readthrough may contain non-Leu residues and needs product/function confirmation. The exact L737* response from a large reporter dataset was not recovered. See the current report R12–R13 and candidate assessment.

Bohers 2008 residual abundances 77%, 58%, 14%, 10%, 8.5% were reviewed at abstract level (PMID 18932004; DOI 10.1007/s00439-008-0572-y). The gap from 14% to 58% cannot establish a 50% cutoff. Another study compared approximately 13% and 6% in a different assay. Abundance is not automatically functional dose. An additive two-allele formula is a conceptual approximation only; interaction, timing and per-cell distribution remain unknown.

SIRT2/K668 and NMN evidence (PMID 24825348; DOI 10.15252/embj.201386907) does not demonstrate niacin rescue of N1002K. Nicotinamide's inhibitory assay effects cannot be transferred to nicotinic acid or ignored by treating all NAD precursors as equivalent.

## Current follow-up

Use the matched-abundance experiment, the WT rescue reference and the exact-context readthrough assay described in the current development plan. Candidate nomination, current requirements and the acknowledgment are in the main report; this technical record should be distributed with that report. This audit is not clinical validation or a completed drug screen.
