# Quality and Measurement: Alignment and Success Metrics

How to check a solution against what was defined (Part 1) and how to measure success after delivery (Part 2).

**In this file**
- [Part 1 — Traceability and alignment](#part-1--traceability-and-alignment)
- [Part 2 — Measuring design success](#part-2--measuring-design-success)

---

## Part 1 — Traceability and alignment

**Created:** 2026-10-05 · **Status:** my synthesis of established ideas (opportunity solution tree, hypothesis statements, heuristic evaluation with your own principles). The activity flow at the end is a proposal, not yet drawn or tested.

### The problem
AI makes it easy to produce plausible screens, including features nobody asked for. Winnie's rule: every solution must pass the UX principles and outputs defined earlier. That needs a way to **check**, not just a promise.

### Short answer: yes, add three prerequisite outputs, then run an alignment check
The solution can only be cross-checked against things that exist in writing. The Define output is the **shared problem brief**: co-defined with product and business, it becomes the requirement. It contains:

| Prerequisite | What it is | Where it comes from |
|---|---|---|
| **Outcome** | The result the work is meant to move, with a metric or an assumed metric | Agreed with the PO and business when co-defining the requirement, or a stated assumption (see `03-quality-and-measurement.md` Part 2) |
| **Opportunities** | Evidence-backed user needs or pain points worth solving, ranked. Problems, not features | The evidence pack from Discover (e.g. competitor analysis, interviews) |
| **Hypotheses** | A testable bet: "We believe [design decision] for [users] will [change], and we will know because [metric / test result]" | You, after Define, one per major design decision |
| **Principles** | The checks the solution must pass. **Baseline: Nielsen's 10 usability heuristics.** Where the organisation has its own UX, business or service principles, add them as a second layer | Foundation lesson (baseline), the organisation (extra layer, if it exists) |

This is the structure of Teresa Torres' **opportunity solution tree**: desired outcome → opportunities → solutions → assumption tests, which makes every solution traceable to a need and a measurable outcome ([Product Talk](https://www.producttalk.org/glossary-discovery-opportunity-solution-tree/)). Using it keeps the series tool-agnostic and keeps AI-generated extras visible.

### The chain, end to end
```
Outcome → Opportunity → Hypothesis → Design decision → Principle(s) → Test / Metric
```
Every design decision in the prototype must have a line back to an opportunity and forward to a test. A decision with no line back has no user need behind it.

### The alignment check (the cross-check itself)
A matrix in the working file, one row per design decision (a screen, a flow, a component choice):

| Design decision | Opportunity it serves | Hypothesis | Principle(s) it follows | Principle(s) it pulls against | Test or metric |
|---|---|---|---|---|---|

Four checks, which map to "found a problem" signals:
1. **Decisions with no user need behind them:** a decision with no opportunity → remove it, or justify it in writing. (This catches AI-added extras.)
2. **Opportunities no decision serves:** a high-ranked opportunity with no decision → a gap.
3. **Decision pulls against a principle:** the decision conflicts with a principle → fix it, or record a deliberate trade-off with the reason.
4. **Untested hypotheses:** a hypothesis with no usability task or metric → add one before testing.

Principle checking is **heuristic evaluation**, where a product is reviewed against a checklist of principles to give an objective picture of quality and an action list ([uxdesign.cc — measuring design quality with heuristics](https://uxdesign.cc/measuring-design-quality-with-heuristics-44857efa514), [LUMA — heuristic review](https://www.luma-institute.com/heuristic-review/)). The checklist is the **baseline heuristics plus any organisation principles**. Each principle is turned into yes/no questions for the product at hand (the AI may draft these; you approve them), with the reason and anti-patterns (practice from design-principle guidance; secondary source). Large companies often have their own UX, business and service principles for their products; students in those companies use them as the first layer and Nielsen's 10 as the fallback.

### The Experience Hub: where the chain becomes clickable
**The final report of the series is one experience hub** that stores every output of the case and lets the designer cross-reference them. (Defined by Winnie, 2026-10-05.)

**What it holds (one page each, built as the series goes):** Scope · Competitor analysis and other evidence · Problem brief (outcome, opportunities, hypotheses, principle checks) · Options and flows · Prototype link · Alignment table and principle audit · Usability findings · Handoff pack and measurement plan · Case log (decisions).
**What makes it a hub, not a folder of reports:** cross-links.
- Give every **opportunity (O1…), hypothesis (H1…), design decision (D1…), principle check (P1…), test (T1…) and metric (M1…)** a short ID in the working files.
- In the hub, every ID links to where it is defined and to everything that references it. From a decision you can reach its opportunity, hypothesis, principles, test and metric, and back.
- The **alignment table is the hub's spine**: it is the table whose cells are those links, so decisions with no user need behind them and opportunities no decision serves show up as items with missing links.
- An **index page** shows the thread end to end plus gate status and the access/agreement status from Lesson 2 (agreed / pending / not available).
**Template (built 2026-10-05):** `assets/templates/hub/`. Nine linked pages (Overview, Scope, Evidence, Problem brief, Options/flows/prototype, Alignment check, Findings, Handoff and measurement, Case log), a shared stylesheet, an engine script, and one data file (`hub-data.js`) listing every ID and its links. From that file the Overview **builds the alignment table and the warnings itself** (decisions with no user need behind them, opportunities no decision serves, untested hypotheses, a decision pulling against a principle, decisions with no principle, broken links). IDs typed in the page text become links automatically, and each item shows what it connects to. Principles P1 to P10 are pre-filled with Nielsen's 10 heuristics. Robustness (added 2026-10-05): the engine validates `hub-data.js` and each page and shows setup problems in a box at the top instead of failing silently; the example metric is "4 of 5 finish unaided" because five users give counts, not rates. Tested by loading in a browser with good and broken data; not yet used by a student. Known gap: students can clear the warnings by over-linking (for example one principle to every decision), so the principle audit page must still carry the reason for each link. How-to: `assets/templates/hub/README.md`.
**Publishing and sharing (decided 2026-10-05):** designers must be able to show stakeholders their hub. A live link is one way; for confidential work it is not the right one. **Decision (revised again 2026-10-05): the hub is private by default; publishing is optional and only for a case free to share. A student who publishes uses GitHub Pages in their own public repository** (address `https://<username>.github.io/<repo>/`), taught as a short demo in the first lesson with the setup as homework (guide: `assets/templates/publish-guide.md`). The link opens with no login, can be emailed, and the student updates it themselves. **Winnie does not host:** every student hosts their own hub and is responsible for their project and for what they publish. Because most students use their own, often confidential, cases, hubs are private unless the student chooses to publish. The alternatives below are for students who prefer another host than GitHub. The hub is plain static files, so it can go on a free static host by dragging the folder in (Netlify Drop or Cloudflare Pages; steps and privacy limits are in `assets/templates/hub/README.md`). Free hosting is **public to anyone with the link**, and password protection is a paid feature on Netlify ([Netlify Drop password protection, 2026](https://netli.fyi/blog/password-protect-netlify-drop-site)); GitHub Pages only publishes privately on an enterprise plan ([GitHub docs](https://docs.github.com/en/enterprise-cloud@latest/pages/getting-started-with-github-pages/changing-the-visibility-of-your-github-pages-site)); Cloudflare Access can add a free login for up to 50 users but needs more setup ([Cloudflare Pages direct upload](https://developers.cloudflare.com/pages/platform/direct-upload/)). Pricing and limits change, so recheck before teaching. Pages carry a no-index tag. **Confidentiality rule:** each student chooses a case they are free to share and is responsible for what they publish; if a hub cannot be public, the fallback is a PDF export.
**How it is built:** students build it themselves with an AI coding tool, from a provided hub template, by turning each markdown working file into a page and adding the links by ID. One page is added per lesson, so the hub is never a last-minute job. *(⚠️ my design, untested. Risk: non-technical designers may find generating linked pages hard; the template should do the navigation so they only supply content.)*
**Open choices:** a single scrolling page with a sidebar, or a folder of linked pages? (Recommend a folder of linked pages, so each lesson adds one file.)

## Where AI helps, and where it can't
| AI can | You must |
|---|---|
| Draft the matrix by mapping each decision to an opportunity, hypothesis and principle **with a pointer** | Verify every mapping against the brief; "none" must stay "none" |
| Audit the prototype against each principle and **argue where it violates**, not agree | Decide whether a violation is a defect or a deliberate trade-off |
| List decisions with no user need behind them, and opportunities no decision serves | Decide which to cut or add |
| Write the usability tasks for each hypothesis | Run them with real users |

Same rules as the standard (`02-method.md` Part 1): AI uses only the provided brief and principles, may answer "none", and returns only its own section.

### Hypothesis granularity: no standard, so use a rule of thumb
There is no standard unit. Pick by the solution:
- **One opportunity, one solution** → one hypothesis.
- **One solution serving several opportunities** → one hypothesis per opportunity, if you would test or measure them differently; otherwise one hypothesis listing the opportunities.
- **Several small decisions for one opportunity** → one hypothesis for the group, with each decision still listed as a row in the matrix.
The matrix keeps **one row per design decision**; the hypothesis column can repeat or point to a shared hypothesis. Split a hypothesis whenever you would run a different test or read a different metric. *(My rule of thumb, not an industry standard.)*

### Where it lives: the closing block of "Refine and check your design"
**Decided (revised 2026-10-05):** there is no separate critique-loop lesson. The full alignment check (matrix and principle audit, checks 3b and 3c) is the **closing block of the second prototype lesson**, about 30 minutes, and the hub builds the matrix itself, so the manual part is the principle audit and the fix, accept or cut decisions. A light version runs at the last gate of **every** activity (standard rule 12 in `02-method.md` Part 1). Challenging before deciding is already a step in every activity flow, so a standalone critique lesson would repeat it.

### Proposed activity flow: "Alignment check" (Pattern A, adapted; Develop to Deliver)
1. **YOU** list the design decisions in the prototype and confirm the brief (outcome, opportunities, hypotheses, principles)
2. **AI** map each decision to opportunity, hypothesis and principles, with a pointer; "none" allowed → `## Alignment (AI draft)`
3. **YOU** verify the mapping against the brief → `## Alignment (verified)` — **Gate: traceable? any decision without a user need, or any gap?**
4. **AI** audit each decision against each principle and argue where it fails → `## Principle audit`
5. **YOU** decide per finding: fix, accept as a trade-off (with reason), or cut → `## Decisions` — **Gate: could you defend each decision by the brief?**
6. **AI** write a usability task for each hypothesis that lacks one → `## Test plan (draft)`
7. **YOU** edit the test plan so it measures the metrics chosen in Part 2 of `03-quality-and-measurement.md` (task success, time, errors, SUS) — **Gate: measurable before launch?**
If a gate fails: gate 1 → step 2; gate 2 → step 4; gate 3 → step 6.
*(Not yet drawn; 7 steps, 3 gates, within the standard.)*

### How this connects to the other files
- Stage map: the Define output grows from "problem brief" to "problem brief with outcome, opportunities, hypotheses, principles" (diagram needs a small update if you agree).
- Gate by stage (`02-method.md` Part 3): this activity is the concrete form of checks **3b and 3c** of the Develop gate (and 3d for the design system and accessibility).
- Measurement (`03-quality-and-measurement.md` Part 2): the Test column feeds the usability plan and metrics.

### Decided (2026-10-05)
| Question | Answer |
|---|---|
| What are the principles? | Nielsen's 10 heuristics as the baseline; the organisation's own UX, business and service principles as an extra layer where they exist |
| Hypothesis granularity | No standard; depends on the solution (rule of thumb above) |
| Own lesson or part of another? | Part of "Refine and check your design" (closing block); a light check at every activity's last gate |
| Stage map | Define output updated to show outcome, opportunities, hypotheses and principles (done) |

### Still open
1. ~~Is Nielsen's 10 enough when a company has no written principles?~~ **Yes, enough** (decided 2026-10-05).
2. How should students handle conflicts between the organisation's principles and Nielsen's (for example a brand principle that breaks a heuristic)? Suggest: record it as a deliberate trade-off with the reason.


---

## Part 2 — Measuring design success

**Created:** 2026-10-05 · **Confidence:** frameworks (HEART, task metrics, SUS) are well established; how to wire them into the AI workflow is **my synthesis**, untested. Figures marked ⚠️ come from secondary summaries.

### The short answer
Measure on two separate things, and don't mix them:

| | Question | Examples |
|---|---|---|
| **A. Product outcome** | Did the solution work for users and the business? | Task success, time on task, errors, adoption, retention, satisfaction, conversion |
| **B. Workflow quality** | Did the AI-assisted process produce better work, not just faster work? | Time per step, error rate caught at the gates, rework, decisions later reversed |

A can be good while B is bad (lucky), and B good while A is bad (a well-run process aimed at the wrong problem). Teaching both is what makes the series a *system*, not a speed trick.

### A. Product outcome

#### Define success *before* you design (Frame step)
Success criteria belong in step 1 of the workflow, not after delivery. Use **Goals → Signals → Metrics** (from Google's HEART framework): state the goal, pick the signal that would show it, then the number.
Example: Goal "new users finish setup without help" → Signal "they complete onboarding unaided" → Metric "setup completion rate, median time to first success".

#### The HEART categories (pick 2–3, not all five)
Happiness (satisfaction, SUS, NPS) · Engagement (use depth) · Adoption (new users or feature uptake) · Retention (users who return) · Task success (completion, errors, time). Source: [HEART overview (Statsig)](https://statsig.com/perspectives/heart-framework-measuring-ux), [Appcues](https://www.appcues.com/blog/google-improves-user-experience-with-heart-framework). Created at Google (2010) by Rodden, Hutchinson and Fu.

#### Usability basics that work early and cheaply
- **Task success rate** — NN/g calls it the simplest usability metric; the bottom line of usability. General-purpose sites median roughly 78–85% ⚠️ ([Koji summary](https://koji.so/docs/usability-metrics-guide)).
- **Time on task and error rate** — success with three times the expected effort is still poor.
- **SUS (System Usability Scale)** — a 10-question survey; the commonly quoted average is **68**, so above 68 is above average ⚠️ ([MeasuringU](https://measuringu.com/ux-benchmarks/)). Use it to compare releases, not as a verdict.

#### Behavioural + attitudinal
Pair what users **do** (analytics, task results) with what they **say** (surveys, interviews). Either alone misleads.

#### Baseline and timing
- **Capture a baseline before the change** (current task success, time, SUS). Without it you can't claim improvement.
- Separate **leading** signals (usability test results before launch; first-week completion) from **lagging** ones (retention, revenue; weeks to months).
- Attribute carefully: many things change at once after a launch. Use a comparison group or staged rollout where possible.

### B. Measuring the AI workflow itself
- **Time per step**, compared with your own pre-AI baseline for the same activity.
- **Error rate at the gates** (e.g. the step 6 spot-check in competitor analysis). A falling error rate over projects shows better instructions, not just faster output.
- **Rework:** how many steps were rerun after a gate failed; how many insights were thrown away at Gate C.
- **Reversed decisions:** decisions in the decision log later changed because the evidence was weak.
- **Don't trust felt speed.** A METR trial found experienced developers were about 19% *slower* with AI while feeling about 20% faster ⚠️ ([summary](https://radar.zurb.com/article/metr-trial-developers-were-19-slower-with-ai-while-feeling-20-faster)). Designers show a similar gap: 89% say AI makes them faster, only ~58% say quality improves (see `01-research.md` Part 1). Measure with a stopwatch and counts, not impressions.

### Where it fits in the workflow
| Stage | Measurement job | Gate link |
|---|---|---|
| Frame (Define) | Write success criteria as Goals → Signals → Metrics. Record the baseline. These live in the **problem brief** (outcome and success metrics) | Checks 1a and 2c: agreed or marked assumed; each hypothesis has a test and a metric |
| Validate (Deliver) | Run tests with **real users** to get task success, time, errors, SUS. AI may help prepare and analyse, never act as the users | Checks 4a and 4b (see `02-method.md` Part 3, §2) |
| Hand off (Deliver) | Put the metrics and a measurement plan in the handoff: what to track, where, when to review | Check 4c and 4d: can the team actually instrument it? |
| After launch | Review at set dates against baseline and targets; feed learnings into the next Frame | Closes the loop |

### What AI can and can't do here
- **Can:** draft the measurement plan, suggest signals, write survey and test scripts, clean and summarise analytics, spot candidate patterns in open-text feedback (then you verify against raw responses, as in the standard flow).
- **Can't:** replace real users. Synthetic users were found "too shallow to be useful" and too positive ([NN/g via Userbrain](https://userbrain.com/blog/synthetic-users-experiment/)). It also can't tell you which metric the business cares about.

### Proposed activity for the series (activity flow to draw)
**"Plan and read the measurement"** — Pattern A, Investigate, using the standard in `02-method.md` Part 1:
1. Frame: the decision and the goal (YOU)
2. Suggest signals and metrics per goal (AI)
3. Choose 2–3 metrics and set the baseline (YOU) — Gate: tied to the decision? measurable by us?
4. Collect data: test results, analytics export, survey responses (YOU)
5. Analyse against baseline (AI)
6. Verify numbers against the raw data (YOU) — Gate: traceable?
7. Compare, challenge ("what else could explain this change?") (AI)
8. Interpret and decide: keep, iterate, or roll back (YOU) — Gate: evidence, not AI opinion?
*(Not yet drawn or tested.)*

### Decided (2026-10-05, from Winnie)
| Question | Answer | Consequence |
|---|---|---|
| Do students have analytics and real users after launch? | **Mostly no.** They can run usability tests before launch. Some can ask the PO or AI about product metrics afterwards, but usually have no access | **Core = pre-launch usability metrics** (task success, time on task, errors, SUS). Post-launch outcome metrics are background, not taught in depth |
| One framework or a small kit? | **One framework** | Use **Goals → Signals → Metrics** as the spine. From HEART, use only **Task success** and **Happiness** pre-launch. Adoption, Engagement, Retention are "ask the PO to track after launch" |
| Do designers see business metrics? | **Rarely; the PO owns them** | Teach designers to **ask for them actively** (see below), and to state any assumed metric as "assumed, unconfirmed" |

Why Goals → Signals → Metrics rather than HEART as a whole: HEART assumes product analytics. With pre-launch only, the useful part is the discipline of goal → signal → metric plus the usability measures. *(My judgement.)*

### Getting business metrics from the product side
The aim is not to take over product's job but to design with the numbers in view, not from the brief alone. Fold this into the **Shape the brief** activity (Discover/Define) and into Frame (step 1) of every activity.

**Questions to ask product and business (starter kit)**
1. What business outcome is this change meant to move, and what is the number today?
2. What would count as success? Would a 30% result be a success? 29%? (adapted from [UX Planet — KPIs](https://uxplanet.org/kpis-9942c5c4b560))
3. By when will we check, and who looks at the data?
4. Which user behaviour should change if the design works?
5. What would make us stop or roll back?
6. Can you share the current dashboard or last quarter's numbers for this area?

**If the numbers can't be shared yet** (some students have little or no access; the three access access levels are in Lesson 2 of `lesson-details.md`)
- Write the metric as a **stated assumption** in the Scope section: "Assumed: onboarding completion is the success measure. Not yet confirmed with product."
- Fall back to pre-launch proxies the student controls: task success, time on task, errors, SUS.
- Offer something in return: a usability baseline and test results give product evidence they may not have. Bringing numbers is an easy way to start the exchange.
- Frame it as practising a premium skill: the Vietnam salary report names "business mindset" (linking design to ROI and retention) as a pay differentiator, though from a source with no stated method (see `01-research.md` Part 3). Also: [Readymag — why metrics matter to designers](https://blog.readymag.com/a-discipline-for-designers-product-designer-on-why-metrics-matter/) (not read in full).

### Still open
1. Should "Plan and read the measurement" stay a separate activity, or be folded into Validate (usability testing) since students are pre-launch? *(Recommend: fold in, and keep the post-launch part as a short "hand to the PO" step.)*
2. Which usability test format do students actually run (moderated 5-user, unmoderated, guerrilla)? Decides the sample sizes and how much a SUS score is worth.

