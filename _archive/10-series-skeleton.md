# Series Skeleton: Lesson Names and Learning Objectives

**Created:** 2026-10-05 · **Status:** draft for discussion. Built from decisions in `00-decisions.md` and the method in `06`–`09`. Nothing here is taught or tested yet.
Lesson folders would be siblings under `ai design workflow/`, each with its own `materials/`, `slides/`, `assets/` (slugs suggested below). Per CLAUDE.md, lesson content stays generic: no tool names, no mentee names.

## Series
**Working title:** AI Design Workflow for Experienced Designers
**Audience:** mid/senior UI/UX/product designers with design foundations (no basics taught).
**Series outcome:** *By the end, the designer can act as a strategic partner: start from the business question, co-define the requirement with product and business, then run a repeatable AI-assisted workflow to a validated, handoff-ready prototype, where every step's output is the next step's input and every output passes a review gate.*
**Prerequisites:** working knowledge of research, UX design and prototyping; access to an AI chat tool and an AI coding tool; one real work case to use across the series (a project, or a realistic one).
**Positioning (decided 2026-10-05):** designers do not wait for the PRD to arrive. They start from the business question and co-define the requirement, so the PRD becomes something they help write, not something they receive. Where a PRD already exists, it is treated as a draft to improve.
**Through-line:** one real case from lesson 1 to the capstone. Each lesson adds one section to the same case file.

## Overview
Lesson 1 is the existing lesson `ai-workflow-for-ux-designers` ("Set Up Your AI Workflow"), re-scoped to **AI terminology and how to structure your project folder** (decided 2026-10-05). The constraint layer moved: the context pack starts in Lesson 1's folder, principle checks are written in Lesson 4 (they are part of the problem brief), and the design system context is added in Lesson 6.

| # | Lesson | Stage | Main output (feeds next) | Gate practised |
|---|---|---|---|---|
| 1 | AI terminology and your project folder | Foundation | Case folder with context pack started; shared vocabulary | (sets up all gates) |
| 2 | Co-define the requirement | Discover | Shared scope: business question, outcome and success metrics agreed with the PO, beliefs | Right question, agreed? |
| 3 | Discover with AI you can trust | Discover | Evidence pack | Traceable? |
| 4 | From evidence to a shared problem brief | Define | Shared problem brief (the requirement), co-signed: outcome, opportunities, hypotheses, principle checks | Evidence + agreement |
| 5 | Explore options and shape the solution | Develop | Three directions, one chosen; flows and content | Principles |
| 6 | Prototype on your design system | Develop | Working prototype | Design system + a11y |
| 7 | The critique loop and the alignment check | Develop | Alignment matrix + revised prototype | Alignment |
| 8 | Validate with real users | Deliver | Findings (task success, time, errors, SUS) | Real users |
| 9 | Hand off and plan the measurement | Deliver | Handoff pack + measurement plan | Buildability |
| 10 | Capstone: run the whole chain, show your value | All | Complete case + portfolio piece | All |

---

## Lesson 1 — AI terminology and your project folder
*Existing lesson:* `ai-workflow-for-ux-designers` (keep the folder and slug). *Re-scoped from* "Set Up Your AI Workflow".
**Why:** every later lesson assumes students can follow AI terms and keep their work in a folder the AI can use. This lesson gives them that once, so no later lesson re-teaches it.
**By the end, students can:**
1. Explain the core AI terms in their own words: model, AI chat tool vs AI coding tool vs in-tool AI features, prompt, context and context window, hallucination, agent, connector (MCP), and reusable instructions (skills, rules files, project memory).
2. Distinguish AI-assisted from AI-generated work, and say what stays the designer's decision.
3. Recognise Markdown and HTML and know why a plain local folder matters.
4. Set up the series **case folder** using the standard layout, with a started context pack, and say why the structure helps an AI tool find and reuse their work.
5. Reuse a saved artifact as context instead of retyping a project description.
**Key activity:** build the case folder and run one instruction against a saved artifact (Level 3 cards; no Level 2 flow needed).
**Output:** case folder with `00-context/` started (product and users, accessibility rules, glossary of the terms learnt).

### Proposed terminology list (⚠️ my proposal; adjust to your students)
| Group | Terms |
|---|---|
| Tools | AI chat tool, AI coding tool, in-tool AI features |
| Talking to AI | prompt, context, context window, tokens (why very long inputs get fuzzy), grounding in your sources |
| Failure | hallucination (why "unknown" is an allowed answer) |
| How tools act | agent, connector / MCP (lets a tool read your files and design files) |
| Reusable instructions | skills, rules files, project memory (plain text files or settings that carry your standards between sessions) |
| Files | Markdown (`.md`), HTML, local folder |
| Stance | AI-assisted vs AI-generated |
Basis: Figma describes MCP as the interface that lets AI tools read designs, and skills as reusable markdown instructions ([Figma — design systems, AI and MCP](https://www.figma.com/blog/design-systems-ai-mcp/)); other terms are standard usage. Keep each to one plain sentence plus a designer example.

### The case folder students build (replaces Options A/B/C as the series default)
```
[case-name]/                         one plain local folder per project
├── 00-context/                      the constraint layer, pasted into AI steps first
│   ├── product-and-users.md
│   ├── principle-checks.md          (written in Lesson 4)
│   ├── design-system-notes.md       (added in Lesson 6)
│   └── accessibility-rules.md
├── 01-discover/                     one living .md file per activity, plus sources/
├── 02-define/                       problem-brief.md
├── 03-develop/                      options.md, alignment.md, prototype/
├── 04-deliver/                      test-plan.md, findings.md, handoff.md
└── case-log.md                      the decision log: one line per decision and why
```
**Why this suits AI work:** numbered stage folders keep order; one file per activity gives each AI step a named input; `00-context` is the first thing pasted into every step; short plain-text files are easy to give the AI selectively; and an AI coding tool can open the whole folder as its project. Keep it a plain local folder while an AI tool is writing files; copy to cloud storage afterwards (as the existing lesson already teaches).
The existing lesson's three options (by stage, by file type, by deliverable) become *alternatives students may know about*; the series uses the stage layout because later lessons point to it.

### Mapping the existing lesson to the new scope
| Existing part | Keep / trim / replace |
|---|---|
| Overview and objective 4: AI-assisted vs AI-generated | **Keep.** It is the throughline |
| Phase 1 Mindset (data, role shift) | **Trim to ~10 minutes.** The series already opens with the market case; keep the 91% / 7-tool data and the split finding (Figma, 36/35/29). **Add the partner message:** designers who wait for a PRD are the most exposed; the series moves them upstream. Say plainly that access to the PO and business varies, and that the workflow still works when it is limited (see the access risk in Lesson 2). The existing role-shift line ("maker to strategist and editor") is the natural place |
| Phase 2 Technical literacy (Markdown, HTML, local folder, three folder options) | **Keep and extend.** Add the terminology list above; replace the three folder options with the case folder |
| Phase 3 CARE prompting + feed forward / context | **Keep, shorten.** Keep feed-forward and context reuse. Keep CARE as a light frame and map it to the series instruction checklist: Context = sections you give; Ask = the task; Rules = use only the provided material, say "unknown", return only your section; Examples = the format wanted |
| Phase 4 Four buckets mapped to five Design Thinking stages | **Replace.** Use the Double Diamond stage map (`assets/diagrams/ai-design-workflow-double-diamond.svg`) as the preview of the series. Move the bucket examples out; the later lessons cover them |
| Phase 5 Build your workflow | **Keep, change the content:** build the case folder, run one instruction against a saved artifact |
| Activity 1 (stage-mapping canvas) | **Rework** onto the four-stage map, or drop in favour of the folder build |
| Homework | Review after the above |

### Issues found in the existing lesson (fix when it is edited)
1. **Tool brand names** appear in student-facing text (for example in Materials Needed and Pre-Class Preparation). The program convention requires generic labels.
2. **Private mentee names** appear in the activity notes (lines ~369 and ~397). Lesson files must not name mentees.
3. **Program framing:** the front matter says `program: ux-class` with Design Thinking as the previous session, and the content uses the five Design Thinking stages. The series uses the four Double Diamond stages.
4. **Unverified figures:** the McKinsey "22% higher feature adoption" figure and the "NN/g Meet Ari" framing came from earlier research I have not re-checked. Verify before teaching.
5. **Missing partner framing (checked 2026-10-05):** the lesson never mentions a PRD, requirements, or working with the business; stakeholders appear only as an audience for outputs, and the process starts at Empathise. There is no "received brief" wording to remove, but the partner message and the access reality need adding to Phase 1.
6. **Sync rule:** any change to the lesson must be mirrored in `ai-workflow-for-ux-designers-slide-outline.md` (43 headings) and may need the deck rebuilt. Nothing has been edited yet.

---

## Lesson 2 — Co-define the requirement
*Slug:* `co-define-the-requirement`
**Why:** Designers who only receive a PRD are the most exposed. This lesson moves them upstream, to where the requirement is shaped.
**By the end, students can:**
1. Start from the business question (a goal, idea or problem) instead of waiting for a finished PRD, and treat any existing PRD as a draft to improve.
2. Use an AI chat tool to prepare for the conversation: questions for the business, assumptions to test, and what evidence exists or is missing (verified against what they actually know).
3. Ask the PO and the business for the outcome, the success metric and its baseline, and record any metric they could not confirm as "assumed".
4. Bring evidence to the table (even a small piece) to earn a say, and write a shared scope that the PO agrees to.
5. Write down what they already believe so it can be tested later.
**Key activity:** Co-define flow (Investigate archetype, adapted): you gather what exists → AI prepares questions and assumptions → you verify → you meet the PO and business (a human-only step) → AI turns your notes into a draft scope → you verify against the notes → you share back and agree *(to draw)*.
**Output:** `## Scope`: business question, outcome, metrics (confirmed or assumed), beliefs, and an **agreement status** (agreed / pending / not available).
**Partner moves taught:** ask early, bring a small piece of evidence, write things down and share them back, and treat the draft as shared property.

### ⚠️ Access risk: some students cannot reach the PO or the business
Some students truly have no access to the PO or the business. The lesson must not assume the meeting happens. Teach three tiers and make the course work in all of them:

| Tier | Situation | What the student does | Agreement status |
|---|---|---|---|
| 1 Full access | Can meet the PO and business | Run the meeting step, then share the draft scope back and get agreement | **agreed** |
| 2 Limited access | Can message or reach the PO indirectly (via a lead, PM or account manager) | Send the AI-drafted written questions and an assumptions memo, with a response date. Ask for corrections, not for a full meeting | **pending** until answered |
| 3 No access | Cannot reach the PO or business at all | Build the scope from what exists (the PRD or brief, public company information, product data they can see, colleagues who do talk to the business). Record every outcome and metric as **assumed**. Choose usability measures they control (task success, time, errors, SUS). Flag the scope as unconfirmed in the case log | **not available** |

**Fallback flow step (for tiers 2 and 3):** replace "you meet the PO and business" with "you send written questions and an assumptions memo". The AI drafts both from the student's materials; the student edits and sends them. If nobody replies, the student proceeds on labelled assumptions and carries the risk forward.
**Rules for the AI in this lesson:** it prepares questions and drafts notes. It must **not** play the PO and supply business facts or "typical" metrics. Simulated answers are not evidence (see the synthetic-user finding in `03-failure-cases-and-risks.md`).
**What the student still gains in tier 3:** a written, assumption-flagged scope that someone can correct later is better than designing from a brief with the assumptions hidden. It also gives them something to show when they do get a seat.
**Teach this honestly in class:** say plainly that access varies, that tier 3 is a weaker position, and that the workflow is built to degrade gracefully, not to pretend the problem does not exist. *(⚠️ The tiers are my design, not tested; the Vietnam context is described in `04-vietnam-market.md` with low-confidence sources.)*

## Lesson 3 — Discover with AI you can trust
*Slug:* `discover-with-ai`
**By the end, students can:**
1. Run a competitor analysis in which the AI works only from sources the student collected, with a source pointer in every cell and "unknown" allowed.
2. Spot-check an AI-filled table, record the error rate, and decide whether to rerun a step.
3. Use an AI step that argues against the findings and test their own beliefs against the evidence.
**Key activity:** Competitor analysis flow ✅ (`examples/competitor-analysis/`). Interview synthesis and desk research as variations.
**Output:** `## Evidence` (AI draft and verified) and `## Patterns`; the evidence pack.

## Lesson 4 — From evidence to a shared problem brief
*Slug:* `evidence-to-problem-brief`
**By the end, students can:**
1. Turn an evidence pack into a ranked list of opportunities (user needs, not features), each linked to its evidence.
2. Turn Nielsen's 10 heuristics (plus any organisation principles) into yes/no principle checks for this product, saved in `00-context/principle-checks.md`.
3. Write testable hypotheses for the solution direction ("we believe X for Y will change Z, and we will know because M") and set the right level for each.
4. Define success using Goals → Signals → Metrics, choosing metrics they can measure before launch.
**Key activity:** Problem brief flow *(to draw)*.
**Output:** the shared problem brief, co-signed by product and business, which becomes the requirement: outcome and success metrics, ranked opportunities, hypotheses, principles to check against.
**Partner move:** walk product and business through the brief and get their agreement before design begins; a PRD, if one is written, is written from this.
**If access is limited or absent (see Lesson 2):** the "agreement" part of the gate cannot be met. Carry the Lesson 2 agreement status into the brief, mark every unconfirmed outcome and metric as **assumed**, and keep the evidence part of the gate fully intact. Students in tier 3 still complete the brief; it is labelled "unconfirmed by business".

## Lesson 5 — Explore options and shape the solution
*Slug:* `explore-and-shape`
**By the end, students can:**
1. Direct an AI chat tool to generate at least three genuinely different directions from the problem brief and constraints.
2. Select a direction by checking each against the principle checks and the opportunities, and record why the others were set aside.
3. Shape user flows and content with AI drafts they edit and own (no AI-written final copy without review).
**Key activity:** Ideation and flow flow (Generate archetype) *(to draw)*.
**Output:** chosen direction, flow, content model.

## Lesson 6 — Prototype on your design system
*Slug:* `prototype-on-your-design-system`
**By the end, students can:**
1. Add design system notes to `00-context/` and give an AI coding tool the design system, tokens, accessibility requirements and flow so the prototype follows them (without writing code themselves).
2. Compare a vague prompt against a constrained one on the same task and explain the difference in output.
3. Judge a prototype's fidelity level and know it is a reference, not production code.
**Key activity:** Prototype build flow (Generate archetype) *(to draw)*.
**Output:** working prototype on the design system.

## Lesson 7 — The critique loop and the alignment check
*Slug:* `critique-loop-and-alignment`
**By the end, students can:**
1. Build an alignment matrix that traces each design decision to an opportunity, a hypothesis and the principles, and find orphan decisions and uncovered opportunities.
2. Use an AI step that argues where the design violates each principle, then decide: fix, accept as a recorded trade-off, or cut.
3. Run a light alignment check at the end of any activity.
**Key activity:** Alignment check flow ✅ drafted in `09` *(to draw)*.
**Output:** alignment matrix, principle audit, revised prototype, decision log.

## Lesson 8 — Validate with real users
*Slug:* `validate-with-real-users`
**By the end, students can:**
1. Use AI to prepare a test plan and script from their hypotheses, and explain why AI-simulated users cannot replace real ones.
2. Run a usability test and measure task success, time on task, errors and SUS against a baseline.
3. Verify AI-assisted analysis of findings against raw recordings or notes, and weigh findings by importance rather than frequency.
**Key activity:** Plan-and-read-the-measurement flow (Investigate archetype), pre-launch scope *(to draw)*.
**Output:** findings, updated decision log, updated prototype.

## Lesson 9 — Hand off and plan the measurement
*Slug:* `handoff-and-measurement`
**By the end, students can:**
1. Produce a handoff pack in which the prototype is the reference and the decision log explains the choices, so a developer can build without asking.
2. Write a measurement plan for after launch (what to track, where, when to review) and hand it to the PO, even if they cannot access the data themselves.
3. Describe their own AI workflow results (time per step, error rate, rework) with counts, not impressions.
**Key activity:** Handoff flow *(to draw)*.
**Output:** handoff pack and measurement plan.

## Lesson 10 — Capstone: run the whole chain, show your value
*Slug:* `capstone-ai-design-workflow`
**By the end, students can:**
1. Run the full chain on a real case, each step's output feeding the next, with every gate recorded.
2. Present the case showing evidence, decisions and trade-offs, so an employer or PO sees the judgement, not just the speed.
3. State which parts of the workflow they would keep, tune, or skip, with reasons from their own measured results.
**Output:** complete case file, report, and a portfolio piece.

---

## Open items for discussion
1. **Length and format:** how long is each lesson, and is the series live, self-paced, or a cohort? Sets how much fits in Lesson 1 (terminology plus folder plus the context habit is a lot for one session).
2. **Edit the existing lesson now?** *(Winnie: "check it when I apply the re-scope"; confirm the go-ahead to apply.)* Lesson and slide outline would both need changes, plus the deck. I have not touched them. Say go and I will apply the re-scope, fix the convention issues, and keep the pair in sync.
3. **Lesson 1 carries a lot.** If it overruns, move "context reuse" or the CARE mapping to Lesson 2, where students first use it for real.
4. **Overlap with Library Discover lessons:** Lesson 3 should point to them for method and teach only the AI-assisted layer.
5. **Case:** each student's own real case, or a shared case study so work can be compared in class?
6. **Flows still to draw:** co-define the requirement, problem brief, ideation/flow, prototype build, alignment check, plan-and-read-measurement, handoff.
