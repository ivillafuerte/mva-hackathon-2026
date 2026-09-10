# Track 2 requirements and submission readiness

Verified against public official materials on September 10, 2026. This is a readiness record, not a claim that an upload or institutional approval has occurred. The participant's separately accepted gated-data agreement must also be observed; its account-specific acceptance state cannot be inspected here.

## Official requirement mapping

| Requirement | Source | Package implementation / status |
|---|---|---|
| Existing market-approved medication candidates | Official Rules; discussion 5 | Named product-level hypotheses in report and candidate assessment; new mRNA product excluded from nomination |
| Characterize variant mechanism and biological consequence | Submission tab | Report sections 1–3; structural/transcript outputs |
| Written report in PDF or Markdown, filename including user/team | Submission tab | `ivillafuerte_track2_report.md`; verify chosen submission identity |
| Reproducible GitHub code and configuration | Submission tab | Track 2 scripts, pinned dependencies, inputs with hashes, results and validation command |
| Repository public at challenge end | Submission tab | Existing repository is public; new local files are not yet confirmed published |
| Three-minute video hosted on YouTube or Vimeo | Submission tab | English script prepared; actual recording, timing and public/unlisted judge-accessible URL pending |
| Provider, plan/tier and relevant AI handling settings | Submission tab; discussion 2 | Methods row 9 identifies verified use and exact participant-confirmed fields still needed |
| Methods template answers | Official workbook, Track 2 sheet | All rows 7–17 mapped in English Markdown; most fields optional, AI disclosure required |
| Up to three versions; latest reviewed; one representative | Configuration, FAQ, submission code | Do not spend a version on an unfinished package; live quota is not known here |
| Submission deadline | About timeline | October 24, 2026, 23:59 UTC; recheck before upload |
| Judging rubric | Rules/About | Scientific rigor 35%, impact 25%, innovation 25%, scalability 15%; addressed in report section 8 |
| Each team member registered and at least 18 | Official Rules | Participant reports prior registration/Track 1 completion; no additional members assumed; do not treat this report as registration |
| Required acknowledgment | Official Rules | Exact supplied acknowledgment included in main report; include it in public communications and video |
| CC BY outputs | Rules/FAQ | `LICENSE.md` applies to original Track 2 contributions; third-party sources retain their own terms |

## Data and publication duties

Keep the small submitted findings, HPO terms, mechanism analysis and clean code/report. Remove raw genomic files, genotype-scale derivatives and genome-bearing logs from controlled systems within the official deletion window; indices and intermediate copies are included. No such patient-scale files were ingested by this Track 2 workflow. The participant's separate local Track 1 environment still requires its own inventory and eventual deletion.

The Rules specify deletion within 30 days of challenge close and an email attestation to `RarediseaserealkidMVAhackathon2026@synapse.org`. With the currently listed close, the calculated outer date is November 23, 2026; re-evaluate if the organizer changes close or the accepted agreement specifies an earlier duty. No deletion or email has been performed. Do not claim compliance on systems not checked.

The official privacy clarification permits service processors only under specified no-training/no-independent-use and limited-retention conditions. It distinguishes publishable findings from genome-bearing data and limits attestation to participant-controlled systems. Record actual provider settings and consider special credit terms; do not infer compliance from a product name. See discussion 2 for controlling detail.

Do not identify or contact the child, family or MVA Society contacts about the case. Any suspected unauthorized disclosure follows the organizer's Privacy and Compliance Office reporting route; no disclosure incident is asserted here.

The publication embargo runs from challenge close until the organizer publicly posts its summary report/preprint. During that interval, manuscripts using the challenge dataset may not be submitted for peer review. Preliminary conference abstracts/posters require prior written organizer approval. Clean code and permitted derived outputs may be shared. This package is not a journal submission. At publication, use the dataset citation supplied by the organizer's Synapse page; the exact formal citation is still to be resolved. The public landing-page citation is not falsely labeled as that formal reference.

## Official ambiguities preserved

- The About timeline lists judging October 24–November 24 and awards November 25; FAQ/submission text describes approximately two to three months. Do not promise an announcement date from inconsistent text.
- “One final submission per team” in the template is consistent with three revision opportunities followed by review of the latest version. It is not permission for parallel submissions from several members.
- No exhaustive list of accepted approval jurisdictions or policy for withdrawn historic products was recovered. The package uses specific listed US prescription products; no eligibility is asserted for unresolved experimental/withdrawn candidates.
- A local file check cannot certify the user's account settings, accepted agreement, video availability, repository write access or actual submission quota.

## Final release checklist

- [ ] Confirm final HF username/team display name and one representative.
- [ ] Complete accurate provider/tier/settings declarations for all materially used AI environments.
- [ ] Review report and candidate nomination; remove draft status only after outstanding items are resolved.
- [ ] Publish the reviewed code/documentation to the existing GitHub repository through authorized access.
- [ ] Record the script, verify actual duration, include acknowledgment and obtain the video URL.
- [ ] Verify judge access to repository and video, plus current rule/product status and live quota.
- [ ] Upload the report once the concrete package is final and save receipt/version information.
- [ ] At the required time, inventory/delete restricted data in participant-controlled environments and send the required attestation.

The current technical verification result is in `validation.json`; open human-dependent items must remain open even when file checks pass.

## Official sources

- [Rules](https://huggingface.co/spaces/SageBio/rare-disease-real-kid-mva-hackathon-2026/blob/main/tabs/rules.py)
- [Submission implementation](https://huggingface.co/spaces/SageBio/rare-disease-real-kid-mva-hackathon-2026/blob/main/tabs/submit_track2.py)
- [Configuration](https://huggingface.co/spaces/SageBio/rare-disease-real-kid-mva-hackathon-2026/blob/main/config.py)
- [FAQ](https://huggingface.co/spaces/SageBio/rare-disease-real-kid-mva-hackathon-2026/blob/main/tabs/faq.py)
- [Timeline and rubric](https://huggingface.co/spaces/SageBio/rare-disease-real-kid-mva-hackathon-2026/blob/main/tabs/about.py)
- [Methods workbook](https://huggingface.co/spaces/SageBio/rare-disease-real-kid-mva-hackathon-2026/resolve/main/static/templates/methods_description_form.xlsx)
- [Combination eligibility](https://huggingface.co/spaces/SageBio/rare-disease-real-kid-mva-hackathon-2026/discussions/5)
- [Privacy clarification](https://huggingface.co/spaces/SageBio/rare-disease-real-kid-mva-hackathon-2026/discussions/2)

Downloaded-source hashes are recorded in `../evidence/rules_manifest.json`. Re-fetch current materials when revising; do not treat a snapshot as a permanent rule.

## Final computational verification

On September 10, a repeat execution with freshly installed pinned dependencies reproduced the complete metrics JSON and both residue/rotamer tables exactly. All public reference input hashes matched the audited manifest. An initial native execution failure and truncated public PAE cache were resolved before this comparison. Script syntax and package consistency checks also passed. These checks do not establish biological efficacy.
