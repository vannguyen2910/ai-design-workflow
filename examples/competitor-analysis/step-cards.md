# Step Cards — Competitor Analysis

**Created:** 2026-10-05 · **Revised 2026-10-05:** single working file; 8 steps (was 7); gate-fail rules; belief check; decision answered at the end.
**Worked example of the standard** in `../../02-method.md` Part 1, using the card format in `../../02-method.md` Part 2. Pattern: A Investigate. Diagram: `../../assets/diagrams/competitor-analysis-activity-flow.svg`. Report page: the hub's Evidence page, `../../assets/templates/hub/evidence.html`.
**Status: draft, untested.** The AI instructions are my design, built from the research principles, and have not been run in a class. Test on one real case before teaching. Uses generic labels ("AI chat tool") per CLAUDE.md.

## The working file (one file, one folder)
```
competitor-analysis-[product]/
├── competitor-analysis.md      ← the one working file; each step fills one section
├── sources/                    ← raw evidence: screenshots, saved pages, review exports
└── analysis.html               ← this activity's page in the Experience Hub, built by you from the template (also exported to PDF)
```
Sections inside `competitor-analysis.md`, in order:

| Section | Filled in step | By |
|---|---|---|
| `## Scope` (decision, criteria, beliefs) | 1 | You |
| `## Competitors` | 2 and 3 | Step 2: AI suggestions go in, labelled. Step 3: you turn them into your final list with reasons |
| `## Evidence (AI draft)` | 5 | AI. **Never edit.** |
| `## Evidence (verified)` | 6 | You: a copy of the draft you correct |
| `## Patterns` | 7 | AI: patterns, belief check, counter-case |
| `## Insights + open questions` (incl. the decision) | 8 | You |

Step 4 (collect sources) fills the `sources/` folder, not a section.

**Two rules that keep one file safe:**
1. **The AI returns only its own section.** Say so in the instruction, then you paste it in. This stops the AI from silently rewriting your earlier sections.
2. **Keep the AI draft and the verified table as two sections.** The difference shows what you corrected and gives you your error rate.

**Trade-offs of one file (⚠️ my read, untested):** it grows long, so give the AI only the sections each step needs (stated on each card); use your cloud drive's version history as the safety net.
**Why markdown inside, HTML out:** plain text is what the AI reads and writes reliably. Students build the finished page as one HTML page of the hub, from `assets/templates/hub/evidence.html` (and export a PDF if needed).

## If a gate fails
| Gate | After step | Supports stage check | If the answer is no |
|---|---|---|---|
| A: right competitors? | 3 | (local to this activity) | Go back to step 2 and revise the list |
| B: traceable? | 6 | 1b, 1c | Rerun step 5 with a tighter instruction (many errors), then spot-check again |
| C: evidence, not AI opinion? | 8 | 1b, and 2a if the insight supports an opportunity | Go back to step 7 and redo the comparison |

Stage checks are listed in `../../02-method.md` Part 3, §2.

---

## Step 1 — Frame the question (YOU)
**Goal:** Know what decision this analysis serves, so the AI doesn't produce a generic market overview, and write down what you already think so you can test it.
**Do:** Fill the `## Scope` section:
- **Decision it informs** (e.g. "Should we add a self-serve onboarding flow?")
- Our users and their main job
- **Criteria that matter** (max 6). *You* set these; the AI may only add ones you missed.
- Market and time box
- **What you already believe** (3–5 statements, so step 7 can test them)

**Check:** Could a stranger tell what a good answer looks like?
**Failure sign:** Criteria like "features" and "UI" with no link to the decision; no beliefs written.
**Output:** `## Scope` section

## Step 2 — Suggest (AI)
**Goal:** Widen the list beyond the obvious three.
**Give the AI:** the `## Scope` section only.
**Instruction essentials:**
> Using only the scope below, suggest competitors in three groups: direct, indirect, and substitutes (including "do nothing" and manual workarounds). For each, say in one line why it competes for our users' job. Say how confident you are and what you are unsure about. Do not invent products; if you are not sure a product exists, say so. Then suggest only criteria that are **missing** from my list, and say why each matters to the decision. Do not replace my criteria.

**Check:** Anything that sounds plausible but you can't find online? Mark it for removal.
**Failure sign:** Only famous brands; invented-sounding names; your criteria quietly replaced; confident tone with no uncertainty.
**Output:** AI suggestions pasted under `## Competitors`, labelled "AI suggestions"

## Step 3 — Review the list (YOU) · Gate A
**Goal:** Decide the real competitor set before spending time on evidence.
**Do:** Edit the suggestions into your final list under `## Competitors`, with a reason for each inclusion and exclusion. Add anyone missing. Ask someone in sales, support or the customer team.
**Gate A questions:**
- Are these real alternatives for **our** users, not just famous names?
- Who is missing?
- Why were others cut?

**Failure sign:** Everything on the AI's list survived.
**Output:** final `## Competitors` section

## Step 4 — Collect sources (YOU)
**Goal:** Gather the raw evidence for the competitors you kept, and only those.
**Do:** Save into `sources/`: pricing pages, feature pages, onboarding screens, app store reviews, help-centre pages. Use a clear file name per source (e.g. `competitor-a-pricing-2026-10.png`) and note the date.
**AI role (optional):** it may suggest *where to look* (which pages, which review sites). **You open and save every source yourself.** Never let the AI supply facts from memory.
**Failure sign:** Sources saved for competitors you cut; no dates; links instead of saved copies (pages change).
**Output:** files in `sources/`

## Step 5 — Extract (AI)
**Goal:** Turn your sources into a structured table without invention.
**Give the AI:** the `## Scope` and `## Competitors` sections, and the files in `sources/` (one competitor at a time).
**Instruction essentials:**
> Fill the table using only the sources provided. For every cell, include the source file name and the exact phrase or screen that supports it. If the sources do not say, write "unknown", never guess or use background knowledge. Mark anything that is an inference as "inferred". Return only the markdown table, nothing else, so I can paste it as its own section.

**Table columns (starter):** Competitor · Criterion · Finding · Source file · Quote or screen reference · Status (stated / inferred / unknown)
**Failure sign:** No "unknown" cells at all; sources cited that are not in the folder.
**Output:** `## Evidence (AI draft)` section (do not edit)

## Step 6 — Spot-check (YOU) · Gate B
**Goal:** Confirm the table is true to the sources.
**Do:** Copy the draft table into `## Evidence (verified)`. Check **every cell on your top 2–3 criteria**, plus a random sample (about 20%) of the rest, plus every "inferred" row and anything surprising. Open the source and compare. Fix errors. Note your error rate at the top of the section.
**Gate B questions:**
- Does every cell trace to a source you can open?
- Did "unknown" stay unknown?
- Is the error rate acceptable? If many cells are wrong, go back (see "If a gate fails").

**Failure sign:** You only checked easy cells; error rate not recorded.
**Output:** `## Evidence (verified)` section

## Step 7 — Compare + challenge (AI)
**Goal:** Find patterns, test your beliefs, then stress-test the conclusions.
**Give the AI:** the `## Scope` section (including your beliefs) and `## Evidence (verified)` only. **Not** the AI draft.
**Instruction essentials:**
> From the verified table, list patterns, gaps and differences that matter for the decision in the scope. Cite the rows that support each. Then go through my stated beliefs one by one and say whether the evidence supports, contradicts or does not address each. Then, for each pattern, write the strongest argument that it is wrong or misleading, and say what evidence would change your mind. Do not recommend actions yet. Note anything this table cannot tell us. Return only this section.

**Check:** Does each pattern cite rows? Is the counter-case a real argument, not a token sentence? Did any belief get contradicted (that is the valuable part)?
**Failure sign:** Generic findings ("competitors focus on simplicity"); counter-case that agrees with the finding; beliefs all "supported".
**Output:** `## Patterns` section

## Step 8 — Interpret + decide (YOU) · Gate C
**Goal:** Turn findings into judgments, and **answer the decision from step 1**.
**Do:** Weigh each pattern against our users and the UX principles from the Foundation. A pattern seen in many competitors is not automatically important. In `## Insights + open questions`:
- 3–5 insights, each with evidence links
- **The answer to the step 1 decision**, in one sentence ("We should / should not X, because Y"), or "not enough evidence yet" with what is missing
- Open questions that need real users

Then **build `analysis.html` yourself** from the provided template: comparison, insights with evidence links, the decision, open questions, sources appendix. Export a PDF if needed.
**Gate C questions:**
- Does each insight tie to our problem and principles?
- Is it evidence, or AI opinion you have not checked?
- Could you defend it by opening the source?

**Failure sign:** Insights copied from `## Patterns` unchanged; no decision stated; no open questions listed.
**Output:** `## Insights + open questions` section and `analysis.html` (+ PDF) → feeds **Define** as evidence for the problem brief.

---

## Limits to say out loud
Competitor analysis shows **what rivals do**, not **why users choose them** or whether it works. Treat findings as hypotheses for Discover interviews, not conclusions.

## To test before teaching
1. Run the full flow on one real case; time each step. Step 4 (collecting sources) will probably be the longest.
2. Measure the step-6 error rate (count wrong cells in the AI draft vs your verified table); if above ~10–15%, tighten the step-5 instruction. *(The threshold is my guess.)*
3. Check the whole flow works for a non-technical designer using only an AI chat tool (pasting text and attaching files).
4. Check the hub's Evidence page (`assets/templates/hub/evidence.html`) works when filled by an AI coding tool from the `.md` file.
5. Check whether the belief check in step 7 actually surfaces contradicted beliefs, or whether the AI just agrees.
