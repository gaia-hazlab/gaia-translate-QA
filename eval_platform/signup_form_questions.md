# Reviewer signup + consent — Google Form questions

Paste these questions into a Google Form titled **"Gaia translator — reviewer signup + consent"**. The Form output sheet becomes the master reviewer registry.

The Form should be set to require Google sign-in (for audit trail) and to *not* allow editing after submission. Each reviewer fills it once before being added to the kickoff meeting.

---

## Section 1: Identification

1. **Full name** (short answer, required)
2. **Preferred name for attribution** (short answer, required) — how should we credit you on the Zenodo DOI / acknowledgments / methodology paper?
3. **Email address** (short answer, required, format: email)
4. **Institution and current title** (short answer, required) — e.g., "Postdoc, UW ESS" or "Associate Professor, Caltech GPS"
5. **ORCID** (short answer, optional, format: 0000-0000-0000-0000) — recommended for attribution and identity verification

## Section 2: Discipline self-identification

6. **Primary discipline** (multiple choice, required, single answer):
   - Hydrology
   - Seismology
   - Geotechnical engineering
   - Geomorphology
   - Atmospheric sciences
   - Ecology
   - Agricultural sciences
   - Near-surface geophysics
   - Other (please specify in #8)

7. **Secondary disciplines you can score with confidence** (checkboxes, optional, multi-answer): same list as #6. Pick all that apply. Empty is fine.

8. **If you selected "Other" above, please specify** (short answer, optional)

9. **Briefly describe your research area** (paragraph, required, 1–3 sentences) — used for matching you to QAs in your domain of expertise.

## Section 3: Availability and commitment

10. **How many hours can you commit over the next 6 weeks?** (multiple choice, required):
    - Less than 2 hours (consider opting out — calibration round alone requires ~1 hour)
    - 2–4 hours (calibration round only)
    - 5–8 hours (calibration + 15–25 QAs)
    - 9–15 hours (calibration + 25–50 QAs)
    - 16+ hours (calibration + full set + can help recruit or review v2 rubric)

11. **Are there blackout periods (conference travel, sabbatical, etc.) in the next 6 weeks?** (paragraph, optional)

12. **Time-zone for scheduling the kickoff meeting** (short answer, required) — e.g., "US Pacific" or "UTC+2"

## Section 4: Conflicts of interest

13. **Do you have any papers, methods, or named software products that might appear in the QAs?** (paragraph, required) — list them. We will route around them when assigning QAs. Examples: "My own paper on PhaseNet (Zhu & Beroza 2019)"; "I am the lead developer of DEEPSOIL." No conflict is also a valid answer — write "none."

14. **Are you a co-PI, postdoc, or close collaborator of any current Denolle Group member?** (multiple choice, required):
    - Yes — please describe in the comment box
    - No
    - Comment (paragraph, optional)

## Section 5: Consent, attribution, data use

15. **Consent to participate** (checkbox, required):
    - [ ] I understand I will independently score chatbot answers against a rubric; my scores will be aggregated with other reviewers' scores.

16. **Attribution preference** (multiple choice, required):
    - Named attribution (Zenodo DOI + any methodology paper + acknowledgments)
    - Aggregated attribution only (listed as "X reviewers across N disciplines"; not individually named)
    - Other (please specify)

17. **Co-authorship on the methodology paper** (multiple choice, required) — assumes you score ≥ 20 QAs and provide actionable comments:
    - Yes, please consider me for co-authorship
    - No, acknowledgments only is fine

18. **Data-use consent for aggregated release** (checkbox, required):
    - [ ] I consent to my scores (without my identity) being released as an open dataset under CC-BY-4.0 alongside the final eval set.

19. **Honoraria** (multiple choice, optional):
    - I am eligible to receive a $250 honorarium and will provide tax info separately if needed.
    - I am not eligible (federal employee / institutional policy / personal preference) — please use the funds for someone else or for the project.
    - Other (please specify)

## Section 6: Final

20. **Anything else we should know?** (paragraph, optional)

21. **OK to add you to the project Slack workspace?** (yes/no, required)

---

## Form settings checklist

- [ ] Require Google sign-in (for audit trail)
- [ ] One response per person (toggle on)
- [ ] Show progress bar
- [ ] Send a copy of the response to the reviewer's email automatically
- [ ] Output sheet auto-created and shared with the PI
- [ ] Confirmation page text: "Thanks. You'll receive a calendar invite for the kickoff meeting within 48 hours, plus a personal scoring sheet link before the meeting."

---

## Post-submission workflow

For each Form response:
1. Check the conflict disclosure (#13). Flag any conflicts before QA assignment.
2. Verify the ORCID (#5) against ORCID.org.
3. Add to the master tracker (one row per reviewer): name, email, ORCID, primary discipline, secondary disciplines, hours committed, conflicts.
4. Generate the personal scoring sheet (`Gaia_Eval_<Discipline>_<LastName>_v1.xlsx`) from `templates/scoring_template.xlsx`.
5. Send the calendar invite + the scoring-sheet link + the instructions doc.
