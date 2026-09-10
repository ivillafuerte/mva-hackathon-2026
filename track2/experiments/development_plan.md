# Development plan: amount, cell coverage and timing of BUBR1 rescue

All biological experiments below are proposed. No patient treatment, fetal procedure, cell acquisition or animal experiment has been performed or authorized by this document. Applicable institutional review, consent and authorized access must precede any work using patient-derived material. Public-reference analysis can proceed now.

## Aim 1: establish a functional rescue reference

Use a non-tumor human background with matched genotype models and a genetically corrected comparator. Prefer multiple independently derived isogenic clones and independent differentiation batches when using muscle models. Include WT, L737*, N1002K, the modeled compound pair and L1012P as a related instability control. Expressing a constructed pair in trans is an experimental design choice, not proof of the patient's phase.

Quantify BUB1B RNA, allele-specific RNA where technically justified, N- and C-terminal BUBR1 protein, localization and turnover. Avoid mistaking different cell-cycle distributions for altered protein stability. Protein half-life assays need appropriate stress controls and an orthogonal method if cycloheximide itself changes the phenotype. Proteasomal/HSP90 perturbation can help identify turnover mechanisms; broad inhibition is not proposed as chronic therapy.

Deliver regulated WT BUB1B expression as a reference and compare N1002K at matched protein abundance. Matching plasmid or mRNA input is insufficient. Include a range spanning endogenous WT abundance; extreme overexpression rescue does not establish physiological feasibility. Verify endogenous protein does not mask the modeled allele.

| Observation | Interpretation | Next step |
|---|---|---|
| Low N1002K protein, function improves after protein equalization | Supports dosage/stability contribution | Test stabilization and pathway dependence |
| Protein equalized but function remains defective | Supports function/interaction defect | Examine relevant localization, checkpoint complexes and CENP-E interaction if justified |
| N1002K abundance and function resemble WT | Does not support the assumed defect | Reassess allele contribution, model sensitivity and causal interpretation |
| WT reference fails | Could reflect delivery or model failure | Verify expression/localization and assay competence before rejecting rescue |

## Aim 2: distinguish early protection, late rescue and maintenance

Compare early/sustained, delayed/sustained, early/transient and untreated conditions. Establish baseline karyotype and functional measurements before intervention. Match or record cumulative divisions as well as elapsed time. Vary the fraction of cells receiving rescue separately from per-cell expression. Average protein abundance alone does not describe coverage.

After withdrawal, measure protein disappearance, target function, lineage behavior and error accumulation. Do not map days in culture to fetal gestation. Persistent lineage reporter labels must not be used as a proxy for persistent therapeutic protein.

## Aim 3: evaluate approved medications against the reference

First-stage arms are separate monotherapies: sirolimus, anakinra, everolimus comparator and nicotinic acid exploration. Gentamicin is a readthrough assay benchmark. Vehicle and assay-positive/negative controls accompany every experiment. Separate early prevention of a stress state from treatment after that state is established.

For sirolimus, compare continuous exposure with transient exposure and withdrawal. Recovery must be measured rather than inferred from removal from culture medium. For anakinra, test IL-1 dependence; for nicotinic acid, test NAD response and SIRT2 dependence. Add a combination only after individual benefit and complementary mechanisms are observed, with a factorial design and prespecified interaction analysis.

For L737*, compare an exact-context reporter with an endogenous or splice-preserving system. NMD can be invisible in an intronless cDNA. Measure transcript availability, full-length product with orthogonal methods and inserted amino-acid identity where feasible. Express L737C/R/W and the truncation as controls to determine what functions remain possible. NMD inhibition requires evidence of transcript limitation and separate global-toxicity assessment.

## Outcomes and statistical analysis

**Primary molecular endpoint:** new segregation-error events per completed division, with a prespecified scoring definition and blinded time-lapse assessment. Log failed divisions, prolonged arrest and death separately so treatment cannot improve the denominator artificially.

**Secondary mechanistic endpoints:** checkpoint response, mitotic timing, alignment, kinetochore localization, lagging chromosomes, micronuclei and single-cell karyotype. Changes in total aneuploid-cell fraction are interpreted with lineage expansion and death, not as direct proof of repair.

**Tissue endpoint:** for a validated muscle model, use a prespecified differentiation/fusion or contractile endpoint. Secreted IL-6/IL-8 and pathway phosphorylation are target-engagement outcomes, not substitutes for tissue function. Measure autophagic flux with an appropriate turnover design rather than interpreting a single LC3 measurement.

Randomize treatment allocation within experimental batches and blind image scoring. Independent clones/cultures or differentiation batches are biological replicates; individual cells within a culture are not independent biological replicates. Plan a hierarchical binomial model or cluster-aware analysis for error events, accounting for clone/batch and repeated observations. Report effect sizes and confidence intervals. Use an exploratory stage followed by an independent confirmation stage; control multiplicity across screened candidates. Fit amount–response curves only when supported by data, allowing nonlinearity and declining benefit at high expression.

Use pilot baseline error rates, between-batch variation and a biologically meaningful reduction to calculate sample size prospectively. No invented n or numerical power claim is supplied. Predefine exclusions for technical failure without excluding unfavorable biological outcomes. Preserve blinded scoring records and report missingness.

## Stop/go criteria

Advance a molecular-rescue candidate only if reference rescue works, errors per division improve reproducibly, and improvement is not explained by death or arrested proliferation. A tissue-protection candidate may advance on a separately specified functional endpoint, but cannot be called a BUBR1-restoring agent. Both must pass mitotic safety and exposure-feasibility gates.

Stop or reformulate for absent target engagement, persistent dysfunction despite restored abundance, worsening CIN, unacceptable tissue effects, inability to reach effective exposure, or loss of benefit that makes sustained delivery impractical. Absence of statistical significance is not proof of safety; define an acceptable harm margin during pilot planning.

Evaluate oncology separately. Restoration may affect normal and malignant cells differently; no existing-malignancy benefit follows automatically from reduced new CIN. Do not infer current cancer treatment, renal function or inflammation from supplied phenotype terms.

## Prenatal development sequence

1. Establish genotype-specific rescue in cells and appropriate tissues.
2. Determine whether transient rescue leaves a functional benefit after protein disappears.
3. Evaluate a BUB1B mRNA platform for expression, localization, cell coverage and duration.
4. Only with specialist collaborators and approvals, design fetal biodistribution and developmental-safety studies. Include maternal exposure, placenta, unintended tissues and germ-cell exposure as measurements; mRNA supplementation is not intended germline editing.
5. Compare prenatal-only, postnatal-only and continued rescue at justified developmental stages. Do not assume a single administration is sufficient or that diagnosis precedes all damage.

There is no prenatal clinical protocol in this dossier. The current child's possible future benefit concerns postnatal rescue; prenatal prevention would concern future affected pregnancies and cannot reverse this child's past development.

## Work packages and deliverables

| Work package | Owner role | Deliverable | Dependency / status |
|---|---|---|---|
| Public allele audit and structural analysis | Computational researcher | Reproducible metrics and evidence tables | Completed computationally; no biological validation |
| Drug and rule audit | Researcher/pharmacology reviewer | Candidate matrix and source log | Draft complete; recheck before submission |
| Cell model and reference rescue | Cell biology collaborator | Validated genotype model and WT rescue | Collaborator, facility and approvals not yet secured |
| Temporal and drug validation | Cell biology/pharmacology team | Replicated effect estimates and exposure assessment | Depends on successful reference rescue |
| Tissue and oncology validation | Disease-model specialists | Tissue outcomes and separate tumor assessment | Future; not promised before competition close |
| Prenatal delivery research | Fetal therapy/delivery specialists | Preclinical feasibility package | Future program outside current drug nomination |
| Submission preparation | Participant | Report, public repository, video and declarations | Draft files prepared; readiness items open |

No laboratory budget, staff commitment or experimental completion date is invented. For the contest, use verified computational findings and a candid validation plan if biological work is unavailable. Suggested internal milestones: complete participant/account confirmations by September 17; freeze the evidence narrative by October 10; record and review the pitch by October 17; reserve the final week for repository and upload checks. These are planning targets, not organizer deadlines or automatic reminders.
