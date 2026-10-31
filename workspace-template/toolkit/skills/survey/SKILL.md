---
name: survey
description: Turn an anonymised survey export into results with the number of answers beside every figure, then write the limits. Use when you have survey responses to summarise.
---

# Workflow: Survey results

Summarise a survey so every figure has its `n` and the limits are written down. The AI counts from the anonymised export, you recompute some of it yourself.

*Status: draft. Try it on a real project and adjust it before you rely on it.*

| | |
|---|---|
| Working file | `work/survey-results.md` (copy `../toolkit/skills/survey/templates/survey-results.md` into `work/`) |
| Sources | The anonymised export (a CSV or table) and the question list in `work/sources/anonymised/` |
| Original data | `work/sources/_raw-private/` (raw export with names or emails: the AI does not read it) |
| Examples | `../toolkit/skills/survey/examples/`: the Travel Buddy sample, to see the shape. Do not copy its content |
| Final output | `work/survey-results.md`, status `verified` |

## Step 1: Method and sample

**Who:** YOU · **Output:** `## Method and sample`

Write the tool, the dates, how many responses are valid (and how many were dropped, and why), and how people were recruited. Say how the sample is skewed.

**Check:** Can someone tell who answered and who did not? **Failure sign:** A total with no count of dropped responses.

## Step 2: Count the results

**Who:** AI · **Input:** the anonymised export and the question list · **Output:** `## Key results (AI draft)`

> Use only the export and the question list. For each question give the result and `n`, the number who answered that question (not the total). Show the counts, and give a percentage only next to its `n`. Group free-text answers into themes with a short example each. Write `unknown` where a question has no answers. Return only this section.

**Failure sign:** A percentage with no `n`; counts that do not add up to the rows.

## Step 3: Check the numbers

**Who:** YOU · **Output:** `## Key results` (your checked version)

Recompute three results from the export yourself (a filter or a pivot table is enough) and compare them with the draft. If one is wrong, check them all.

**Check:** Do the counts match the export?

## Step 4: Surprises and limits

**Who:** AI, then YOU · **Output:** `## What surprised us`, `## Limits`

> From the checked results only, write what is surprising, each point naming the row it comes from. Then write the limits: the sample size, the skew, and what a multiple-choice question may under-report. Return only these two sections.

Edit the draft, then write what these results cannot support. Set `status` to `verified`.
