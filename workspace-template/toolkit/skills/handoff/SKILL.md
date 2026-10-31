---
name: handoff
description: Prepare the handoff pack for developers and a measurement plan. Use when the design is ready for developers.
---

# Workflow: Handoff

Hand the design to the people who will build it, and agree how you will know after launch whether it worked. The AI drafts the handoff pack and the measurement plan from what the project already holds, and then reads them as a developer who has never seen the project. You confirm every line against the prototype.

*Status: draft. Try it on a real project and adjust it to how you work before you rely on it.*

| | |
|---|---|
| Working files | `work/handoff.md` (steps 1 to 3 and 6 to 7) and `work/measurement-plan.md` (steps 4 and 5) |
| Sources | The accepted decisions in `insights/decisions/`, `work/findings.md` and `insights/findings/`, the prototype in `work/prototype/`, `context/design-system-notes.md`, `insights/metrics/`, `insights/hypotheses/` |
| Original data | `work/sources/_raw-private/` (the AI does not read it) |
| Final output | `work/handoff.md`, `work/measurement-plan.md`, the report `index.html` (or the bundle) to send, and the metric items updated |
| Related | `../toolkit/skills/user-testing/SKILL.md` is the step before; `../toolkit/skills/refresh-hub/SKILL.md` (warnings before handoff); `../toolkit/skills/build-report/SKILL.md` (the bundle); `../toolkit/skills/handoff/templates/measurement-plan.md` for the shape |
| Examples | `../toolkit/skills/handoff/examples/`: the Travel Buddy sample, to see the shape. Do not copy its content |

A handoff is not a file drop. It is the point where a developer can build without coming back to you for every question, and where everyone has agreed in advance what "it worked" means.

## Sections of the working files

| Section | Filled in step | By |
|---|---|---|
| `## Readiness` in `work/handoff.md` | 1 | YOU |
| `## Handoff pack (AI draft)` | 2 | AI. **Do not edit** |
| `## Handoff pack (verified)` | 3 | YOU: your corrected copy |
| `## Measurement plan (AI draft)` in `work/measurement-plan.md` | 4 | AI. **Do not edit** |
| `## Measurement plan` | 5 | YOU |
| `## Developer's questions (AI)` | 6 | AI. **Do not edit** |
| `## Answers` and `## Agreement` | 7 | YOU |

Two rules: the AI returns only its own section, and the AI draft is always kept apart from the version you checked.

## If a gate is not met

| Gate | After step | If the answer is no |
|---|---|---|
| A: ready to hand off? | 1 | Fix, accept with a reason, or defer each blocking finding before you ask the AI for anything |
| B: every line true to the prototype? | 3 | Correct the line, or mark it `unknown` and put it in the open questions |
| C: measurable, with the rules set before the numbers? | 5 | Rework the metric, the data source or the decision rule |
| D: a developer can build from it? | 7 | Add the missing states, content or rules, and run step 6 again |

---

## Step 1: Check readiness · Gate A

**Who:** YOU
**Input:** The report (`index.html`), `work/findings.md`, `standards/gates.md`, and the warnings from `../toolkit/skills/refresh-hub/SKILL.md`
**Output:** `## Readiness` in `work/handoff.md`

List what blocks the handoff: findings of severity 3 or 4 still `open`; decisions still `proposed`; warnings the report shows for missing links; assumptions in the Problem brief nobody has confirmed. For each, decide: fix it, accept it as a trade-off with the reason (you set `accepted`, not the AI), or defer it with the date. Check the gate list for the stage.

**Gate A:** Is every severity 3 or 4 finding handled? Are the decisions you are handing off accepted by the person who owns them? Does the report show no warning you cannot explain?
**Failure sign:** "Looks ready" with open level 4 findings; a decision still `proposed` that the developers will build.

## Step 2: Draft the handoff pack

**Who:** AI
**Input:** The accepted decisions, `work/findings.md`, the prototype folder, `context/design-system-notes.md`, and `work/prototype/index.md` (known gaps). Only these
**Output:** `## Handoff pack (AI draft)`

**Instruction:**
> Write a handoff pack for a developer who has not seen this project. Use only the files I gave you. Include: (1) what is being built, in two sentences, and where the prototype is; (2) the decisions that apply, each by its code (D#) with its reason, not copied from the files; (3) for each screen: the content, the states (empty, loading, error, success), what each control does, and where it leads; (4) acceptance notes: statements that must be true when it is built, each one testable ("When... the user sees..."); (5) which parts of the prototype are fake or missing (take them from the known gaps); (6) which design system components and tokens are used; (7) open questions. If something is not in the files, write "unknown" and put it in the open questions. Never invent behaviour, content, data rules or technical constraints. Return only this section.

**Failure sign:** A state the prototype does not have; an acceptance note nobody could test ("should feel fast"); no open questions.

## Step 3: Verify against the prototype · Gate B

**Who:** YOU
**Input:** `## Handoff pack (AI draft)` and the prototype in a browser
**Output:** `## Handoff pack (verified)`, with the number of wrong lines at the top

Open the prototype and walk through it with the pack in hand. Check **every** screen description and **every** acceptance note: does the prototype do this? Is the decision cited the right one? Correct wrong lines, delete invented ones, and mark what you do not know as `unknown` in the open questions.

**Gate B:** Is each line true to the prototype and to an accepted decision? Is the error count written down?
**Failure sign:** Only the first screens were checked; the verified copy equals the draft.

## Step 4: Draft the measurement plan

**Who:** AI
**Input:** `insights/metrics/`, `insights/hypotheses/`, `work/problem-brief.md` (the outcome and baseline), `../toolkit/skills/handoff/templates/measurement-plan.md` (the shape only)
**Output:** `## Measurement plan (AI draft)` in `work/measurement-plan.md`

**Instruction:**
> Use only the metrics, the hypotheses and the brief below. For each metric (M#) write: the exact definition, the formula, the baseline and the target as given (or "assumed"/"unknown"), whether it is an outcome, a leading or a guardrail metric, the data source and the events or queries needed, and the segments to split by. Propose one outcome metric, one or two leading metrics and one guardrail, and say which existing M# fits each; do not invent a metric that does not exist. Then write the decision rules before any numbers exist: what result means continue, adjust or stop. List the qualitative signals to follow, and what could make the numbers misleading (small sample, seasonality, another change at the same time). Do not invent baselines or targets.

**Failure sign:** A target with no baseline; a metric nobody can measure with the current tracking; no guardrail.

## Step 5: Fix the measurement plan · Gate C

**Who:** YOU
**Input:** `## Measurement plan (AI draft)`, and the people who own the data
**Output:** `## Measurement plan` (final), and the metric items updated

Check each definition with the person who owns the data (analytics, engineering): can it be measured with the current events? Who builds the missing tracking, and by when? Name an owner and a review date for each metric. Set the decision rules **now**, before the numbers exist. Update `target` and `baseline` in the `insights/metrics/M*.md` files (the item is the single source). Only you set `verdict` later.

**Gate C:** Can every metric be measured? Has each one an owner and a date? Are the rules for continue, adjust and stop written before the numbers arrive?
**Failure sign:** "We will look at the dashboard"; a metric with no owner; rules written after seeing the first week.

## Step 6: Read it as a developer

**Who:** AI
**Input:** `## Handoff pack (verified)` and `## Measurement plan` only. **Do not** give it the rest of the project
**Output:** `## Developer's questions (AI)`

**Instruction:**
> You are a developer who has only these two documents and the prototype link, and who cannot ask the designer. List every question you would have to ask before you can start: what is unclear, what is missing (states, error cases, content, limits, data), what two lines contradict each other, and what you would have to guess. Mark each as "blocks the build" or "can start without it". Do not answer the questions and do not rewrite the documents. Return only the list.

**Failure sign:** Fewer than five questions on a real pack (the AI skimmed); questions that the documents already answer.

## Step 7: Answer and agree · Gate D

**Who:** YOU
**Input:** `## Developer's questions (AI)`
**Output:** `## Answers` and `## Agreement` in `work/handoff.md`

Answer each question in the pack itself, or move it to the open questions with who answers and by when. Then go through the pack with a real developer and the product owner, and record who agreed, when and what they changed. Ask the AI to rebuild the report, read the warnings, and, if you send it out, make the bundle (`../toolkit/skills/build-report/SKILL.md`). Record how the AI-assisted workflow performed in counts, not impressions (time per step, errors caught at the gates, redos) in `work/measurement-plan.md`.

**Gate D:** Do the questions that block the build have an answer? Has a real developer read the pack? Is the agreement status one of agreed, pending or not available, with a name and a date?
**Failure sign:** The pack sent by message with no walk-through; "agreed" with no name.

---

## The limit to state plainly

A handoff pack describes the design as the prototype shows it. Whatever the prototype does not show, the pack cannot promise. Expect questions during the build and keep the open questions list alive; it is the cheapest place to catch a misunderstanding.
