# Gaia translator — reviewer kickoff meeting

**Duration**: 60 minutes
**Format**: Zoom (or hybrid); record for asynchronous attendees
**Attendees**: 2–3 reviewers per discipline (target ~18–25 total) + the PI

**Goals of this meeting** (in priority order):
1. **Calibrate scoring across reviewers** so the independent scoring round produces usable inter-rater reliability.
2. Make sure every reviewer leaves with a clear, concrete next action and a deadline.
3. Give reviewers the cross-discipline overview so they can score answers outside their primary discipline when needed.

**Goals this meeting is NOT trying to achieve**:
- Pitching the project. They're already signed up.
- Comprehensive training on all 8 criteria. The reviewer instructions doc does that; the meeting is for calibration via worked examples.

---

## Before the meeting

- [ ] Send `templates/reviewer_instructions.docx` 48 hours in advance with a note: "please read sections 1–3 before the meeting." Don't expect everyone to read it, but most will skim.
- [ ] Generate each reviewer's personal scoring sheet from `templates/scoring_template.xlsx`. Pre-populate the three calibration QAs in the "Scoring" tab. Share with edit access to that reviewer's email only.
- [ ] Send a calendar invite with the Zoom link, the agenda, and links to their personal scoring sheet.
- [ ] Pre-recruit one "scoring buddy" per discipline pair (e.g., the seismologist who already knows the geotech reviewer) — they'll be helpful when discussion stalls.

---

## Agenda

### 0:00 – 0:05 — Welcome and goal (5 min)

- Quick intros: name, discipline, one sentence on what brought them in.
- The one-line framing: "We're building a research chatbot that translates across geoscience subfields, and you're scoring whether the answers it gives are good enough for your community."
- Two goals stated explicitly: (a) build a defensible evaluation benchmark; (b) feed back into the chatbot's underlying skill files. Both of these need your independent scoring, but to make that score signal usable we first need to calibrate.

### 0:05 – 0:15 — One worked example end-to-end (10 min)

Walk through **one** Nisqually-liquefaction-anchored QA from start to finish:
1. The question (cross-discipline: seismology + geotech + hydrology).
2. The chatbot's answer.
3. The cards it retrieved (`PD-liquefaction`, `CC-geotech-CSR-CRR`, `CC-hydro-p`, `TC-02`).
4. What's good (correct effective-stress framing, real DOIs).
5. What's questionable (does it overclaim about the digital twin's readiness?).

This grounds the rest of the meeting. Don't pitch the architecture — show what scoring actually feels like.

### 0:15 – 0:35 — Live calibration: 3 QAs (20 min)

The core of the meeting. Three QAs from `calibration_qas/calibration_set_v1.md`:

1. **QA-CAL-01** (clearly good) — anchors what a 5 looks like.
2. **QA-CAL-02** (clearly bad) — vocabulary collision, fabricated citation. Anchors what a 1 looks like.
3. **QA-CAL-03** (contested) — reviewers will genuinely disagree. This is the most productive part of the meeting.

For each QA:
- 90 seconds of silent reading (share screen with the QA + the answer).
- 60 seconds of silent scoring on three criteria only: Technical accuracy, Citation discipline, Refusal correctness. Reviewers enter scores in their personal sheet (or read out loud if they prefer).
- 4–5 minutes of discussion. The PI elicits scores from each reviewer (round-robin to avoid first-respondent dominance); identifies disagreements; surfaces what the rubric anchors say; resolves where possible.

The point is not to reach consensus. It's to surface the **shared interpretation of the rubric** so that independent scoring later produces alignable results.

**Watch for**: reviewers who give scores in narrow bands (everything 3–4) regardless of the answer; reviewers who never use the extremes. These bias future IRR.

### 0:35 – 0:45 — Walkthrough of the scoring sheet and instructions (10 min)

Live share. Show:
- The "Scoring" tab — the columns, what each one means, where to enter scores, where comments are mandatory.
- The "Progress" tab — automatic summary of their progress.
- The "Flags" tab — for any QA they want to escalate for group discussion before scoring.
- The "skill_file_to_revise" column — emphasize that this is the row that turns their scoring effort into card revisions for the chatbot.

Common questions to address proactively:
- "What if a QA is outside my expertise?" — Score it; mark Confidence low; mention in comment.
- "What if I disagree with the gold reference?" — Score the model answer as if the gold reference doesn't exist; add a comment.
- "What if the chatbot answer cites a paper I don't know?" — Look it up; if you can't find it after 2 minutes, mark the citation criterion ≤ 2 and flag.

### 0:45 – 0:55 — Q&A and logistics (10 min)

- Communication channel: Slack workspace or shared email thread for ongoing questions.
- Deadlines:
  - Calibration round (the 3 QAs): **1 week from today** at 5pm Pacific.
  - Full scoring (~25 QAs): **6 weeks from today**.
- IRR computation happens between the calibration round and full scoring. If α < 0.7 we hold a 30-minute follow-up; otherwise everyone moves to full scoring directly.
- Honoraria (if applicable) and the co-authorship process per the signed signup form.
- Acknowledgment of conflicts of interest: any reviewer who recognizes a paper or method they personally developed in a QA should flag it and not score that QA.

### 0:55 – 1:00 — Close with a forced decision (5 min)

- One round-robin question: "Will the calibration round (3 QAs in your sheet) be done by [deadline]? Yes or no."
- Anyone who says no, get a real deadline from them. If they can't commit, they're out of this round (no penalty — just plan around it).
- Send the meeting recording, calibration sheet link, and instructions doc in chat before closing.

---

## After the meeting

- [ ] Send written follow-up within 4 hours:
  - Calibration deadline restated.
  - Direct link to each reviewer's scoring sheet.
  - Direct link to `templates/reviewer_instructions.docx`.
  - Communication channel link.
  - Honoraria/co-authorship form for signature if not already collected.
- [ ] Update the master tracker with attendance, calibration commitments, and any conflicts disclosed.
- [ ] Schedule the calibration-debrief slot in your own calendar for 8 days from the meeting (the day after the calibration deadline) — that's when you compute α and decide on the second calibration session.

---

## Failure modes to plan for

- **One reviewer dominates discussion.** Use round-robin elicitation strictly. Time-box each speaker.
- **No reviewer gives a 1 or a 5 in calibration.** Coach explicitly: the calibration QAs are designed so one should score 5 and one should score 1 on Technical Accuracy. If everyone is in the middle, the rubric isn't being used correctly.
- **A reviewer asks questions that should be in the instructions doc.** Politely defer to the doc, note the question, update the doc for the next session.
- **A reviewer disagrees with the rubric itself.** Acknowledge, note for v2, but score against the v1 rubric for this round. The rubric will evolve from feedback — but only with internally-consistent v1 data.
