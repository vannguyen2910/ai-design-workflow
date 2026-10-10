# Measuring Design Success After Delivery

**Created:** 2026-10-05 · **Confidence:** frameworks (HEART, task metrics, SUS) are well established; how to wire them into the AI workflow is **my synthesis**, untested. Figures marked ⚠️ come from secondary summaries.

## The short answer
Measure on two separate things, and don't mix them:

| | Question | Examples |
|---|---|---|
| **A. Product outcome** | Did the solution work for users and the business? | Task success, time on task, errors, adoption, retention, satisfaction, conversion |
| **B. Workflow quality** | Did the AI-assisted process produce better work, not just faster work? | Time per step, error rate caught at the gates, rework, decisions later reversed |

A can be good while B is bad (lucky), and B good while A is bad (a well-run process aimed at the wrong problem). Teaching both is what makes the series a *system*, not a speed trick.

## A. Product outcome

### Define success *before* you design (Frame step)
Success criteria belong in step 1 of the workflow, not after delivery. Use **Goals → Signals → Metrics** (from Google's HEART framework): state the goal, pick the signal that would show it, then the number.
Example: Goal "new users finish setup without help" → Signal "they complete onboarding unaided" → Metric "setup completion rate, median time to first success".

### The HEART categories (pick 2–3, not all five)
Happiness (satisfaction, SUS, NPS) · Engagement (use depth) · Adoption (new users or feature uptake) · Retention (users who return) · Task success (completion, errors, time). Source: [HEART overview (Statsig)](https://statsig.com/perspectives/heart-framework-measuring-ux), [Appcues](https://www.appcues.com/blog/google-improves-user-experience-with-heart-framework). Created at Google (2010) by Rodden, Hutchinson and Fu.

### Usability basics that work early and cheaply
- **Task success rate** — NN/g calls it the simplest usability metric; the bottom line of usability. General-purpose sites median roughly 78–85% ⚠️ ([Koji summary](https://koji.so/docs/usability-metrics-guide)).
- **Time on task and error rate** — success with three times the expected effort is still poor.
- **SUS (System Usability Scale)** — a 10-question survey; the commonly quoted average is **68**, so above 68 is above average ⚠️ ([MeasuringU](https://measuringu.com/ux-benchmarks/)). Use it to compare releases, not as a verdict.

### Behavioural + attitudinal
Pair what users **do** (analytics, task results) with what they **say** (surveys, interviews). Either alone misleads.

### Baseline and timing
- **Capture a baseline before the change** (current task success, time, SUS). Without it you can't claim improvement.
- Separate **leading** signals (usability test results before launch; first-week completion) from **lagging** ones (retention, revenue; weeks to months).
- Attribute carefully: many things change at once after a launch. Use a comparison group or staged rollout where possible.

## B. Measuring the AI workflow itself
- **Time per step**, compared with your own pre-AI baseline for the same activity.
- **Error rate at the gates** (e.g. the step 6 spot-check in competitor analysis). A falling error rate over projects shows better instructions, not just faster output.
- **Rework:** how many steps were rerun after a gate failed; how many insights were thrown away at Gate C.
- **Reversed decisions:** decisions in the decision log later changed because the evidence was weak.
- **Don't trust felt speed.** A METR trial found experienced developers were about 19% *slower* with AI while feeling about 20% faster ⚠️ ([summary](https://radar.zurb.com/article/metr-trial-developers-were-19-slower-with-ai-while-feeling-20-faster)). Designers show a similar gap: 89% say AI makes them faster, only ~58% say quality improves (see `01-market-research.md`). Measure with a stopwatch and counts, not impressions.

## Where it fits in the workflow
| Stage | Measurement job | Gate link |
|---|---|---|
| Frame (Define) | Write success criteria as Goals → Signals → Metrics. Record the baseline. These live in the **problem brief** (outcome and success metrics) | Gate: are the metrics tied to the decision? |
| Validate (Deliver) | Run tests with **real users** to get task success, time, errors, SUS. AI may help prepare and analyse, never act as the users | Real users gate (see `02-stage-methods-and-delegation.md`) |
| Hand off (Deliver) | Put the metrics and a measurement plan in the handoff: what to track, where, when to review | Buildability gate: can the team actually instrument it? |
| After launch | Review at set dates against baseline and targets; feed learnings into the next Frame | Closes the loop |

## What AI can and can't do here
- **Can:** draft the measurement plan, suggest signals, write survey and test scripts, clean and summarise analytics, spot candidate patterns in open-text feedback (then you verify against raw responses, as in the standard flow).
- **Can't:** replace real users. Synthetic users were found "too shallow to be useful" and too positive ([NN/g via Userbrain](https://userbrain.com/blog/synthetic-users-experiment/)). It also can't tell you which metric the business cares about.

## Proposed activity for the series (Level 2 flow to draw)
**"Plan and read the measurement"** — Archetype A, Investigate, using the standard in `06-activity-flow-standard.md`:
1. Frame: the decision and the goal (YOU)
2. Suggest signals and metrics per goal (AI)
3. Choose 2–3 metrics and set the baseline (YOU) — Gate: tied to the decision? measurable by us?
4. Collect data: test results, analytics export, survey responses (YOU)
5. Analyse against baseline (AI)
6. Verify numbers against the raw data (YOU) — Gate: traceable?
7. Compare, challenge ("what else could explain this change?") (AI)
8. Interpret and decide: keep, iterate, or roll back (YOU) — Gate: evidence, not AI opinion?
*(Not yet drawn or tested.)*

## Decided (2026-10-05, from Winnie)
| Question | Answer | Consequence |
|---|---|---|
| Do students have analytics and real users after launch? | **Mostly no.** They can run usability tests before launch. Some can ask the PO or AI about product metrics afterwards, but usually have no access | **Core = pre-launch usability metrics** (task success, time on task, errors, SUS). Post-launch outcome metrics are background, not taught in depth |
| One framework or a small kit? | **One framework** | Use **Goals → Signals → Metrics** as the spine. From HEART, use only **Task success** and **Happiness** pre-launch. Adoption, Engagement, Retention are "ask the PO to track after launch" |
| Do designers see business metrics? | **Rarely; the PO owns them** | Teach designers to **ask for them actively** (see below), and to state any assumed metric as "assumed, unconfirmed" |

Why Goals → Signals → Metrics rather than HEART as a whole: HEART assumes product analytics. With pre-launch only, the useful part is the discipline of goal → signal → metric plus the usability measures. *(My judgement.)*

## Getting business metrics when the PO owns them
The aim is not to take over the PO's job but to stop designing from the PRD alone. Fold this into the **co-define the requirement** activity (Discover/Define) and into Frame (step 1) of every activity.

**Questions to ask the PO (starter kit)**
1. What business outcome is this change meant to move, and what is the number today?
2. What would count as success? Would a 30% result be a success? 29%? (adapted from [UX Planet — KPIs](https://uxplanet.org/kpis-9942c5c4b560))
3. By when will we check, and who looks at the data?
4. Which user behaviour should change if the design works?
5. What would make us stop or roll back?
6. Can you share the current dashboard or last quarter's numbers for this area?

**If the PO can't or won't share** (some students have no access at all; the three access tiers are in Lesson 2 of `10-series-skeleton.md`)
- Write the metric as a **stated assumption** in the Scope section: "Assumed: onboarding completion is the success measure. Not confirmed by PO."
- Fall back to pre-launch proxies the student controls: task success, time on task, errors, SUS.
- Offer something in return: a usability baseline and test results give the PO evidence they don't have. Designers who bring numbers get invited to the numbers.
- Frame it as practising a premium skill: the Vietnam salary report names "business mindset" (linking design to ROI and retention) as a pay differentiator, though from a source with no stated method (see `04-vietnam-market.md`). Also: [Readymag — why metrics matter to designers](https://blog.readymag.com/a-discipline-for-designers-product-designer-on-why-metrics-matter/) (not read in full).

## Still open
1. Should "Plan and read the measurement" stay a separate activity, or be folded into Validate (usability testing) since students are pre-launch? *(Recommend: fold in, and keep the post-launch part as a short "hand to the PO" step.)*
2. Which usability test format do students actually run (moderated 5-user, unmoderated, guerrilla)? Decides the sample sizes and how much a SUS score is worth.
