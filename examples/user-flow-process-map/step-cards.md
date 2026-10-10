# Step Cards — User Flow and Process Map

**Created:** 2026-10-09 · **Status: draft, untested.** Third worked example of the standard in `../../02-method.md` Part 1, using the card format in `../../02-method.md` Part 2. Uses generic labels per CLAUDE.md. The AI instructions are my design and have not been run in a class.

**Decision this activity informs:** which single structural change would remove the most friction from one core task, and is that friction in the user's path (User Flow) or behind the screen (Process Map)?

## The idea in one paragraph
A diagram looks finished long before it is true. AI makes this worse: it draws a clean, plausible flow from a one-line description, and the mentee can no longer tell what is real. So the AI never draws first. The mentee collects the facts, the AI turns them into a **table** (the review copy), the mentee verifies the table against the real product, the AI analyses the verified table, and only then does the AI turn the approved table into diagram code. The table is the source of truth. The diagram is a view of it.

## Two branches, one spine
| | Branch A — User Flow | Branch B — Process Map |
|---|---|---|
| Perspective | One user's path | Whole operation, front-stage and back-stage |
| Facts the mentee collects (step 2) | Own walkthrough notes: every screen, tap, state | Walkthrough notes **plus** back-stage facts: who or what acts, handoffs, waits. Each fact tagged with its source (team member, doc, engineering) |
| Extra table columns (step 3) | — | Lane (actor), Handoff (yes/no), Wait (known / unknown) |
| What the AI does at step 5 | Finds friction against the job; proposes at least three different structures for the worst step | Places steps in lanes, marks handoffs and waits, lists **questions to ask the team** instead of guessing |
| Order | First | Second. Reuse the verified table from A and add back-stage facts only. |

If the task has one actor, run A only. If friction cannot be explained by screens, add B.

## The working file (one file, one folder)
```
user-flow-[task]/
├── user-flow-process-map.md   ← the one working file; each step fills one section
├── sources/                   ← walkthrough notes, screenshots, back-stage facts (each with a source tag)
```
| Section | Filled in step | By |
|---|---|---|
| `## Frame` (task, entry/end, job, constraints, method, current belief) | 1 | You |
| `sources/` (notes with IDs N01…, back-stage facts B01…) | 2 | You |
| `## Table (AI draft)` | 3 | AI. **Never edit.** |
| `## Table (verified)` | 4 | You: a copy you correct |
| `## Analysis (AI)` | 5 | AI |
| `## Fix + decision` | 6 | You |
| `## Diagram code (AI)` | 7 | AI |
| `## Final diagram + limits` | 8 | You |

Same two safety rules as every flow: the AI returns only its own section, and the AI draft and your verified copy stay separate. The gap between them is your error rate for this kind of task.

## If a gate fails
| Gate | After step | Supports stage check | If the answer is no |
|---|---|---|---|
| A: does the table match the real product? | 4 | (local to this activity) | Go back to step 2 and walk the product again; then rerun step 3 |
| B: is the fix defensible? | 6 | 3a, 3b, 3c | Go back to step 5 and ask for alternatives again; check unknowns with the team first |
| C: does the diagram match the table? | 8 | 3b, and 3d when it goes to handoff | Go back to step 7 (code differs from the table) or step 4 (table was wrong) |

Stage checks are in `../../02-method.md` Part 3, §2.

---

## Step 1 — Frame (YOU)
**Goal:** Fix the scope before any tool touches it, and write down what you already believe.
**Do:** Fill `## Frame`:
- the task, specific ("book and confirm a slot as a returning user", not "booking")
- entry point and end point
- the job it serves (from your JTBD Map)
- constraints you must respect (principles, design system, known technical or legal limits)
- the method: A User Flow, B Process Map, or both in order
- what you believe the flow is today, as 5 to 10 words per step (your sketch from memory)

**Check:** Could someone else tell where this task starts and ends?
**Failure sign:** Task is a whole feature area; no end point; no belief written down (then you cannot see what the walkthrough surprised you with).
**Output:** `## Frame`

## Step 2 — Capture the facts (YOU)
**Goal:** Collect what is true, so the AI has nothing to invent.
**Do:**
- *Branch A:* Open the product (or prototype) and complete the task. Narrate aloud. For every step write one note with an ID (N01…): what the screen shows, what you did, what happened next, and any error or empty state you hit. Deliberately trigger one failure (wrong input, no network, not logged in). Add screenshots.
- *Branch B, in addition:* Ask the people who know the back-stage: engineering, support, operations. For every handoff or system action write one fact with an ID (B01…): who or what acts, what triggers it, how long it takes, **and who told you** (source tag). If nobody knows, write "unknown" as a fact. That is data too.

**Check:** Is every note something you saw or someone told you, in their words?
**Failure sign:** Notes written from memory or from how it "should" work; back-stage facts with no source; no failure state tried.
**Output:** files in `sources/`

## Step 3 — Structure (AI)
**Goal:** Turn the raw notes into a table that can be checked line by line.
**Give the AI:** `## Frame` and the notes in `sources/` (and the verified table from a previous run, for branch B).
**Instruction essentials:**
> Using only the notes below, build a step table for this task. Columns: ID, Shape (pill, rectangle, diamond, note; add parallelogram and a Lane column for system or team steps), Label (short, from the notes), Next (the ID it leads to; for a diamond, one row per branch with a label such as Yes / No), Evidence (note IDs), Status (stated, inferred, or unknown). Every step must cite at least one note ID. If you add a step the notes imply but do not state, mark it "inferred". If you do not know what happens, write "unknown"; do not fill the gap. After the table, list: (1) diamonds with fewer than two outgoing branches, (2) paths that never reach an end, (3) states with no coverage in the notes (empty, error, loading, success). Do not suggest improvements yet. Return only the table and the three lists.

**Check:** Does every row cite a note? Are "inferred" rows few and clearly marked?
**Failure sign:** A beautiful complete table with no "unknown" or "inferred" rows. Real notes always leave gaps.
**Output:** `## Table (AI draft)`

## Step 4 — Verify against the product (YOU) · Gate A
**Goal:** Make the table true. Copy the AI draft into `## Table (verified)` and correct the copy.
**Do:** Walk the product again, following the table row by row. Fix wrong labels, remove invented steps, resolve every "inferred" and "unknown" (walk it, or ask someone) or leave it visibly unknown. Count the AI's errors: wrong, invented, missing.
**Gate A questions:**
- Could another person follow this table and reach the same screens?
- Is every "inferred" row either confirmed or removed?
- Does every diamond have two labelled branches, and every path an end?

**Failure sign:** You corrected nothing. (Either the AI was perfect, which is rare, or you did not walk the product.)
**Output:** `## Table (verified)`

## Step 5 — Analyse (AI)
**Goal:** Find where the structure causes friction, and widen the options before you choose.
**Give the AI:** `## Frame` and `## Table (verified)`. Nothing else.
**Instruction essentials:**
> *Branch A — User Flow.* Using only the verified table and the job in the frame: (1) for each step, say whether it helps the user progress toward the job or is friction, with the row ID as evidence and a one-line reason; mark guesses as "inferred". (2) Pick the three highest-friction steps. For the worst one, propose three genuinely different ways to restructure it (for example: remove it, move it earlier or later, merge it with another step, let the system do it). For each: what changes, what it costs, and what it might break. (3) List missing states. (4) Argue against your own conclusion: the strongest reason these steps might exist for a good reason, and what evidence would change your mind. Do not recommend one option. Return only your section.
>
> *Branch B — Process Map.* Using only the verified table and the back-stage facts: (1) place each step in a lane; do not move or rename steps. (2) Mark every handoff and what is passed. (3) Mark every wait, with the fact ID that supports it or "unknown". (4) List the questions to ask the team to close every "unknown", as questions, not guesses. (5) Name the steps the user feels as a delay or error but cannot see the cause of. (6) Argue against your own conclusion, as in branch A. Return only your section.

**Check:** Does every claim point to a row or fact ID? Are the three options really different (not one idea in three wordings)?
**Failure sign:** Confident recommendations about systems the notes never described; options that all keep the same step.
**Output:** `## Analysis (AI)`

## Step 6 — Decide the fix (YOU) · Gate B
**Goal:** Choose one structural change, and know what it rests on.
**Do:** Read the analysis against your verified table. Choose one step to change and one option (or your own). Write: why this step exists today, what would change structurally, what you would test to validate it. Check the AI's "removable" steps with engineering or whoever owns them. A step can be removable on paper and required in the system.
**Gate B questions:**
- Were at least three genuinely different options considered, and is the reason for the choice recorded? (3a)
- Does the fix trace to the job and to evidence in the table, not to the AI's opinion? (3b)
- Does it pass your principles, or is the conflict recorded as a trade-off? (3c)

**Failure sign:** You picked the AI's first option; "unknown" items were never resolved; no test named.
**Output:** `## Fix + decision`

## Step 7 — Turn the table into diagram code (AI)
**Goal:** Draw quickly from a table you already trust.
**Give the AI:** `## Table (verified)` (and, if you want the "after" view, the table plus the decision).
**Instruction essentials:**
> Convert the verified table into Mermaid flowchart code. Use exactly the steps and branches in the table: do not add, remove, rename or reorder anything. Shapes: pill `([text])`, rectangle `[text]`, diamond `{text}`, parallelogram `[/text/]`. Label every branch from a diamond. For a process map, use one `subgraph` per lane. Mark "unknown" rows with a dashed arrow. Return only the code in one block.

**Check:** Count nodes and arrows in the code against the table.
**Failure sign:** An extra "helpful" node, a merged step, a branch with no label.
**Output:** `## Diagram code (AI)`

## Step 8 — Draw, compare, state the limits (YOU) · Gate C
**Goal:** Put the diagram where the team will use it, and say what it cannot tell them.
**Do:** Paste the code into a diagram tool (or redraw in FigJam or Miro) and tidy the layout. Compare the picture to `## Table (verified)`. Highlight in red the steps that exist because of an IA, system or organisational constraint. Write `## Final diagram + limits`.
**Gate C questions:**
- Does the diagram contain exactly the verified steps?
- Is every unresolved "unknown" visible on the diagram?
- Have you said what this cannot tell us?

**Failure sign:** A tidy diagram that hides an unknown; no limits section.
**Output:** `## Final diagram + limits`, diagram attached to the hub page for Develop.

---

## Limits to say out loud
The map shows how the task works **today, as far as you and your sources know**. It does not show why users drop off, how long steps really take, or whether the fix will work. Those need real users and real data. The AI knows only what you gave it; whatever the table marks "unknown" is still unknown on the diagram.

## To test before teaching
1. Run branch A on one real product. Time each step. Step 2 will take longest, and it must not be skipped.
2. Measure the table errors at step 4 (wrong, invented, missing). If the AI invents more than a few rows, tighten the step 3 instruction.
3. Run branch B on a task with a manual back-stage step. Does the AI list questions instead of guessing the owner? If it guesses, tighten step 5.
4. Check that Mermaid output matches the table in node count. If not, the "do not add or remove" instruction is too weak.
5. Check whether the step 5 counter-argument is a real argument or a token sentence.
6. Check whether the three options are really different.
