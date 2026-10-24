## Appendix B. Product-status and exposure source update

This appendix documents two targeted source checks performed October 24, 2026: product-specific FDA status and the published COL4A5 Figure 6 gentamicin conditions. It adds no biological experiment, clinical dose recommendation, new efficacy estimate or revision of the candidate ranking. These findings were incorporated into public main at commit `0cb71c4946fd71d0c0b5b1589026a2ed9e8a33b6`. Publication does not replace the original submitted package or establish official resubmission. The version correction and subsequent computational diagnostics do not make these earlier source checks new experimental achievements.

### Product-specific FDA records

Fetched 2026-10-24 at approximately 09:05:57 UTC. Every response reports `meta.last_updated: 2026-10-23`. This is the database update date, **not a discontinuation date or approval date**. Original approval dates below are the application's ORIG/AP submission dates; individual strengths must not be presumed independently approved on that date without product-specific history.

| Product / FDA sponsor | Application and product | Formulation / route / strength as recorded | Application original AP date | FDA marketing status |
|---|---|---|---|---|
| MONTELUKAST SODIUM (RISING) | [ANDA209012/001](https://api.fda.gov/drug/drugsfda.json?search=application_number:ANDA209012) | TABLET; ORAL; EQ 10MG BASE | 2017-04-24 | **Prescription** |
| MONTELUKAST SODIUM (TEVA PHARMS) | [ANDA078605/001](https://api.fda.gov/drug/drugsfda.json?search=application_number:ANDA078605) | TABLET; ORAL; EQ 10MG BASE | 2012-08-03 | **Prescription** |
| MONTELUKAST SODIUM (AJANTA PHARMA LTD) | [ANDA203432/001](https://api.fda.gov/drug/drugsfda.json?search=application_number:ANDA203432) | TABLET; ORAL; EQ 10MG BASE | 2015-07-31 | **Discontinued** |
| MEFLOQUINE HYDROCHLORIDE (BARR) | [ANDA076392/001](https://api.fda.gov/drug/drugsfda.json?search=application_number:ANDA076392) | TABLET; ORAL; 250MG | 2003-12-29 | **Prescription** |
| GENTAMICIN SULFATE (FRESENIUS KABI USA) | [ANDA062366/002](https://api.fda.gov/drug/drugsfda.json?search=application_number:ANDA062366) | INJECTABLE; INJECTION; EQ 10MG BASE/ML | 1983-08-04 | **Prescription** |
| GENTAMICIN SULFATE (FRESENIUS KABI USA) | [ANDA062366/001](https://api.fda.gov/drug/drugsfda.json?search=application_number:ANDA062366) | INJECTABLE; INJECTION; EQ 40MG BASE/ML | 1983-08-04 | **Prescription** |
| APHTHASOL (ULURU) | [NDA020511/001](https://api.fda.gov/drug/drugsfda.json?search=application_number:NDA020511) | PASTE; DENTAL; 5% | 1996-12-17 | **Discontinued** |
| AMLEXANOX (ULURU) | [NDA021727/001](https://api.fda.gov/drug/drugsfda.json?search=application_number:NDA021727) | PATCH; TOPICAL; 2MG | 2004-09-29 | **Discontinued** |

Prescription status is not guaranteed stock or challenge eligibility. Historical exposure observations are not measurements for every product listed above. Amlexanox systemic-product eligibility remains unresolved; no discontinuation reason is inferred.

### Figure 6 source verification

[Omachi et al. (2022)](https://doi.org/10.1016/j.isci.2022.103891), PMID 35243249, PMCID PMC8866893: the [original Figure 6](https://pmc.ncbi.nlm.nih.gov/articles/PMC8866893/figure/fig6/) was visually inspected and the [official Europe PMC full-text XML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8866893/fullTextXML) checked against its caption, luciferase-assay methods and reagent table. Panels B/D show gentamicin None, 2 mM and 4 mM; the caption specifies mefloquine 20 µM. Panels A/C instead use G418 50/100 µM. Drug addition at 48 h and assay at 72 h after transfection imply 24 h exposure; this is derived from the methods, not an explicit duration in the caption.

The model is transient HEK293 COL4A5-R1563X/G5X NanoLuc cDNA reporters with firefly normalization. Normalized luminescence and fold induction are not endogenous BUB1B rescue or formal synergy. The listed gentamicin reagent (Life Technologies 15750-060, 50 mg/mL) is a stock, not the final assay concentration; no single-component molecular weight or free assay concentration is established. The mefloquine reagent form was not resolved. No mass conversion or numeric human therapeutic window is asserted.

Verification evidence: original figure SHA-256 `546f8fd4663061798061e3b2d69bee2ed34602e79fec5757adcde21280e7dff9`; full-text XML SHA-256 `d0657ba68b343430825ddc1dc1798e30501b0e1bc2b6b4e6012de886c1a17765`. These hashes identify downloaded source evidence, not new experimental output. The figure is linked, not reproduced or adapted in this report.
