# Lesson details

Reference for building each lesson. **Read `00-plan.md` first**; this file holds the detail it leaves out: the series vocabulary, then the objectives, activity and output of each content lesson (Lesson 1 to 9), the practice sessions and the final project.

Lessons are content blocks; they fold into 7 weekly modules (see the schedule in `00-plan.md`). Some of this text was written for the earlier 10-lesson plan, so where it says "week" or "session" check `00-plan.md` for the current timing.

**In this file**
- Series vocabulary
- Lesson 1 to 9
- Practice sessions and final project

---

### Series vocabulary (plain-language rule, 2026-10-05)
Use **one name per idea**, and nothing else, in anything a student reads. Define a term on first use. Do not add new terms without adding them here.

| Say | It means | Do not say |
|---|---|---|
| **case**, **case folder** | The project the student works through, and its folder | case file, project file |
| **working file** | The one Markdown file an activity fills, section by section | living file |
| **context pack** | The `00-context` folder pasted into AI steps first | constraint layer |
| **hub** (Experience Hub on first use) | The connected website that holds every output | final report (only for the finished hub) |
| **output** | A file or page a step produces | artifact, deliverable |
| **gate** and **check** | A gate is a short checklist before moving on; a check is one yes/no question (1a, 3b …) | — |
| **stage map**, **activity flow**, **step card** | The three views: the whole series, one activity, one step | Level 1, Level 2, Level 3 |
| **pattern** (Investigate or Generate) | The starting shape of an activity flow | archetype |
| **alignment check**, **alignment table** | Does each decision trace to a user need and pass the principles | alignment matrix |
| **opportunity** | A user need worth solving, backed by evidence | — |

Plain wording for hub warnings and reviews: a **decision with no user need behind it** (not "orphan"), an **opportunity with no decision** (not "uncovered"), a **decision that pulls against a principle** (not "strain"), **word for word** (not "verbatim"), **access levels** full, limited and no access (not "tiers"), and "**if no, go back to step N**" (not "go-back rule"). The internal key `rel: "strains"` in the hub data file stays as it is; students never see it.

---

### Lesson 1 — Your design process, with AI
*Revised 2026-10-06: now `design-process-with-ai` (see the decisions log). The text below is the earlier "Set up your AI workspace" scope; its objectives 2 to 6 still apply, and the rebalance tables are superseded by the new phase timings.*
*Existing lesson:* `ai-workflow-for-ux-designers` (keep the folder and slug; the lesson title is now "Set up your AI workspace"). *Re-scoped from* "Set Up Your AI Workflow", then **rebalanced 2026-10-05** (see below).
**Why:** every later lesson assumes students can follow AI terms, know what is safe to give an AI tool, and keep their work in a folder the AI can use. This lesson gives them that once, so no later lesson re-teaches it.
**Added 2026-10-07 (session 1, 17 minutes):** where UI/UX and product design are heading, three career paths (strategic designer, design builder, AI product designer) with sourced evidence, and a 2-minute pair talk about each student's direction; the student writes `00-context/my-direction.md` at the start of session 2. Evidence and caveats: `04-future-of-design-careers.md`.
**By the end, students can:**
0. Describe three career paths, the evidence for each and its limits, and choose the one they lean towards.
1. Explain ten core AI terms in their own words: AI chat tool, AI coding tool, context, context window, grounding, hallucination, agent, connector (MCP), reusable instructions (skills, rules files, project memory), and AI-assisted vs AI-generated. (Model, prompt and in-tool AI features are covered in passing.)
2. Recognise Markdown and HTML, and explain why a plain local folder matters.
3. Set up the series **case folder** with the standard layout, a started context pack and an empty hub.
4. Reuse a saved file as context instead of retyping, and ask for a source pointer and an "unknown" answer.
5. Decide what is safe to give an AI tool: sort material into safe, ask first and never in a public tool; anonymise before pasting; write their own data rules.
6. Explain how to share their hub with a stakeholder: private by default (a PDF or zipped folder), published on GitHub only when the case is free to share.
**Key activity:** an instructor demo of one task done twice (vague vs structured instruction on a case card), then build the case folder and run one instruction against a saved file. **Homework (up to 60 minutes):** Assignment 1 (case folder, required, about 35 minutes) and Assignment 2 (share your hub, optional, about 25 minutes: PDF export, or publish if the case is free to share).
**Output:** case folder with `00-context/` started (product and users, accessibility rules, data rules, optional glossary) for the student's own case, and an empty hub (private).

**Rebalance (2026-10-05, for the earlier 120-minute version)** — fixes from the content review (overloaded, no early value):
| Before | After |
|---|---|
| 120 minutes fully used (13 / 38 / 23 / 30 / 16), no slack | **106 minutes of content + 14 minutes buffer** (14 / 30 / 18 / 30 / 14) |
| First value came late (after terms and folders) | **"One task, done twice" demo in the first 14 minutes**: a vague and a structured instruction on a case card, so the terms later explain something students have already seen |
| 14 terms in 5 groups, 15 + 15 minutes | **10 terms**, 12 minutes of terms + 10-minute pair activity; model, prompt and in-tool features in passing |
| Separate stat slides; Markdown to HTML pipeline slide; "public means" slide | Merged or folded into speaker notes; 38 slides become **35** |
| GitHub teach 7 minutes with its own public-link slide | **5 minutes**, two slides; the public/private rules are in the speaker notes of the five-steps slide and in the guide |
| Lesson file ~6,000 words | **~5,100 words** (outline ~5,000) |
**Refit to the 90-minute class (2026-10-05).** The weekly format (see Class format) shrinks the live session from 120 to 90 minutes: terms and folder detail move to a one-page pre-read (the Week 1 brief, inside the lesson file); live phases are 12 / 21 / 10 / 25 / 8 minutes plus a 14-minute buffer; Activity 1 is 5 minutes; the data safety block stays; GitHub publishing becomes optional homework; the lesson file is about 4,550 words and the outline has 30 slides. Terms are taught "in action" against the demo, not read out.
Superseded by the refit above for the 90-minute class: the GitHub teach is now optional homework and the case model is the student's own case by default. Kept: the data safety block (now 10 minutes of the live session), never to be cut.
Still true: this is the heaviest lesson in the series; a pilot should check the clock. Cut order if it overruns: "reuse" block in Phase 3, then the Phase 5 hub description, never data safety.

### Terminology list (ten terms; rebalanced 2026-10-05)
| Group | Terms |
|---|---|
| The tools | AI chat tool, AI coding tool |
| Talking to the AI | context, context window, grounding |
| When it goes wrong | hallucination (why "unknown" is an allowed answer) |
| How some tools act | agent, connector (MCP) |
| Carrying your standards | reusable instructions: skills, rules files, project memory |
| Stance (covered in the mindset phase) | AI-assisted vs AI-generated |
In passing, not on the cards: model, prompt, in-tool AI features, tokens. Markdown, HTML and the local folder are taught as files, in the folder phase. Basis: Figma describes MCP as the interface that lets AI tools read designs, and skills as reusable markdown instructions ([Figma — design systems, AI and MCP](https://www.figma.com/blog/design-systems-ai-mcp/)); other terms are standard usage. Keep each to one plain sentence plus a designer example.

#### The case folder students build (replaces Options A/B/C as the series default)
```
[case-name]/                         one plain local folder per project
├── 00-context/                      the context pack, pasted into AI steps first
│   ├── product-and-users.md
│   ├── principle-checks.md          (written in Lesson 4)
│   ├── design-system-notes.md       (added in Lesson 6)
│   ├── accessibility-rules.md
│   └── data-rules.md
├── 01-discover/                     one living .md file per activity, plus sources/
├── 02-define/                       problem-brief.md
├── 03-develop/                      options.md, alignment.md, prototype/
├── 04-deliver/                      test-plan.md, findings.md, handoff.md
├── hub/                             the Experience Hub: one HTML page per activity, plus index.html (started in Lesson 1 from a template, grown every lesson)
└── case-log.md                      the decision log: one line per decision and why
```
**Why this suits AI work:** numbered stage folders keep order; one file per activity gives each AI step a named input; `00-context` is the first thing pasted into every step; short plain-text files are easy to give the AI selectively; and an AI coding tool can open the whole folder as its project. Keep it a plain local folder while an AI tool is writing files; copy to cloud storage afterwards (as the existing lesson already teaches).
The existing lesson's three options (by stage, by file type, by deliverable) become *alternatives students may know about*; the series uses the stage layout because later lessons point to it.

#### Mapping the existing lesson to the new scope
| Existing part | Keep / trim / replace |
|---|---|
| Overview and objective 4: AI-assisted vs AI-generated | **Keep.** It is the throughline |
| Phase 1 Mindset (data, role shift) | **Trim to ~10 minutes.** The series already opens with the market case; keep the 91% / 7-tool data and the split finding (Figma, 36/35/29). **Add the partner message:** designers who wait for a PRD are the most exposed; the series moves them upstream. Say plainly that access to the PO and business varies, and that the workflow still works when it is limited (see the access risk in Lesson 2). The existing role-shift line ("maker to strategist and editor") is the natural place |
| Phase 2 Technical literacy (Markdown, HTML, local folder, three folder options) | **Keep and extend.** Add the terminology list above; replace the three folder options with the case folder |
| Phase 3 CARE prompting + feed forward / context | **Keep, shorten.** Keep feed-forward and context reuse. Keep CARE as a light frame and map it to the series instruction checklist: Context = sections you give; Ask = the task; Rules = use only the provided material, say "unknown", return only your section; Examples = the format wanted |
| Phase 4 Four buckets mapped to five Design Thinking stages | **Replace.** Use the Double Diamond stage map (`assets/diagrams/ai-design-workflow-double-diamond.svg`) as the preview of the series. Move the bucket examples out; the later lessons cover them |
| Phase 5 Build your workflow | **Keep, change the content:** build the case folder, run one instruction against a saved output |
| Activity 1 (stage-mapping canvas) | **Rework** onto the four-stage map, or drop in favour of the folder build |
| Homework | Review after the above |

#### Issues found in the existing lesson (fixed 2026-10-05)
1. ~~Tool brand names in student-facing text~~ **Fixed.** Generic labels only.
2. ~~Private mentee names in the activity notes~~ **Fixed.** The old private-mentee notes and the second assignment (capturing screens for a Design Thinking-era lesson) were removed.
3. ~~Program framing (ux-class, five Design Thinking stages)~~ **Fixed.** Front matter now `program: ai-design-workflow`; content uses the four-stage series map; no Design Thinking dependency.
4. ~~Unverified figures~~ **Fixed.** The McKinsey figure and the "Meet Ari" framing were dropped. Phase 1 now uses the AI + Design 2026 and Figma figures that were checked in this research.
5. ~~Missing partner framing~~ **Fixed.** Phase 1 now carries the partner stance and the honest note about access.
6. ~~Sync rule~~ **Done.** Lesson and slide outline rewritten together (34 slides). **The deck (HTML) has not been rebuilt.** The previous deck is in `slides/_archive/`, so it no longer shows as a deck link. The root-level copy `AI Workflow Deck.html` in the lesson folder and the old `materials/ai-workflow-for-ux-designers-brainstorm.md` are untouched and describe the earlier version.

---

### Lesson 2 — Discover the problem
*Renamed 2026-10-07 from "Align the brief together"; slug was `shape-the-brief`, now `discover-the-problem`. Together with Lesson 3 it forms **module 2 (week 2)**, one slug `discover-the-problem`. The PO rehearsal was removed 2026-10-07 and replaced by a written stakeholder check and peer user interviews (see "Discover without role-play" in the decisions log). The internal activity name "Shape the brief" in `02-method.md` and the hub is unchanged.*
*Slug:* `discover-the-problem`
**Why:** The strongest briefs are shaped by product, business and design together, early, with evidence on the table. This lesson gives designers a way to join that conversation with something concrete, and gives product people a way to say what they need from design.
**By the end, students can:**
1. Start from the business question (a goal, idea or problem), and treat any existing brief or PRD as a good starting point to test together.
2. Use an AI chat tool to prepare for the conversation: questions for the business, assumptions to test, and what evidence exists or is missing (verified against what they actually know).
3. Ask the PO and the business for the outcome, the success metric and its baseline, and record any metric they could not confirm as "assumed".
4. Bring evidence to the table (even a small piece) to earn a say, and write a shared scope that the PO agrees to.
5. Write down what they already believe so it can be tested later.
**Key activity:** Discover-the-problem flow (Investigate pattern, adapted): you gather what exists → AI prepares business questions and assumptions → you verify → you send the written questions to the business or product (a human-only step; the written route works at every access level) → you run peer user interviews in class (see Lesson 3) → AI drafts the scope from your notes → you verify against the notes → you share back and record the agreement status *(to draw)*.
**In class (session 3):** draft the business questions and the assumptions list with AI, check each one against what you actually know, and write the message you will send. **Between sessions:** send it to a real stakeholder (or the nearest person who talks to the business) with a reply date, and record the agreement status in the scope. No role-play: AI never plays the PO and nobody rehearses a PO answer.
**Output:** `## Scope`: business question, outcome, metrics (confirmed or assumed), beliefs, and an **agreement status** (agreed / pending / not available).
**Partner moves taught:** ask early, bring a small piece of evidence, write things down and share them back, and treat the draft as shared property.
**If you are a PO, PM or BA (mixed class, 2026-10-06; reworded 2026-10-07):** you are the person the written questions are written for, so answer them as you would answer a designer: what a useful question looks like, what evidence changes your mind, what a brief must contain for you to sign it. In the peer interviews you interview and are interviewed like everyone else, about your own work. Your own output is the same scope page, from the other side of the table.

#### ⚠️ Access risk: some students cannot reach the PO or the business
Some students truly have no access to the PO or the business. **The default case is now the student's own, so the three access levels below apply to everyone.** The written stakeholder check is the main route for everyone, and a meeting is a bonus. Teach the levels so students know what to do when no reply or meeting is available, and make the workflow work in all three:

| Access level | Situation | What the student does | Agreement status |
|---|---|---|---|
| 1 Full access | Can meet the PO and business | Send the written questions, then take a meeting if offered; share the draft scope back and get agreement | **agreed** |
| 2 Limited access | Can message or reach the PO indirectly (via a lead, PM or account manager) | Send the AI-drafted written questions and an assumptions memo, with a response date. Ask for corrections, not for a full meeting | **pending** until answered |
| 3 No access | Cannot reach the PO or business at all | Build the scope from what exists (the PRD or brief, public company information, product data they can see, colleagues who do talk to the business). Record every outcome and metric as **assumed**. Choose usability measures they control (task success, time, errors, SUS). Flag the scope as unconfirmed in the case log | **not available** |

**Fallback flow step (for limited and no access):** the written route is the default for everyone; at limited or no access, "you send written questions and an assumptions memo" is all there is, with no meeting. The AI drafts both from the student's materials; the student edits and sends them. If nobody replies, the student proceeds on labelled assumptions and carries the risk forward.
**Rules for the AI in this lesson:** it prepares questions and drafts notes. It must **not** play the PO and supply business facts or "typical" metrics. Simulated answers are not evidence (see the synthetic-user finding in `01-research.md` Part 2).
**What the student still gains with no access:** a written, assumption-flagged scope that someone can correct later is better than designing from a brief with the assumptions hidden. It also gives them something to show when they do get a seat.
**Teach this honestly in class:** say plainly that access varies, that having no access is a weaker position, and that the workflow is built to degrade gracefully, not to pretend the problem does not exist. *(⚠️ The access levels are my design, not tested; the Vietnam context is described in `01-research.md` Part 3 with low-confidence sources.)*

### Lesson 3 — Turn research into insights you can trust
*2026-10-07: Lessons 2 and 3 form module 2 (one week, one slug `discover-the-problem`). The peer user interviews run in session 4 and feed the user-voice synthesis below; the interview guide is drafted by AI and checked by the student, and notes are anonymised before AI sees them.*
*Slug:* `research-you-can-trust`
**Why (widened 2026-10-05):** competitor analysis shows what rivals do. It cannot show why users behave as they do, so a Discover built on it alone is the weakest evidence. This lesson pairs two kinds of evidence and keeps the AI honest on both.
**By the end, students can:**
1. Choose evidence types that fit their question from a menu, and always pair **what others do** (competitors, desk research) with **what users say or do** (reviews, forum posts, interviews, tickets, analytics).
2. Run a **user-voice synthesis**: the AI works only from real, anonymised quotes (public reviews and forum posts, plus 3 to 5 short interviews), returns every quote word for word with its ID, and may answer "unclassified" or "unknown".
3. Verify it: trace each top theme to its quotes, confirm they are word for word, read a sample of what the AI left out, count the errors, and decide whether to rerun a step.
4. Weigh themes by severity, context and reach, not by count alone, write opportunity candidates with quote IDs, and state what the sample cannot tell them.
5. Run a competitor analysis as a second activity, and combine both into one evidence pack.
**Key activities:** **User-voice synthesis** is the main in-class activity ✅ (`examples/user-voice-synthesis/`, flow and step cards). **Competitor analysis** is the second ✅ (`examples/competitor-analysis/`): a 20-minute live demo, with the full analysis as optional homework. Interview synthesis, desk research and support tickets are variations of the same flow (swap the source in step 4). *(Assumed split for 90 minutes: user voice about 50, competitor demo about 20, combining the evidence pack and wrap-up about 10, buffer 10. Students use the evidence they already have, anonymised, or a prepared set of quotes. Untested.)*
**Evidence menu (pick by question):**
| Evidence | Tells you | Source type | Watch out for |
|---|---|---|---|
| Competitor analysis | What others do | Public pages | Not why users choose; copying competitors |
| Desk research | What is known | Articles, reports | Invented citations; check each claim against its source |
| Public reviews and forum posts | What users say, at scale | Secondary | Skew to extremes; fake reviews |
| Short interviews (3 to 5) | Why, and past behaviour | Primary | Small sample; polite friends; personal data and consent |
| Support tickets, analytics | Real problems, real behaviour | Internal | Data safety; access; anonymise |
**Data safety applies here:** anonymise before the AI sees any quote (find and replace on your own computer), and keep real-work data private (Lesson 1).
**Output:** `## Evidence` (AI draft and verified) plus `## Themes` / `## Patterns`; the Evidence page in the hub; the evidence pack that feeds the problem brief. Gate checks 1b, 1c (and 2a when the evidence supports an opportunity).

### Lesson 4 — Frame the problem worth solving
*Slug:* `frame-the-problem`
**By the end, students can:**
1. Turn an evidence pack into a ranked list of opportunities (user needs, not features), each linked to its evidence.
2. Turn Nielsen's 10 heuristics (plus any organisation principles) into yes/no principle checks for this product, saved in `00-context/principle-checks.md`.
3. Write testable hypotheses for the solution direction ("we believe X for Y will change Z, and we will know because M") and set the right level for each.
4. Define success using Goals → Signals → Metrics, choosing metrics they can measure before launch.
**Key activity:** Problem brief flow *(to draw)*.
**Output:** the shared problem brief, co-signed by product and business, which becomes the requirement: outcome and success metrics, ranked opportunities, hypotheses, principles to check against.
**Partner move:** walk product and business through the brief and get their agreement before design begins; a PRD, if one is written, is written from this.
**If access is limited or absent (see Lesson 2):** the "agreement" part of the gate cannot be met. Carry the Lesson 2 agreement status into the brief, mark every unconfirmed outcome and metric as **assumed**, and keep the evidence part of the gate fully intact. Students in no access still complete the brief; it is labelled "unconfirmed by business".

### Lesson 5 — Explore ideas and pick a direction
*Slug:* `explore-ideas`
**By the end, students can:**
1. Direct an AI chat tool to generate at least three genuinely different directions from the problem brief and constraints.
2. Select a direction by checking each against the principle checks and the opportunities, and record why the others were set aside.
3. Shape user flows and content with AI drafts they edit and own (no AI-written final copy without review).
**Key activity:** Ideation and flow flow (Generate pattern) *(to draw)*.
**Output:** chosen direction, flow, content model.

### Lesson 6 — Build your first prototype
*Slug:* `build-your-first-prototype`
**Why (split 2026-10-05):** prototyping on a design system takes more than one lesson. This one gets a first working version, built the right way.
**By the end, students can:**
1. Write `00-context/design-system-notes.md` (tokens, components, patterns, do and don't, accessibility rules) in a form an AI coding tool can read, and put the standing rules in a rules file.
2. Set up the prototype project in the case folder: rules file, flow and content model from the previous lesson, and a clear view of what the tool can see and change (agent, connector).
3. Compare a vague instruction with a constrained one on the same screen, and explain the difference. (Detailed specifications, linked design files and stated accessibility requirements improve results; vague instructions give generic layouts.)
4. Build the first version of the main flow, one screen at a time, by checking the files the agent changed, not only its reply, and saving each working state.
5. Judge fidelity, and know the prototype is a reference, not production code.
**Key activity:** Prototype build flow (Generate pattern) *(to draw)*.
**Output:** a first working prototype in `03-develop/prototype/`, design system notes, a rules file, and the first design decisions (D items) in the hub. Gate check 3d (design system used) begins here.
**No design system?** Use a starter system supplied by the instructor or an open design system, with a short note on what was borrowed.
**If you are a PO, PM or BA (2026-10-06):** do not build a design system. Use a ready-made one, point the AI coding tool at it, and ask it to generate templates (screens, patterns) for your flow. You are checking that the prototype matches the requirement and the principle checks, not judging visual craft. Designers in the class do the full design-system notes and rules file. Building a design system from scratch needs high design skill, so it is never asked of non-designers.

### Lesson 7 — Refine and check your design
*Slug:* `refine-and-check`
**Why:** the first version is never the one you test. This lesson extends it, checks it against the system and accessibility, and closes the Develop stage with the alignment check (the former critique-loop lesson is folded in here).
**By the end, students can:**
1. Extend the prototype to states and edge cases (empty, loading, error, success), responsive behaviour and real content, one change at a time, checking changed files and keeping a saved state each time.
2. Run an AI first-pass check against the design system (tokens, components, spacing) and against the accessibility rules (contrast, labels, focus, tap targets), confirming each finding themselves. An AI check is a first pass, not an audit.
3. Fill the hub with design decisions and let its alignment table show decisions with no user need behind them and opportunities no decision serves.
4. Run the principle audit: the AI argues where each decision breaks a principle (Nielsen's 10 plus any organisation principles); decide for each finding to fix, accept as a recorded trade-off, or cut.
5. Run a light alignment check at the end of any activity.
**Key activities:** Refine loop (Generate pattern) *(to draw)*, then the **Alignment check** flow ✅ drafted in `03-quality-and-measurement.md` Part 1 *(to draw)* as a closing block of about 30 minutes. *(Assumed split for 90 minutes: states and content 30, system and accessibility check 20, alignment check on the top three decisions 25, buffer 15. Untested.)*
**Output:** a refined prototype, the alignment table and principle audit in the hub, the decision log updated. Gate checks 3d, 3b, 3c.

### Lesson 8 — Test with real users
*Slug:* `test-with-real-users`
**By the end, students can:**
1. Use AI to prepare a test plan and script from their hypotheses, and explain why AI-simulated users cannot replace real ones.
2. Run a usability test and measure task success, time on task, errors and SUS against a baseline.
3. Verify AI-assisted analysis of findings against raw recordings or notes, and weigh findings by importance rather than frequency.
**Key activity:** Plan-and-read-the-measurement flow (Investigate pattern), pre-launch scope *(to draw)*. **Live in a 90-minute session:** plan and script the test, then peer usability tests in pairs (students test each other's prototypes under the confidentiality ground rules; sanitise if needed). Outside tests are optional homework.
**Output:** findings, updated decision log, updated prototype.

### Lesson 9 — Hand off and measure success
*Slug:* `hand-off-and-measure`
**By the end, students can:**
1. Produce a handoff pack in which the prototype is the reference and the decision log explains the choices, so a developer can build without asking.
2. Write a measurement plan for after launch (what to track, where, when to review) and hand it to the PO, even if they cannot access the data themselves.
3. Describe their own AI workflow results (time per step, error rate, rework) with counts, not impressions.
**Key activity:** Handoff flow *(to draw)*.
**If you are a PO, PM or BA (2026-10-06):** your handoff is the requirement, not the screens. From the hub, write the PRD or user stories with acceptance criteria that point back to the opportunities and decisions, and check them against the problem brief. Keep it as a short variation inside the same lesson, not a second lesson.
**Output:** handoff pack and measurement plan.

### Practice sessions (session B of every module) — practice, no new lesson
*Replaces the separate "studio" sessions of the 12-session draft, 2026-10-07.* No slug and no deck: each module's B session is a coached working session on the student's own case, plus catch-up for anyone behind. A one-page facilitation guide per module (not yet written) lists the exit test for that week:
- **Module 1 (session 2):** case folder, context pack and data rules in place.
- **Module 2 (session 4):** peer interviews done, themes verified, opportunity candidates started (checks 1a to 1c).
- **Module 3 (session 6):** problem brief written (checks 2a to 2d).
- **Module 4 (session 8):** a direction chosen and flows drafted (check 3a).
- **Module 5 (session 10):** first prototype of the main flow built (check 3d).
- **Module 6 (session 12):** prototype refined, peer test run, findings fixed (checks 3b, 3c, 4a, 4b).
- **Module 7 (session 14):** final project (below).
- **Format:** 10-minute check-in (where are you stuck), about 60 minutes of own work in breakout rooms of 3 to 4 with coaching, 20 minutes of live review of two hubs. Homework only continues this work.
- **To do:** write the facilitation guides, and decide whether each B session needs a starter checkpoint folder (the table above names them).

### Session 14 — Final project: present your case
*Was "Lesson 10 — Capstone" until 2026-10-07; now the practice session of module 7 (week 7), with no slug of its own.*
**By the end, students can:**
1. Run the full chain on a real case, each step's output feeding the next, with every gate recorded in the hub.
2. Present the case showing evidence, decisions and trade-offs, so an employer or PO sees the judgement, not just the speed.
3. State which parts of the workflow they would keep, tune, or skip, with reasons from their own measured results.
4. Finish the **Experience Hub**: every output from the case on one connected site, with the cross-links working, so a reader can start from any decision and reach its opportunity, hypothesis, principle, test and metric.
**Output:** the finished Experience Hub (the final report), the complete case folder, and a portfolio piece.

---

