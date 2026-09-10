# Functional BUBR1 Rescue Windows in Mosaic Variegated Aneuploidy

## Allele-aware prioritization of approved medications, calibrated against wild-type rescue

**Track:** Rare Disease, Real Kid: MVA Hackathon 2026, Track 2.

**Repository:** https://github.com/ivillafuerte/mva-hackathon-2026

**Working team:** Stackfire Networks. **Repository contributor:** ivillafuerte.

**Version:** September 10, 2026. **Status:** research proposal draft; not submitted. Account disclosure, video and repository publication remain outstanding; see [submission readiness](../submission/readiness.md).

## Abstract

BUB1B-associated mosaic variegated aneuploidy (MVA) poses two distinct therapeutic questions: can functional BUBR1 be restored sufficiently to reduce new chromosome-segregation errors, and can downstream tissue dysfunction be mitigated when molecular rescue is incomplete? We investigate the challenge's nominated L737*/N1002K pair using public transcript, population, structural and experimental evidence. Transcript reconstruction supports nonsense-mediated decay susceptibility for L737*, while analysis of the actual human AlphaFold model provides only weak support for N1002K destabilization. Neither molecular phase nor the missense allele's functional mechanism is experimentally established here.

We propose a rescue-calibrated evaluation of existing approved medications rather than a claim of established treatment. Sirolimus is the leading downstream repurposing hypothesis, tested through transient exposure and recovery against continuous exposure. Nicotinic acid is a lower-confidence molecular-rescue candidate that must demonstrate a NAD–SIRT2–BUBR1 effect in the genotype model. Anakinra and everolimus are alternative mechanistic comparators; gentamicin is retained only as a readthrough benchmark because its chronic-use limitations are substantial. The drugs are not proposed as an upfront combination.

Wild-type BUB1B expression provides an experimental reference for recoverable function. Early, delayed, sustained and withdrawn rescue distinguish preventing new errors from reversing established damage. Primary molecular outcomes are errors per completed division, supported by checkpoint and single-cell measurements; tissue benefit is assessed independently. A prenatal mRNA-BUB1B program is a future direction, not the eligible intervention. This submission contributes reproducible allele characterization, transparent candidate prioritization and falsifiable development criteria. It contains no new wet-laboratory efficacy results, fitted therapeutic threshold or patient dosing recommendation.

## 1. Research status and causal interpretation

The participant reports Track 1 Rank Points 100.0 and F-max 1.000 for the BUB1B pair. We treat this as challenge-level support, not independent clinical validation or proof of trans phase. Both variants were reported heterozygous; useful molecular phasing was not available in the handoff. Track 2 did not ingest the private VCF, BAM, CRAM or FASTQ.

| Allele, GRCh38 | MANE consequence | Working interpretation | Critical limitation |
|---|---|---|---|
| chr15:40209701 T>G | NM_001211.6:c.2210T>G; p.Leu737Ter | Likely severe loss of function; NMD susceptibility predicted | Actual RNA decay, truncated protein and residual activity unmeasured |
| chr15:40220612 T>G | NM_001211.6:c.3006T>G; p.Asn1002Lys | Missense candidate; exact mechanism unresolved | No direct N1002K functional experiment retrieved |

BUBR1 contributes to checkpoint signaling and chromosome attachment/alignment. Insufficiency can increase segregation errors and mosaic aneuploidy [R1]. Clinical features supplied by the challenge include rhabdomyosarcoma, nephrocalcinosis, short stature, failure to thrive, skeletal muscle atrophy, prematurity, small-for-gestational-age birth and recurrent parental miscarriages. These features do not establish inflammation, NAD deficiency, mTOR activation, impaired renal function or a particular tumor subtype. No additional clinical facts are inferred.

**Evidence labels:** DIRECT-N1002K; DIRECT-BUBR1; RELATED-MVA-VARIANT; PATHWAY EVIDENCE; COMPUTATIONAL; OUR INFERENCE; SPECULATIVE FUTURE DIRECTION. A regulatory label establishes product status and known risks, not MVA efficacy.

Confirmed public reference identities and computed results are distinguished from participant-reported findings. Unsupported assumptions include inevitable N1002K instability, additive dual-allele rescue, a universal 50% threshold, and normalization of established aneuploid cells following protein supplementation.

## 2. Allele characterization and computed results

### N1002K

**COMPUTATIONAL.** Human UniProt O60566 and AF-O60566-F1-model_v6 were sequence-matched across 1,050 residues. In residues 985–1020, mean/minimum pLDDT were 89.79/77.25. N1002 pLDDT was 91.06; SASA was 27.04 Å², with RSA 13.87% using Tien and 17.11% using Miller reference areas. Side-chain/backbone SASA were 16.35/10.69 Å². L1012 was effectively buried and had pLDDT 95.31. These are actual protein-model results, not the earlier synthetic helix self-test.

N1002 has geometric polar-contact candidates involving the W978 backbone and V998. These are not experimentally established hydrogen bonds. Its Cα is 12.32 Å from L1012. A rigid-backbone search found 22 of 486 locally perturbed lysine conformations below the chosen clash criterion. That count is not a stability probability. No ΔΔG, free energy, experimental half-life or DSSP assignment was calculated. Phi/Psi provide a geometric secondary-structure description. Seven selected vertebrate homologs conserved the aligned Asn; this small, non-independent panel does not establish universal conservation.

**Classification: structure weakly supports destabilization.** It supports testing altered local interactions, but does not show unavoidable steric incompatibility. Normal cellular stability also cannot be inferred. L1012P is an instability control, not a mechanistic substitute for N1002K. The reviewed ClinVar record for the same protein change uses **c.3006T>A**, not the project's T>G allele, and is a VUS; no RNA-level equivalence is assumed [R18].

The decisive experiment equalizes N1002K protein abundance to WT before comparing function. Rescue after equalization supports a dosage component; persistent dysfunction redirects the program toward interaction/function defects. Normal abundance and function require reconsidering the allele's contribution.

### L737*

**COMPUTATIONAL / OUR INFERENCE.** RefSeq reconstruction places the premature stop in exon 17/23, with 73 nucleotides from codon end to the next exon junction and 746 to the final junction. NMD is plausible but unmeasured. The mutant context is:

`5'-UCCCUACCAGAG-[UGA]-AGUGCCUCUGCA-3'`

The +4 base is A, not the C in a favorable motif reported in other systems [R12]. No exact-context readthrough efficiency has been recovered. UGA suppression can insert Cys, Arg or Trp in other proteins, so full-length protein cannot be equated with WT BUBR1 [R13]. The proposed assay must retain endogenous splicing/NMD context, verify both protein termini and identify the incorporated residue when feasible. An intronless reporter alone is insufficient. L737C/R/W and an expressed truncation are functional controls, not presumed therapeutic products. NMD inhibition is not automatically necessary or beneficial; test whether transcript depletion limits rescue before considering it.

## 3. Why functional restoration is a defensible reference

**DIRECT-BUBR1 / RELATED-MVA-VARIANT.** In patient fibroblasts, transient LAP-tagged BUB1B cDNA improved the nocodazole checkpoint response, approaching the parental comparator in 731X/Y155C cells [R1, Fig. 1D]. This supports recovery of a function in affected cells, not correction of all pre-existing karyotypes. Other experiments distinguished low-abundance mutants from stable dysfunctional mutants [R1].

**DIRECT-BUBR1.** Sustained transgenic BubR1 elevation protected mice against instability and selected disease phenotypes [R2]. It does not establish late-start replacement efficacy in this child. Dose-response experiments used different models and endpoints: residual levels of 77%, 58%, 14%, 10% and 8.5% in one study cannot locate a precise threshold between 14% and 58% [R3, abstract reviewed]. Another assay distinguished approximately 13% from 6% residual abundance [R1, Fig. 4D]. We therefore propose genotype- and endpoint-specific curves, not a universal 50% target.

## 4. Approved-drug nomination and ranking

**Nominated candidates are hypotheses for experimental follow-up.** The shortlist below uses a tiered judgment, not a numerical probability of benefit. Market approval is documented for specific US products in the [candidate assessment](../drugs/candidate_assessment.md). None is approved for MVA. Oral formulation, intracellular exposure and fetal delivery are separate questions.

| Priority and role | Drug | Mechanistic rationale | Required evidence to advance |
|---|---|---|---|
| 1: downstream lead | Sirolimus | Test whether transient mTOR inhibition reduces a harmful secretory state while allowing subsequent functional recovery | Relevant pathway state and tissue benefit; no worsening of errors per division or BUBR1 function |
| 2: downstream alternative | Anakinra | Test IL-1-dependent paracrine injury with a more focused pathway intervention | IL-1 dependence and muscle benefit; no inappropriate proliferation of damaged cells |
| 3: rapalog comparator | Everolimus | Compare pharmacology and recovery with sirolimus | A demonstrable advantage over sirolimus, not merely a different drug name |
| 4: molecular-rescue exploration | Nicotinic acid (niacin) | Test whether NAD elevation increases SIRT2-dependent functional BUBR1 | NAD response, BUBR1 target engagement and mitotic benefit; no assumption of baseline deficiency |
| Benchmark, not chronic lead | Gentamicin | Assess whether exact-context L737* readthrough is measurable | Full-length functional product at defensible exposure; toxicity blocks automatic clinical progression |

The leading **disease-mechanism experiment** remains WT BUBR1 rescue; the leading **approved-drug hypothesis by present pathway evidence** is sirolimus. These rankings answer different questions. Nicotinic acid is not promoted above stronger evidence merely to preserve a preferred molecular story.

Sirolimus's rationale combines allele-dependent mTOR activation in a mouse model [R4] with rapamycin effects on the senescence-associated secretory phenotype in human fibroblasts [R5]. Neither demonstrates drug rescue in L737*/N1002K. A brief exposure in R5 had effects after withdrawal, but mTOR remained partly suppressed. Consequently, a useful recovery window is a hypothesis, not an established intermittent regimen. No clinical schedule is proposed.

Anakinra's rationale combines experimental IL-1 receptor antagonism in senescent fibroblasts [R6] with its approved pharmacology. A genetic senescent-cell elimination experiment in BubR1 mice supports studying tissue consequences, but does not prove IL-1 dependence or anakinra efficacy [R7].

For nicotinic acid, direct BUBR1 evidence concerns SIRT2/K668 regulation and NMN experiments [R8]. Human niacin data concern adult mitochondrial myopathy [R9]. The connection from nicotinic acid to functional N1002K is **OUR INFERENCE**. Nicotinamide, NMN and NR are not interchangeable drugs; nicotinamide reduced BUBR1 under inhibitory assay conditions in R8. Raising protein without restoring activity is insufficient.

No upfront combination is selected. After beneficial monotherapies are established, a factorial comparison can test whether molecular rescue and tissue protection add benefit. Sirolimus plus anakinra may converge on the same secretory circuit; synergy is not assumed. New BUB1B mRNA, UPCP and other investigational agents remain outside the nominated approved-drug intervention.

## 5. Contradictions and failure criteria

1. **Genotype specificity:** the mouse mTOR phenotype is allele-dependent [R4]. The human genotype may lack the proposed pathway abnormality.
2. **Muscle effects can oppose the hypothesis:** rapamycin impaired regeneration in one injury model [R10] but improved satellite-cell outcomes in hypercapnia [R11]. Neither establishes the direction in MVA.
3. **Oncology requires an independent assessment:** adding temsirolimus did not improve event-free survival in a phase III rhabdomyosarcoma trial [R14]. This is another drug and clinical setting, but argues against promising a general dual antitumor/MVA benefit. The patient's treatment history and tumor biology are not known here.
4. **Selection can mimic correction:** fewer abnormal cells after treatment may reflect death, slowed division or differential clonal expansion. Report new errors per division with lineage tracking and survival.
5. **Protein supplementation has a distribution problem:** a population average can conceal many unrescued cells. Quantity, cell coverage and duration must be measured separately.
6. **Structure does not settle N1002K:** folding-compatible conformations do not establish normal abundance or functional interactions.
7. **Pregnancy is not an extension of an adult label:** neither drug approval nor a favorable culture result establishes fetal use. No nominated medication is proposed for administration during pregnancy in this report.

Terminate a candidate branch if target engagement fails, apparent benefit is explained by cytotoxicity/cytostasis, function worsens, or effective exposures are pharmacologically implausible. A negative result remains an informative output.

## 6. Validation and temporal rescue

The [experimental development plan](../experiments/development_plan.md) defines controls, analysis units, blinding, dose-response modeling, exposure checks, orthogonal confirmation and stop/go criteria. No prospective measurements or sample sizes are represented as completed.

First establish reference rescue in non-tumor human cells carrying the modeled pair, alongside corrected controls and individual alleles. Modeling in trans is an explicit experimental assumption until participant phasing is resolved. Measure endogenous-context RNA, full-length protein, turnover and localization. Compare N1002K at matched protein abundance with WT and L1012P.

Next compare early versus delayed rescue, continuous exposure versus withdrawal, and different fractions of rescued cells. These conditions separate accumulation prevention, recovery of existing cellular functions and durability. Cell-culture time is not converted into a fetal gestational window. Validate promising outcomes in a relevant tissue model before considering animal development work.

For drugs, keep molecular rescue and downstream tissue protection as separate outcome categories. An anti-inflammatory drug can pass a tissue-benefit gate without being called a BUBR1-restoring drug; it must still pass mitotic safety checks. A drug that only raises BUBR1 abundance fails the functional-rescue gate if errors do not improve.

## 7. Prenatal extension

**SPECULATIVE FUTURE DIRECTION.** Prenatal BUB1B mRNA replacement could test whether transient restoration reduces the accumulation of abnormal lineages during development. Mouse fetal mRNA delivery [R15–R16] and a prenatal/postnatal enzyme-replacement case in Pompe [R17] are precedents for platform and timing, not BUBR1 efficacy. Persistent Cre reporter marking does not demonstrate persistent therapeutic mRNA. BUBR1 requires intracellular function, unlike a secreted replacement protein.

Development must establish tissue and progenitor coverage, dose distribution, duration, repeat-delivery feasibility, maternal/fetal effects, placental exposure, undesired tissue delivery and oncologic consequences. Protein supplementation does not correct the underlying alleles; errors may resume after withdrawal. Intervention after prenatal diagnosis may already follow early embryonic injury. No best gestational window, complete reversibility or cure is claimed. An investigational product cannot become an eligible repurposed drug by sharing a delivery platform with approved products.

## 8. Reproducibility, contribution and limits

The public workflow validates sequence numbering, maps transcript context, calculates model geometry and keeps compact outputs with reference URLs and hashes. Dependencies and commands are in [README](../README.md). Literature screening and ranking were AI-assisted and manually curated in this workflow, not an independent expert-panel review or an exhaustive systematic review. Predictor scores inherited from Track 1 were not recalculated. No private genome was required for these Track 2 calculations.

Scientific rigor comes from traceable claims and falsification criteria; potential impact concerns fewer new errors or preserved tissue function; innovation concerns measuring rescue amount, coverage and timing; scalability concerns reusable allele-specific controls. None guarantees clinical benefit or competition placement. We do not claim that generic mTOR inhibition, prenatal mRNA delivery or NAD supplementation originated in this project.

## 9. AI disclosure and data governance

OpenAI ChatGPT Work/Codex assisted literature discovery, code execution, evidence synthesis and English drafting. Earlier work was reported to involve other AI assistance. The account plan/tier, relevant training/retention settings and any earlier providers must be confirmed by the participant in the [methods declaration](../submission/methods.md) before submission; this report does not certify uninspected account settings. No patient-scale genomic files were uploaded or read in the present Track 2 workspace.

Retain publishable findings and public references; do not publish raw genomic files, genotype-scale derivatives, genome-bearing logs or trained artifacts. Participant registration, the applicable data agreement, deletion attestation and publication restrictions are addressed in the [compliance checklist](../submission/readiness.md). Methods are reported candidly; proposed experiments are never described as completed results.

## References

R1. Suijkerbuijk et al. Cancer Research (2010). PMID 20516114. DOI [10.1158/0008-5472.CAN-09-4319](https://doi.org/10.1158/0008-5472.CAN-09-4319). Patient cells and protein-replacement systems; Fig. 1D, 2–5.

R2. Baker et al. Nature Cell Biology (2013). PMID 23242215. DOI [10.1038/ncb2643](https://doi.org/10.1038/ncb2643). Transgenic mice; Fig. 1–4.

R3. Bohers et al. Human Genetics (2008). PMID 18932004. DOI [10.1007/s00439-008-0572-y](https://doi.org/10.1007/s00439-008-0572-y). HeLa depletion; abstract reviewed.

R4. Sieben et al. JCI (2020). PMID 31738183. DOI [10.1172/JCI126863](https://www.jci.org/articles/view/126863). Mouse alleles; Fig. 5, 8–9. Corrigendum DOI [10.1172/JCI144781](https://www.jci.org/articles/view/144781) corrects Fig. 2E.

R5. Laberge et al. Nature Cell Biology (2015). PMID 26147250. DOI [10.1038/ncb3195](https://doi.org/10.1038/ncb3195). Human fibroblasts; IL1A/SASP and withdrawal, Fig. 7.

R6. Orjalo et al. PNAS (2009). PMID 19805069. DOI [10.1073/pnas.0905299106](https://doi.org/10.1073/pnas.0905299106). HCA2 fibroblasts; Fig. 2–5.

R7. Baker et al. Nature (2011). PMID 22048312. DOI [10.1038/nature10600](https://doi.org/10.1038/nature10600). BubR1 hypomorphic/INK-ATTAC mice; Fig. 2, 4.

R8. North et al. EMBO Journal (2014). PMID 24825348. DOI [10.15252/embj.201386907](https://doi.org/10.15252/embj.201386907). Cells and mice; Fig. 1–3, 6.

R9. Pirinen et al. Cell Metabolism (2020). PMID 32386566. DOI [10.1016/j.cmet.2020.04.008](https://doi.org/10.1016/j.cmet.2020.04.008). Adult mitochondrial myopathy; abstract-level support only here. Linked erratum PMID 32640244; no figure-specific claim is used.

R10. Ge et al. American Journal of Physiology Cell Physiology (2009). PMID 19794149. DOI [10.1152/ajpcell.00248.2009](https://doi.org/10.1152/ajpcell.00248.2009). Muscle injury and transgenic mice.

R11. Balnis et al. JCI Insight (2025; online 2024). PMID 39589836. DOI [10.1172/jci.insight.182842](https://insight.jci.org/articles/view/182842). Hypercapnic mice and muscle cells; Fig. 7–8.

R12. Mangkalaphiban et al. Nature Communications (2024). PMID 38509072. DOI [10.1038/s41467-024-46703-z](https://doi.org/10.1038/s41467-024-46703-z). Readthrough context in human cells.

R13. CFTR readthrough study (2024). PMID 38725656. DOI [10.3389/fphar.2024.1389586](https://doi.org/10.3389/fphar.2024.1389586). Product identity in a different protein.

R14. ARST1431 phase III trial (2024). PMID 38936378. DOI [10.1016/S1470-2045(24)00255-9](https://doi.org/10.1016/S1470-2045(24)00255-9). Rhabdomyosarcoma; Fig. 2.

R15. Riley et al. Science Advances (2021). PMID 33523869. DOI [10.1126/sciadv.aba1028](https://doi.org/10.1126/sciadv.aba1028). Fetal mouse mRNA delivery.

R16. Fetal heart/diaphragm/muscle mRNA delivery (2023). PMID 36844366. DOI [10.1016/j.bioactmat.2023.02.011](https://doi.org/10.1016/j.bioactmat.2023.02.011). Mouse reporter/editing models.

R17. Cohen et al. NEJM (2022). PMID 36351280. DOI [10.1056/NEJMoa2200587](https://doi.org/10.1056/NEJMoa2200587). One prenatal Pompe case with postnatal treatment.

R18. Public references: [UniProt O60566](https://www.uniprot.org/uniprotkb/O60566/entry), [AlphaFold](https://alphafold.ebi.ac.uk/entry/O60566), [RefSeq NM_001211.6](https://www.ncbi.nlm.nih.gov/nuccore/NM_001211.6), [ClinVar L737*](https://www.ncbi.nlm.nih.gov/clinvar/variation/533901/), [ClinVar alternative N1002K DNA allele](https://www.ncbi.nlm.nih.gov/clinvar/variation/4600147/), [challenge dataset landing page](https://huggingface.co/datasets/SageBio/mva-hackathon-2026-data). The formal dataset citation required at publication must be copied from the organizer's Synapse record; it has not been independently resolved here.

## Required acknowledgment

This work was made possible through the Hackathon, organized by Sage Bionetworks in partnership with the MVA Society, Hugging Face, and BEACON (The Benchmarking, Evaluation, and Assessment Consortium for Science), with prize sponsorship from AWS and Anthropic. We are deeply grateful to the child and their family who generously contributed their data and their story to advance research into this rare disease. We acknowledge their trust in making this Hackathon possible.

## Final computational verification

On September 10, a repeat execution with freshly installed pinned dependencies reproduced the complete metrics JSON and both residue/rotamer tables exactly. All public reference input hashes matched the audited manifest. An initial native execution failure and truncated public PAE cache were resolved before this comparison. Script syntax and package consistency checks also passed. These checks do not establish biological efficacy.
