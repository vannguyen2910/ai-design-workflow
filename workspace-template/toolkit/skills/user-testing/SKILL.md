---
name: user-testing
description: Test a prototype with real users and rate the findings. Use when you have a prototype to test.
---

# Workflow: Test with users

Test the prototype with real people, record what they did, and turn it into findings that are rated and traced to the decision they affect. The AI drafts the script and sorts the notes; the sessions, the ratings and the verdict on each finding are yours.

*Status: draft. Try it on a real project and adjust it to how you work before you rely on it.*

| | |
|---|---|
| Working files | `work/test-plan.md` (steps 1 to 3), `work/findings.md` (steps 5 to 8). Copy `../toolkit/skills/user-testing/templates/usability-test-script.md` into `work/` for the script |
| Sources | `work/sources/anonymised/T01.md`, `T02.md`... (one file per session, quotes with IDs: T01-01, T01-02...) |
| Original data | `work/sources/_raw-private/` (recordings, raw notes: the AI does not read it) |
| Final output | `work/findings.md`, the evidence items `insights/evidence/E*.md` (one per session or one per round), the finding items `insights/findings/F*.md` |
| Related | `../toolkit/skills/prototype/SKILL.md` is the step before; `standards/severity-levels.md` (the 0 to 4 scale); `../toolkit/skills/user-testing/templates/test-report.md` for the shape of the report; `../toolkit/skills/handoff/SKILL.md` is the step after |
| Examples | `../toolkit/skills/user-testing/examples/`: the Travel Buddy sample, to see the shape. Do not copy its content |

**A test needs real people.** An AI that "plays a user" tells you what a language model expects a user to say, not what a person does. If you cannot get real users yet, a simulated run can find obvious problems in the script, but label it **simulated** everywhere it appears and never count it as evidence for a hypothesis.

## Sections of the working files

| Section | Filled in step | By |
|---|---|---|
| `work/test-plan.md` (hypothesis, tasks, participants, metrics) | 1 | YOU |
| `## Script (AI draft)` in `work/test-plan.md` | 2 | AI. **Do not edit** |
| `## Script` | 3 | YOU: the final script, after a pilot |
| `sources/anonymised/T01.md`... | 4 | YOU |
| `## Observations (AI draft)` | 5 | AI. **Do not edit** |
| `## Observations (verified)` | 6 | YOU: your corrected copy, with the error count |
| `## Findings (proposed)` | 7 | AI proposes in the chat. **No file is created** |
| `## Results against the baseline`, `## Findings` | 8 | YOU |

Two rules: the AI returns only its own section, and the AI draft is always kept apart from the version you checked.

## If a gate is not met

| Gate | After step | If the answer is no |
|---|---|---|
| A: a test that can show you wrong? | 3 | Rewrite the tasks so they do not name the buttons, and pilot again |
| B: observations true to what happened? | 6 | Run step 5 again for that session with a tighter instruction, then check again |
| C: findings rated by you and traced to evidence? | 8 | Go back to step 7 and re-rate with the scale in `standards/severity-levels.md` |

---

## Step 1: Plan the test

**Who:** YOU
**Input:** `work/options.md` or the prototype's `## Scope`, `insights/hypotheses/`, `insights/metrics/`
**Output:** `work/test-plan.md`

Fill in: the hypothesis (H#) and **what result would change your mind**; 3 to 5 tasks, each a situation in the user's words, not a list of clicks; who you need (criteria) and how many (3 to 5 people show the big problems); what you measure with today's baseline and a target (task success without help, time, errors, satisfaction); consent. Mark each number you have not confirmed as `assumed`.

**Check:** If the test goes badly, would you really change the design? Is any task phrased with the name of a button?
**Failure sign:** No hypothesis; "test the whole app"; the participants are your colleagues.

## Step 2: Draft the script

**Who:** AI
**Input:** `work/test-plan.md` and `../toolkit/skills/user-testing/templates/usability-test-script.md` (the shape only)
**Output:** `## Script (AI draft)`

**Instruction:**
> Use only my test plan below and the template. Write the script: an opening to read aloud (this tests the product, not them; no right or wrong answers; they can stop), two warm-up questions about their background and not about the product, each task as a situation with a success condition, a time limit and a neutral follow-up ("What are you thinking?"), a one-question difficulty rating after each task, and a closing. Never name a button or a menu in a task, never suggest the answer, never describe a feature as good. List the three tasks most likely to lead the participant and why. Do not invent results. Return only the script.

**Failure sign:** A task that says "click the...", "Do you find it easy...", praise for the design.

## Step 3: Pilot and fix · Gate A

**Who:** YOU
**Input:** `## Script (AI draft)`
**Output:** `## Script` (final), with the note-taking sheet

Run the script once with someone outside the team. Note where they were confused by the task wording, and fix those tasks. Time it and cut tasks to fit. Check the prototype has no blocking bug other than the ones you want to test. Decide how you take notes and where the recordings go (`work/sources/_raw-private/`).

**Gate A:** Could this test prove you wrong? Does a pilot participant understand each task without help? Is consent written down?
**Failure sign:** No pilot; the final script is the AI draft unchanged.

## Step 4: Run and anonymise

**Who:** YOU
**Input:** Your script and the real sessions
**Output:** `work/sources/anonymised/T01.md`, `T02.md`... (one per session)

Run the sessions yourself. Write behaviour, not interpretation: what they did, where they hesitated, what they said word for word. Keep recordings and raw notes in `_raw-private/`. **Anonymise before the AI sees anything** (participant code P#, no names, no company names; find and replace on your machine). Give each quote an ID (`T01-01`...) and keep it verbatim. For each task record: completed (yes / with help / no), time, errors.

**Failure sign:** Notes that say "the user was confused" with no quote and no moment; a name left in the file.

## Step 5: Sort the notes

**Who:** AI
**Input:** `work/test-plan.md` and **one** session file. Run this step once per session
**Output:** `## Observations (AI draft)`, one sub-heading per session (`### T01`)

**Instruction:**
> Use only this session file. For each task, fill a row: completed (yes / with help / no) as recorded, time, the errors and hesitations that are in the notes, and the verbatim quote with its ID that shows it. Then list the moments where the participant did something different from what the task expected. Write what happened, not why; do not interpret and do not suggest fixes. If the notes do not say, write "unknown". Never rewrite or invent a quote. Return only the `### T01` block.

**Failure sign:** A cause ("because the label is unclear") instead of an observation; a quote not in the file.

## Step 6: Verify · Gate B

**Who:** YOU
**Input:** `## Observations (AI draft)`, the session files, and the recording
**Output:** `## Observations (verified)`, with the number of wrong cells and the error rate at the top

Check every "no" and "with help" against the recording or your raw notes, and every quote against the session file. Add the moments the AI missed. Fix and count the errors.

**Gate B:** Is every quote verbatim and every result true to the recording? Is the error rate written down?
**Failure sign:** Only the first session was checked; the verified copy equals the draft.

## Step 7: Propose findings

**Who:** AI proposes, then YOU decide
**Input:** `## Observations (verified)`, `work/test-plan.md`, `standards/severity-levels.md`, `standards/principle-checks.md`, the decisions in `insights/decisions/`
**Output:** A proposal table in the chat. **No file is created yet**

**Instruction:**
> From the verified observations only, propose findings, one row each: what happened (from the user's view, not a solution), how many of the participants met it and in which task, the evidence IDs, the principle (P#) it relates to, the decision (D#) it affects, and a suggested severity 0 to 4 with the three reasons (how often, how bad when met, whether it comes back). Group the same problem seen in several sessions into one finding. Do not propose a fix. Do not mark any finding fixed or accepted. List what these few sessions cannot tell us. Say what you are unsure about.

**Failure sign:** A finding seen once presented as "users"; a severity with no reasons; a fix in the finding.

## Step 8: Rate and record · Gate C

**Who:** YOU
**Input:** The proposal table, the verified observations
**Output:** `## Results against the baseline`, `## Findings` in `work/findings.md`, and the items in `insights/`

Rate each finding yourself on the 0 to 4 scale, ideally with a second person, and write the reason for levels 3 and 4. Drop findings you cannot trace to a quote. Compare the results with the baseline and target from step 1 (met or not). Create the evidence with `new-item.py E` (`--tests H1`, participants, `--status run`) and each approved finding with `new-item.py F` (`--found-in E1 --affects D2 --severity 3`). (`../toolkit/skills/add-insights/SKILL.md` describes the same propose-approve-create routine for research documents; here the source is your verified observations.) The resolution stays `open` until you decide: fix, accept as a trade-off with the reason, or defer. Write what will change because of the test.

**Gate C:** Is every finding rated by you, with its quote? Does every level 3 or 4 have a decision (fix, accept, defer) and a reason? Did the results answer the hypothesis, or did you write what the test cannot tell?
**Failure sign:** Severity copied from the AI; "users struggled" from three sessions; a level 4 left `open` with no plan.

---

## The limit to state plainly

Three to five sessions show you the large problems, not how often they happen. A test shows where people stumble, not whether the product will succeed. Treat the findings as reasons to change the design, then test again.
