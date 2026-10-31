---
name: ideation
description: Explore and compare solution directions for a chosen opportunity. Use when you have a chosen opportunity.
---

# Workflow: Ideation

Explore several really different solution directions for the opportunity you chose, compare them on written criteria, and record why you picked one and parked the others. The AI widens the field and argues against your favourite; you choose.

*Status: draft. Try it on a real project and adjust it to how you work before you rely on it.*

| | |
|---|---|
| Working file | `work/options.md` (copy it from `../toolkit/skills/ideation/templates/options.md` if it is not there yet). Each step fills one section |
| Sources | `work/problem-brief.md` (the chosen problem and opportunities), `insights/opportunities/`, `insights/hypotheses/`, `standards/principle-checks.md`, `context/` |
| Original data | `work/sources/_raw-private/` (the AI does not read it) |
| Final output | `work/options.md`, and the files `insights/decisions/D*.md` (state `proposed` until you accept them) |
| Related | `../toolkit/skills/ideation/templates/prioritization.md` if you also need to rank opportunities; `../toolkit/skills/framing/SKILL.md` is the step before this one |
| Examples | `../toolkit/skills/ideation/examples/`: the Travel Buddy sample, to see the shape. Do not copy its content |

Ideas are cheap and the AI produces them fast, so the risk is not too few ideas: it is **settling on the first one**, or on ten variations of the same idea. This card forces you to write first, widen second, and argue against your own favourite.

## Sections of the working file

| Section | Filled in step | By |
|---|---|---|
| `## Problem and criteria` | 1 | YOU |
| `## Your ideas` | 2 | YOU, before you see anything from the AI |
| `## Directions (AI draft)` | 3 | AI. **Do not edit** |
| `## Directions` | 4 | YOU: three or more really different directions |
| `## Comparison (AI draft)` | 5 | AI. **Do not edit** |
| `## Recommendation` and `## Parked directions` | 6 | YOU |
| `## Challenge (AI)` | 7 | AI. **Do not edit** |

Two rules: the AI returns only its own section, and the AI draft is always kept apart from the version you chose.

## If a gate is not met

| Gate | After step | If the answer is no |
|---|---|---|
| A: really different directions? | 4 | Go back to step 3 and ask for directions that differ in approach, not in detail |
| B: a choice you can defend? | 6 | Go back to step 5 with the criterion you were missing |
| C: still the right choice after the challenge? | 7 | Switch direction, or add the test that would settle it (a hypothesis) |

---

## Step 1: Frame the problem and the criteria

**Who:** YOU
**Input:** `work/problem-brief.md`, `insights/opportunities/`, `standards/principle-checks.md`
**Output:** `## Problem and criteria`

Pick **one** opportunity (O#) and restate it as a How-might-we question that contains no solution. Write 3 to 5 criteria to compare on. Criteria come from the outcome and metric, the principles (P#) and the real constraints (time, team, technology, data), not from taste. Give each a one-sentence meaning.

**Check:** Could someone who has not seen the brief tell what is being solved and how you will judge the options?
**Failure sign:** A How-might-we that already says "an app that..."; criteria like "looks good".

## Step 2: Write your own ideas first

**Who:** YOU
**Input:** `## Problem and criteria`
**Output:** `## Your ideas`

Set a timer for 10 minutes and write or sketch at least six ideas (Crazy 8s works). No filtering, no judging. Do this **before** you ask the AI for anything: once you have read the AI's list, your own ideas bend towards it.

**Failure sign:** Fewer than five ideas; the section is empty because "the AI will do it".

## Step 3: Widen the field

**Who:** AI
**Input:** `## Problem and criteria` and `## Your ideas` (only these)
**Output:** `## Directions (AI draft)`

**Instruction:**
> Use only the problem, the criteria and my ideas below. Propose eight solution directions that are different from each other in approach (for example: change the flow, automate a step, remove a step, move the task to another moment, change who does it, use content or education instead of a feature). At least four must differ from all of my ideas. For each: one sentence for the idea, the user need it serves (an O code from my list), its biggest assumption, and one way it could hurt the user. Do not rank or recommend. Do not invent evidence, numbers or user behaviour. Say what you are unsure about. Return only a table.

**Failure sign:** Eight versions of the same screen; no assumption column; a direction with no O code.

## Step 4: Choose directions · Gate A

**Who:** YOU
**Input:** `## Your ideas`, `## Directions (AI draft)`
**Output:** `## Directions`

Merge your ideas and the AI's. Group the ones that are really the same idea. Pick **three or more** directions to compare: at least one of them should be one you do not like. For each, write the idea in one sentence, the opportunity it serves, its biggest assumption and its main risk.

**Gate A:** Do the directions differ in approach (not only in detail)? Does each one serve a named opportunity? Is there an option you added only to make the favourite look good?
**Failure sign:** Three directions that are one idea at three sizes; a straw man.

## Step 5: Compare

**Who:** AI
**Input:** `## Problem and criteria`, `## Directions`, `standards/principle-checks.md`
**Output:** `## Comparison (AI draft)`

**Instruction:**
> Compare my directions against my criteria. Return a table with one column per direction and one row per criterion, each cell "good", "fair" or "weak" with a short reason. Do not add the cells up into one score. Then, for each direction, name the principles it pulls against and why. Mark every cell where your judgement rests on something not in the documents I gave you as "assumed". Finally list the cheapest test that would settle the biggest uncertainty for each direction. Do not choose a winner.

**Failure sign:** A total score; reasons that could fit any product; no "assumed" labels.

## Step 6: Decide · Gate B

**Who:** YOU
**Input:** `## Comparison (AI draft)`, `## Directions`
**Output:** `## Recommendation`, `## Parked directions`, and the decision files

Check at least three cells of the comparison against what you know. Change the ratings you disagree with. Write the direction you recommend and **why**, plus what must be true for it to work (these become hypotheses, `new-item.py H`). For each parked direction write why and when you would look again. Record the choice as a decision with `new-item.py D --title "..." --reason "..." --state proposed`. Marking it `accepted` is your call with the people who own it.

**Gate B:** Can you defend the choice to someone who preferred another direction? Is every parked direction written down with a reason?
**Failure sign:** The AI's cells copied without reading; no parked list; a decision created already `accepted`.

## Step 7: Challenge your choice · Gate C

**Who:** AI
**Input:** `## Problem and criteria`, `## Directions`, `## Recommendation`, `## Parked directions`
**Output:** `## Challenge (AI)`

**Instruction:**
> Argue for the strongest parked direction as if you were its owner: why it might be better than my recommendation. Then list the three most likely reasons my recommended direction fails with real users, which user group it would serve worst, and which principle it is most likely to break. For each point, say what I should check and how. Do not rewrite my recommendation. Return only this section.

**Gate C:** Write a response under each point: change the choice, add a hypothesis to test, or say why you keep it. Is the choice still standing, with its riskiest assumption turned into a test?
**Failure sign:** Every point answered "ok"; the riskiest assumption has no test.

---

## The limit to state plainly

Comparing directions on paper shows which is more *plausible*, not which is *better*. Only users trying something can tell you that. Treat the recommendation as the first thing to test.
