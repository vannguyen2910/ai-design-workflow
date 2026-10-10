# Activity Flow Standard (the method for every design activity)

**Created:** 2026-10-05 · **Status:** draft standard, built from one worked example (competitor analysis) and not yet tested on other activities.
This file is the **standard**. It applies to any design activity (competitor analysis, interview synthesis, ideation, flows, prototyping, usability findings, and so on). Specific activities live in `examples/`, and each one follows this file. Step card format: `07-step-card-template.md`.

## 1. Three levels of detail
| Level | Shows | Format | Used for |
|---|---|---|---|
| 1 Stage map | Stages (Discover, Define, Develop, Deliver), input → output artifact, gate | Double Diamond columns | Series overview slide |
| 2 Activity flow | Steps inside one activity: who does each (you / AI), the file it writes to, the review gates | **Swimlane flowchart** | One slide per activity |
| 3 Step card | Per step: goal, input, AI instruction, checks, failure signs, output | Text card | Lesson handout |

Swimlane is the format because the series' claim is *human review after every AI step*: the alternation between the YOU and AI lanes is the review loop.

## 2. Rules every activity flow follows
1. **Frame first.** Step 1 is always human: the decision this activity informs, the constraints (from the Foundation: principles, design system, context), and what you already believe.
2. **Alternate you and AI.** Every AI step is followed by a human step that reviews it. No two AI steps in a row.
3. **AI works only from what you give it.** Name the inputs (sections of the working file, files in `sources/`). Facts must come from provided sources, never from the AI's memory.
4. **Uncertainty is allowed and visible.** The AI says "unknown" or "inferred" instead of guessing.
5. **Evidence per claim.** Every AI claim carries a pointer to where it came from.
6. **Keep the AI draft.** The AI's output stays untouched as one section; your corrected version is a separate section. The gap is your error rate.
7. **Challenge before deciding.** One AI step argues against the conclusion before you decide.
8. **Maximum three gates.** Each gate is a yes/no question the student can answer, with a **go-back rule** ("if no, return to step N").
9. **End with the decision.** The last step answers the decision from step 1 (or says what evidence is missing).
10. **State the limit.** Every flow ends with "what this cannot tell you" (usually: why users behave this way; that needs real users).
11. **Eight steps or fewer** so the flow fits one slide.
12. **Alignment check at the last gate.** Before the output moves on, check it against the problem brief: does it serve the outcome and an evidenced opportunity, test a hypothesis, and pass the principles (Nielsen's 10 plus any organisation principles)? If not, go back. The full version (matrix, principle audit) is taught in the critique loop lesson; see `09-traceability-and-alignment.md`.

## 3. One working file
Each activity has one folder:
```
[activity]-[subject]/
├── [activity].md       ← the one living file; each step fills one section
├── sources/            ← raw evidence (only if the activity uses sources)
└── [deliverable].html  ← the shareable output, built by the student from a template (+ PDF export)
```
- **One file, sections per step.** One place to read and update.
- **The AI returns only its own section;** the student pastes it in. This prevents silent rewrites of settled work.
- **Give each AI step only the sections it needs.**
- **Markdown inside** (plain text is what AI reads and writes reliably); **HTML outside** for stakeholders.
- Version history in the cloud drive is the safety net. *(⚠️ my recommendation, untested.)*

## 4. Two archetypes (starting skeletons)
Most activities fit one of two spines. Pick one, then adapt.

**A. Investigate** (competitor analysis, desk research, interview synthesis, usability findings analysis)
Frame → Suggest (AI) → Review the list (YOU, gate) → Collect sources (YOU) → Extract (AI) → Verify (YOU, gate) → Compare + challenge (AI) → Interpret + decide (YOU, gate)
Gate type: **evidence and traceability.**

**B. Generate** (ideation, user flows, content, prototype, critique loop) *(⚠️ hypothesis, not yet drawn or tested)*
Frame with constraints (YOU) → Generate at least 3 genuinely different options (AI) → Select against principles (YOU, gate) → Develop the chosen one (AI) → Critique: AI argues back (AI) → Check against principles, design system, accessibility (YOU, gate) → Decide and refine (YOU)
Gate type: **alignment to the brief, principles, design system, accessibility.**

This follows the series decision to use a different gate by stage: evidence early (Discover, Define), principles and system in the middle (Develop), real users and buildability late (Deliver). See `02-stage-methods-and-delegation.md`.

## 5. Standard AI instruction checklist
Every AI step's instruction should contain, in plain words:
- the **scope** (paste the relevant sections, nothing else)
- **use only** the provided material
- an **evidence pointer** for each claim
- permission to say **"unknown"** and to mark **inferences**
- **return only your section**, in a stated format
- for synthesis steps: **no recommendations yet**, and note **what this cannot tell us**
- for challenge steps: **strongest argument that it is wrong**, and **what evidence would change your mind**

## 6. Research basis
- Trace outputs back to raw sources: [Parallel HQ](https://www.parallelhq.com/blog/ai-assisted-ux-research-workflow)
- Synthetic output is agreeable and shallow, so "unknown" and real-user gates: [NN/g via Userbrain](https://userbrain.com/blog/synthetic-users-experiment/), [NN/g — Real Design Scenarios](https://www.nngroup.com/articles/testing-ai-methodology)
- Make the AI argue against you; keep judgment human: [Designer Fund — Linear](https://designerfund.substack.com/p/ai-design-linear)
- Frequency is not importance (so the human weighs): Parallel HQ
- Rules 2, 6, 8 and 11 and the two archetypes are **my design choices**, not research findings. Tune after testing.

## 7. Diagram style (all Level 1 and Level 2 diagrams)
Three colours only: **black, white, purple** (`#6B3FEE`). Your steps solid purple, AI steps solid black, the working file a pale purple tint. Gates are white circles with a black ring. Flat fills, no bold outlines. Reference: `assets/diagrams/competitor-analysis-activity-flow.svg` (Level 2) and `assets/diagrams/ai-design-workflow-double-diamond.svg` (Level 1).

## 8. Worked examples
| Activity | Archetype | Status |
|---|---|---|
| Competitor analysis | A Investigate | ✅ Flow, step cards and HTML template: `examples/competitor-analysis/` |
| Co-define the requirement (partnering with business and product) | A (adapted; includes a human-only meeting step) | To draw |
| Interview synthesis | A | To draft |
| Ideation (3 distinct directions) | B Generate | To draft |
| User flow and information architecture | B | To draft |
| Critique loop | B | To draft |
| Usability findings analysis | A | To draft |
