# Gaia eval platform — v1

The first version of the human-expert evaluation platform for the Gaia translator chatbot. Used for the kickoff calibration meeting and the subsequent independent scoring rounds.

This v1 is intentionally **lightweight by design**: Google Sheets + a Google Form, no custom web app yet. The data model is generic enough to extend to other evaluation exercises (coding agents, document-review agents, future LLM/MoE work). When the lightweight workflow hits friction we escalate per the roadmap (Phase 7c → Streamlit app with ORCID auth).

## What's here

```
eval_platform/
├── README.md                                ← you are here
├── meeting_agenda.md                        ← 60-min kickoff calibration meeting
├── signup_form_questions.md                 ← questions to paste into a Google Form
├── architecture_note.md                     ← future-generalization design notes
│
├── templates/
│   ├── reviewer_instructions.docx           ← what reviewers read first; Google-Doc compatible
│   └── scoring_template.xlsx                ← per-reviewer scoring sheet; Google-Sheets compatible
│
├── calibration_qas/
│   └── calibration_set_v1.md                ← 3 example QAs (good, bad, contested) used in the meeting and pre-populated in each reviewer's sheet
│
└── aggregation/
    └── (Python aggregator + master tracker template; populated in Phase 7b)
```

## Key design decisions and why

### One Google Sheet per reviewer (not one per discipline)

Each reviewer gets a single file named `Gaia_Eval_<Discipline>_<LastName>_v1.xlsx`, pre-populated with the QAs they're assigned. Reasons:

- **No accidental peer visibility.** During the independent-scoring phase, IRR requires that reviewers score without seeing each other's scores. Tabs in a shared workbook leak this.
- **Clean permissions.** One file, one share, one editor.
- **Easy progress tracking.** A master tracker lists every reviewer + their file URL + their last-modified timestamp; you can see at a glance who has started, who is half-done, who is silent.
- **Easy aggregation.** A Python script (Phase 7b deliverable) globs the reviewer files into a single JSON record and computes Krippendorff's α; trivial to do with N independent files, more brittle with N tabs in one workbook.

### Google Form for signup + consent only

A single Form captures: name, ORCID, institution, discipline self-identification, availability (hours), consent to data use, co-authorship preference, conflict-of-interest disclosure. **The Form is not used for the scoring itself.** Scoring needs a side-by-side view of question, model answer, retrieved context, and gold reference; a Form's one-page-per-question UX is inferior for this and adds friction.

### Eight-criterion rubric, 1–5 Likert per criterion

Modeled on the `pre-submission-reviewer` skill but adapted for chatbot output (not paper review). Eight criteria:

1. **Technical accuracy** — are the claims correct?
2. **Citation discipline** — are cited works real, DOIs accurate, claims actually supported by the citation?
3. **Vocabulary precision** — is discipline-specific language used correctly; are vocabulary collisions handled?
4. **Cross-discipline integration** — when the question spans disciplines, does the answer correctly bridge?
5. **Refusal correctness** — when the question invites a forced analogy or fabrication, does the chatbot refuse cleanly?
6. **Completeness** — does the answer address what was asked?
7. **Presentation** — clarity, structure, technical level appropriate to the audience.
8. **Overall usefulness** — would a researcher in your discipline actually find this helpful?

Each on 1–5. Mandatory free-text comment for any score ≤ 2 or ≥ 5. Mandatory "which card / playbook section should be revised" column when a low score is given — this is how the eval feeds back into card improvement.

### Calibration round before independent scoring

The three calibration QAs (`calibration_qas/calibration_set_v1.md`) are scored *live during the kickoff meeting*, then compared and discussed. After the meeting, reviewers score the same three QAs independently in their own sheet — those scores anchor the IRR baseline. Only after the calibration round (and any second-round if α < 0.7) do reviewers receive the full assignment.

### Two goals, both addressed by the data model

The user's two stated goals:
1. **Build a proper benchmark eval set.** The xlsx output is JSON-exportable; reviewer scores plus aggregate metrics become a citable dataset.
2. **Improve the skill files for the subagents.** Every low-score row has a "skill_file_to_revise" column pointing at a specific `CC-*`, `MC-*`, `PD-*`, or `TC-*` card, or a playbook section. The aggregator can rank cards by how often they appear in low-score comments; that ranks revision priorities.

## How to run a session — short version

1. **Recruit + signup**: send the Google Form. Get signed consent, ORCID, conflict disclosures, availability.
2. **Generate per-reviewer xlsx** from `templates/scoring_template.xlsx`. Pre-populate with their assigned QAs (first 3 are calibration). One file per reviewer.
3. **Schedule the kickoff meeting** (see `meeting_agenda.md`). 60 minutes. Hard deadline communicated for the calibration-scoring follow-up.
4. **Calibration round**: 1 week. Reviewers score the 3 calibration QAs independently. PI computes IRR.
5. **Decision gate**: if α ≥ 0.7, proceed to full scoring. If α < 0.7, hold a second 30-minute calibration session focused on the criteria with the worst agreement.
6. **Full scoring**: 4–8 weeks depending on the QA count.
7. **Aggregation + revision**: weekly digest of low-score comments → card revisions → eventual re-evaluation on a held-out QA set.

See `meeting_agenda.md` for the meeting-day details and `templates/reviewer_instructions.docx` for what to send the reviewers.

## Reusability for future exercises

The data model — `{question, agent_output, retrieved_context, gold_reference?, 8-criterion scores + comments, attribution metadata}` — is intentionally generic. To run a parallel evaluation of, say, a coding agent:

- Swap `discipline` for `language` or `task_domain` (Python, Rust, embedded, etc.).
- Swap the cross-discipline integration criterion for one that fits (e.g., "API correctness" or "security awareness").
- Reuse the technical-accuracy / citation / completeness / presentation / usefulness criteria as-is.
- Keep the calibration-round-first workflow.
- The aggregator and the master tracker code generalize without change.

See `architecture_note.md` for the longer version, including the generic data model and the path to a citable benchmark.
