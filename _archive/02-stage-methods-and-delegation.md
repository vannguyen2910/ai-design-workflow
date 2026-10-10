# Stage-by-Stage Methods: What to Delegate, What to Keep

**Researched:** 2026-10-05 · Builds on the six-stage draft in `01-market-research.md` §6.
**Confidence:** Research and prototyping stages have decent sources. Frame, Shape and Handoff rest mostly on practitioner blogs and my synthesis. ⚠️ marks the weakest claims.

## 1. Evidence by stage

### Frame (PRD → problem brief)
- AI produces convincing problem statements in seconds, "but it takes a person to notice when the statement is pointing the wrong way." AI doesn't resist jumping to solutions. ([Parallel HQ](https://www.parallelhq.com/blog/ai-assisted-ux-research-workflow), [LogRocket](https://blog.logrocket.com/ux-design/state-of-ai-for-ux-design))
- Linear's pattern is the best model: a custom skill **interrogates a request against the team's own principles and customer data to find the underlying need**, rather than accepting the surface ask. Rules: gather context, not opinions; make AI argue against you; define success before building. ([Designer Fund — Linear](https://designerfund.substack.com/p/ai-design-linear))
- ⚠️ Teaching implication: this is where a PRD-only designer gains the most (challenging the brief), and it needs the least tooling.

### Explore (research and options)
- AI is useful for cleaning data, transcribing, clustering and tagging. It is weak at importance: "A minor visual bug might get mentioned 20 times because it is obvious" while critical issues appear rarely. Frequency isn't weight. ([Parallel HQ](https://www.parallelhq.com/blog/ai-assisted-ux-research-workflow))
- NN/g tested LLM synthesis tools: several research steps benefit, but "analysis and synthesis consistently falls short", producing insight-shaped output. Their 2025 testing is summarised in secondary sources, not read directly. ⚠️
- Verification habits that work: trace every finding back to a raw quote or recording; ask for counterexamples and hesitations; hunt for outliers the algorithm smoothed over.

### Shape (flows, IA, content)
- NN/g tested design, code-based and chatbot tools on two real scenarios: simple pages came out fine, **complex multi-step flows (a bulk-purchase flow) were much harder**; layouts were repetitive and "solution diversity" and "creative judgment" fell short. ([NN/g — Real Design Scenarios](https://www.nngroup.com/articles/testing-ai-methodology))
- Linear deliberately keeps AI **out of** UI copy and messaging.
- ⚠️ Implication: AI drafts options; the designer chooses and writes final content.

### Prototype
- NN/g: detailed specs improved results; **linking to existing design files held the visual language**; vague prompts gave generic layouts; **accessibility wasn't reliably met unless mandated**. Recommends controlled, repeatable testing of prompts, and design artifacts rather than text alone as input.
- Cross-company pattern (Spotify, Figma, Shopify in `01`): design system and tokens act as the guardrail; AI prototypes are not production code.
- Fidelity ladder (Lenny's Newsletter): screenshots → library extension → production code, each higher fidelity.

### Validate
- Synthetic users: NN/g found them "too shallow to be useful" against three real studies and overly positive and cooperative (a synthetic persona claimed it completed all courses). A 2025 CHI paper (UXAgent) found AI agents followed neat paths while real users wandered and gave up. Defensible use: **prepare and catch obvious issues, never replace real testing.** ([Userbrain](https://userbrain.com/blog/synthetic-users-experiment/), [PM Toolkit](https://pmtoolkit.ai/learn/experimentation/synthetic-users-promise-and-trap))
- AI moderators can't see behaviour beyond spoken words.
- Linear avoids AI for design critique because designers need provocation, not affirmation. A good use is making AI *argue against* the design.
- Critique risk: AI prototypes pull critique toward surface polish; anchor critique in vision and problem framing. ([Designative](https://www.designative.info/2025/11/10/rethinking-design-critiques-in-the-age-of-ai-prototyping/))

### Hand off
- ⚠️ Thinnest area. Sources describe the interactive prototype replacing the static spec, plus Code Connect and rules files at Figma, but I found no strong source on **decision logs** or acceptance notes. The decision log is my proposal, not a market practice.

## 2. Proposed gate by stage (the "mix by stage" decision)

| Stage | Gate | Question the student must answer before moving on |
|---|---|---|
| 1 Frame | **Evidence + stakeholder intent** | Is this the right problem, and what would change my mind? |
| 2 Explore | **Evidence** | Is each insight traceable to a raw source? Did I look for counterexamples? |
| 3 Shape | **UX principles** | Does each flow and content decision map to a principle I wrote down in the Foundation? |
| 4 Prototype | **Alignment + principles + design system + a11y** | Does every decision trace to an evidenced opportunity and a hypothesis, and pass Nielsen's 10 plus any organisation principles? Same tokens and components? Accessibility stated as requirements? |
| 5 Validate | **Real users** | Did real people confirm it? (AI may prepare; it cannot be the evidence.) |
| 6 Hand off | **Buildability** | Could a developer build this without asking me? |

The shift from evidence → principles → evidence → buildability is what "mix by stage" looks like. It answers the weakness of a single gate (principles can't judge whether a problem is real).

## 3. Draft series skeleton (8–10 lessons) — superseded by `10-series-skeleton.md`
*(Kept for history. The current names and learning objectives are in `10-series-skeleton.md`.)*

| # | Lesson | Output artifact (feeds next) |
|---|---|---|
| 0 | Foundation: your constraint layer | Principles + project context pack |
| 1 | Frame: challenge the PRD | Problem brief |
| 2 | Explore: research with AI, verify the AI | Evidence-backed opportunity map |
| 3 | Shape: flows and content | Flow + content model |
| 4 | Prototype I: build on your design system | First working prototype |
| 5 | Prototype II: critique loop **with the alignment check** (make AI argue back; trace every decision to the brief) | Revised prototype + alignment matrix + critique log |
| 6 | Validate: prepare with AI, prove with people | Findings + decision log |
| 7 | Hand off: prototype as spec | Handoff pack |
| 8 | Capstone: run the full chain on a real work case | Complete project |
| 9 (optional) | Show your value: portfolio and team rollout | Portfolio piece, team playbook |

The existing `ai-workflow-for-ux-designers` lesson is not yet mapped onto this. It should be read before any restructuring (see `course-restructure` skill and the lesson-sync rule in CLAUDE.md).

## 4. Gaps to close next
- Primary sources for Frame and Hand off.
- Read the NN/g articles directly (the figures above come through summaries).
- Hear from 3–5 practising mid/senior designers about what they refuse to delegate.
