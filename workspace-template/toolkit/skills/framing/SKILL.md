---
name: framing
description: Choose the problem, the opportunities and the hypotheses from checked evidence. Use when the evidence is checked and you need to frame the problem.
---

# Workflow: Framing the problem

Turn what you learned in Discover into a problem worth solving: a few opportunities written as user needs, a problem statement, and a one-page problem brief that you can sign off with product and business. The AI proposes and challenges; you choose.

*Status: draft. Try it on a real project and adjust it to how you work before you rely on it.*

| | |
|---|---|
| Working file | `work/problem-brief.md` (the Define page in Stages is built from this file). Each step fills one section |
| Sources | The checked evidence from Discover: `work/user-voice-synthesis.md` (verified sections), checked interview summaries from `../toolkit/skills/interview/SKILL.md`, and the `insights/` items that already exist |
| Original data | `work/sources/_raw-private/` (the AI does not read it) |
| Final output | `work/problem-brief.md`, plus the files `insights/opportunities/O*.md`, `insights/hypotheses/H*.md` and `insights/metrics/M*.md` |
| Related | `../toolkit/skills/framing/templates/problem-brief.md` and `opportunity-solution-tree.md` (document shapes), `../toolkit/tools/new-item.py` (creates the items), `standards/principle-checks.md` |
| Examples | `../toolkit/skills/framing/examples/`: the Travel Buddy sample, to see the shape. Do not copy its content |

Use only evidence you have **already checked**. If the AI frames a problem from an unchecked draft, the whole brief stands on sand.

## Sections of the working file

| Section | Filled in step | By |
|---|---|---|
| `## Outcome and success metrics` | 1 | YOU |
| `## Problem statements (AI draft)` | 2 | AI. **Do not edit** |
| `## Problem statements (verified)` | 3 | YOU: your corrected copy, with the chosen statement marked |
| `## Opportunities (ranked)` | 4 | AI proposes in chat, YOU decide, then the items are created |
| `## Hypotheses` | 5 | AI proposes in chat, YOU decide, then the items are created |
| `## Challenge (AI)` | 6 | AI. **Do not edit** |
| `## Agreement` | 7 | YOU |

Two rules: the AI returns only its own section, and the AI draft is always kept apart from the checked version. Nothing becomes an item until you approve it.

## If a gate is not met

| Gate | After step | If the answer is no |
|---|---|---|
| A: a problem, not a solution? | 3 | Go back to step 2 and add "Do not describe a solution or a feature" to the instruction |
| B: every need backed by evidence you checked? | 4 | Drop the need, or go back to Discover and collect what is missing |
| C: worth solving, and can it be measured? | 6 | Rework the metric (step 1) or the ranking (step 4) |

---

## Step 1: Fix the outcome

**Who:** YOU
**Input:** `work/scope.md`, `context/product-and-users.md`
**Output:** `## Outcome and success metrics`

Write one outcome the business cares about, within the team's reach, then the signal you would see and the metric that measures it, with today's baseline and a target. Write `assumed` for any number nobody has confirmed. Create each metric as an item with `new-item.py M` (the item file is the single source).

**Check:** Can you measure it? Is the baseline real or marked `assumed`?
**Failure sign:** "Improve the experience"; a target with no baseline and no `assumed` label.

## Step 2: Draft problem statements

**Who:** AI
**Input:** `## Outcome and success metrics`, the verified evidence sections listed under Sources (only those), and the list of existing items in `insights/` (codes and titles)
**Output:** `## Problem statements (AI draft)`

**Instruction:**
> Use only the outcome and the checked evidence below. Write three different problem statements in this form: "[Users] struggle with [what] when [situation], which leads to [consequence]." Each statement must describe a problem, not a solution, a feature or a screen. After each one, list the quote or evidence IDs it rests on, and how many different people or sources those come from. Say which user group or situation the statement does not cover. If the evidence supports fewer than three distinct problems, write fewer and say why. Do not invent evidence, numbers or users. Return only this section.

**Failure sign:** A statement containing "needs a", "should have" or a feature name; no IDs; three statements that are the same problem reworded.

## Step 3: Choose and edit · Gate A

**Who:** YOU
**Input:** `## Problem statements (AI draft)` and the evidence it cites
**Output:** `## Problem statements (verified)`, with the chosen statement marked

For each statement, open two of the cited IDs and check the evidence says what the statement claims. Edit the wording into your own; pick **one** statement to carry forward (you can keep the others as "not now", with the reason). Check the statement does not hide a solution.

**Gate A:** Is it a problem and not a solution? Can you point to the evidence for who, what and when? Is the chosen problem big enough to move the outcome from step 1?
**Failure sign:** The AI's wording kept unchanged; no evidence opened; the statement already implies a feature.

## Step 4: Propose opportunities · Gate B

**Who:** AI proposes, then YOU decide
**Input:** `## Problem statements (verified)` (the chosen one), the verified evidence, the existing opportunities in `insights/opportunities/`
**Output:** A proposal table in the chat. **No file is created yet.** After you approve, the items are created with `new-item.py O` and listed in `## Opportunities (ranked)`

**Instruction:**
> Break the chosen problem into 3 to 5 opportunities, each written as "[user] needs [outcome] because [insight]", a user need and not a feature. For each: the evidence IDs behind it, how many people or sources, and one How-might-we question that does not contain a solution. Say whether it is new or already exists in the list (give its code). Do not rank and do not set impact or confidence: leave them empty for me. Say what evidence is missing for each.

**Your decision:** keep, edit or cut each row. Then set the **impact**, **confidence** and the reason for the rank yourself, weighing severity, context and breadth, not only how many quotes mention it. Ask the AI to create the approved ones with `new-item.py O --title "..." --evidence-note "I01-02"`.

**Gate B:** Can you defend each opportunity by pointing at the evidence you checked? Does any opportunity secretly describe a solution?
**Failure sign:** Opportunities written as features ("add a filter"); no evidence IDs; the top rank goes to the need with the most quotes automatically.

## Step 5: Propose hypotheses

**Who:** AI proposes, then YOU decide
**Input:** `## Opportunities (ranked)`, `## Outcome and success metrics`
**Output:** A proposal table in the chat. After you approve, the items are created with `new-item.py H` (`--serves O1 --metric M1`) and listed in `## Hypotheses`

**Instruction:**
> For the top two opportunities, propose hypotheses in the form: "We believe that [change] for [users] will [effect], and we will know by [test] and [metric]." Each hypothesis must link to an existing opportunity code and an existing metric code. Give the cheapest way to test it and what result would prove it wrong. Do not propose a solution design. Return a table: hypothesis, serves, metric, how to test, what would disprove it.

**Check:** Can each hypothesis fail? Does it name a metric that exists?
**Failure sign:** A hypothesis that cannot be disproved; an opportunity or metric code that does not exist.

## Step 6: Challenge the framing · Gate C

**Who:** AI
**Input:** The whole of `work/problem-brief.md` as you have filled it so far, and the items it points to
**Output:** `## Challenge (AI)`

**Instruction:**
> Act as a sceptical product lead reading this brief. List: (1) the three strongest reasons this might be the wrong problem to solve; (2) any claim without evidence; (3) any opportunity that sounds like a solution; (4) any metric that cannot be measured with what we have; (5) who is missing from the evidence; (6) what the principle checks in `standards/principle-checks.md` would say about the chosen problem. For each point, say what I should check. Do not rewrite the brief. Return only this section.

**Gate C:** Answer each point in writing under it: fix the brief, or say why you keep it. Is this problem still the one worth solving after the challenge? Is every metric measurable?
**Failure sign:** Every point answered "fine"; the challenge is skipped because the brief "feels right".

## Step 7: Agree

**Who:** YOU
**Input:** The finished `work/problem-brief.md`
**Output:** `## Agreement`, and the status in the Project card

Share the one page with product and business (the report's Problem brief page, or a PDF). Record who agreed, when, and what they said. If you cannot reach them, write `not available` and list the assumptions that need confirming. Then ask the AI to rebuild the report and read you the warnings (`../toolkit/skills/refresh-hub/SKILL.md`).

**Check:** Is the status one of agreed, pending or not available, with names and a date?
**Failure sign:** "Agreed" with no name or date.

---

## The limit to state plainly

A problem brief is a belief about what matters, built from a small amount of evidence. Treat it as the best current hypothesis and revise it when the tests in Develop and Deliver bring new evidence.
