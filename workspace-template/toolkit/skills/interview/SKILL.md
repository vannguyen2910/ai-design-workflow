---
name: interview
description: Plan interviews or summarise anonymised interview notes. Use when you plan interviews or have interview notes to summarise.
---

# Workflow: Interview

Plan and run user interviews with the AI as a helper: it drafts the guide and summarises each anonymised interview, and you check every summary against your own notes before anything goes into the hub.

*Status: draft. Try it on a real project and adjust it to how you work before you rely on it.*

| | |
|---|---|
| Working file | `work/interview-guide.md` (copy it from `../toolkit/skills/interview/templates/interview-guide.md` if it is not there yet). Each step fills one section |
| Sources | `work/sources/anonymised/I01.md`, `I02.md`... (one file per interview, quotes with IDs: I01-01, I01-02...) |
| Original data | `work/sources/_raw-private/` (recordings, raw notes: the AI does not read it) |
| Final output | Checked interview summaries in the working file, ready for `../toolkit/skills/user-voice-synthesis/SKILL.md` (step 5) or `../toolkit/skills/add-insights/SKILL.md` |
| Related | `../toolkit/skills/interview/templates/research-plan.md` if the research needs a full plan; `context/data-rules.md` for what may go to the AI |

The interview itself is **always yours**: you meet the real person. The AI helps before (the guide) and after (the summary), never instead.

## Sections of the working file

| Section | Filled in step | By |
|---|---|---|
| `## Goal` (decision, research questions, beliefs, who) | 1 | YOU |
| `## Core questions (AI draft)` | 2 | AI. **Do not edit** |
| `## Core questions` and `## Before the session` | 3 | YOU: the final guide, participants, consent |
| `sources/anonymised/I01.md`... | 4 | YOU |
| `## Summaries (AI draft)` | 5 | AI. **Do not edit** |
| `## Summaries (verified)` | 6 | YOU: your corrected copy, with the error count |
| `## Next` | 7 | YOU |

Two rules: the AI returns only its own section, and the AI draft is always kept apart from the checked version.

## If a gate is not met

| Gate | After step | If the answer is no |
|---|---|---|
| A: a guide that does not lead? | 3 | Go back to step 2 with the questions you cut, and ask for replacements |
| B: summaries true to what was said? | 6 | Run step 5 again for that interview with a tighter instruction, then check again |
| C: enough interviews? | 7 | Plan more interviews with the people who are missing, then repeat steps 4 to 6 |

---

## Step 1: Frame the goal

**Who:** YOU
**Input:** `work/scope.md` (if there is one), `context/product-and-users.md`
**Output:** `## Goal`

Fill in: the **decision** this research will help make (no decision, no interviews yet); at most 3 research questions (RQ1, RQ2, RQ3: what you need to learn, not questions to ask people); 3 to 5 beliefs the team already holds; who you need to hear from, including who is easy to forget (light users, people who stopped using it, people who never signed up).

**Check:** Does each research question ask about behaviour and problems, not about whether people like an idea?
**Failure sign:** "Do users want feature X?"; no decision named; only one kind of user.

## Step 2: Draft the guide

**Who:** AI
**Input:** `## Goal` (only this section)
**Output:** `## Core questions (AI draft)`

**Instruction:**
> Use only the goal below. Draft an interview guide of 30 to 45 minutes: two warm-up questions, then 8 to 10 core questions grouped by research question, each with two follow-ups. Every core question asks about something that already happened ("Tell me about the last time you..."), never about the future or an opinion of an idea, and never suggests its answer. Do not mention our product's features or any solution. Add a short screener: 3 to 5 criteria to include or exclude a participant. Then list the three questions most at risk of leading, and why. Return only this section, as a table: research question, main question, follow-ups.

**Check:** Read each question aloud. Does any question contain the answer, a feature, or the word "would"?
**Failure sign:** "Would you use...", "Do you find it hard to...", questions about the product's screens.

## Step 3: Review and pilot · Gate A

**Who:** YOU
**Input:** `## Core questions (AI draft)`, `## Goal`
**Output:** `## Core questions` (final) and `## Before the session` (participants, length, consent)

Edit the draft into your own guide: cut or rewrite the leading questions, keep 6 to 8 core questions you can ask in the time. Run it once with a colleague or a friend (a pilot). Note where they got confused or answered "yes / no", and fix those questions. Write who you will interview (codes P1, P2..., no names), how you find them, and how you ask for consent to take notes or record.

**Gate A:** Is every research question covered by at least one question? Does any question lead or pitch a solution? Is consent clear and written down?
**Failure sign:** The pilot was skipped; the final guide is the AI draft unchanged; no consent note.

## Step 4: Run and anonymise

**Who:** YOU
**Input:** Your guide and the real interviews
**Output:** `work/sources/anonymised/I01.md`, `I02.md`... (one per interview)

Run the interviews yourself. Keep recordings and raw notes in `work/sources/_raw-private/`. **Anonymise before the AI sees anything:** replace names, usernames, emails, company names and places that identify someone (find and replace on your machine, do not ask the AI). At the top of each file write the participant code and their situation (role, how long they have used the product), not who they are. Give each quote an ID (`I01-01`, `I01-02`...) and keep it verbatim.

**Failure sign:** A real name left in the file; quotes rewritten "to read better"; no IDs.

## Step 5: Summarise each interview

**Who:** AI
**Input:** `## Goal` and **one** interview file (`sources/anonymised/I01.md`). Run this step once per interview
**Output:** `## Summaries (AI draft)`, one sub-heading per interview (`### I01`)

**Instruction:**
> Use only this interview file. Summarise it against the research questions in the goal: (1) the participant's situation in one line; (2) for each research question, what this person did, what got in the way, and how they worked around it, each point with the IDs of the quotes it comes from; (3) the 3 to 5 quotes that matter most, verbatim with their ID; (4) which of the team's beliefs this interview supports, contradicts or does not touch; (5) what was surprising; (6) what is still unknown. Do not generalise to other users, do not suggest solutions, and never rewrite, shorten or invent a quote. If something is not in the file, write "unknown". Return only the `### I01` block.

**Failure sign:** A quote that is not in the file; "users want..." (one person is not "users"); a solution in the summary.

## Step 6: Verify · Gate B

**Who:** YOU
**Input:** `## Summaries (AI draft)` and the interview files in `sources/anonymised/`
**Output:** `## Summaries (verified)`, with the number of wrong quotes, the number of wrong or missing points, and the error rate at the top

Copy each summary into `## Summaries (verified)`. (1) Find **every quote** in the interview file: is it verbatim and with the right ID? (2) Re-read your own notes from the session: did the summary miss a moment you remember as important, or give weight to something the person said in passing? (3) Fix the errors and count them.

Better, once: summarise the first interview yourself before you read the AI's version, then compare.

**Gate B:** Is every quote verbatim and traceable? Would the participant recognise themselves in the summary? Is the error rate written down?
**Failure sign:** Only the first summary was checked; no error rate; the verified copy is identical to the draft.

## Step 7: Decide what comes next · Gate C

**Who:** YOU
**Input:** `## Summaries (verified)`, `## Goal`
**Output:** `## Next`

Write: which research questions now have an answer and which do not; whether the last two interviews still brought something new (if yes, you need more); who is still missing from the sample. Then choose the next step: code the quotes across interviews with `../toolkit/skills/user-voice-synthesis/SKILL.md` (step 5), or turn what you learned into items with `../toolkit/skills/add-insights/SKILL.md` (one evidence per interview).

**Gate C:** Can you answer each research question by pointing at quotes from at least two people? Is the missing group named?
**Failure sign:** Moving on after one or two interviews; the summaries go straight into opportunities without synthesis.

---

## The limit to state plainly

Interviews show what people **say** about what they did, a few people at a time. Memory is selective and people are polite. Treat what you learn as evidence for hypotheses, and test them later with behaviour (analytics, usability tests).
