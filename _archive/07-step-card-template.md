# Step Card Template (Level 3, for every activity)

**Created:** 2026-10-05 · Use with `06-activity-flow-standard.md`. One card per step in an activity flow. A finished example: `examples/competitor-analysis/step-cards.md`.
Use generic labels ("AI chat tool", "AI coding tool") per CLAUDE.md.

## How to start a new activity
1. Choose the archetype in `06` (Investigate or Generate) and write the step list (8 or fewer).
2. Draw the Level 2 flow in the standard style (copy the competitor-analysis SVG as a base).
3. Define the working file's sections: one per step that produces content.
4. Write one card per step using the format below.
5. Build the report template (HTML) for the final deliverable.
6. Run it once on a real case, time each step, and fill in "To test".

## Page header for each activity's card file
- Activity name, archetype, and the decision it supports
- Working file layout (folder tree and the section-by-step table)
- **If a gate fails** table (gate · after step · go back to)
- Cards
- Limits to say out loud
- To test before teaching

## Card format
```
## Step N — [Name] (YOU | AI) · [Gate X, if any]
**Goal:** one sentence: what must be true after this step.
**Give the AI / Do:** which sections or files go in (AI steps) or what you do (YOU steps).
**Instruction essentials:** (AI steps only) a quoted instruction built from the checklist in 06 §5.
**Gate X questions:** (gate steps only) 2–3 yes/no questions.
**Check:** what to look at before moving on.
**Failure sign:** what a bad result looks like.
**Output:** the section or file this step writes.
```

## Quality checklist for a finished card file
- [ ] No two AI steps in a row; every AI step followed by a human review
- [ ] Every input is named (a section or a file); nothing comes from the AI's memory
- [ ] Every AI instruction includes: scope, use only provided material, evidence pointer, "unknown" allowed, return only its section
- [ ] AI draft and verified version are separate sections (where a verify step exists)
- [ ] One challenge step before the decision
- [ ] 3 gates or fewer, each with a go-back rule
- [ ] Last step answers the step 1 decision
- [ ] The last gate includes an alignment question (outcome, opportunity, hypothesis, principles)
- [ ] "Limits to say out loud" is written
- [ ] Failure sign written for every step
- [ ] Tested on one real case; times and error rate recorded

## Report template (the shareable output)
Start from `assets/templates/competitor-analysis-template.html` and keep its skeleton: decision banner → our answer → what was compared/explored and why → main evidence table → beliefs or hypotheses tested → insights (each with a counter-argument and evidence link) → what this cannot tell us → appendix of sources and method. Rename sections to fit the activity.
