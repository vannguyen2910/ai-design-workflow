# Research: Market, Risks, Vietnam, Teaching

The evidence base behind the series. Confidence levels are marked in each part; items marked ⚠️ were not verified at the primary source.

**In this file**
- [Part 1 — Market research](#part-1--market-research)
- [Part 2 — Failure cases and risks](#part-2--failure-cases-and-risks)
- [Part 3 — Vietnam market](#part-3--vietnam-market)
- [Part 4 — Teaching working designers](#part-4--teaching-working-designers)

---

## Part 1 — Market research

**Purpose:** Ground the "AI design workflow for experienced designers" series in what the market is actually doing, before designing the curriculum.
**Researched:** 2026-10-05 · **Status:** First pass (desk research, web only)

> **Read this first — confidence levels.** Numbers below come from surveys and blog summaries, several of them second-hand. Anything marked ⚠️ was not verified at the primary source. Google, Microsoft and Airbnb internal workflows could **not** be found in any citable source, so they are deliberately absent. Don't quote ⚠️ items to students without checking the link.

---

### 1. The big picture (what the market says)

| Finding | Source |
|---|---|
| ~91% of designers use AI weekly (up from ~54%); ~75% daily | Designer Fund / Foundation Capital "AI + Design 2026" report (906 designers, 60+ countries) ⚠️ via secondary summaries |
| Average designer uses **7 AI tools**, up from 3 a year earlier | Same report |
| ~Half of designers have **shipped AI-generated code to production** | Same report |
| **65%** of designers do more PM/engineering tasks; **40%** say PMs/engineers do more design | Same report |
| **43%** of designers say their company expects working prototypes; **36%** say projects now start with them rather than a brief | Foundation Capital write-up |
| **50%** of design leaders now prioritise AI fluency in hiring, then systems thinking and strategy | Designer Fund |
| 89% say AI makes them faster, but only ~58% say it improves quality | Secondary summary of 2026 surveys ⚠️ |
| Figma State of the Designer 2026: 72% use generative AI; AI-in-process is the #2 most-demanded skill (54%), behind visual design (58%) | Figma report ⚠️ (survey run Sep–Oct 2025, so older than the Designer Fund one) |
| 90% say design is at least as important as before AI; nearly 60% say more important | Figma report ⚠️ |
| Only 28% of leaders have updated how designers are evaluated; 73% of designers feel rising output expectations | Designer Fund |
| Collaboration is getting **worse**: 20% (up from 5%) report less teamwork because of AI | Designer Fund |

**What this means for your pitch**
- Your CEO quote is supported: the market is not removing designers, it is *raising the bar* and rewarding AI fluency in hiring.
- The sharper problem is the one you named: designers who only receive a PRD and hand over screens are the most exposed, because "PRD → screens" is exactly what AI compresses. Surveys show the role moving *upstream* (problem framing) and *downstream* (prototype/ship).
- The honest counter-risk: speed is commoditising and quality is not guaranteed. "AI can make weak UX look polished" (Designlab panelist). That is your opening for **principles-gated** workflow, which is the heart of your idea.

### 2. How named companies actually work

#### Spotify — design system as AI infrastructure *(strongest, most concrete)*
- Exposed the Encore design system through an **MCP server** so coding assistants generate against Spotify's standards instead of guessing.
- Rewrote docs as **machine-readable** (machines are treated as equal users of the system).
- Split components into layers (foundations → styles → behaviours; headless components) to cut context complexity for the AI.
- Built a **testing framework** that checks AI-generated UI for visual consistency with Encore.
- Pragmatic target: ~80% coverage at scale, not perfection.
- Principle quoted: design systems "must exist where AI operates, otherwise they get bypassed."
- Source: [Into Design Systems — Spotify](https://www.intodesignsystems.com/use-cases/spotify-design-system)

#### Linear — AI for context, not for taste *(best counter-example to "AI does everything")*
- Design is "a search, not a production pipeline." AI is used to *deepen problem understanding*, not to accelerate output.
- Custom skill interrogates customer requests against Linear's own principles and 40k+ requests to find the underlying need.
- Used for: context gathering, UI refinements, dynamic prototypes for edge cases.
- **Deliberately not used for:** design critique (they want provocation, not agreement), UI copy, major creative decisions.
- Rules of thumb: *gather context, not opinions · make AI argue against you · define success before building · ask for explanations while building.*
- One designer uses AI on only ~20–30% of new work.
- Source: [Designer Fund — Inside design at Linear](https://designerfund.substack.com/p/ai-design-linear)

#### Shopify — prototype-first, platform not policy
- Standardises infrastructure (central LLM gateway, internal MCP servers, a "Quick" tool for non-engineers to deploy small apps) rather than mandating one tool.
- Screenshots → AI prototype → faster feedback before the full team invests.
- ~20% productivity gain, mostly from *faster prototyping and exploring more approaches*, not from raw code volume. Human review still gates code merges.
- "Code is cheap now" — the scarce thing is the right solution.
- Source: [Bessemer — Inside Shopify's AI-first playbook](https://www.bvp.com/atlas/inside-shopifys-ai-first-engineering-playbook)

#### Figma — the tool vendor shaping the default workflow
- Positioning has moved from "AI inside the canvas" to **AI agents working inside your design system's constraints**: MCP server passes components, variables and Code Connect mappings to coding agents; "skills" (markdown instruction files) define how agents behave; rules files encode tokens, components, naming.
- Recommended loop: audit design↔code alignment → generate code that follows patterns → automate token usage → document via Code Connect.
- Sources: [Figma — design systems & AI MCP](https://www.figma.com/blog/design-systems-ai-mcp/) · [Figma — State of the Designer 2026](https://www.figma.com/reports/state-of-the-designer-2026/)

#### Others mentioned but thin
- **Sierra** (scaling design systems with 100+ engineers), **Stripe** (culture of adoption, no rigid playbook), **Notion**, **Framer**, **Anthropic** appear as case studies in the State of AI Design report; several were "coming soon" and I could not read them. Worth reading in full at [stateofaidesign.com](https://stateofaidesign.com).
- **Atlassian, Airbnb:** search summaries claim AI-assisted design→prototype workflows, but I found no primary source. ⚠️ Treat as unverified.

### 3. The prototyping workflow pattern (cross-company)

From [Lenny's Newsletter — getting your whole team prototyping](https://www.lennysnewsletter.com/p/how-to-get-your-entire-team-prototyping) and the AI-native product design literature:

| Stage | Who prototypes | Fidelity | Note |
|---|---|---|---|
| Discovery | PM + designer | Medium, ~20 min | Express idea internally |
| User testing | Often PM | Medium | Test with real users |
| Stakeholder review | Designer | High | Polished for execs |
| Engineering handoff | Designer | Interactive reference | Replaces static spec |
| Iteration | Everyone | Fork the baseline | Don't rebuild from scratch |

Key lessons: set fidelity expectations early; keep a **shared component library** so prototypes look like the real product; use screenshots → extension → production code as three levels of design-system fidelity; **AI prototypes are not production code.**

### 4. Patterns that repeat across companies

1. **Design system / principles become the control layer.** Spotify, Figma and the AI-native literature all say the same thing: AI output is only as aligned as the context it is given. *This directly validates your "every idea must pass our UX principles and defined outputs" idea.*
2. **Context in, judgment out.** Linear's strongest rule: use AI to gather context and argue against you, keep taste and decisions human.
3. **Prototype replaces the spec.** Working prototypes are expected earlier and increasingly *start* projects.
4. **Roles blur toward "builder".** Design engineers, designers shipping code, PMs designing.
5. **Infrastructure over tools.** Shopify and Spotify invest in shared gateways, MCP servers and guardrails rather than picking a favourite tool.
6. **Known failure modes:** tool sprawl (7 tools, no standard), messier collaboration, polished-but-weak UX, skill atrophy, no updated performance criteria.

### 5. Gaps in the market = your opening

| Gap | Evidence | What your series could do |
|---|---|---|
| Everyone teaches tools or prompts | Tool-count rising, "nearly half still searching for go-to tools" | Teach a **system**: each step's output is the next step's input |
| Quality gate is informal | "Speed up, quality not guaranteed" | Make UX principles + outputs an explicit **gate** between steps |
| Non-technical designers can't reach the "builder" role | Half of designers ship code, but mostly design engineers | Prototype with AI **without needing engineering skills** |
| Teams lack process updates | 28% of leaders updated evaluation | Teach how to *show* AI-era value to employers |
| Vietnam-specific context | I found only generic market stats (demand growing; salaries up) and no data on PRD-handoff-only roles ⚠️ | Validate with your own network: interview 5–8 designers/hiring managers |

### 6. Draft workflow (superseded)
*This section held my first six-stage draft diagram. It is replaced by the stage map (`assets/diagrams/ai-design-workflow-double-diamond.svg`) and the single gate list in `02-method.md` Part 3, §2. Removed 2026-10-05 so there is only one version of the workflow.*

### 7. Open questions from this first pass (answered)
| Question | Answer (see `00-plan.md`; the full dated decisions are in `_archive/00-plan-full-2026-10-07.md`) |
|---|---|
| Student profile | Mid and senior designers |
| Tool-agnostic? | Yes: generic labels only |
| Prototype depth | No code written by the student; an AI coding tool builds it |
| Evidence for Vietnam | Still thin; see Part 3 and the validation plan there |

---

## Part 2 — Failure cases and risks

**Researched:** 2026-10-05 · Why this matters: each risk below should become a **checkpoint** in the workflow, not just a warning slide.

| Risk | Evidence | Where it shows up | Workflow countermeasure |
|---|---|---|---|
| **Satisficing / polished but weak** | "AI can make weak UX look polished" (Designlab panelist); satisficing is "the default" without checkpoints ([uxdesign.cc](https://uxdesign.cc/89755c86869b)) | Prototype | Principle gate before showing anyone |
| **Generic, repetitive output** | NN/g found repetitive layouts and weak solution diversity; vague prompts → generic layouts ([NN/g](https://www.nngroup.com/articles/testing-ai-methodology)) | Shape, Prototype | Feed outputs and design system; require 3 genuinely different directions |
| **Accessibility gaps** | NN/g: not reliably met unless mandated | Prototype | State a11y as a requirement in the context pack |
| **Frequency mistaken for importance** | Parallel HQ | Explore | Human weighting step; hunt for outliers |
| **Synthetic users too agreeable** | NN/g, UXAgent (CHI 2025) | Validate | Use only to prepare; real users are the gate |
| **Critique drifts to polish** | Designative | Validate, Critique | Anchor critique in the problem brief |
| **Deskilling / cognitive offloading** | Qualitative analysis of 120+ UX subreddit posts raised over-reliance and erosion of critical skills (arXiv 2503.03924). Wider: a 45-person study on "prompt dependency" and, in medicine, doctors' adenoma detection fell from 28.4% to 22.4% without AI after routine AI use ⚠️ secondary reports | All stages | Keep "do it by hand first" reps; Linear's 20–30% usage as a norm |
| **Collaboration degrades** | Designer Fund: 20% report less teamwork (up from 5%); 33% messier collaboration | Whole team | Decision log; shared prototypes, not private chats |
| **Tool sprawl** | 7 tools per designer; nearly half still searching for a go-to tool | Whole workflow | Tool-agnostic stages; a small standard core |
| **Expectations rise, evaluation doesn't** | 73% of designers feel higher expectations; only 28% of leaders updated evaluation | Career | Teach how to evidence value (lesson 9) |
| **Responsibility ambiguity** | arXiv 2503.03924 on "misplaced responsibilities" | Hand off | Name an owner for every AI-assisted decision in the log |

### Evidence quality
- The deskilling paper analyses Reddit posts, so it shows *what practitioners worry about*, not measured loss of skill. The medical example is a different field. Present both as "plausible risk", not as proven for designers.
- NN/g findings come through summaries; read the originals before quoting.

### Teaching implication
Build a **"verify" move into every stage** (trace to source, argue back, test with real people) so the risks are practised, not just listed. This is also the strongest answer to a student who asks "what do I still do that AI can't?"


---

## Part 3 — Vietnam market

**Researched:** 2026-10-05 · **Confidence: low.** Everything here is from local blogs, training academies and job-board aggregates. Nothing is a rigorous survey. Treat as leads to validate, not facts for slides.

### What the sources say
- **Salary bands (2026, monthly, VND millions)** per Telos Academy citing UIUXJobsBoard, with no sample size or method stated ([Telos](https://academy.telos.vn/bao-cao-muc-luong-uiux-product-designer-tai-vn/)):

| Role | Junior (1–3y) | Mid (3–5y) | Senior (6–9y) | Lead+ |
|---|---|---|---|---|
| UI/UX Designer | 16–21 | 21–31 | 36–51 | 51+ |
| Product Designer | 17–22 | 22–37 | 37–52 | 52+ |

- Same source: premium pay goes to **AI orchestration, business mindset, domain expertise (fintech, healthtech, B2B SaaS) and English**. It claims AI is "displacing execution-focused designers," and cites emerging roles with 25–30% salary premiums. ⚠️ unverified.
- A Vietnamese blog claims the old flow "PRD → wireframe in Figma → send static screens → wait a week for approval" is being replaced by "PRD → analysis with an LLM → prototype blueprint → client tries it immediately", especially at outsourcing firms. ⚠️ opinion, not data (snippet from search results, [TELOS Academy](https://academy.telos.vn/ai-va-ui-ux-co-bi-thay-the/); I did not open the page).
- Same body of writing warns of the **"factory-style" risk**: companies wanting designers to "press buttons in AI tools". That supports your argument for teaching judgment and system, not tool operation.
- Tuổi Trẻ (June 2025) is generic: AI as an accelerator, "creativity of humans remains irreplaceable"; no local company names or numbers ([Tuổi Trẻ](https://tuoitre.vn/ai-tao-sinh-ho-tro-nha-thiet-ke-trong-nganh-ui-ux-20250610111512323.htm)).
- Other search snippets claimed the Vietnam design market grew 35% in 2025 and salaries rose 18–22%; I couldn't trace these to a primary source. ⚠️ Don't quote.

### What I could not find
- Any data on how many Vietnamese designers work in a **PRD-handoff-only** setup.
- How Vietnamese outsourcing firms or product companies actually restructure design work around AI.
- Whether local employers now list AI skills in job posts, and which ones.

### Access to the PO and business (Winnie, 2026-10-05)
Some students truly have **no access** to the PO or the business, and designers rarely see business metrics (the PO owns them). The series is built to work in three access levels (full, limited, none); see Lesson 2 in `00-plan.md` Part 2. Worth asking in the interviews below how often designers are invited to requirement discussions.

### Validation plan (needs you)
Short interviews (20 min each), 5–8 people:
1. Mid/senior designers at product companies and at outsourcing firms.
2. 2–3 hiring managers or design leads.

Questions: What does your day look like from PRD to handoff? What do you use AI for today and what do you refuse to use it for? What would you pay to learn? What skill is your employer asking for that you lack?
These interviews could also become your first **testimonial and needs-analysis evidence**, but get permission before using names.


---

## Part 4 — Teaching working designers

**Researched:** 2026-10-05 · **Confidence: low.** My search returned mostly generic university and L&D workshop listings, not evidence on what works for experienced designers. The notes below are **hypotheses drawn from the other research files**, to be tested in your first cohort.

### What the search did support
- General adult-learning guidance for AI courses: hands-on practice contextualised to the learner's job beats lectures, and groups should cover benefits, threats and barriers before integrating tools. Sources were workshop listings, not studies.

### Hypotheses for the series (derived, not proven)
1. **One real work case across the whole series.** The chain only proves itself if output n becomes input n+1 on the same project. Supports the "repeatable workflow" outcome.
2. **Teach the gate, not the tool.** NN/g found tool capability "jagged" and changing; the verification habits (trace to source, argue back, test with real users) don't expire.
3. **"Do it by hand first" reps** to counter deskilling (see `03`). Mid/senior designers already have the baseline to compare AI output against.
4. **Make students write their own principles in lesson 0.** It forces ownership and gives the gate something concrete to check. Matches Linear's "define success before building".
5. **Show failure live.** Run a vague prompt and a constrained prompt on the same task (NN/g's method) so students see why constraints matter.
6. **Peer critique over solo prompting.** Designer Fund reports AI makes work more solitary; the class can restore review.
7. **Keep the Vietnamese/English code-switching style** from your writing-style guide for scripts. Not a research finding, just a reminder.

### Failure modes of existing AI design courses (my read, unverified ⚠️)
Tool-of-the-month tutorials, prompt template lists, no through-line project, no quality gate. Worth checking by sampling 5 competitor syllabi (global and Vietnamese).

### Next step
Sample 5 competing course syllabi and list what each teaches and omits. That gives an evidence base for the "what makes this series different" claim.

