# Track 2 requirements and submission readiness

October 24 documentation synchronization following participant approval of the reviewed report. The original requirements mapping was checked against official materials September 10; the final video brief records later October checks. Reconfirm live rules and quota before an actual upload. This is a readiness record, not a claim that an upload or institutional approval has occurred. The participant's separately accepted gated-data agreement must also be observed; its account-specific acceptance state cannot be inspected here.

## Official requirement mapping

| Requirement | Source | Package implementation / status |
|---|---|---|
| Existing market-approved medication candidates | Official Rules; discussion 5 | Current report has conditional candidates; especially amlexanox product/jurisdiction/formulation eligibility remains unresolved; new mRNA product excluded |
| Characterize variant mechanism and biological consequence | Submission tab | Report sections 1–3; structural/transcript outputs |
| Written report in PDF or Markdown, filename including user/team | Submission tab | `ivillafuerte_track2_report.md`; verify chosen submission identity |
| Reproducible GitHub code and configuration | Submission tab | September allele computations and recovered October scripts are public; see ../reproduction/README.md for clean-checkout commands, tested scope and upstream limits |
| Repository public at challenge end | Submission tab | Public Track 2 draft PR #1 / research branch exists, separate from main; verify final commit before submission |
| Three-minute video hosted on YouTube or Vimeo | Submission tab | [YouTube video](https://youtu.be/u527j7tO0OA) available without login; displayed runtime 2:57. Full audiovisual review and credits verification remain open |
| Provider, plan/tier and relevant AI handling settings | Submission tab; discussion 2 | Methods row 9 records participant-confirmed ChatGPT “Premium”, Claude Max and model-improvement settings disabled in both; no independent account audit or zero-retention guarantee |
| Methods template answers | Official workbook, Track 2 sheet | All rows 7–17 mapped in English Markdown; most fields optional, AI disclosure required |
| Up to three versions; latest reviewed; one representative | Configuration, FAQ, submission code | Do not spend a version on an unfinished package; live quota is not known here |
| Submission deadline | About timeline | October 24, 2026, 23:59 UTC; recheck before upload |
| Judging rubric | Rules/About | Scientific rigor 35%, impact 25%, innovation 25%, scalability 15%; addressed in report section 8 |
| Each team member registered and at least 18 | Official Rules | Participant reports prior registration/Track 1 completion; no additional members assumed; do not treat this report as registration |
| Required acknowledgment | Official Rules | Exact supplied acknowledgment included in main report; include it in public communications and video |
| CC BY outputs | Rules/FAQ | `LICENSE.md` applies to original Track 2 contributions; third-party sources retain their own terms |

## Data and publication duties

Keep the small submitted findings, HPO terms, mechanism analysis and clean code/report. Remove raw genomic files, genotype-scale derivatives and genome-bearing logs from controlled systems within the official deletion window; indices and intermediate copies are included. No such patient-scale files were ingested by this Track 2 workflow. The participant's separate local Track 1 environment still requires its own inventory and eventual deletion.

The current Rules (last updated October 13; re-fetched October 22) specify deletion within 30 days of challenge close and an email attestation to `cnb@sagebase.org`. The [October 13 organizer commit](https://huggingface.co/spaces/SageBio/rare-disease-real-kid-mva-hackathon-2026/commit/22726e3eeb1b007c754c01a4d8113d32be913a3c) supersedes the earlier email address. With the currently listed close, the calculated outer date is November 23, 2026; re-evaluate if the organizer changes close or the accepted agreement specifies an earlier duty. No deletion or email has been performed. Do not claim compliance on systems not checked.

The official privacy clarification permits service processors only under specified no-training/no-independent-use and limited-retention conditions. It distinguishes publishable findings from genome-bearing data and limits attestation to participant-controlled systems. Record actual provider settings and consider special credit terms; do not infer compliance from a product name. See discussion 2 for controlling detail.

Do not identify or contact the child, family or MVA Society contacts about the case. Any suspected unauthorized disclosure follows the organizer's Privacy and Compliance Office reporting route; no disclosure incident is asserted here.

The publication embargo runs from challenge close until the organizer publicly posts its summary report/preprint. During that interval, manuscripts using the challenge dataset may not be submitted for peer review. Preliminary conference abstracts/posters require prior written organizer approval. Clean code and permitted derived outputs may be shared. This package is not a journal submission. At publication, use the dataset citation supplied by the organizer's Synapse page; the exact formal citation is still to be resolved. The public landing-page citation is not falsely labeled as that formal reference.

## Official ambiguities preserved

- The September snapshot had older judging/awards dates. The October 22 video brief records an updated December 18 announcement and unchanged October 24 23:59 UTC close. Recheck current official discussions 26/28 and timeline before relying on dates; a narrative revision does not refresh rules_manifest.json.
- “One final submission per team” in the template is consistent with three revision opportunities followed by review of the latest version. It is not permission for parallel submissions from several members.
- No exhaustive list of accepted approval jurisdictions or policy for withdrawn historic products was recovered. Historical US product precedents do not establish current eligibility of the October shortlist. Amlexanox remains unresolved; no eligibility is asserted for experimental/withdrawn candidates.
- Participant AI settings are attestations, not an account audit. Video availability and 2:57 displayed duration were checked separately; complete audio/image quality remains unverified. A local file check cannot certify the accepted agreement or actual submission quota.

## Final release checklist

- [ ] Confirm final HF username/team display name and one representative.
- [x] Record participant-confirmed provider/tier/settings declarations in methods row 9, retaining the stated scope and historical-model limitations.
- [ ] Review report and candidate nomination; remove draft status only after outstanding items are resolved.
- [x] Public Track 2 draft branch exists (PR #1); this is not a main-branch merge or competition submission.
- [x] Recover and rerun the four deterministic October reanalyses from public processed inputs; preserve stated upstream limitations (see ../reproduction/README.md).
- [x] Participant approved the reviewed report on October 24; synchronize the exact approved Markdown and verify its remote contents. Approval and repository synchronization are not competition submission.
- [ ] Resolve current medication product/jurisdiction/formulation eligibility, especially amlexanox.
- [x] Record the available video URL: https://youtu.be/u527j7tO0OA ; displayed runtime 2:57, accessible without login.
- [ ] Complete uninterrupted audiovisual review and verify any on-screen/spoken credits; caption artifacts are not proof of an audio defect.
- [ ] Verify judge access to repository and video, plus current rule/product status and live quota.
- [ ] Upload the report once the concrete package is final and save receipt/version information.
- [ ] At the required time, inventory/delete restricted data in participant-controlled environments and send the required attestation.

The September technical verification result in `validation.json` is historical and its file hashes predate this revision. It does not certify the revised report or October reanalyses. The first October 22 documentation-only check is preserved in `documentation_check_2026-10-22.json`; the later source-execution audit lives with the reproduction package and the follow-on documentation check is recorded in `followup_check_2026-10-22.json`. Human-dependent and biological items remain open even when file checks pass.

## Official sources

- [Rules](https://huggingface.co/spaces/SageBio/rare-disease-real-kid-mva-hackathon-2026/blob/main/tabs/rules.py)
- [Submission implementation](https://huggingface.co/spaces/SageBio/rare-disease-real-kid-mva-hackathon-2026/blob/main/tabs/submit_track2.py)
- [Configuration](https://huggingface.co/spaces/SageBio/rare-disease-real-kid-mva-hackathon-2026/blob/main/config.py)
- [FAQ](https://huggingface.co/spaces/SageBio/rare-disease-real-kid-mva-hackathon-2026/blob/main/tabs/faq.py)
- [Timeline and rubric](https://huggingface.co/spaces/SageBio/rare-disease-real-kid-mva-hackathon-2026/blob/main/tabs/about.py)
- [Methods workbook](https://huggingface.co/spaces/SageBio/rare-disease-real-kid-mva-hackathon-2026/resolve/main/static/templates/methods_description_form.xlsx)
- [Combination eligibility](https://huggingface.co/spaces/SageBio/rare-disease-real-kid-mva-hackathon-2026/discussions/5)
- [Privacy clarification](https://huggingface.co/spaces/SageBio/rare-disease-real-kid-mva-hackathon-2026/discussions/2)

Historical downloaded-source hashes are recorded in `../evidence/rules_manifest.json`; the separately fetched October 22 rules check is recorded in `../evidence/rules_check_2026-10-22.json`. Re-fetch current materials when revising; do not treat a snapshot as a permanent rule.

## Final computational verification

On September 10, a repeat execution with freshly installed pinned dependencies reproduced the complete metrics JSON and both residue/rotamer tables exactly. All public reference input hashes matched the audited manifest. An initial native execution failure and truncated public PAE cache were resolved before this comparison. Script syntax and package consistency checks also passed. These checks do not establish biological efficacy.

## October 24 synchronization boundary

The participant-approved report is copied without changing its reviewed scientific content or REVIEW status. Methods are copied from its Appendix A. The video is available, but cloud playback did not permit complete audiovisual quality review; no defective upload is inferred. Amlexanox eligibility and the organizer-prescribed dataset citation remain unresolved. No competition submission receipt has been verified. No main-branch merge, workflow reactivation, raw patient-data publication or clinical validation is implied by this documentation synchronization.
