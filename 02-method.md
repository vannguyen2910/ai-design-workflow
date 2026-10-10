# Method: Activity Flow Standard, Step Cards, Stage Gates

How every activity in the series is designed. Part 1 is the standard; Part 2 is the step card format; Part 3 is what to delegate and which gate applies at each stage. Worked example: `examples/competitor-analysis/`.

**In this file**
- [Part 1 — Activity flow standard](#part-1--activity-flow-standard)
- [Part 2 — Step card template](#part-2--step-card-template)
- [Part 3 — Stage methods, delegation and gates](#part-3--stage-methods-delegation-and-gates)

---

## Part 1 — Activity flow standard

**Created:** 2026-10-05 · **Status:** draft standard, built from one worked example (competitor analysis) and not yet tested on other activities.
This file is the **standard**. It applies to any design activity (competitor analysis, interview synthesis, ideation, flows, prototyping, usability findings, and so on). Specific activities live in `examples/`, and each one follows this file. Step card format: `02-method.md` Part 2.

### 1. Three views
| View | Shows | Format | Used for |
|---|---|---|---|
| 1 Stage map | Stages (Discover, Define, Develop, Deliver), input → output, gate | Double Diamond columns | Series overview slide |
| 2 Activity flow | Steps inside one activity: who does each (you / AI), the file it writes to, the review gates | **Swimlane flowchart** | One slide per activity |
| 3 Step card | Per step: goal, input, AI instruction, checks, failure signs, output | Text card | Lesson handout |

Swimlane is the format because the series' claim is *human review after every AI step*: the alternation between the YOU and AI lanes is the review loop.

### 2. Rules every activity flow follows
1. **Frame first.** Step 1 is always human: the decision this activity informs, the constraints (from the Foundation: principles, design system, context), and what you already believe.
2. **Alternate you and AI.** Every AI step is followed by a human step that reviews it. No two AI steps in a row.
3. **AI works only from what you give it.** Name the inputs (sections of the working file, files in `sources/`). Facts must come from provided sources, never from the AI's memory.
4. **Uncertainty is allowed and visible.** The AI says "unknown" or "inferred" instead of guessing.
5. **Evidence per claim.** Every AI claim carries a pointer to where it came from.
6. **Keep the AI draft.** The AI's output stays untouched as one section; your corrected version is a separate section. The gap is your error rate.
7. **Challenge before deciding.** One AI step argues against the conclusion before you decide.
8. **Maximum three activity gates.** Each is a yes/no question the student can answer, with a **a line saying where to go back to** ("if no, return to step N"), and each names the **stage check** it supports (the gate list in Part 3, §2).
9. **End with the decision.** The last step answers the decision from step 1 (or says what evidence is missing).
10. **State the limit.** Every flow ends with "what this cannot tell you" (usually: why users behave this way; that needs real users).
11. **Eight steps or fewer** so the flow fits one slide.
12. **Alignment check at the last gate.** Before the output moves on, check it against the problem brief: does it serve the outcome and an evidenced opportunity, test a hypothesis, and pass the principles (Nielsen's 10 plus any organisation principles)? If not, go back. The full version (matrix, principle audit) is taught in the closing block of the second prototype lesson; see `03-quality-and-measurement.md` Part 1.

### 3. One working file
Each activity has one folder:
```
[activity]-[subject]/
├── [activity].md       ← the one working file; each step fills one section
├── sources/            ← raw evidence (only if the activity uses sources)
└── [deliverable].html  ← the shareable output, built by the student from a template (+ PDF export)
```
- **One file, sections per step.** One place to read and update.
- **The AI returns only its own section;** the student pastes it in. This prevents silent rewrites of settled work.
- **Give each AI step only the sections it needs.**
- **Markdown inside** (plain text is what AI reads and writes reliably); **HTML outside** for stakeholders.
- Version history in the cloud drive is the safety net. *(⚠️ my recommendation, untested.)*
- **Each activity's HTML page is one page of the Experience Hub** (`hub/` in the case folder), not a standalone report. Items that other activities refer to (opportunities, hypotheses, decisions, principle checks, tests, metrics) get short IDs so the hub can link them; see `03-quality-and-measurement.md` Part 1.

### 4. Two patterns (starting skeletons)
Most activities fit one of two spines. Pick one, then adapt.

**A. Investigate** (competitor analysis, desk research, interview synthesis, usability findings analysis)
Frame → Suggest (AI) → Review the list (YOU, gate) → Collect sources (YOU) → Extract (AI) → Verify (YOU, gate) → Compare + challenge (AI) → Interpret + decide (YOU, gate)
Feeds stage checks **1b, 1c** (and 2a when the evidence supports an opportunity).

**B. Generate** (ideation, user flows, content, prototype, refine loop) *(⚠️ hypothesis, not yet drawn or tested)*
Frame with constraints (YOU) → Generate at least 3 genuinely different options (AI) → Select against principles (YOU, gate) → Develop the chosen one (AI) → Critique: AI argues back (AI) → Check against principles, design system, accessibility (YOU, gate) → Decide and refine (YOU)
Feeds stage checks **3a to 3d**.

This follows the series decision to use a different gate by stage (the single gate list is in Part 3, §2): evidence early (Discover, Define), principles and system in the middle (Develop), real users and buildability late (Deliver). See `02-method.md` Part 3.

### 5. Standard AI instruction checklist
Every AI step's instruction should contain, in plain words:
- the **scope** (paste the relevant sections, nothing else)
- **use only** the provided material
- an **evidence pointer** for each claim
- permission to say **"unknown"** and to mark **inferences**
- **return only your section**, in a stated format
- for synthesis steps: **no recommendations yet**, and note **what this cannot tell us**
- for challenge steps: **strongest argument that it is wrong**, and **what evidence would change your mind**

### 6. Research basis
- Trace outputs back to raw sources: [Parallel HQ](https://www.parallelhq.com/blog/ai-assisted-ux-research-workflow)
- Synthetic output is agreeable and shallow, so "unknown" and real-user gates: [NN/g via Userbrain](https://userbrain.com/blog/synthetic-users-experiment/), [NN/g — Real Design Scenarios](https://www.nngroup.com/articles/testing-ai-methodology)
- Make the AI argue against you; keep judgment human: [Designer Fund — Linear](https://designerfund.substack.com/p/ai-design-linear)
- Frequency is not importance (so the human weighs): Parallel HQ
- Rules 2, 6, 8 and 11 and the two patterns are **my design choices**, not research findings. Tune after testing.

### 7. Diagram style (all stage map and activity flow diagrams)
Three colours only: **black, white, purple** (`#6B3FEE`). Your steps solid purple, AI steps solid black, the working file a pale purple tint. Gates are white circles with a black ring. Flat fills, no bold outlines. Reference: `assets/diagrams/competitor-analysis-activity-flow.svg` (activity flow). New activity flows are drawn as plain HTML, not SVG: see `assets/diagrams/user-flow-process-map-activity-flow.html`. Same three colours and symbols and `assets/diagrams/ai-design-workflow-double-diamond.svg` (stage map).

### 8. Worked examples
| Activity | Pattern | Status |
|---|---|---|
| Competitor analysis | A Investigate | ✅ Flow, step cards and HTML template: `examples/competitor-analysis/` |
| User-voice synthesis (public reviews, forum posts, short interviews) | A Investigate | ✅ Flow and step cards: `examples/user-voice-synthesis/` |
| Shape the brief (partnering with business and product) | A (adapted; includes a human-only meeting step) | To draw |
| Interview synthesis | A | To draft |
| Ideation (3 distinct directions) | B Generate | To draft |
| User flow and process map (current-state map, then fix) | A + B (adapted) | ⚠️ Draft, untested: `examples/user-flow-process-map/` |
| Refine loop, inside "Refine and check your design" | B | To draft |
| Usability findings analysis | A | To draft |


---

## Part 2 — Step card template

**Created:** 2026-10-05 · Use with `02-method.md` Part 1. One card per step in an activity flow. A finished example: `examples/competitor-analysis/step-cards.md`.
Use generic labels ("AI chat tool", "AI coding tool") per CLAUDE.md.

### How to start a new activity
1. Choose the pattern in Part 1 of `02-method.md` (Investigate or Generate) and write the step list (8 or fewer).
2. Draw the activity flow in the standard style (copy the competitor-analysis SVG as a base).
3. Define the working file's sections: one per step that produces content.
4. Write one card per step using the format below.
5. Build the page template (HTML) for this activity's page in the Experience Hub.
6. Run it once on a real case, time each step, and fill in "To test".

### Page header for each activity's card file
- Activity name, pattern, and the decision it supports
- Working file layout (folder tree and the section-by-step table)
- **If a gate fails** table (gate · after step · go back to)
- Cards
- Limits to say out loud
- To test before teaching

### Card format
```
## Step N — [Name] (YOU | AI) · [Gate X, if any]
**Goal:** one sentence: what must be true after this step.
**Give the AI / Do:** which sections or files go in (AI steps) or what you do (YOU steps).
**Instruction essentials:** (AI steps only) a quoted instruction built from the checklist in Part 1 §5.
**Gate X questions:** (gate steps only) 2–3 yes/no questions.
**Check:** what to look at before moving on.
**Failure sign:** what a bad result looks like.
**Output:** the section or file this step writes.
```

### Quality checklist for a finished card file
- [ ] No two AI steps in a row; every AI step followed by a human review
- [ ] Every input is named (a section or a file); nothing comes from the AI's memory
- [ ] Every AI instruction includes: scope, use only provided material, evidence pointer, "unknown" allowed, return only its section
- [ ] AI draft and verified version are separate sections (where a verify step exists)
- [ ] One challenge step before the decision
- [ ] 3 activity gates or fewer, each saying where to go back to and which stage check it supports (Part 3, §2)
- [ ] Last step answers the step 1 decision
- [ ] The last gate includes an alignment question (outcome, opportunity, hypothesis, principles)
- [ ] "Limits to say out loud" is written
- [ ] Failure sign written for every step
- [ ] Tested on one real case; times and error rate recorded

### Report template (the shareable output)
Start from the hub's Evidence page (`assets/templates/hub/evidence.html`) and keep its skeleton: decision banner → our answer → what was compared/explored and why → main evidence table → beliefs or hypotheses tested → insights (each with a counter-argument and evidence link) → what this cannot tell us → appendix of sources and method. Rename sections to fit the activity.


---

## Part 3 — Stage methods, delegation and gates

**Researched:** 2026-10-05 · Builds on the early six-stage draft, which is now replaced by the stage map and the gate list in §2 below.
**Confidence:** Research and prototyping stages have decent sources. Frame, Shape and Handoff rest mostly on practitioner blogs and my synthesis. ⚠️ marks the weakest claims.

### 1. Evidence by stage

#### Frame (PRD → problem brief)
- AI produces convincing problem statements in seconds, "but it takes a person to notice when the statement is pointing the wrong way." AI doesn't resist jumping to solutions. ([Parallel HQ](https://www.parallelhq.com/blog/ai-assisted-ux-research-workflow), [LogRocket](https://blog.logrocket.com/ux-design/state-of-ai-for-ux-design))
- Linear's pattern is the best model: a custom skill **interrogates a request against the team's own principles and customer data to find the underlying need**, rather than accepting the surface ask. Rules: gather context, not opinions; make AI argue against you; define success before building. ([Designer Fund — Linear](https://designerfund.substack.com/p/ai-design-linear))
- ⚠️ Teaching implication: this is where designers gain the most (testing the brief with evidence, together with product), and it needs the least tooling.

#### Explore (research and options)
- AI is useful for cleaning data, transcribing, clustering and tagging. It is weak at importance: "A minor visual bug might get mentioned 20 times because it is obvious" while critical issues appear rarely. Frequency isn't weight. ([Parallel HQ](https://www.parallelhq.com/blog/ai-assisted-ux-research-workflow))
- NN/g tested LLM synthesis tools: several research steps benefit, but "analysis and synthesis consistently falls short", producing insight-shaped output. Their 2025 testing is summarised in secondary sources, not read directly. ⚠️
- Verification habits that work: trace every finding back to a raw quote or recording; ask for counterexamples and hesitations; hunt for outliers the algorithm smoothed over.

#### Shape (flows, IA, content)
- NN/g tested design, code-based and chatbot tools on two real scenarios: simple pages came out fine, **complex multi-step flows (a bulk-purchase flow) were much harder**; layouts were repetitive and "solution diversity" and "creative judgment" fell short. ([NN/g — Real Design Scenarios](https://www.nngroup.com/articles/testing-ai-methodology))
- Linear deliberately keeps AI **out of** UI copy and messaging.
- ⚠️ Implication: AI drafts options; the designer chooses and writes final content.

#### Prototype
- NN/g: detailed specs improved results; **linking to existing design files held the visual language**; vague prompts gave generic layouts; **accessibility wasn't reliably met unless mandated**. Recommends controlled, repeatable testing of prompts, and design outputs rather than text alone as input.
- Cross-company pattern (Spotify, Figma, Shopify in `01`): design system and tokens act as the guardrail; AI prototypes are not production code.
- Fidelity ladder (Lenny's Newsletter): screenshots → library extension → production code, each higher fidelity.

#### Validate
- Synthetic users: NN/g found them "too shallow to be useful" against three real studies and overly positive and cooperative (a synthetic persona claimed it completed all courses). A 2025 CHI paper (UXAgent) found AI agents followed neat paths while real users wandered and gave up. Defensible use: **prepare and catch obvious issues, never replace real testing.** ([Userbrain](https://userbrain.com/blog/synthetic-users-experiment/), [PM Toolkit](https://pmtoolkit.ai/learn/experimentation/synthetic-users-promise-and-trap))
- AI moderators can't see behaviour beyond spoken words.
- Linear avoids AI for design critique because designers need provocation, not affirmation. A good use is making AI *argue against* the design.
- Critique risk: AI prototypes pull critique toward surface polish; anchor critique in vision and problem framing. ([Designative](https://www.designative.info/2025/11/10/rethinking-design-critiques-in-the-age-of-ai-prototyping/))

#### Hand off
- ⚠️ Thinnest area. Sources describe the interactive prototype replacing the static spec, plus Code Connect and rules files at Figma, but I found no strong source on **decision logs** or acceptance notes. The decision log is my proposal, not a market practice.

### 2. The gate list (canonical, one list for the whole series)

**This is the only list of gates.** The stage map, the lesson plan, the activity flows and the hub all refer to it. (Earlier drafts had a six-stage table, a four-gate stage map and a per-lesson list; they are replaced by this.)

**How it works**
- There are **four stage gates**, one per stage. Each is a short list of **checks**, numbered by stage and lettered: 1a, 1b, 2a and so on. (The letters avoid clashing with the hub's item IDs O, H, D, P, T, M.)
- A **check** is a yes/no question the student can answer by pointing at something in the hub. A stage gate **passes** when every check is passed, or a failed check has a recorded reason (for example "assumed, unconfirmed").
- **Activity gates** (A, B, C inside an activity flow) are local to that activity. Each one names the stage check it supports, and its "if no" line sends the student to the activity step that produced the problem.
- **Mix by stage:** evidence and agreement early, alignment in the middle, real users and buildability last. A single gate type cannot do all three jobs, because principles cannot tell you whether a problem is real.
- The hub Overview shows these checks and **derives** each gate's status from them.

| Gate | Check | The question |
|---|---|---|
| **1 Discover: Question + evidence** | 1a | Is the business question and outcome agreed with the PO, or marked "assumed" with the agreement status recorded? |
| | 1b | Does every insight trace to a raw source you can open? |
| | 1c | Was nothing guessed? "Unknown" and counterexamples are recorded; the AI draft is kept beside your verified version, with the error rate. |
| **2 Define: Evidence + agreement** | 2a | Does each opportunity cite the evidence behind it? |
| | 2b | Is the problem brief co-signed by product and business, or its agreement status recorded? |
| | 2c | Does each hypothesis have a test and a metric (unconfirmed metrics marked "assumed")? |
| | 2d | Are the principle checks (Nielsen's 10 plus any organisation principles) written as yes/no questions? |
| **3 Develop: Alignment** | 3a | Were at least three genuinely different directions explored, with the choice and reasons recorded? |
| | 3b | Does every decision trace to an evidenced opportunity and a hypothesis (no decision without a user need, no opportunity left unserved)? |
| | 3c | Does every decision pass the principle checks, or is the conflict a recorded trade-off? |
| | 3d | Does the prototype use the design system, and were the accessibility rules checked? |
| **4 Deliver: Real users + buildability** | 4a | Did real users test the hypotheses, with results set against the baseline? (AI prepared and analysed; it did not stand in for users.) |
| | 4b | Do findings trace to raw notes or recordings, and are they weighted by importance, not frequency? |
| | 4c | Could a developer build it without asking? Handoff pack and decision log complete. |
| | 4d | Is the measurement plan handed to the PO (what to track, where, when to review)? |

**Where each check is practised (lesson plan):** Shape the brief 1a · Research you can trust 1b, 1c · Frame the problem 2a to 2d · Explore ideas 3a · First prototype 3d (design system) · Refine and check 3d (accessibility), then the closing alignment check 3b, 3c · Test with users 4a, 4b · Hand off and measure 4c, 4d · Capstone all.

**Working stages used earlier in this part.** The six headings above (Frame, Explore, Shape, Prototype, Validate, Hand off) are the working stages used while researching delegation. They map onto the four gates like this: Frame and Explore feed gates 1 and 2; Shape and Prototype feed gate 3; Validate and Hand off feed gate 4.

### 3. Gaps to close next
- Primary sources for Frame and Hand off.
- Read the NN/g articles directly (the figures above come through summaries).
- Hear from 3–5 practising mid/senior designers about what they refuse to delegate.

