# Research: Market, Risks, Vietnam, Teaching, Careers

The evidence base behind the series. Parts 1 to 4 are the first pass (2026-10-05, in English). Part 5 and Part 6 are the deeper career and data-safety research (2026-10-07, in Vietnamese), merged from `future-of-design-careers.md` on 2026-10-18. Confidence levels are marked in each part; items marked ⚠️ were not verified at the primary source.

**In this file**
- [Part 1 — Market research](#part-1--market-research)
- [Part 2 — Failure cases and risks](#part-2--failure-cases-and-risks)
- [Part 3 — Vietnam market](#part-3--vietnam-market)
- [Part 4 — Teaching working designers](#part-4--teaching-working-designers)
- [Part 5 — The future of UI/UX and career paths with AI](#part-5--the-future-of-uiux-and-career-paths-with-ai)
- [Part 6 — Data safety sources](#part-6--data-safety-sources)

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

> **Verified since:** the Designer Fund figures above (91% weekly, 7 tools, 65%, 28% leaders, 20% less teamwork) were later read at the primary source and are marked ✅ in Part 5, sections 3 and 5. Prefer the Part 5 wording and sample size when quoting.

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
*This section held my first six-stage draft diagram. It is replaced by the single gate list in `method.md` Part 3, §2 (the stage map diagram that stood beside it has since been removed). Removed 2026-10-05 so there is only one version of the workflow.*

### 7. Open questions from this first pass (answered)
| Question | Answer (see `plan.md`; the full dated decisions are in `_archive/00-plan-full-2026-10-07.md`) |
|---|---|
| Student profile | Mid and senior designers |
| Tool-agnostic? | Yes: generic labels only |
| Prototype depth | No code written by the student; an AI coding tool builds it |
| Evidence for Vietnam | Still thin; see Part 3 and the validation plan there |

---

## Part 2 — Failure cases and risks

> **See also:** [ai-strengths-and-limits.md](ai-strengths-and-limits.md) pulls together what AI is good at, where it falls short, and the case for not automating a bad workflow, with a pre-automation checklist.

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

> **See also:** Part 5, section 7 adds worker-level Vietnam survey data (all ⚠️ or 🟡) and repeats the same gap list.

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
Some students truly have **no access** to the PO or the business, and designers rarely see business metrics (the PO owns them). The series is built to work in three access levels (full, limited, none); see Lesson 2 in `plan.md` Part 2. Worth asking in the interviews below how often designers are invited to requirement discussions.

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


---

## Part 5 — The future of UI/UX and career paths with AI

Desk research cho series. Mục đích: làm chỗ dựa cho lập trường "partner, không phải biến PRD thành screen", và kiểm tra các con số đang dùng trong Module 1.
**Thời điểm research:** 2026-10-07 · **Cách làm:** tìm kiếm web, và đọc trực tiếp nguồn gốc ở những trang mở được · **Trạng thái:** bản đầu, chưa có ai review

Số mục (1 đến 11) giữ nguyên như file gốc để các tham chiếu "mục 9" hay "mục 10" vẫn đúng. Dấu ✅, 🟡, ⚠️ và mã nguồn [S1] đến [S15] chỉ dùng trong Part 5.

### 1. How to read this

Mỗi con số đi kèm một dấu độ tin cậy và một mã nguồn trong ngoặc vuông, ví dụ [S3]. Trích dẫn đầy đủ nằm ở mục 11.

| Dấu | Nghĩa |
|---|---|
| ✅ | Mình đã đọc ở nguồn gốc (báo cáo, bài nghiên cứu hoặc trang của cơ quan thống kê) trong lần research này |
| 🟡 | Chỉ có nguồn thứ cấp đưa lại; nguồn gốc bị khoá, bị chặn hoặc không đọc được. Có thể đúng, nhưng cần kiểm tra trước khi đưa lên slide |
| ⚠️ | Chỉ có một nguồn yếu, các con số mâu thuẫn nhau, hoặc không truy ngược được. Không dạy như một sự thật |

Có hai giới hạn áp dụng cho gần như mọi số liệu bên dưới. **Khảo sát designer là tự khai báo và không phải mẫu ngẫu nhiên**, nên "9 trên 10 designer" thực ra là "9 trên 10 designer đã trả lời". Và **không có nguồn nào mình tìm thấy đo đúng nhóm mà series nhắm tới** (designer nhận brief rồi làm ra screen), nên lập trường của series được ủng hộ về tinh thần, chưa được đo trực tiếp (xem mục 8).

---

### 2. The short version

1. **Gần như ai cũng đã dùng AI.** Trong khảo sát 906 designer, 91% dùng AI ít nhất mỗi tuần (so với 54% một năm trước) và trung bình mỗi người dùng 7 tool. ✅ [S1]
2. **Trên giấy tờ, nghề này chưa co lại.** Cục Thống kê Lao động Mỹ (BLS) dự báo web và digital interface designer tăng 7% từ 2024 đến 2034, trong khi mức trung bình mọi ngành là 3,1%. ✅ [S5][S6] Bảng mới hơn (2025 đến 2035) gộp developer và designer, cho ra 5%, và cảnh báo AI "may soften" mức tăng. ✅ [S4]
3. **Áp lực lộ ra ở entry level.** NN/g nói vị trí entry-level UX vẫn "scarce and highly competitive" trong khi vị trí senior phục hồi. ✅ [S3] Một nghiên cứu của Stanford trên dữ liệu bảng lương cho thấy người đi làm sớm (22 đến 25 tuổi) trong các nghề chịu tác động của AI mất 16% việc làm tương đối, còn người có kinh nghiệm thì ổn định. ✅ [S7] Nghiên cứu này không tách riêng designer.
4. **Ranh giới giữa các vai trò đang mờ đi.** Một nửa số designer được khảo sát đã đưa code do AI tạo ra lên production; 65% làm nhiều việc product hoặc engineering hơn. ✅ [S1]
5. **Thứ còn giá trị là judgment.** NN/g: người thành công là những "adaptable generalists" coi UX là việc giải quyết vấn đề mang tính chiến lược, không phải sản xuất deliverable. ✅ [S3]

---

### 3. What designers are doing with AI

| Phát hiện | Nguồn | Dấu |
|---|---|---|
| 91% dùng AI cho công việc design ít nhất mỗi tuần, tăng từ 54% một năm trước; 75% dùng mỗi ngày | Designer Fund và Foundation Capital, *AI in Design 2026* [S1] | ✅ |
| Trung bình designer thường xuyên dùng 7 AI tool có sẵn trên thị trường, tăng từ 3 | [S1] | ✅ |
| Một nửa số người trả lời đã đưa code do AI tạo ra lên production | [S1] | ✅ |
| 65% làm nhiều việc product hoặc engineering hơn; 40% nói PM và engineer làm nhiều việc design hơn | [S1] | ✅ |
| 73% cảm thấy kỳ vọng về output, chất lượng và tốc độ đang tăng | [S1] | ✅ |
| Tỷ lệ báo cáo "ít collaboration hơn vì AI" tăng từ 5% lên 20% | [S1] | ✅ |
| Cơ sở khảo sát: 906 designer, hơn 60 quốc gia, hơn 25 buổi phỏng vấn sâu, bảy case study công ty; khảo sát chạy vào tháng 3/2026; khoảng 60% người trả lời có trên 10 năm kinh nghiệm | Trang [S1], cộng với bản tóm tắt trong kết quả tìm kiếm | 🟡 (chi tiết về mẫu) |
| 72% designer dùng generative AI; 98% trong số đó tăng mức dùng trong năm qua | Figma, *State of the Designer 2026* (906 digital designer, thực hiện cùng NewtonX) [S2] | 🟡 |
| 36% nói ngành đã tốt hơn, 35% nói tệ hơn, 29% nói không đổi | [S2], theo trích dẫn của [S9] | 🟡 |
| Designer tăng mức dùng AI có khả năng báo cáo hạnh phúc tăng cao hơn 25%; trong nhóm mức dùng đứng yên, 40% nói công việc đang tệ đi (so với 18% ở nhóm tăng mức dùng) | [S2], qua bản tóm tắt trong kết quả tìm kiếm | 🟡 |
| 41% nói AI thay đổi đáng kể cách team làm việc cùng nhau, so với 7% hai năm trước; số designer tham gia development tăng gấp đôi lên 41%, số developer làm việc design tăng từ 44% lên 60% | [S2], qua bản tóm tắt trong kết quả tìm kiếm | 🟡 |

**Ghi chú khi đọc.** Hai khảo sát có cùng cỡ mẫu (906) nhưng là hai báo cáo riêng của hai tổ chức khác nhau. Cả hai đều do bên có lợi ích trong design và AI tooling thực hiện hoặc viết, nên hãy xem **mức độ dùng AI** là có thể cao, còn các con số về **cảm nhận** chỉ mang tính tham khảo.

---

### 4. The job market

#### 4.1 Official employment outlook (US)

| Phát hiện | Nguồn | Dấu |
|---|---|---|
| Web và digital interface designer: 128.900 việc làm năm 2024, dự báo 137.900 vào năm 2034 (+7,0%), khoảng 9.100 vị trí mở mỗi năm; mức trung bình mọi ngành là +3,1% | Dự báo của BLS, được Adobe tổng hợp trong *The Economic State of Creative Professions* (06/2026) [S5]; trang O\*NET Bright Outlook, có dự báo BLS 2024 đến 2034 [S6] (số liệu đã đối chiếu trong [S5]; bản thân [S6] mình chỉ thấy qua bản tóm tắt tìm kiếm) | ✅ với [S5], 🟡 với [S6] |
| Bảng BLS mới hơn, 2025 đến 2035, **gộp web developer và digital designer**: 220.100 việc làm, +5%, khoảng 13.600 vị trí mở mỗi năm. Trang này nói công cụ ngày càng tốt và "increasing use of artificial intelligence (AI) for web development may soften the employment growth of these workers" | BLS Occupational Outlook Handbook, trang sửa lần cuối 27/08/2026 [S4] | ✅ |
| Mức lương trung vị của web và digital interface designer: 104.000 USD (05/2025) | [S4][S5] | ✅ |
| 2015 đến 2025: lương trung vị tăng 60,1% tính theo đô la và 17,8% sau khi điều chỉnh lạm phát, cao nhất trong chín nghề sáng tạo. Graphic designer: lương thực -1,2%; commercial và industrial designer -8,0% | [S5] | ✅ |

**Lưu ý.** (1) Hai con số 7% và 5% dùng cách gộp nghề và năm gốc khác nhau; đừng trừ cái này cho cái kia. (2) Dự báo của BLS tính tác động của AI rất hạn chế, và bản 2024 đến 2034 có trước phần lớn những thay đổi gần đây. (3) Tài liệu của Adobe là bản tổng hợp từ dữ liệu BLS và O\*NET, và tự nói chỉ trình bày "what the data shows, not what it may mean". (4) Báo cáo của Adobe do một công ty bán phần mềm sáng tạo xuất bản; mình chỉ dùng nó như một bản dễ đọc của số liệu BLS. Hãy đối chiếu với bảng gốc của BLS trước khi trích dẫn.

#### 4.2 Employer outlook (global)

| Phát hiện | Nguồn | Dấu |
|---|---|---|
| WEF *Future of Jobs 2025* (khoảng 1.000 employer, 14 triệu lao động, 55 nền kinh tế): UI và UX designer nằm trong nhóm mười vai trò tăng nhanh nhất đến 2030; graphic designer nằm trong nhóm giảm nhanh nhất | WEF [S8], theo báo chí chuyên ngành [S10][S11] | 🟡 (trang WEF trả về lỗi 403; cần kiểm tra ở báo cáo của WEF) |

Sự tương phản giữa graphic design (giảm) và UI/UX (tăng) là tín hiệu hữu ích: employer kỳ vọng AI thay thế phần sản xuất hình ảnh nhanh hơn phần interaction và product thinking.

#### 4.3 Entry level versus experienced

| Phát hiện | Nguồn | Dấu |
|---|---|---|
| Vị trí entry-level UX vẫn "scarce and highly competitive"; vị trí senior phục hồi nhanh hơn; lượng người muốn vào nghề UX vượt số vị trí junior | NN/g, *State of UX in 2026* (16/01/2026) [S3] | ✅ |
| Người đi làm sớm (22 đến 25 tuổi) trong các nghề chịu tác động mạnh nhất của AI: **việc làm giảm 16% tương đối** kể từ khi generative AI phổ biến, sau khi loại trừ cú sốc ở cấp công ty; người có kinh nghiệm ổn định; sự điều chỉnh diễn ra ở số việc làm chứ không phải ở lương; mức giảm tập trung ở nơi AI **thay thế** thay vì **hỗ trợ** | Brynjolfsson, Chandar, Chen, Stanford Digital Economy Lab, bản ngày 13/11/2025 (dữ liệu bảng lương ADP) [S7] | ✅ |
| Cùng nghiên cứu: kết quả vẫn đứng vững khi loại trừ các công ty công nghệ và các nghề có thể làm từ xa | [S7] | ✅ |

**Lưu ý.** [S7] xét mọi nghề, xếp theo mức độ chịu tác động của AI (ví dụ của họ là software developer và nhân viên chăm sóc khách hàng). Nghiên cứu không báo cáo riêng designer, nên nó là bằng chứng về **cơ chế** (entry level và tự động hoá), không phải về số lượng việc làm design.

#### 4.4 Demand signals that are weaker

| Phát hiện | Nguồn | Dấu |
|---|---|---|
| Designer Fund ước tính số tin tuyển dụng design trong danh mục các công ty của quỹ tăng khoảng 60% năm 2025 so với 2024 | Blog của Figma trích Designer Fund [S12], chỉ thấy qua bản tóm tắt tìm kiếm | 🟡 (danh mục của một quỹ, không phải toàn thị trường) |
| Tháng 4/2026, tin tuyển design engineering +14% so với tháng trước, UX research +15%, product design -5% | Một blog nghề nghiệp, không rõ dữ liệu gốc | ⚠️ (một tháng, không có phương pháp) |

---

### 5. How roles and skills are changing

**Execution đang bị nén lại; judgment đang lên giá.** NN/g (2026): các tổ chức gộp nhiều vai trò chuyên môn vào một vị trí và đòi hỏi kỹ năng rộng hơn; research, stakeholder management và critical thinking "distinguish performers"; phần design bề mặt đang trở nên có thể thay thế bằng AI tool. ✅ [S3]

**Designer đang đi lên và đi ngang.** [S1] mô tả designer "up a layer of abstraction" thành builder, tạo ra không chỉ deliverable mà cả công cụ tạo ra deliverable. 65% làm nhiều việc product và engineering hơn. ✅ [S1]

**Lãnh đạo chưa theo kịp.** Chỉ 28% leader đã cập nhật chính sách đánh giá hoặc lương thưởng chính thức; 8% đổi performance metrics; 4% đổi lương thưởng. Khoảng 50% leader nói AI fluency giờ quan trọng hơn khi tuyển dụng. ✅ [S1]

**Việc học diễn ra không chính thức.** Học từ đồng nghiệp tăng từ 24% lên 80% trong khảo sát của Designer Fund, trong khi lời khuyên từ lãnh đạo giảm từ 32% xuống 16%. ✅ [S1] Điều này ủng hộ một format thực hành cùng nhau như series này.

**Craft đang được định nghĩa lại.** Trong [S2], khi được hỏi craft nghĩa là gì, 57 đến 58% chọn visual polish và sự chú ý đến chi tiết, và 47% chọn thoughtful problem solving. 🟡 (hai nguồn thứ cấp lệch nhau một điểm, 57 so với 58). Cách đọc: phần lớn designer vẫn định nghĩa craft ở bề mặt; problem solving là quan điểm của một nhóm thiểu số đáng kể.

**AI fatigue.** NN/g gọi 2026 là "the year of AI fatigue": cơn sốt đã nguội, và practitioner báo cáo áp lực phải ship tính năng AI dù không mang lại giá trị cho user. ✅ [S3]

---

### 6. Career paths

Bằng chứng ở mục này mỏng hơn các mục 3 đến 5. Phần lớn bài viết về career path do bên bán khoá học hoặc nhà tuyển dụng viết, nên mình ghi rõ đâu là nguồn gốc, đâu là ý kiến.

| Hướng đi | Bằng chứng cho thấy gì | Độ mạnh |
|---|---|---|
| **Senior generalist / strategic designer** (research, framing, làm việc với stakeholder) | NN/g: vị trí senior và generalist phục hồi nhanh hơn; adaptable generalist thành công [S3]. Stanford: người có kinh nghiệm ổn định [S7] | Trung bình: một bài có thẩm quyền cộng một nghiên cứu gián tiếp |
| **Designer-builder / design engineer** (làm prototype và ship bằng AI tool) | Một nửa designer được khảo sát đã ship code do AI tạo; số designer tham gia development tăng gấp đôi lên 41% [S1][S2]. Có những tuyên bố về tăng trưởng trên job board nhưng yếu (mục 4.4) | Trung bình về xu hướng, yếu về số liệu tuyển dụng |
| **AI product design** (thiết kế sản phẩm có AI, conversation design) | NN/g và các blog nghề nghiệp xếp AI UX và conversation design vào nhóm chuyên môn đang lên [S3][S13]. Con số tăng trưởng "+145%" mình tìm thấy không truy ngược được | Yếu: hướng đi hợp lý, số liệu chưa dùng được |
| **UX research** | NN/g xem research là điểm tạo khác biệt [S3]; có một tín hiệu yếu về tin tuyển tăng (mục 4.4) | Trung bình về giá trị, yếu về dữ liệu nhu cầu |
| **Hướng junior thiên về execution** (wireframe, sản xuất asset) | Chịu tác động nhiều nhất: NN/g về việc vị trí entry-level khan hiếm [S3]; Stanford về mức giảm ở người đi làm sớm ở nơi AI thay thế [S7]; các blog nghề nghiệp nói studio cắt vị trí wireframe cho junior [S13] | Trung bình: ba nguồn cùng chỉ một hướng |
| **Graphic / vị trí sản xuất hình ảnh** | WEF xếp graphic design vào nhóm nghề giảm [S8][S10]; lương thực của graphic designer theo số liệu BLS giảm 1,2% trong mười năm [S5] | Trung bình (WEF là 🟡) |

**Điều rút ra.** Những hướng dựa trên việc **quyết định** (giải vấn đề nào, biết là đã đúng bằng cách nào) có vẻ bền hơn những hướng dựa trên việc **làm ra** screen. Điều này khớp với lập trường của series, nhưng các nguồn mô tả một xu hướng, không phải một sự đảm bảo, và không nguồn nào nói về Việt Nam.

---

### 7. Vietnam

Dữ liệu riêng cho design gần như không có. Những gì mình tìm được là dữ liệu chung cho người đi làm, nên chỉ dùng làm bối cảnh.

| Phát hiện | Nguồn | Dấu |
|---|---|---|
| 98% chuyên gia được khảo sát ở Việt Nam dùng AI trong công việc; 83% kỳ vọng AI tác động tích cực đến cơ hội nghề nghiệp; chỉ 55% tự tin cập nhật được kỹ năng AI. Mối lo hàng đầu: trách nhiệm với quyết định của AI (48%), kỹ năng lỗi thời (45%), mất yếu tố con người (37%) | Bài của Asia News Network [S14]; khảo sát gốc không được nêu tên trong bản tóm tắt mình đọc được | ⚠️ (cần tìm khảo sát gốc trước khi dùng) |
| Lương năm 2026 ở Việt Nam dự báo tăng, riêng nhóm AI, dữ liệu và chuyển đổi số tăng đến 25% | Tuoi Tre News, trích một khảo sát lương [S15] | 🟡 (không nói về designer) |
| Báo cáo lương UI/UX (đã có trong series) | TELOS Academy, xem Part 3 ở trên và `assets/SOURCES.md` | ⚠️ (như đã ghi ở đó) |

**Khoảng trống.** Chưa có nguồn nào về số lượng designer, tuyển dụng junior hay tác động của AI ở Việt Nam. Kế hoạch kiểm chứng ở Part 3 (phỏng vấn 5 đến 8 designer hoặc hiring manager trong nước) vẫn là cách để lấp khoảng trống này.

---

### 8. What this means for the course

1. **Lập trường của series được ủng hộ về tinh thần.** Bằng chứng mạnh nhất cho thấy giá trị đang chuyển từ làm ra screen sang framing vấn đề, làm việc với stakeholder và judgment [S3], và entry-level execution là lớp chịu tác động nhiều nhất [S3][S7]. Điều này khớp với "bắt đầu từ business question, cùng định nghĩa requirement".
2. **Không nguồn nào đo trực tiếp** nhận định "designer chỉ nhận PRD rồi biến thành screen là nhóm dễ bị ảnh hưởng nhất". Hãy nói đó là suy luận ("phần việc AI nén nhanh nhất là từ brief sang screen"), không nói như một phát hiện.
3. **Đối tượng học viên quan trọng.** Khoá nhắm tới designer mid và senior. Dữ liệu cho thấy lớp senior là lớp ổn định [S3][S7], nên thông điệp không phải là "AI sẽ lấy việc của bạn" mà là "công việc quanh bạn đang đổi; đây là cách dẫn dắt nó".
4. **Dùng số liệu làm bối cảnh, không làm nỗi sợ.** Phát hiện "AI fatigue" của NN/g [S3] là đối trọng hữu ích với sự cường điệu khi mở đầu Module 1.
5. **Khi dạy, nêu năm và cỡ mẫu.** Trích mỗi con số kèm nguồn, năm và mẫu ("trong khảo sát 906 designer năm 2026"), như mục 9 khuyến nghị.

---

### 9. Module 1 fact-check

Mình đã kiểm tra các con số dùng trong `design-process-with-ai-lesson.md` (Phase 1 và Further Resources) và slide tương ứng trong slide outline.

| Nội dung trong Module 1 | Kết quả | Đề xuất sửa |
|---|---|---|
| "Khoảng 9 trên 10 designer dùng AI ít nhất mỗi tuần" (Designer Fund và Foundation Capital, *AI + Design 2026*) | ✅ Khớp [S1]: 91%, tăng từ 54%, khảo sát 906 designer | Ghi "trong khảo sát 906 designer" để không bị hiểu là cả nghề. Tiêu đề slide "9 in 10 designers use AI weekly" cũng cần sửa vì cùng lý do |
| "Trung bình dùng bảy tool" | ✅ Khớp [S1] (7, tăng từ 3) | Không cần sửa |
| "Figma, State of the Designer 2026: 36% tốt hơn, 35% tệ hơn, 29% không khác" | 🟡 Con số được xác nhận qua một trích dẫn thứ cấp [S9]; báo cáo Figma nằm sau form nên mình chưa đọc được | Trước khi dạy, hãy tải báo cáo và xác nhận. Về cách viết: nguồn nói **ngành** (field) đã "tốt hơn" hoặc "tệ hơn"; lesson đang viết "design tốt hơn nhờ AI", tức là thêm một nguyên nhân mà con số không nêu. Đề xuất: "36% nói ngành đã tốt hơn, 35% nói tệ hơn, 29% nói không đổi" |
| "Cùng một tool, kết quả khác nhau" (phần suy luận) | ✅ Cách đọc hợp lý, nhưng đây là suy luận của lesson, không phải của báo cáo | Giữ, và trình bày đó là cách nhìn của bạn |
| Link trong Further Resources (trang Designer Fund, trang báo cáo Figma) | ✅ Cả hai trang đều tồn tại. Trang Figma là form tải về | Ghi chú "cần điền form (miễn phí)" cạnh link Figma |
| Các nội dung data safety (Luật 91/2025/QH15, Nghị định 356/2025/NĐ-CP, mặc định dùng hội thoại để train ở gói consumer) | Chưa nằm trong lần research này | Kiểm tra riêng trước khi dạy; lesson đã dặn như vậy |

Mình chưa sửa file lesson hay slide outline. Nếu bạn muốn áp dụng các đề xuất sửa trên, mình sẽ sửa cả hai file cùng lúc theo sync rule.

---

### 10. Claims not to use yet

| Nhận định | Lý do |
|---|---|
| "Tin tuyển entry-level UX giảm 71% trong hai năm; chỉ 4,2% vị trí dành cho junior (18 trên 1.147)" | Chỉ có một blog của bên bán khoá học; mình không truy ngược được bộ dữ liệu hay phương pháp |
| "Các team design bị cắt 35% trong năm 2025" | Xuất hiện trong bản tóm tắt tìm kiếm, không có nguồn truy ngược được |
| "AI product design tăng trưởng +145%" | Trang tổng hợp, không có phương pháp |
| "Một tin tuyển junior thu hút 500 đến 800 ứng viên; 90% portfolio giống nhau" | Giai thoại từ một blog |
| "73% designer nói AI là cộng sự thiết kế sẽ có tác động lớn nhất năm 2026; 93% đã dùng generative AI" | Nằm trong một blog xu hướng chung, không nêu tên khảo sát |
| "Tin tuyển design engineering tăng 14% trong tháng 4/2026" | Một tháng, một blog, không có phương pháp |

---

### 11. Sources

Truy cập ngày 2026-10-07 trừ khi ghi khác. "Primary" nghĩa là tổ chức chạy khảo sát hoặc tổng hợp dữ liệu.

| ID | Nguồn | Loại | Link |
|---|---|---|---|
| S1 | Designer Fund và Foundation Capital, *AI in Design 2026* (khảo sát 906 designer, hơn 25 buổi phỏng vấn, 7 case study công ty) | Primary, khảo sát do bên có lợi ích trong ngành thực hiện | https://designerfund.com/blog/ai-in-design-2026 |
| S2 | Figma, *State of the Designer 2026* (906 digital designer; cùng NewtonX; bản tóm tắt trên blog đề ngày 12/02/2026, báo cáo đầy đủ nằm sau form) | Primary, bị khoá | https://www.figma.com/reports/state-of-the-designer-2026/ và https://www.figma.com/blog/state-of-the-designer-2026/ |
| S3 | Kate Moran, Raluca Budiu, Sarah Gibbons và các chuyên gia NN/g, *State of UX in 2026*, Nielsen Norman Group, 16/01/2026 | Primary, phân tích của chuyên gia (không phải khảo sát) | https://www.nngroup.com/articles/state-of-ux-2026/ |
| S4 | US Bureau of Labor Statistics, *Occupational Outlook Handbook: Web Developers and Digital Designers* (dự báo 2025 đến 2035; trang sửa 27/08/2026) | Primary, thống kê chính thức | https://www.bls.gov/ooh/computer-and-information-technology/web-developers.htm |
| S5 | Adobe, *The Economic State of Creative Professions*, Edition 1, 06/2026 (tổng hợp từ BLS OEWS 05/2025 và BLS Projections 2024 đến 2034) | Thứ cấp, tổng hợp từ dữ liệu gốc; do một vendor xuất bản | https://www.adobe.com/cc-shared/assets/ai/research/adobe-ai-research-june-2026-economic-state-of-creative-professions.pdf |
| S6 | US Bureau of Labor Statistics, dữ liệu nghề *Web and Digital Interface Designers* qua O\*NET Bright Outlook (2024 đến 2034) | Primary, thống kê chính thức | https://www.onetonline.org/help/bright/15-1255.00 |
| S7 | Erik Brynjolfsson, Bharat Chandar và Ruyu Chen, *Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence*, Stanford Digital Economy Lab, 13/11/2025 | Primary, working paper dùng dữ liệu bảng lương ADP (lúc đó chưa qua peer review) | https://digitaleconomy.stanford.edu/publications/canaries-in-the-coal-mine/ |
| S8 | World Economic Forum, *The Future of Jobs Report 2025* | Primary; trang bị chặn (HTTP 403), số liệu lấy từ [S10][S11] | https://www.weforum.org/publications/the-future-of-jobs-report-2025/ |
| S9 | Creative AI News, *Figma State of Design 2026: AI impact* (trích tỷ lệ 36/35/29; ngày phát hành ghi 16/03/2026, mâu thuẫn với [S2]) | Thứ cấp | https://www.creativeainews.com/blog/figma-state-of-design-2026-ai-impact/ |
| S10 | Creative Boom, *It's official: AI is coming for your graphic design job* | Thứ cấp (báo chí chuyên ngành) | https://creativeboom.com/news/its-official-ai-is-coming-for-your-graphic-design-job |
| S11 | Design Week, *Graphic design among most at risk jobs from AI, report* | Thứ cấp (báo chí chuyên ngành) | https://www.designweek.co.uk/graphic-design-among-most-at-risk-jobs-from-ai-report/ |
| S12 | Blog Figma, *Why demand for designers is on the rise* (trích một ước tính của Designer Fund) | Thứ cấp, blog của vendor | https://www.figma.com/blog/why-demand-for-designers-is-on-the-rise/ |
| S13 | UX Design Institute, *The UX job market in 2026: what roles are growing and what skills matter most* | Thứ cấp, đơn vị đào tạo | https://www.uxdesigninstitute.com/blog/the-ux-job-market-in-2026-2/ |
| S14 | Asia News Network, *AI won't replace jobs, but Vietnam's professionals feel less confident* | Thứ cấp; chưa xác định được khảo sát gốc | https://asianews.network/?p=297785 |
| S15 | Tuoi Tre News, *Vietnam's 2026 salaries set to surge, AI professionals seen gaining up to 25%: survey* | Thứ cấp, báo chí | https://news.tuoitre.vn/vietnams-2026-salaries-set-to-surge-ai-professionals-seen-gaining-up-to-25-survey-103251129202137422.htm |

**Việc kiểm tra nguồn còn mở.** (1) Đọc báo cáo đầy đủ của Figma và của WEF ở nguồn gốc. (2) Xác nhận khảo sát đứng sau [S14]. (3) Xác nhận ngày xuất bản của [S1]: một bản tóm tắt tìm kiếm ghi 20/05/2026, trong khi khi tải trang lại thấy 06/10/2026; bản thân khảo sát chạy vào tháng 3/2026. (4) Xác nhận ngày phát hành của báo cáo Figma (12/02 so với 16/03/2026).


---


## Part 6 — Data safety sources


Kiểm tra ngày 2026-10-07. Các nguồn này đứng sau mục 5 (Data safety) của lesson Module 1; lesson trích dẫn chúng dưới dạng [10], [11], [12] và không nêu tên tool cụ thể, theo quy ước dùng tên chung trong nội dung lesson. Tên nhà cung cấp chỉ xuất hiện ở file này.

| Nội dung | Nguồn | Kết quả kiểm tra | Dấu |
|---|---|---|---|
| Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15, thông qua 26/06/2025, hiệu lực 01/01/2026 | Toàn văn trên Thư viện Pháp luật: https://thuvienphapluat.vn/van-ban/Bo-may-hanh-chinh/Luat-Bao-ve-du-lieu-ca-nhan-2025-so91-2025-QH15-625628.aspx | Số hiệu, ngày thông qua và ngày hiệu lực khớp ở nhiều nguồn (Thư viện Pháp luật, VCCI, luatvietnam). Trang gốc chưa mở được bằng công cụ (bị chặn), nên chưa đọc được toàn văn | 🟡 |
| Nghị định 356/2025/NĐ-CP, ban hành 31/12/2025, hiệu lực 01/01/2026, quy định chi tiết thi hành luật, thay thế Nghị định 13/2023/NĐ-CP | Bản tiếng Anh trên luatvietnam: https://english.luatvietnam.vn/decree-no-356-2025-nd-cp-dated-december-31-2025-of-the-government-detailing-a-number-of-articles-and-measures-for-the-implementation-of-the-law-on-p-422896-doc1.html | Đã đọc: tên, số hiệu, ngày ban hành, luật được hướng dẫn. Ngày hiệu lực và việc thay thế Nghị định 13/2023 lấy từ các bản tin của hãng luật (Rajah & Tann, EY Vietnam), chưa đối chiếu với văn bản gốc | ✅ số hiệu và ngày; 🟡 hiệu lực và thay thế |
| Bài KPMG Vietnam về luật mới (đã dùng ở bản trước) | https://kpmg.com/vn/en/home/insights/2025/06/vietnam-new-personal-data-protection-law.html | Đã bỏ khỏi lesson. URL ghi 2025/06, tức trước khi nghị định hướng dẫn được ban hành (12/2025), nên không thể là nguồn cho phần nghị định | Bỏ |
| Chính sách dùng hội thoại để cải thiện model, gói consumer so với gói doanh nghiệp (nhà cung cấp thứ nhất) | Trang cập nhật điều khoản consumer: https://www.anthropic.com/news/updates-to-our-consumer-terms | Đã đọc. Áp dụng cho gói Free, Pro, Max (kể cả công cụ lập trình). Không áp dụng cho gói Work, Government, Education và API (kể cả qua nền tảng cloud của bên thứ ba). Người dùng hiện tại phải chọn trước 08/10/2025; nếu chọn cho phép dùng để train thì dữ liệu được lưu tối đa 5 năm, nếu từ chối thì 30 ngày. Có thể đổi lựa chọn trong Privacy Settings bất kỳ lúc nào | ✅ |
| Chính sách tương tự (nhà cung cấp thứ hai) | Trang data controls: https://help.openai.com/en/articles/7730893-data-controls-in-chatgpt | Chưa đọc trực tiếp (trang trả về lỗi 403). Bản tóm tắt trong kết quả tìm kiếm: gói consumer có tuỳ chọn "Improve the model for everyone" cho phép dùng hội thoại để train; gói business mặc định không train. Cần mở và xác nhận trước khi dùng như một dẫn chứng | 🟡 |
| Bài tổng hợp chính sách của các tool (blog) | https://theaicareerlab.com/blog/does-ai-train-on-your-data | Đã bỏ khỏi lesson. Nguồn thứ cấp, được thay bằng trang gốc của nhà cung cấp | Bỏ |

**Cách lesson diễn đạt sau khi sửa.** Lesson nêu mô hình hai lớp (consumer có lựa chọn cho phép train, doanh nghiệp và API mặc định không train) và dặn đọc trực tiếp trang data controls của tool đang dùng, thay vì khẳng định chính sách cụ thể của từng tool. Cách này đúng với nguồn đã đọc ở nhà cung cấp thứ nhất và nhất quán với bản tóm tắt ở nhà cung cấp thứ hai.

**Việc còn mở.** (1) Mở trang gốc của luật và nghị định để đọc toàn văn, đặc biệt các điều về dữ liệu nhạy cảm và xử lý tự động. (2) Mở trang data controls của nhà cung cấp thứ hai. (3) Lặp lại kiểm tra này mỗi lần dạy, vì điều khoản thay đổi thường xuyên.
