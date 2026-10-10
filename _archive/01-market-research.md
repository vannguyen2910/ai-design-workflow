# AI Design Workflow — Market Research

**Purpose:** Ground the "AI design workflow for experienced designers" series in what the market is actually doing, before designing the curriculum.
**Researched:** 2026-10-05 · **Status:** First pass (desk research, web only)

> **Read this first — confidence levels.** Numbers below come from surveys and blog summaries, several of them second-hand. Anything marked ⚠️ was not verified at the primary source. Google, Microsoft and Airbnb internal workflows could **not** be found in any citable source, so they are deliberately absent. Don't quote ⚠️ items to students without checking the link.

---

## 1. The big picture (what the market says)

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

## 2. How named companies actually work

### Spotify — design system as AI infrastructure *(strongest, most concrete)*
- Exposed the Encore design system through an **MCP server** so coding assistants generate against Spotify's standards instead of guessing.
- Rewrote docs as **machine-readable** (machines are treated as equal users of the system).
- Split components into layers (foundations → styles → behaviours; headless components) to cut context complexity for the AI.
- Built a **testing framework** that checks AI-generated UI for visual consistency with Encore.
- Pragmatic target: ~80% coverage at scale, not perfection.
- Principle quoted: design systems "must exist where AI operates, otherwise they get bypassed."
- Source: [Into Design Systems — Spotify](https://www.intodesignsystems.com/use-cases/spotify-design-system)

### Linear — AI for context, not for taste *(best counter-example to "AI does everything")*
- Design is "a search, not a production pipeline." AI is used to *deepen problem understanding*, not to accelerate output.
- Custom skill interrogates customer requests against Linear's own principles and 40k+ requests to find the underlying need.
- Used for: context gathering, UI refinements, dynamic prototypes for edge cases.
- **Deliberately not used for:** design critique (they want provocation, not agreement), UI copy, major creative decisions.
- Rules of thumb: *gather context, not opinions · make AI argue against you · define success before building · ask for explanations while building.*
- One designer uses AI on only ~20–30% of new work.
- Source: [Designer Fund — Inside design at Linear](https://designerfund.substack.com/p/ai-design-linear)

### Shopify — prototype-first, platform not policy
- Standardises infrastructure (central LLM gateway, internal MCP servers, a "Quick" tool for non-engineers to deploy small apps) rather than mandating one tool.
- Screenshots → AI prototype → faster feedback before the full team invests.
- ~20% productivity gain, mostly from *faster prototyping and exploring more approaches*, not from raw code volume. Human review still gates code merges.
- "Code is cheap now" — the scarce thing is the right solution.
- Source: [Bessemer — Inside Shopify's AI-first playbook](https://www.bvp.com/atlas/inside-shopifys-ai-first-engineering-playbook)

### Figma — the tool vendor shaping the default workflow
- Positioning has moved from "AI inside the canvas" to **AI agents working inside your design system's constraints**: MCP server passes components, variables and Code Connect mappings to coding agents; "skills" (markdown instruction files) define how agents behave; rules files encode tokens, components, naming.
- Recommended loop: audit design↔code alignment → generate code that follows patterns → automate token usage → document via Code Connect.
- Sources: [Figma — design systems & AI MCP](https://www.figma.com/blog/design-systems-ai-mcp/) · [Figma — State of the Designer 2026](https://www.figma.com/reports/state-of-the-designer-2026/)

### Others mentioned but thin
- **Sierra** (scaling design systems with 100+ engineers), **Stripe** (culture of adoption, no rigid playbook), **Notion**, **Framer**, **Anthropic** appear as case studies in the State of AI Design report; several were "coming soon" and I could not read them. Worth reading in full at [stateofaidesign.com](https://stateofaidesign.com).
- **Atlassian, Airbnb:** search summaries claim AI-assisted design→prototype workflows, but I found no primary source. ⚠️ Treat as unverified.

## 3. The prototyping workflow pattern (cross-company)

From [Lenny's Newsletter — getting your whole team prototyping](https://www.lennysnewsletter.com/p/how-to-get-your-entire-team-prototyping) and the AI-native product design literature:

| Stage | Who prototypes | Fidelity | Note |
|---|---|---|---|
| Discovery | PM + designer | Medium, ~20 min | Express idea internally |
| User testing | Often PM | Medium | Test with real users |
| Stakeholder review | Designer | High | Polished for execs |
| Engineering handoff | Designer | Interactive reference | Replaces static spec |
| Iteration | Everyone | Fork the baseline | Don't rebuild from scratch |

Key lessons: set fidelity expectations early; keep a **shared component library** so prototypes look like the real product; use screenshots → extension → production code as three levels of design-system fidelity; **AI prototypes are not production code.**

## 4. Patterns that repeat across companies

1. **Design system / principles become the control layer.** Spotify, Figma and the AI-native literature all say the same thing: AI output is only as aligned as the context it is given. *This directly validates your "every idea must pass our UX principles and defined artifacts" idea.*
2. **Context in, judgment out.** Linear's strongest rule: use AI to gather context and argue against you, keep taste and decisions human.
3. **Prototype replaces the spec.** Working prototypes are expected earlier and increasingly *start* projects.
4. **Roles blur toward "builder".** Design engineers, designers shipping code, PMs designing.
5. **Infrastructure over tools.** Shopify and Spotify invest in shared gateways, MCP servers and guardrails rather than picking a favourite tool.
6. **Known failure modes:** tool sprawl (7 tools, no standard), messier collaboration, polished-but-weak UX, skill atrophy, no updated performance criteria.

## 5. Gaps in the market = your opening

| Gap | Evidence | What your series could do |
|---|---|---|
| Everyone teaches tools or prompts | Tool-count rising, "nearly half still searching for go-to tools" | Teach a **system**: each step's output is the next step's input |
| Quality gate is informal | "Speed up, quality not guaranteed" | Make UX principles + artifacts an explicit **gate** between steps |
| Non-technical designers can't reach the "builder" role | Half of designers ship code, but mostly design engineers | Prototype with AI **without needing engineering skills** |
| Teams lack process updates | 28% of leaders updated evaluation | Teach how to *show* AI-era value to employers |
| Vietnam-specific context | I found only generic market stats (demand growing; salaries up) and no data on PRD-handoff-only roles ⚠️ | Validate with your own network: interview 5–8 designers/hiring managers |

## 6. Draft workflow (hypothesis for us to debate — not from research)

This is my synthesis of the patterns above plus your constraints. Each stage produces a named **artifact** that is the **input** to the next, and a **gate** that checks it against the principles before moving on.

```
        ┌──────────────────────────────────────────────────────────────┐
        │  FOUNDATION (set once, reused every project)                │
        │  UX principles · design system/tokens · project context     │
        └───────────────┬──────────────────────────────────────────────┘
                        │ feeds every stage as constraints
                        ▼
 1 FRAME ──► 2 EXPLORE ──► 3 SHAPE ──► 4 PROTOTYPE ──► 5 VALIDATE ──► 6 HAND OFF
 PRD →       research &    flows,       interactive     test + critique  spec + prototype
 problem     options       IA, content  prototype       vs principles    as reference
 statement
   │            │             │              │               │               │
 Artifact:   Artifact:     Artifact:      Artifact:       Artifact:       Artifact:
 problem     opportunity   user flow +    working         findings +      prototype link,
 brief       map + 3       content        prototype       decision log    decision log,
                directions  model                                         acceptance notes
   ▼            ▼             ▼              ▼               ▼               ▼
 GATE 1      GATE 2        GATE 3         GATE 4          GATE 5          GATE 6
 "Is this    "Does each    "Consistent    "Matches        "Evidence,      "Dev can build
  the right   option cite  with           design system   not AI opinion" it without asking"
  problem?"   evidence?"    principles?"   + a11y?"
                                          
        ◄──────────── human judgment at every gate (Linear rule) ────────────►
```

**Series shape this suggests (for discussion):**
1. Foundation: build your principles + context pack (the reusable "constraint layer")
2. Frame & explore: from PRD to problem brief and options, with AI arguing against you
3. Shape: flows and content with AI, checked against principles
4. Prototype: non-technical prototyping on top of your design system
5. Validate: critique and testing; what *not* to delegate to AI
6. Hand off & show value: the decision log, the portfolio of AI-era work

## 7. Open questions for you

> **Update 2026-10-05:** Questions 1 and 2 are answered (mid/senior; tool-agnostic). See `00-decisions.md`. Remaining open items live there.


1. **Student profile:** mid/senior designers only, or also juniors who "received a PRD and made screens"? That changes how much Stage 1–2 you need.
2. **Tool-agnostic?** Your rules say to use generic labels ("AI chat tool", "AI coding tool"), so the series would teach the *workflow*, not products. Agree?
3. **Prototype depth:** is "working prototype via an AI coding tool, no code written by the student" the ceiling, or do you want design-engineer skills?
4. **Evidence for Vietnam:** do you want me to run a second pass specifically on Vietnamese job postings and agency/outsourcing practice?

## Sources

- [Designer Fund — AI in Design 2026](https://designerfund.com/blog/ai-in-design-2026)
- [Foundation Capital — How AI is reshaping design in tech](https://foundationcapital.com/ideas/how-ai-is-reshaping-design-in-tech)
- [Magic Patterns — AI design toolstack (2026 report summary)](https://www.magicpatterns.com/blog/ai-design-toolstack)
- [Designlab — State of AI in UX & Product Design 2026](https://designlab.com/blog/ai-in-ux-product-design-trends-2026)
- [Figma — State of the Designer 2026](https://www.figma.com/reports/state-of-the-designer-2026/)
- [Figma — Design systems, AI and MCP](https://www.figma.com/blog/design-systems-ai-mcp/)
- [Into Design Systems — Spotify Encore](https://www.intodesignsystems.com/use-cases/spotify-design-system)
- [Designer Fund — Linear](https://designerfund.substack.com/p/ai-design-linear)
- [Bessemer — Shopify](https://www.bvp.com/atlas/inside-shopifys-ai-first-engineering-playbook)
- [Lenny's Newsletter — team prototyping](https://www.lennysnewsletter.com/p/how-to-get-your-entire-team-prototyping)
- [uxdesign.cc — designers who survive 2026](https://uxdesign.cc/one-skill-separates-the-designers-who-survive-2026-from-the-ones-who-dont-f4dec8c3ffe0) (not opened; paywall/403)
- [State of AI Design](https://stateofaidesign.com)
