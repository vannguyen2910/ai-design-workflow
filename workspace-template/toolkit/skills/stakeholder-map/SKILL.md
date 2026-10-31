---
name: stakeholder-map
description: Map who decides, who is affected and what they need, with decision rights and an engagement plan. Use at the start of a project or when a decision keeps stalling.
---

# Workflow: Stakeholder map

Map the people who decide or are affected by one project or decision. The AI drafts from what you know, you correct it, and **decision rights come only from you**. Write roles, needs and worries. No personal notes or comments about character.

*Status: draft. Try it on a real project and adjust it before you rely on it.*

| | |
|---|---|
| Working file | `work/stakeholder-map.md` (copy `../toolkit/skills/stakeholder-map/templates/stakeholder-map.md` into `work/`) |
| Sources | The list you write in step 1, and anonymised meeting notes in `work/sources/anonymised/` (use role labels, not names) |
| Original data | `work/sources/_raw-private/` (the AI does not read it) |
| Final output | `work/stakeholder-map.md`, status `verified` |

## Step 1: Scope and list

**Who:** YOU · **Output:** `## Scope`, and a list of stakeholders by role

Write the project or decision and why the map is needed now. List who you know by role (for example "head of product", "support lead").

**Check:** Is each stakeholder a role, with no name and no comment on character?

## Step 2: Draft the table

**Who:** AI · **Input:** `## Scope`, your list and the notes · **Output:** `## Stakeholders (AI draft)`

> Use only the scope, my list and the notes. For each stakeholder fill one row: role, influence (high or low), interest (high or low), what they need, what they worry about, spoken to (yes or no, from the notes only). Write `assumed` where you infer a value and `unknown` where nothing says. Do not add stakeholders I did not list. Return only this section.

**Failure sign:** A need or worry with no source and no `assumed`; a stakeholder you never listed.

## Step 3: Check, place, and decide rights

**Who:** YOU · **Output:** `## Stakeholders`, `## Influence and interest`, `## Decision rights`

Correct influence and interest from what you know. Place each stakeholder in the grid. Fill in `## Decision rights` yourself: who decides, is consulted, is informed, can block. The AI does not write this section.

**Check:** For each important decision, is there exactly one who decides?

## Step 4: Draft conflicts and the plan

**Who:** AI · **Input:** the checked sections · **Output:** `## Conflicts and risks (AI draft)`, `## Engagement plan (AI draft)`

> From the checked table and decision rights only, list where stakeholders want different things and the risk if it is not resolved early. Then write one engagement row per stakeholder you should work with: what we need from them, how we work with them, how often, who is responsible (write `unknown` if not given). Each conflict names the rows it comes from. Return only these two sections.

## Step 5: Finish

**Who:** YOU · **Output:** the two sections checked, `## What this cannot tell us`

Edit until it is true to what you know. Write who you have not met and what is second-hand. Set `status` to `verified`.
