# Rare Disease, Real Kid: MVA Hackathon 2026
## Track 1 - Variant Prediction Technical Report

**Participant:** ivillafuerte  
**Proband:** PROBAND01  
**Genome build:** GRCh38  
**Submission date:** 28 August 2026  
**Primary model:** Phenotype-guided, evidence-weighted BUB1B compound-heterozygous prioritization

> **Scope statement.** This report presents a ranked research hypothesis for the hackathon. It is not an independent clinical diagnosis. The final compound-heterozygous phase was not established from the supplied VCF, and no parental segregation data were available in the analyzed materials.

## 1. Executive summary

The Track 1 analysis prioritized **BUB1B** because the challenge concerns mosaic variegated aneuploidy (MVA), and the challenge phenotype includes a combination of cancer predisposition and severe growth restriction. The challenge-provided phenotype document lists rhabdomyosarcoma (HP:0002859), nephrocalcinosis (HP:0000121), short stature (HP:0004322), failure to thrive (HP:0001508), skeletal muscle atrophy (HP:0003202), premature birth (HP:0001622), small for gestational age (HP:0001518), and recurrent spontaneous abortion in the parental history (HP:0200067).

A targeted review of the BUB1B locus identified seven PASS heterozygous variants, of which two fall in exons of the MANE Select transcript **NM_001211.6**. The top-ranked hypothesis is the following pair:

| Rank | GRCh38 variant | Transcript consequence | Evidence summary | EPCR |
|---|---|---|---|---:|
| 1 | **chr15:40209701 T>G** + **chr15:40220612 T>G** | **BUB1B c.2210T>G (p.Leu737Ter)** + **BUB1B c.3006T>G (p.Asn1002Lys)** | Known pathogenic truncating allele plus an ultra-rare, computationally damaging missense allele in the BubR1 catalytic domain | **0.95** |

The first allele is a known pathogenic BUB1B variant associated with MVA1. The second allele is observed once in approximately 1.46 million gnomAD exome alleles, has no homozygotes in the queried gnomAD v4.1 dataset, and is predicted damaging by SIFT and PolyPhen-2 with elevated CADD. It lies in the conserved BubR1 serine/threonine kinase catalytic domain. These data support submission of the pair as the highest-ranked causal hypothesis, while explicitly retaining **phase/segregation as an unresolved limitation**.

## 2. Data and privacy handling

Analysis was performed locally on an Apple Silicon workstation using Docker. Raw or genotype-scale challenge data were kept outside the public-repository surface. The public code package is intended to contain only code, documentation, configuration examples, and reproducibility instructions.

The challenge organizers clarified that raw VCF/BAM/CRAM files, subsets or reformats carrying genome-scale genotypes, and genotype-scale intermediate tables must be deleted according to the challenge deletion requirement. Ranked candidate variants, HPO terms, gene/pathway findings, code, reports, and leaderboard entries may be retained. The organizers also state that third-party services may be used only when they act as processors rather than recipients, including no provider training on inputs/outputs and time-limited retention for service purposes.

### LLM-assisted analysis disclosure

OpenAI ChatGPT Business workspace (GPT-5.6 Sol) was used as an analysis and drafting assistant. OpenAI's current business privacy documentation states that ChatGPT Business workspace inputs and outputs are excluded from model training by default. Raw VCF/FASTQ files were not uploaded through ChatGPT; analysis discussions used challenge phenotype information, public-reference annotations, terminal outputs, and a small number of candidate findings. Organizer guidance recommends avoiding feedback/rating actions that could alter provider data-use treatment.

## 3. Computational environment

The reproducible analysis environment was containerized and used the following core tools:

| Component | Version / configuration |
|---|---|
| Host | macOS, Apple Silicon (M3 Max) |
| Container | Ubuntu 24.04 ARM64 |
| Python | 3.12.3 |
| bcftools | 1.19 |
| samtools | 1.19.2 |
| bedtools | 2.31.1 |
| pysam | 0.24.0 |
| pandas | 2.3.3 |
| NCBI Datasets CLI | 18.36.0 |
| Reference assembly | GRCh38 |
| ClinVar | GRCh38 VCF downloaded 28 Aug 2026 |
| gnomAD | v4.1 exomes, chr15 VCF |
| gnomAD embedded VEP | v105 |
| BUB1B MANE transcript | NM_001211.6 / NP_001202.5 |

A local Ensembl VEP v116 environment was also prepared, but the final evidence reported here does not depend on completion of the v116 cache download; transcript consequence confirmation used NCBI reference sequence plus the annotation embedded in gnomAD v4.1.

## 4. Variant callset quality control

The supplied indexed GRCh38 VCF contained one sample. Initial bcftools QC produced:

| Metric | Count |
|---|---:|
| Total variant sites | 5,012,204 |
| PASS sites | 4,740,790 |
| SNP-class sites | 4,086,641 |
| Indel-class sites | 930,181 |
| Biallelic sites | 4,945,344 |
| Multiallelic sites | 66,860 |
| Heterozygous genotype sites | 3,113,937 |
| Homozygous alternate genotype sites | 1,898,267 |
| PASS heterozygous sites | 2,913,813 |

SNP and indel category counts are not treated as mutually exclusive for mixed multiallelic records. The VCF contained genotype depth/allele-depth and genotype-quality information sufficient for targeted review.

## 5. Phenotype-guided gene prioritization

The challenge is explicitly centered on MVA. BUB1B was prioritized as a high-value candidate because biallelic BUB1B variants are a known cause of MVA1 and because the original BUB1B/MVA literature describes growth retardation, childhood cancer predisposition, chromosome-segregation defects, and affected individuals with embryonal rhabdomyosarcoma.

This targeted prioritization was not used as proof of causality. The downstream analysis required variant-level support from transcript consequence, clinical databases, population frequency, and functional/domain evidence.

## 6. BUB1B locus analysis

NCBI Gene places BUB1B on GRCh38 chromosome 15 at **40161069..40221123**. The MANE Select transcript **NM_001211.6** contains 23 exons and encodes **NP_001202.5**, a 1050-amino-acid protein.

Targeted extraction of the BUB1B interval found:

- 14 total variants in the interval
- 13 PASS variants
- 7 PASS heterozygous variants
- 0 of the 7 candidates had explicit PGT/PID phase information in the supplied VCF
- 2 of the 7 PASS heterozygous candidates were exonic in NM_001211.6

The two exonic variants were independently mapped using the NCBI MANE transcript and RNA sequence.

## 7. Candidate variant 1: BUB1B p.Leu737Ter

**Genomic:** chr15:40209701 T>G (GRCh38)  
**Transcript:** NM_001211.6:c.2210T>G  
**Protein:** NP_001202.5:p.Leu737Ter  
**Consequence:** stop-gained / truncating

Direct codon reconstruction from the NCBI RNA sequence produced **TTA -> TGA**, converting leucine to a premature stop codon.

ClinVar identifies this exact GRCh38 variant as **BUB1B c.2210T>G (p.Leu737Ter)** and associates it with **Mosaic variegated aneuploidy syndrome 1**. The locally downloaded ClinVar GRCh38 VCF returned `Pathogenic/Likely_pathogenic` across the available assertions, with MVA1 among the conditions.

Population evidence from the local gnomAD v4.1 exome chr15 resource:

| Field | Value |
|---|---:|
| AC | 115 |
| AN | 1,461,846 |
| AF | 7.86677e-05 |
| Homozygous alternate | 0 |
| CADD PHRED | 38 |
| SpliceAI max | 0.03 |

The allele is therefore rare but observable in heterozygous carriers, which is compatible with an autosomal-recessive disease model.

## 8. Candidate variant 2: BUB1B p.Asn1002Lys

**Genomic:** chr15:40220612 T>G (GRCh38)  
**Transcript:** NM_001211.6:c.3006T>G  
**Protein:** NP_001202.5:p.Asn1002Lys  
**Consequence:** missense, exon 23/23

Direct codon reconstruction from the NCBI RNA sequence produced **AAT -> AAG**, changing asparagine to lysine at residue 1002. gnomAD's embedded VEP annotation independently confirmed `missense_variant`, `NM_001211.6:c.3006T>G`, and `NP_001202.5:p.Asn1002Lys`.

No exact entry was returned for this allele from the locally downloaded ClinVar GRCh38 VCF. Population and computational evidence from gnomAD v4.1 was:

| Evidence | Value | Interpretation |
|---|---:|---|
| AC | **1** | Seen once in the queried exome callset |
| AN | 1,461,878 | High callable allele number at site |
| AF | **6.84052e-07** | Ultra-rare |
| Homozygous alternate | **0** | No homozygotes observed |
| CADD PHRED | **26.4** | Elevated deleteriousness rank |
| REVEL | 0.472 | Intermediate computational support |
| SIFT | **0.000** | Predicted deleterious |
| PolyPhen-2 | **0.997** | Predicted probably damaging |
| SpliceAI max | 0.02 | Does not support a major splice effect |

The gnomAD VEP domain field includes **CDD:cd14029**. NCBI defines cd14029 as the catalytic serine/threonine kinase domain of vertebrate BubR1, spanning approximately residues 750-1045. Residue **Asn1002** therefore lies inside this domain.

The combination of extreme rarity, a protein-altering consequence, location in a known BubR1 functional domain, and concordant SIFT/PolyPhen/CADD evidence makes p.Asn1002Lys a strong second-allele candidate. However, the available evidence does **not** independently establish it as pathogenic, and the moderate REVEL score is retained as counterbalancing evidence.

## 9. Compound-heterozygous model

The submitted causal model is:

```text
BUB1B allele 1: c.2210T>G  -> p.Leu737Ter   (known pathogenic truncating allele)
BUB1B allele 2: c.3006T>G  -> p.Asn1002Lys (ultra-rare missense candidate)

Hypothesis: compound heterozygosity -> reduced/abnormal BubR1 function
           -> impaired spindle-assembly checkpoint / chromosome segregation
           -> mosaic aneuploidy and cancer-predisposition phenotype
```

This model is biologically coherent with prior BUB1B/MVA studies. Hanks et al. established biallelic BUB1B mutations as a cause of constitutional aneuploidy and childhood cancer predisposition. Subsequent functional work showed that MVA-associated truncating/missense BUBR1 pairs can reduce protein abundance or impair checkpoint/microtubule functions, with missense alleles commonly occurring in or near the kinase domain.

## 10. Phase and validation limitations

The VCF has no PGT/PID phase information for the seven heterozygous BUB1B candidates. Therefore, this analysis does not independently prove that p.Leu737Ter and p.Asn1002Lys are in **trans**.

The most informative follow-up validation would be:

1. Parental segregation testing showing one allele inherited from each parent; or
2. Read-backed phasing from aligned WGS data if the local haplotype can be connected across the approximately 10.9 kb interval; and
3. Clinical-laboratory confirmation of both variants using a validated orthogonal method when required.

If p.Asn1002Lys remained a variant of uncertain significance after segregation analysis, functional studies of BubR1 abundance, spindle checkpoint activity, chromosome segregation, and/or kinase-domain behavior would provide additional evidence.

## 11. Ranking rationale and submission record

Only one row is submitted because the evidence converges on a specific BUB1B pair and adding lower-confidence rows would not improve the primary hypothesis.

```csv
proband_id,chrom_1,pos_1,ref_1,alt_1,chrom_2,pos_2,ref_2,alt_2,epcr,finding_type,notes
PROBAND01,chr15,40209701,T,G,chr15,40220612,T,G,0.95,primary,BUB1B compound-heterozygous candidate
```

The EPCR of **0.95** reflects a high-confidence hackathon prediction based on one clinically established pathogenic allele plus a compelling second allele. It does not imply 95% clinical certainty or a formal ACMG classification.

## 12. Reproducibility and public repository design

The public repository should include the Docker environment, scripts, Makefile, and documentation required to reproduce the workflow after an authorized participant places the challenge data in local private paths. It should **not** include raw genomic files, genotype-scale derived tables, challenge clinical source files, indexes, notebook state containing genome-scale genotypes, or large reference datasets.

Recommended reproducibility flow:

```bash
make build
make check
make qc
make bub1b
make bub1b-phase
```

Public-reference resources can be downloaded from ClinVar, gnomAD, NCBI, and Ensembl by the documented scripts. Private challenge data remain local and git-ignored.

## 13. Conclusion

The highest-ranked Track 1 hypothesis is a **BUB1B compound-heterozygous pair** consisting of **p.Leu737Ter** and **p.Asn1002Lys**. p.Leu737Ter is a known pathogenic MVA1 allele. p.Asn1002Lys is an ultra-rare missense allele with no observed homozygotes in the queried gnomAD v4.1 exomes, strong SIFT/PolyPhen/CADD support, and location within the BubR1 catalytic kinase domain. The pair is strongly supported as a hackathon prediction, but independent proof of trans phase remains pending.

---

## References

1. Sage Bionetworks. Rare Disease, Real Kid: MVA Hackathon 2026 - Track 1 submission instructions and evaluation code. https://huggingface.co/spaces/SageBio/rare-disease-real-kid-mva-hackathon-2026
2. Sage Bionetworks. Clarification on using third-party LLM APIs with the dataset. https://huggingface.co/spaces/SageBio/rare-disease-real-kid-mva-hackathon-2026/discussions/2
3. Challenge-provided confidential document: *Rare Disease Genomic Challenge - Proband Clinical Phenotype - Participant Reference Document*.
4. NCBI ClinVar. NM_001211.6(BUB1B):c.2210T>G (p.Leu737Ter) and Mosaic variegated aneuploidy syndrome 1. RCV000641226. https://www.ncbi.nlm.nih.gov/clinvar/RCV000641226/
5. NCBI Gene. BUB1B, Gene ID 701. https://www.ncbi.nlm.nih.gov/gene/701
6. Hanks S, et al. Constitutional aneuploidy and cancer predisposition caused by biallelic mutations in BUB1B. *Nature Genetics*. 2004;36:1159-1161. PMID:15475955. https://pubmed.ncbi.nlm.nih.gov/15475955/
7. Suijkerbuijk SJE, et al. Molecular causes for BUBR1 dysfunction in the human cancer predisposition syndrome mosaic variegated aneuploidy. *Cancer Research*. 2010. PMID:20516114. https://pubmed.ncbi.nlm.nih.gov/20516114/
8. gnomAD Production Team. gnomAD v4.1. https://gnomad.broadinstitute.org/news/2024-04-gnomad-v4-1
9. OpenAI. Enterprise privacy / business data commitments. https://openai.com/enterprise-privacy/

