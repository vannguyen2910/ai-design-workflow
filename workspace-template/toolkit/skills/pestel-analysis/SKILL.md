---
name: pestel-analysis
description: Describe the outside context of a product (political, economic, social, technological, environmental, legal) with every factor tied to a source. Use when a decision depends on the market, region or regulation around the product.
---

# Workflow: PESTEL analysis

Describe the outside context that affects one decision, with every factor tied to a saved source. The AI drafts the factors from your sources, you check each one. PESTEL does not say what users need.

*Status: draft. Try it on a real project and adjust it before you rely on it.*

| | |
|---|---|
| Working file | `work/pestel-analysis.md` (copy `../toolkit/skills/pestel-analysis/templates/pestel-analysis.md` into `work/`) |
| Sources | `context/product-and-users.md`, and the articles or reports you saved in `work/sources/anonymised/` |
| Original data | `work/sources/_raw-private/` (the AI does not read it) |
| Final output | `work/pestel-analysis.md`, status `verified` |

## Step 1: Scope

**Who:** YOU · **Output:** `## Scope`

Write the product or market, the region, the time frame, and the decision this analysis serves.

**Check:** Can you name the decision? **Failure sign:** "Understand the market" with no decision.

## Step 2: Draft the factors

**Who:** AI · **Input:** `## Scope` and the saved sources · **Output:** `## Factors (AI draft)`

> Use only the scope and the saved sources. Keep only the PESTEL groups that affect the decision in Scope. For each factor write one specific row: the group, the factor, its effect on the product, a level (high, medium or low) and the source file. Write `assumed` in the Source column for anything the sources do not say. Do not invent figures or laws. Return only this section.

**Failure sign:** A row with no source and no `assumed`; a generic factor that fits any product.

## Step 3: Check the factors

**Who:** YOU · **Output:** `## Factors` (your checked version)

Open the source of each row and check it says what the row says. Cut factors that do not touch the decision. Set the level yourself.

**Check:** Does every row have a source or `assumed`?

## Step 4: Draft the implications

**Who:** AI · **Input:** the checked `## Factors` · **Output:** `## Opportunities and threats (AI draft)`, `## Implications (AI draft)`

> From the checked factors only, list which open an opportunity and which are a threat, high-level factors only. Then write three to five implications for the decision in Scope. Each implication points back to a row of the Factors table. Return only these two sections.

**Failure sign:** An implication that points to no row.

## Step 5: Finish

**Who:** YOU · **Output:** the two sections checked, `## What this cannot tell us`

Edit the draft until you would defend it. Write what this analysis does not tell you. Set `status` to `verified`.
