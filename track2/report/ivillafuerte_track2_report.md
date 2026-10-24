# BUB1B Virtual Lab: Evidence-Guided Drug Repurposing

## Allele-aware hypotheses and functional validation for mosaic variegated aneuploidy

**Track:** Rare Disease, Real Kid: MVA Hackathon 2026, Track 2.

**Working team:** Stackfire Networks. **Repository contributor:** ivillafuerte.

**Version:** October 24, 2026 (review copy). **Scientific snapshot:** `mva-results-2026-10-17-immunotherapy-audit-v1`, data as of October 17. The report revision date is not a new experimental-result date.

**Research status:** computational evidence synthesis and proposed functional validation. No exact-genotype pharmacological rescue has been established. Candidate eligibility and the organizer-prescribed dataset citation remain unresolved.

**Repository:** https://github.com/ivillafuerte/mva-hackathon-2026/tree/research/track2-functional-rescue/track2

**Evidence workspace:** https://www.stackfire.com/labs/biolab/mvabub1b

**Pitch video:** https://youtu.be/u527j7tO0OA (displayed duration: 2:57).

## Abstract

Which drug hypotheses deserve the next experiment? We use the challenge-nominated BUB1B L737\*/N1002K pair to connect public evidence with falsifiable candidate decisions. L737\* introduces premature termination, with nonsense-mediated decay (NMD) susceptibility predicted rather than measured for the exact variant. N1002K stability and residual function remain unresolved. Neither increased RNA nor increased protein alone establishes functional BUBR1 rescue.

The virtual lab records four quantitative reanalyses, six qualitative evidence audits and one explicitly synthetic software test. A reanalysis of normal human fibroblasts found a BUB1B-spanning RNA-feature mean 41.43% lower after continuous rapamycin than in proliferative vehicle controls; it does not support an RNA-increase rationale for sirolimus in that model. A separate readthrough analysis found no exact L737\* measurement among the analyzed contexts. These observations constrain prioritization; they do not demonstrate pharmacological rescue.

Amlexanox is a conditional research candidate: other-gene functional evidence is counterbalanced by negative neuronal findings and reported neurite toxicity. Montelukast is a conditional NMD-modulation hypothesis that depends on useful residual function of the exact truncated protein. Gentamicin plus mefloquine remains an experimental branch only. Immunotherapy is deprioritized for BUB1B disease rescue because tumor control is a different endpoint. No current market-approval or systemic-use eligibility is inferred from a historical amlexanox oral-paste label.

The decisive next experiment uses matched controls to measure allele-specific RNA and protein, checkpoint response and segregation errors per completed division, with viability and proliferation tracked independently. The contribution is a traceable evidence-to-decision framework, supported by public allele computations and a versioned evidence workspace. No exact-genotype pharmacological rescue is established; wet-laboratory validation remains future work. This is not a treatment recommendation.

## 1. Research status and causal interpretation

The participant reports Track 1 Rank Points 100.0 and F-max 1.000 for the BUB1B pair. We treat this as challenge-level support, not independent clinical validation or proof of trans phase. Both variants were reported heterozygous; useful molecular phasing was not available in the handoff. The source Track 2 methods report that its workspace did not ingest private VCF, BAM, CRAM or FASTQ files.

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

### L737\*

**COMPUTATIONAL / OUR INFERENCE.** RefSeq reconstruction places the premature stop in exon 17/23, with 73 nucleotides from codon end to the next exon junction and 746 to the final junction. NMD is plausible but unmeasured. The mutant context is:

`5'-UCCCUACCAGAG-[UGA]-AGUGCCUCUGCA-3'`

The +4 base is A, not the C in a favorable motif reported in other systems [R12]. No exact-context readthrough efficiency has been recovered. UGA suppression can insert Cys, Arg or Trp in other proteins, so full-length protein cannot be equated with WT BUBR1 [R13]. The proposed assay must retain endogenous splicing/NMD context, verify both protein termini and identify the incorporated residue when feasible. An intronless reporter alone is insufficient. L737C/R/W and an expressed truncation are functional controls, not presumed therapeutic products. NMD inhibition is not automatically necessary or beneficial; test whether transcript depletion limits rescue before considering it.

## 3. Why functional restoration is a defensible reference

**DIRECT-BUBR1 / RELATED-MVA-VARIANT.** In patient fibroblasts, transient LAP-tagged BUB1B cDNA improved the nocodazole checkpoint response, approaching the parental comparator in 731X/Y155C cells [R1, Fig. 1D]. This supports recovery of a function in affected cells, not correction of all pre-existing karyotypes. Other experiments distinguished low-abundance mutants from stable dysfunctional mutants [R1].

**DIRECT-BUBR1.** Sustained transgenic BubR1 elevation protected mice against instability and selected disease phenotypes [R2]. It does not establish late-start replacement efficacy in this child. Dose-response experiments used different models and endpoints: residual levels of 77%, 58%, 14%, 10% and 8.5% in one study cannot locate a precise threshold between 14% and 58% [R3, abstract reviewed]. Another assay distinguished approximately 13% from 6% residual abundance [R1, Fig. 4D]. We therefore propose genotype- and endpoint-specific curves, not a universal 50% target.

## 4. Evidence that changed candidate decisions

### 4.1 A check on the sirolimus rationale

**COMPUTATIONAL REANALYSIS; not a new biological experiment.** In GSE65145, the selected unstranded genomic-span RNA feature encompassing BUB1B had vehicle replicate values 6.227185 and 5.570779 RPKM, reduced-serum values 1.2674783 and 0.9291951, and rapamycin values 3.7114706 and 3.198672. The rapamycin/proliferative-vehicle mean ratio is 0.585706, or **41.43% lower**. The study used normal 2DD fibroblasts, two biological replicates per condition, continuous 500 nM rapamycin for five days [O1; record `MVA-RAP-GSE65145-001`].

The observation concerns a deposited RNA feature, not a validated mature BUB1B isoform estimate or BUBR1 protein. No washout, checkpoint, chromosome-segregation or rescue endpoint was measured in this reanalysis. Reduced serum is not cell-cycle matched. Overlapping locus features are sensitivity views, not extra biological replicates. No new significance test, confidence interval or clinical probability is inferred. The 149,122 rows in each deposited track differ from the paper's stated 149,135 probes; that discrepancy remains unresolved.

This finding **does not support an RNA-abundance-increase rationale for sirolimus in this model**. It neither proves a protein decrease nor excludes post-transcriptional or downstream effects. The September sirolimus-first prioritization is therefore superseded by the conditional shortlist below; sirolimus remains a mechanistic comparator, not an established rescue lead. The original downstream mTOR/SASP rationale [R4–R5] remains background evidence rather than a demonstrated treatment effect in the exact genotype.

### 4.2 Nearby readthrough is not exact-variant evidence

**COMPUTATIONAL REANALYSIS.** The analyzed 5,837-PTC table does not provide an exact L737\* measurement or exact six-flanking-base match. Twelve nearby contexts have untreated and gentamicin median reporter readthrough of 0.1745% and 0.1985%, respectively. The **median paired increment is 0.0165 percentage points**, not the difference between those two medians and not “0.0165% rescue” [O2; `MVA-RT-002`]. Reporter sequences are not endogenous BUB1B. These numbers cannot predict L737\* efficacy, native-leucine incorporation or a patient's outcome.

### 4.3 RNA, protein, checkpoint and segregation are separate gates

**REANALYSIS / EVIDENCE AUDIT.** Montelukast's three normalized NMD/non-NMD RNA ratios in published mouse Neuro-2a reporters are 1.3153820850896314, 3.406494677098417 and 1.7654686351224798. The published permutation q = 0.02115 is not a therapeutic probability. Reporter dependence, non-NMD isoform changes and unavailable replicate Ct values prevent interpreting those summaries as BUB1B-specific decay inhibition [O3; `MVA-NMD-003`].

Published checkpoint-control source data give median nocodazole-challenge arrest durations of 650 minutes for WT and 60 for D137R, from 27 and 39 cells in a representative replicate. These are **not drug arms, N1002K measurements or independent biological replicates**; no between-replicate precision is inferred [O4; `MVA-CTRL-006`].

Related BUBR1 variants can show checkpoint rescue after matching protein abundance, while equally expressed B56-binding mutants still fail chromosome-congression rescue [R1, O5]. Neither comparator substitutes for N1002K. The equal-expression gate must therefore measure function independently; checkpoint-only improvement is not relabeled segregation rescue [`MVA-N1002K-GATE-002`].

### 4.4 Current conditional shortlist

[Organizer guidance](https://huggingface.co/spaces/SageBio/rare-disease-real-kid-mva-hackathon-2026/discussions/5) permits combinations of market-approved medications when each component and the combination are justified. This does not establish efficacy, safety or approval of the proposed combination. Investigational or trial-stage compounds are outside the stated Track 2 medication scope.

Priorities are research branches, not a numeric efficacy ranking or a prescribed combination. Current product, jurisdiction, formulation and competition eligibility must be checked separately for each nominated medication. **Amlexanox remains eligibility-unresolved**, not an asserted market-approved systemic MVA lead.

| Candidate / role | Evidence supporting investigation | Contrary evidence / unresolved gap | GO: evidence required to advance | STOP: evidence that rejects this branch |
|---|---|---|---|---|
| **Amlexanox — conditional** | Functional CFTR response in another-gene model [O6] | Negative NEFL rescue with neurite toxicity; GDAP1 staining alone does not prove full-length product; no exact L737\* functional rescue [O7–O8] | At matched, defensible exposure, identify the translated protein and demonstrate allele-specific target engagement, checkpoint and segregation benefit with preserved viability; separately resolve product/formulation eligibility | No exact-context target engagement; no correctly identified useful protein despite RNA increase; checkpoint/segregation worsens; apparent benefit explained by cytostasis or toxicity; required unbound exposure is not pharmacologically credible. Unresolved product eligibility blocks nomination, not all mechanistic research |
| **Montelukast — conditional NMD hypothesis** | Other-gene reporter RNA increase [O3] | NMD inhibition leaves the stop codon; exact L737\* NMD sensitivity and residual protein function are unknown | First show that exact L737\* yields a useful product under controlled expression; then show allele-specific endogenous RNA stabilization produces functional benefit beyond altered proliferation at credible exposure | Exact truncated product has no useful function or worsens mitosis; no endogenous allele-specific engagement; RNA rises without functional gain; toxicity/cytostasis explains the signal. A reporter-only increase cannot pass |
| **Gentamicin + mefloquine — experimental only** | COL4A5 reporter combination evidence [O9] | Exact BUB1B context absent; other-gene G418/ELX-02 results are not gentamicin evidence [O10]; systemic exposure and safety constraints (see product/exposure fiche) | Test each component and the combination in endogenous or splice-preserving exact context; confirm full-length protein identity and separate checkpoint/segregation rescue, with vehicle and corrected controls and exposure verification | No exact-context full-length product or no functional rescue; combination does not improve the prespecified functional endpoint versus the relevant component; worsened mitotic errors, viability, or unacceptable exposure margin. Do not call an additive signal synergy |
| **Sirolimus — comparator / downstream branch, not lead** | Earlier mTOR/SASP pathway evidence [R4–R5] | Normal-fibroblast reanalysis shows lower, not higher, BUB1B RNA signal; no exact-genotype rescue | Establish the relevant pathway abnormality and a separately specified tissue/functional endpoint; retain equal-proliferation controls and mitotic safety checks | Pathway abnormality absent; benefit disappears under cell-cycle/lineage controls; checkpoint or segregation worsens. Failure of an RNA-increase rationale does not itself test every downstream mechanism |

These are **prospective falsification criteria**, not completed experiments or retrospectively optimized numerical cutoffs. Before generating validation data, preregister the primary functional endpoint, independent biological units, minimally meaningful effect, uncertainty criterion and toxicity/exposure bounds. A result lacking adequate precision is inconclusive, not a GO. Failure rejects the stated mechanism/model/exposure branch; it is not evidence that a medicine is ineffective for its approved indications. No candidate switch or treatment regimen is proposed.

The [product and exposure evidence fiche](https://github.com/ivillafuerte/mva-hackathon-2026/blob/b85dfb2aa8f28b691318d31c29d6b846bab77b3d/track2/drugs/product_exposure_fiche.md) separates dosage-form concentration, total plasma concentration, unbound exposure and experimental-medium concentration. Product approval, current market availability, systemic target exposure and hackathon eligibility are four separate questions.

A related 731X construct motivates testing truncated-protein function, but it is a frameshift product with about 715 native residues, not a clean L737\* surrogate [R1; `MVA-L737-NMD-FIRST-001`]. Preserving a nonfunctional transcript may not help. Amlexanox's positive and negative studies differ by gene, cell state, concentration and duration; they cannot define a BUB1B therapeutic window. Its historical 5% oral-paste label [O11] does not establish a systemic formulation, MVA efficacy or competition eligibility. The October 22 FDA product check lists that US dental-paste product as discontinued; this does not establish why or imply a safety withdrawal. Current systemic product status and a quantitative human systemic exposure bridge remain unresolved; see the primary sources and formulation-specific comparisons in the [exposure fiche](https://github.com/ivillafuerte/mva-hackathon-2026/blob/b85dfb2aa8f28b691318d31c29d6b846bab77b3d/track2/drugs/product_exposure_fiche.md).

**Not promoted:** arimoclomol lacks direct BUBR1/N1002K rescue evidence in the targeted audit; conditional and negative heat-shock responses prevent treating approval for another disease as target engagement [`MVA-ARI-007`]. Anakinra, everolimus and nicotinic acid remain documented historical alternatives, not the current video's lead nominations. The September [candidate assessment](https://github.com/ivillafuerte/mva-hackathon-2026/blob/b85dfb2aa8f28b691318d31c29d6b846bab77b3d/track2/drugs/candidate_assessment.md) retains their evidence with an explicit supersession notice. No upfront three-drug cocktail or synergy is proposed. The gentamicin–mefloquine branch is a hypothesis to compare experimentally, not a validated regimen.

The rules and organizer clarification reviewed October 24 do not specify eligible jurisdictions or whether a discontinued but historically approved product qualifies. The [FDA application record for Aphthasol](https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?ApplNo=020511&event=overview.process) lists the 5% dental paste as discontinued; this does not establish a safety withdrawal or current systemic eligibility. Historical approval alone therefore does not establish entry eligibility. Amlexanox remains an eligibility-unresolved research hypothesis, not a verified eligible systemic lead.

### 4.5 Immunotherapy: disease rescue is not tumor control

**QUALITATIVE EVIDENCE AUDIT.** Genetic senescent-cell ablation in BubR1-deficient mice is not immunotherapy. uPAR CAR T findings came from different mouse models, while HER2 CAR T and checkpoint-inhibitor sarcoma studies address antitumor outcomes, not correction of BUB1B dysfunction. Senescent, aneuploid and malignant cells are not interchangeable. The audited sources establish no exact-genotype immunotherapy rescue, and experimental CAR T products are not asserted eligible repurposed medications. Immunotherapy is **deprioritized for BUB1B disease rescue**, not dismissed as an oncology research area [R7; snapshot sources `amor-2024`, `her2-sarcoma-2024`, `nivolumab-2020`, `nivolumab-ipilimumab-2022`; `MVA-IMMUNE-011`].

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

The [experimental development plan](https://github.com/ivillafuerte/mva-hackathon-2026/blob/b85dfb2aa8f28b691318d31c29d6b846bab77b3d/track2/experiments/development_plan.md) defines controls, analysis units, blinding, dose-response modeling, exposure checks, orthogonal confirmation and stop/go criteria, now aligned to the conditional branches in section 4. No prospective measurements or sample sizes are represented as completed.

First establish reference rescue in non-tumor human cells carrying the modeled pair, alongside corrected controls and individual alleles. Modeling in trans is an explicit experimental assumption until participant phasing is resolved. Measure endogenous-context RNA, full-length protein, turnover and localization. Compare N1002K at matched protein abundance with WT and L1012P.

Next compare early versus delayed rescue, continuous exposure versus withdrawal, and different fractions of rescued cells. These conditions separate accumulation prevention, recovery of existing cellular functions and durability. Cell-culture time is not converted into a fetal gestational window. Validate promising outcomes in a relevant tissue model before considering animal development work.

For drugs, keep molecular rescue and downstream tissue protection as separate outcome categories. An anti-inflammatory drug can pass a tissue-benefit gate without being called a BUBR1-restoring drug; it must still pass mitotic safety checks. A drug that only raises BUBR1 abundance fails the functional-rescue gate if errors do not improve.

## 7. Prenatal extension

**SPECULATIVE FUTURE DIRECTION.** Prenatal BUB1B mRNA replacement could test whether transient restoration reduces the accumulation of abnormal lineages during development. Mouse fetal mRNA delivery [R15–R16] and a prenatal/postnatal enzyme-replacement case in Pompe [R17] are precedents for platform and timing, not BUBR1 efficacy. Persistent Cre reporter marking does not demonstrate persistent therapeutic mRNA. BUBR1 requires intracellular function, unlike a secreted replacement protein.

Development must establish tissue and progenitor coverage, dose distribution, duration, repeat-delivery feasibility, maternal/fetal effects, placental exposure, undesired tissue delivery and oncologic consequences. Protein supplementation does not correct the underlying alleles; errors may resume after withdrawal. Intervention after prenatal diagnosis may already follow early embryonic injury. No best gestational window, complete reversibility or cure is claimed. An investigational product cannot become an eligible repurposed drug by sharing a delivery platform with approved products.

## 8. Evidence workspace, reproducibility and limits

The website's snapshot contains **11 records: four reanalyses, six evidence audits and one software test**, with **four quantitative reanalysis charts**. Record counts are not biological experiment counts. The charts have different units and models and must not be combined into a drug-efficacy leaderboard. Interactive conceptual illustrations and preset research guidance do not run experiments or calculate drug efficacy. No independent human scientific review is claimed.

| Record | Type | Role in the decision |
|---|---|---|
| `MVA-NMD-003` | Reanalysis | Montelukast remains conditional; reporter RNA is not BUBR1 function. |
| `MVA-RT-002` | Reanalysis | Exact L737\* context absent; nearby readthrough is not a prediction. |
| `MVA-CTRL-006` | Reanalysis | Checkpoint competence needs its own control; no drug effect measured. |
| `MVA-N1002K-GATE-002` | Evidence audit | Require equal-expression and separate segregation testing. |
| `MVA-L737-NMD-FIRST-001` | Evidence audit | Test exact truncated-protein function before NMD-first progression. |
| `MVA-ARI-007` | Evidence audit | Arimoclomol not promoted without BUBR1 target engagement. |
| `MVA-FUNC-005` | Software test | Synthetic denominator fixture only; no sirolimus activity measured. |
| `MVA-RAP-GSE65145-001` | Reanalysis | RNA-feature decrease constrains the sirolimus rationale. |
| `MVA-RT-TRANSFER-009` | Evidence audit | Other-gene endogenous-protein findings do not establish BUB1B transfer. |
| `MVA-AMLEXANOX-010` | Evidence audit | Positive and contrary evidence keep amlexanox conditional. |
| `MVA-IMMUNE-011` | Evidence audit | Tumor control does not establish disease rescue. |

### What was reproduced, and what remains outside that check

The September public workflow checks sequence numbering, transcript context and structural geometry, with pinned dependencies, compact outputs and reference hashes in [README](https://github.com/ivillafuerte/mva-hackathon-2026/blob/b85dfb2aa8f28b691318d31c29d6b846bab77b3d/track2/README.md). The September reproduction audit is historical evidence of those computations, not a rerun of the October reanalyses.

The [frozen public snapshot](https://github.com/ivillafuerte/mva-hackathon-2026/blob/b85dfb2aa8f28b691318d31c29d6b846bab77b3d/track2/evidence/mva-results-2026-10-17.json) remains unchanged (SHA-256 `678706bf000be1d358af6317af5a03136291ae35889e6fccbbeeb8ce9f66d1e3`). The initial October 22 update checked its consistency only. The subsequent reproduction audit recovered the original four analysis scripts, kept their bytes unchanged, removed prior outputs and reran the deterministic calculations from public processed sources. New retrieval/check wrappers are explicitly identified; the website JSON is **never an analysis input**.

| Reanalysis | Checked result | Boundary that remains |
|---|---|---|
| GSE65145 rapamycin | Original output hash reproduced; six public processed tracks and metadata retrieved and checked | Archived public UCSC annotation preserves its retrieval timestamp; this is not raw-read realignment. The 149122/149135 row-count discrepancy remains unresolved |
| NMD screen | Selected-candidate CSV reproduced; source workbook ratios and deterministic screen calculations rerun | Published permutation results are reused; no original stochastic permutation rerun or new biological-replicate uncertainty. Unused article HTML was omitted, so the new summary input inventory differs transparently |
| PTC nearest-context analysis | Original result hash reproduced from complete publisher workbook; original tests pass | Eight-row public prediction extract is archived; full Figshare extraction/upstream mapping is not rerun. Measured nearest-context observations are not exact-L737\* efficacy predictions |
| Checkpoint controls | Original result hash reproduced from publisher individual-cell source table | Representative replicate, not biological replication; not a drug or N1002K experiment |

The [clean-checkout instructions, source manifest and executable originals](https://github.com/ivillafuerte/mva-hackathon-2026/blob/b85dfb2aa8f28b691318d31c29d6b846bab77b3d/track2/reproduction/README.md) specify dependencies, commands, expected artifacts, fresh-download checks and exclusions. The dated execution audit records what actually ran; no treatment efficacy, clinical exposure or biological validity follows from matching computational hashes. No source measurements, historical structural outputs or website chart values were edited to obtain agreement. Current systemic exposure and product eligibility—particularly for amlexanox—remain unresolved in the [exposure fiche](https://github.com/ivillafuerte/mva-hackathon-2026/blob/b85dfb2aa8f28b691318d31c29d6b846bab77b3d/track2/drugs/product_exposure_fiche.md).

Public access to the research branch does not mean it has been merged into main or submitted. No new wet-lab experiment, efficacy score or clinical prediction was generated.

Literature screening was AI-assisted and curated in this workflow, not an exhaustive systematic review or independent expert-panel assessment. Source access limits remain in the snapshot; this report revision does not claim to have re-reviewed inaccessible primary full texts. Existing structural outputs, source measurements and original chart values were not modified to match the narrative. Predictor scores from Track 1 were not recalculated, and no private genome-scale files were needed for this revision.

Scientific rigor comes from explicit models, contradictory evidence and falsification criteria. Potential impact concerns choosing more informative experiments, not demonstrated clinical benefit. Innovation and scalability concern a reusable evidence-to-decision process across variant mechanisms. No competition placement or scientific superiority is predicted.

## 9. AI disclosure and data governance

OpenAI ChatGPT Work/Codex supported literature discovery, code execution, evidence synthesis and English drafting; the participant reports the ChatGPT plan as “Premium” (name as reported, not relabeled Pro or Business). Anthropic Claude Max was used to generate the web laboratory. On October 24, 2026, the participant confirmed that use of conversations to improve the models was disabled in both ChatGPT and Claude during the project. These plan and setting statements are participant attestations, not an independent account audit; they do not establish zero retention.

The participant also stated that no patient data were shared with AI services. The source methods nevertheless document the challenge-derived small variant pair and permitted phenotype summary, so this statement is not treated as evidence that no case-derived information entered the workflow. The source Track 2 report states that its workspace did not upload or read patient-scale genomic files; no broader claim about earlier local Track 1 analysis or all account activity is inferred. Exact historical model identifiers and the scope of earlier Claude analysis assistance remain unverified.

Retain publishable findings and public references; do not publish raw genomic files, genotype-scale derivatives, genome-bearing logs or trained artifacts. Participant registration, the applicable data agreement, deletion attestation and publication restrictions are addressed in the [compliance checklist](https://github.com/ivillafuerte/mva-hackathon-2026/blob/b85dfb2aa8f28b691318d31c29d6b846bab77b3d/track2/submission/readiness.md). Methods are reported candidly; proposed experiments are never described as completed results.

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

R18. Public references: [UniProt O60566](https://www.uniprot.org/uniprotkb/O60566/entry), [AlphaFold](https://alphafold.ebi.ac.uk/entry/O60566), [RefSeq NM_001211.6](https://www.ncbi.nlm.nih.gov/nuccore/NM_001211.6), [ClinVar L737\*](https://www.ncbi.nlm.nih.gov/clinvar/variation/533901/), [ClinVar alternative N1002K DNA allele](https://www.ncbi.nlm.nih.gov/clinvar/variation/4600147/). The challenge dataset is documented separately in R19.

R19. Sage Bionetworks (SageBio). *Rare Disease, Real Kid: MVA Hackathon 2026 – Dataset*. [Hugging Face dataset card](https://huggingface.co/datasets/SageBio/mva-hackathon-2026-data); [official Synapse project syn76251147, wiki 642892](https://www.synapse.org/Synapse:syn76251147/wiki/642892). Public metadata accessed October 24, 2026. Observed Hugging Face repository revision: `9f155b06551c3a16b6ccc1eb3e06ac4f84ebd24c` (last modified October 13, 2026); this identifies metadata observed at review, not a verified historical analysis input version. This metadata-based reference is not represented as the organizer-prescribed citation: that reference was not found in the complete public Synapse wiki or dataset card inspected. No DOI was verified.

## October evidence references

These references are traceable to the preserved October 17 snapshot. They support model-specific observations and research hypotheses, not an exact-genotype treatment claim.

O1. [Gillespie et al. — rapamycin and normal human fibroblast transcription](https://pmc.ncbi.nlm.nih.gov/articles/PMC4915505/). PMID 26652669. Model: 2DD normal human foreskin fibroblasts; two biological replicates per condition. Location: GSE65145 processed tracks; Figures 1 and 3; Figure S2; Cell culture and RNA-seq methods.

O2. [Toledano et al. — genome-scale PTC readthrough](https://www.nature.com/articles/s41588-024-01878-5). PMID 39174735. Model: Human HEK293T landing-pad reporters; not endogenous BUB1B. Location: Supplementary Table 3; Extended Data Figure 4.

O3. [Zhao et al. — molecular profiling of NMD modulators](https://pmc.ncbi.nlm.nih.gov/articles/PMC8718828/). PMID 35024243. Model: Mouse Neuro-2a; three AS-NMD isoform reporters. Location: Tables S1/S2/S4; Figures 2–5 and 7.

O4. [BUBR1 TPR / MCC–APC/C functional controls](https://www.nature.com/articles/s42003-026-10384-9). PMID 42477419. Model: HeLa endogenous BUBR1 RNAi and RNAi-resistant YFP replacement. Location: Figure 4B; supplementary source-data workbook, Sheet1.

O5. [Xu et al. — BUBR1 recruits PP2A-B56 for chromosome congression](https://pmc.ncbi.nlm.nih.gov/articles/PMC3654266/). PMID 23789096. Model: HeLa BUBR1 depletion/reconstitution and BUB1B-mutated MVA fibroblast rescue. Location: Figures 2 and 4; equally expressed B56-binding mutants are functional counterexamples.

O6. [Amlexanox rescue in human cells](https://doi.org/10.1186/1750-1172-7-58). PMID 22938201. Model: Human 6CFSMEo- CFTR nonsense cells. Location: Figure 6.

O7. [NEFL motor-neuron negative rescue](https://doi.org/10.3389/fcell.2021.820105). PMID 35237613. Model: Human iPSC-derived NEFL nonsense motor neurons. Location: Figure 6; Treatments.

O8. [Amlexanox in GDAP1 neuronal progenitors](https://doi.org/10.3390/ph16071034). PMID 37513945. Model: Human iPSC-derived neuronal progenitors with GDAP1 p.Ser194\* (UGA). Location: Figures 2-4.

O9. [Omachi et al. — COL4A5 readthrough reporters](https://pmc.ncbi.nlm.nih.gov/articles/PMC8866893/). PMID 35243249. Model: HEK293 COL4A5 cDNA reporters; different gene and context. Location: Figure 6: gentamicin plus mefloquine.

O10. [Torban et al. — PKD1 readthrough and partial cellular rescue](https://www.nature.com/articles/s41598-025-26775-7). PMID 41274954. Model: Human HEK293 PKD1 reporters and WT9-12 cells; other-gene evidence. Location: Figures 1H-I, 4, 5 and 6; published 2025-11-22.

O11. [FDA historical Aphthasol label](https://www.accessdata.fda.gov/drugsatfda_docs/label/2002/20511s002lbl.pdf). Model: Historical FDA Aphthasol 5% oral-paste label. Location: Pharmacokinetics and Metabolism, page 1.

Additional immunotherapy and arimoclomol source IDs, models and access limitations are retained in the [snapshot](https://github.com/ivillafuerte/mva-hackathon-2026/blob/b85dfb2aa8f28b691318d31c29d6b846bab77b3d/track2/evidence/mva-results-2026-10-17.json). Historical September references above remain supporting or contrary evidence; retaining them does not retain the old ranking.

## Required acknowledgment

This work was made possible through the Hackathon, organized by Sage Bionetworks in partnership with the MVA Society, Hugging Face, and BEACON (The Benchmarking, Evaluation, and Assessment Consortium for Science), with prize sponsorship from AWS and Anthropic. We are deeply grateful to the child and their family who generously contributed their data and their story to advance research into this rare disease. We acknowledge their trust in making this Hackathon possible.

## Historical computational verification (September 10)

On September 10, a repeat execution with freshly installed pinned dependencies reproduced the complete metrics JSON and both residue/rotamer tables exactly. All public reference input hashes matched the audited manifest. An initial native execution failure and truncated public PAE cache were resolved before this comparison. Script syntax and package consistency checks also passed. These checks do not establish biological efficacy.

## Appendix A. Methods declaration aligned to the official Track 2 template

The following answers follow rows 7–17 of the official Track 2 methods template. The scientific evidence snapshot is dated October 17, 2026; participant declarations were updated October 24, 2026.

### Team name — worksheet row 7

Stackfire Networks. GitHub contributor: ivillafuerte.

### Approach from variant to medication — row 8

Start from the nominated BUB1B L737\*/N1002K pair. Verify transcript/codon identity, NMD context and model geometry. Keep RNA, protein, checkpoint and segregation evidence separate. A versioned virtual lab organizes four quantitative reanalyses, six qualitative evidence audits and one synthetic software test; these are not eleven biological experiments. The rapamycin RNA-feature observation constrains a sirolimus RNA-increase rationale. Amlexanox and montelukast remain conditional hypotheses; gentamicin + mefloquine remains experimental. Immunotherapy is deprioritized for BUB1B disease rescue rather than equated with antitumor activity. The proposed next step is exact-variant validation with WT/matched controls, viability and proliferation tracking. Current product eligibility and systemic exposure, especially amlexanox, remain open; recovered October scripts and explicit reproduction limits are documented in the reproduction guide. No efficacy or synergy is assumed.

### Required generative-AI disclosure — row 9

OpenAI ChatGPT Work/Codex supported literature discovery, code execution, evidence synthesis and English drafting; the participant reports the ChatGPT plan as “Premium” (name as reported, not relabeled Pro or Business). Anthropic Claude Max was used to generate the web laboratory. On October 24, 2026, the participant confirmed that use of conversations to improve the models was disabled in both ChatGPT and Claude during the project. These plan and setting statements are participant attestations, not an independent account audit; they do not establish zero retention.

The participant also stated that no patient data were shared with AI services. The source methods nevertheless document the challenge-derived small variant pair and permitted phenotype summary, so this statement is not treated as evidence that no case-derived information entered the workflow. The source Track 2 report states that its workspace did not upload or read patient-scale genomic files; no broader claim about earlier local Track 1 analysis or all account activity is inferred. Exact historical model identifiers and the scope of earlier Claude analysis assistance remain unverified.

### Automated versus manual identification — row 10

Hybrid: automated public reference retrieval, sequence checks, structural/transcript calculations and metadata validation; AI-assisted literature retrieval and evidence curation; explicit judgment-based candidate prioritization. No automated drug-target score is represented as a therapeutic prediction.

### Literature review and curation — row 11

Search public web and Europe PMC/PubMed using BUB1B/BUBR1, exact variant names, rescue, turnover, HSP90, NMD, readthrough, SIRT2/NAD, mTOR, IL-1 and prenatal delivery terms. Prefer primary experimental articles and regulatory product labels. Inspect model, perturbation, outcome, figures when accessible, corrections and evidence against the hypothesis. Distinguish full-text review from abstract-only support. Search results are not an exhaustive systematic review; no PRISMA completeness claim or independent human expert review is made. Negative retrieval does not prove absence of evidence.

### Public versus proprietary sources — row 12

Track 2 computations use public references and the participant-provided small causal finding. The causal finding originates from the gated challenge dataset through Track 1, so this is not described as an entirely case-independent public-data discovery. No commercial proprietary drug database or additional private patient-scale dataset was used here.

### Public sources — row 13

SageBio challenge rules, FAQ, implementation and methods template; NCBI RefSeq and ClinVar; public gnomAD variant annotations; UniProt O60566; AlphaFold model and PAE; selected PDB coordinate files; primary literature retrieved through PubMed/Europe PMC and publishers; DailyMed product labels. IDs, DOI links, source access limits and reference hashes are preserved in the report and evidence files. The October snapshot adds GSE65145 processed tracks and published reporter/checkpoint source tables; their record-level source IDs and provenance hashes are preserved in evidence/mva-results-2026-10-17.json. A follow-on October 22 audit recovered the original four scripts and reran their deterministic calculations from public processed sources; source/hash checks, commands and remaining upstream limits are documented in the [reproduction guide](https://github.com/ivillafuerte/mva-hackathon-2026/blob/b85dfb2aa8f28b691318d31c29d6b846bab77b3d/track2/reproduction/README.md). Open Targets, ChEMBL and other resources suggested in the project brief are not listed as actually used analyses unless an output documents that use.

### Proprietary sources — row 14

None newly accessed for this Track 2 work. The underlying challenge case is gated and governed by its agreement. No redistribution of that dataset is implied by citing its landing page.

### Variant mechanism — row 15

L737\*: premature UGA in exon 17/23; NMD susceptibility inferred from exon-junction distances, not experimentally measured. Full-length readthrough may carry a non-leucine residue and requires functional testing. N1002K: conserved missense site with model-supported polar contacts but some lysine conformations compatible with the fixed backbone. Instability is weakly supported computationally and unproven biologically. Neither the intended compound pair nor Track 1 scoring establishes molecular trans phase. Disease mechanism is loss of sufficient functional BUBR1; the specific contribution of N1002K remains unresolved.

### Time and effort — row 16

Not prospectively logged across the original conversations. Do not infer billable hours, total project cost or laboratory effort from document length. New verification commands record elapsed runtime for their own scope only. No laboratory expenditure or experiments occurred in this workspace.

### Method abstract — row 17, fewer than 500 words

We developed an allele-aware evidence-to-decision workflow for BUB1B-associated mosaic variegated aneuploidy using the challenge-nominated L737\*/N1002K pair. Earlier public sequence and structural computations established transcript context and model geometry without proving variant function. The October evidence workspace contains four reanalyses, six qualitative evidence audits and one synthetic software test, with four charts. It does not run biological experiments or calculate drug efficacy.

Two observations constrain prioritization. A BUB1B-spanning RNA feature was 41.43% lower in a limited normal-fibroblast rapamycin reanalysis, not a protein or rescue endpoint. Nearby readthrough contexts did not include an exact L737\* measurement. Amlexanox is a conditional other-gene-supported hypothesis with contradictory neuronal evidence and unresolved current product eligibility. Montelukast is an NMD-modulation hypothesis contingent on useful exact-truncation function. Gentamicin plus mefloquine remains experimental; immunotherapy tumor outcomes are not disease rescue.

The proposed decisive experiment measures allele-specific RNA and protein, checkpoint response and segregation errors per completed division against matched controls, while tracking viability and proliferation. No exact-genotype pharmacological rescue is established. The public snapshot and final video brief were cross-checked. Recovered October scripts reproduced four deterministic output artifacts from public processed inputs, without using the snapshot as input. Upstream limits include reused published permutation results, archived annotation and a small prediction extract. September allele computations remain separately documented. Systemic exposure, product eligibility and the organizer-prescribed dataset citation remain unresolved. No new wet-laboratory efficacy evidence or patient treatment recommendation is presented.

