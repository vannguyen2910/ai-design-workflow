# Traceability and Alignment: How to Cross-Check a Solution Against What We Defined

**Created:** 2026-10-05 · **Status:** my synthesis of established ideas (opportunity solution tree, hypothesis statements, heuristic evaluation with your own principles). The activity flow at the end is a proposal, not yet drawn or tested.

## The problem
AI makes it easy to produce plausible screens, including features nobody asked for. Winnie's rule: every solution must pass the UX principles and artifacts defined earlier. That needs a way to **check**, not just a promise.

## Short answer: yes, add three prerequisite artifacts, then run an alignment check
The solution can only be cross-checked against things that exist in writing. The Define output is the **shared problem brief**: co-defined with product and business, it becomes the requirement. It contains:

| Prerequisite | What it is | Where it comes from |
|---|---|---|
| **Outcome** | The result the work is meant to move, with a metric or an assumed metric | Agreed with the PO and business when co-defining the requirement, or a stated assumption (see `08-measuring-design-success.md`) |
| **Opportunities** | Evidence-backed user needs or pain points worth solving, ranked. Problems, not features | The evidence pack from Discover (e.g. competitor analysis, interviews) |
| **Hypotheses** | A testable bet: "We believe [design decision] for [users] will [change], and we will know because [metric / test result]" | You, after Define, one per major design decision |
| **Principles** | The checks the solution must pass. **Baseline: Nielsen's 10 usability heuristics.** Where the organisation has its own UX, business or service principles, add them as a second layer | Foundation lesson (baseline), the organisation (extra layer, if it exists) |

This is the structure of Teresa Torres' **opportunity solution tree**: desired outcome → opportunities → solutions → assumption tests, which makes every solution traceable to a need and a measurable outcome ([Product Talk](https://www.producttalk.org/glossary-discovery-opportunity-solution-tree/)). Using it keeps the series tool-agnostic and keeps AI-generated extras visible.

## The golden thread
```
Outcome → Opportunity → Hypothesis → Design decision → Principle(s) → Test / Metric
```
Every design decision in the prototype must have a line back to an opportunity and forward to a test. A decision with no line back is an **orphan**.

## The alignment check (the cross-check itself)
A matrix in the working file, one row per design decision (a screen, a flow, a component choice):

| Design decision | Opportunity it serves | Hypothesis | Principle(s) it follows | Principle(s) it strains | Test or metric |
|---|---|---|---|---|---|

Four checks, which map to "found a problem" signals:
1. **Orphan decisions:** a decision with no opportunity → remove it, or justify it in writing. (This catches AI-added extras.)
2. **Uncovered opportunities:** a high-ranked opportunity with no decision → a gap.
3. **Principle strain:** the decision conflicts with a principle → fix it, or record a deliberate trade-off with the reason.
4. **Untested hypotheses:** a hypothesis with no usability task or metric → add one before testing.

Principle checking is **heuristic evaluation**, where a product is reviewed against a checklist of principles to give an objective picture of quality and an action list ([uxdesign.cc — measuring design quality with heuristics](https://uxdesign.cc/measuring-design-quality-with-heuristics-44857efa514), [LUMA — heuristic review](https://www.luma-institute.com/heuristic-review/)). The checklist is the **baseline heuristics plus any organisation principles**. Each principle is turned into yes/no questions for the product at hand (the AI may draft these; you approve them), with the reason and anti-patterns (practice from design-principle guidance; secondary source). Large companies often have their own UX, business and service principles for their products; students in those companies use them as the first layer and Nielsen's 10 as the fallback.

## Where AI helps, and where it can't
| AI can | You must |
|---|---|
| Draft the matrix by mapping each decision to an opportunity, hypothesis and principle **with a pointer** | Verify every mapping against the brief; "none" must stay "none" |
| Audit the prototype against each principle and **argue where it violates**, not agree | Decide whether a violation is a defect or a deliberate trade-off |
| List orphans and uncovered opportunities | Decide which to cut or add |
| Write the usability tasks for each hypothesis | Run them with real users |

Same rules as the standard (`06-activity-flow-standard.md`): AI uses only the provided brief and principles, may answer "none", and returns only its own section.

## Hypothesis granularity: no standard, so use a rule of thumb
There is no standard unit. Pick by the solution:
- **One opportunity, one solution** → one hypothesis.
- **One solution serving several opportunities** → one hypothesis per opportunity, if you would test or measure them differently; otherwise one hypothesis listing the opportunities.
- **Several small decisions for one opportunity** → one hypothesis for the group, with each decision still listed as a row in the matrix.
The matrix keeps **one row per design decision**; the hypothesis column can repeat or point to a shared hypothesis. Split a hypothesis whenever you would run a different test or read a different metric. *(My rule of thumb, not an industry standard.)*

## Where it lives: inside the critique loop
**Decided:** the alignment check is **not its own lesson**. It is part of the critique loop lesson (Prototype II), and a light version runs at the last gate of **every** activity (standard rule 12 in `06-activity-flow-standard.md`). The full version below is what the critique loop lesson teaches.

## Proposed activity flow: "Alignment check" (Archetype A, adapted; Develop to Deliver)
1. **YOU** list the design decisions in the prototype and confirm the brief (outcome, opportunities, hypotheses, principles)
2. **AI** map each decision to opportunity, hypothesis and principles, with a pointer; "none" allowed → `## Alignment (AI draft)`
3. **YOU** verify the mapping against the brief → `## Alignment (verified)` — **Gate: traceable? any orphan or gap?**
4. **AI** audit each decision against each principle and argue where it fails → `## Principle audit`
5. **YOU** decide per finding: fix, accept as a trade-off (with reason), or cut → `## Decisions` — **Gate: could you defend each decision by the brief?**
6. **AI** write a usability task for each hypothesis that lacks one → `## Test plan (draft)`
7. **YOU** edit the test plan so it measures the metrics chosen in `08` (task success, time, errors, SUS) — **Gate: measurable before launch?**
Go-back rules: gate 1 fails → step 2; gate 2 fails → step 4; gate 3 fails → step 6.
*(Not yet drawn; 7 steps, 3 gates, within the standard.)*

## How this connects to the other files
- Stage map: the Define output grows from "problem brief" to "problem brief with outcome, opportunities, hypotheses, principles" (diagram needs a small update if you agree).
- Gate by stage (`02-stage-methods-and-delegation.md`): this activity is the concrete form of the Prototype gate "principles + design system + accessibility".
- Measurement (`08-measuring-design-success.md`): the Test column feeds the usability plan and metrics.

## Decided (2026-10-05)
| Question | Answer |
|---|---|
| What are the principles? | Nielsen's 10 heuristics as the baseline; the organisation's own UX, business and service principles as an extra layer where they exist |
| Hypothesis granularity | No standard; depends on the solution (rule of thumb above) |
| Own lesson or part of another? | Part of the critique loop; a light check at every activity's last gate |
| Stage map | Define output updated to show outcome, opportunities, hypotheses and principles (done) |

## Still open
1. ~~Is Nielsen's 10 enough when a company has no written principles?~~ **Yes, enough** (decided 2026-10-05).
2. How should students handle conflicts between the organisation's principles and Nielsen's (for example a brand principle that breaks a heuristic)? Suggest: record it as a deliberate trade-off with the reason.
