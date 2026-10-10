# AI Design Workflow Series — Decisions Log

Running record of what Winnie and Claude have decided. Update this file whenever a decision changes. Research files in this folder (`01-` onward) inform these decisions but don't overrule them.

## Decided (2026-10-05)

| Decision | Choice | Notes |
|---|---|---|
| Audience | **Mid/senior designers** | Students must already have design foundations. No teaching of basics. |
| Main outcome | **Run a repeatable AI workflow** | A chain where each step's output is the next step's input. Not prompt tips, not tools. |
| Quality gate | **Mix by stage** | A different gate at each stage (see `02-stage-methods-and-delegation.md` for the proposed mapping). |
| Series size | **8–10 lessons** | Foundation + stages (concept and practice) + capstone. |
| Artifact storage | **One living working file** (sections per step) + `sources/` folder; final report is an HTML page | Replaces the earlier one-file-per-artifact idea. See `06-activity-flow-standard.md` §3. |
| Final report | **Students build `analysis.html` themselves** from a provided template | Template: `assets/templates/competitor-analysis-template.html` |
| Measurement scope | **Pre-launch usability metrics are the core** (students rarely have post-launch access); post-launch is background | `08-measuring-design-success.md` |
| Measurement framework | **One framework: Goals → Signals → Metrics**, using HEART's Task success and Happiness pre-launch | Others: ask the PO to track after launch |
| Business metrics | Designers rarely see them (PO owns them). Teach students to **ask actively** and to record assumed metrics as unconfirmed | PO question kit in `08` |
| Positioning | **Design is a strategic partner that co-defines the requirement with business and product, not a recipient of the PRD.** Start from the business question; any existing PRD is a draft to improve | Stage map, Lesson 2 (now "Co-define the requirement"), and the Define output ("shared problem brief") updated |
| Access risk | **Some students have no access to the PO or business.** The series degrades gracefully: three access tiers (full, limited, none) with a written-questions fallback; AI never plays the PO; unconfirmed outcomes are recorded as assumed; agreement status travels with the scope and brief | Lessons 2 and 4 in `10-series-skeleton.md`; mention in Lesson 1 |
| Lesson 1 | **The existing lesson `ai-workflow-for-ux-designers` is Lesson 1**, re-scoped to AI terminology and project folder structure. Series is now numbered 1–10 | Not yet edited; mapping and issues in `10-series-skeleton.md` |
| Principles sufficiency | **Nielsen's 10 are enough** for students whose company has no written principles | No need for the Foundation lesson to add product-specific ones |
| UX principles | **Nielsen's 10 heuristics as the baseline**; add the organisation's own UX, business and service principles where they exist | `09-traceability-and-alignment.md` |
| Hypothesis granularity | No standard; depends on the solution. Rule of thumb in `09` | |
| Alignment check | **Lives inside the critique loop lesson**, with a light version at every activity's last gate (standard rule 12) | Not its own lesson |
| Stage map | **Define output = problem brief with outcome + success metrics, ranked opportunities, hypotheses, principles** | Diagram updated; alignment check shown at every gate |
| Activity method | **Generic standard for all activities**; competitor analysis is one worked example | `06-activity-flow-standard.md` and `07-step-card-template.md` are generic; examples live in `examples/` |
| Diagram style | Flat fills, no bold outlines | Level 2 flows follow this |
| Tool naming | Generic labels only ("AI chat tool", "AI coding tool") | Per CLAUDE.md general lesson conventions. |

## Framing from Winnie (source of the series)
- Market fear: designers who only receive a PRD from the PO and turn it into screens fear AI will take their job. **Response (decided 2026-10-05):** do not wait for the PRD; co-define the requirement with the business and product.
- "AI won't replace people; people who use AI will replace people who don't."
- Goal: leverage existing design skill with AI as an assistant in daily work, with systematic thinking, not a prompt course.
- Every AI idea or solution must pass the UX principles and artifacts defined earlier in the workflow.

## Still open
1. Where does the existing lesson `ai-workflow-for-ux-designers` fit in the series? (Not yet re-read against the new outline.)
2. How strict is "no code" for the prototype stage? (Assumed: no code written by the student; AI coding tool does it.)
3. Capstone format: individual project on a real work case, or a shared case study?
4. Vietnam validation: interview 5–8 local designers or hiring managers (see `04-vietnam-market.md`).

## Research index
- `01-market-research.md` — global market, named companies, draft workflow
- `02-stage-methods-and-delegation.md` — what to delegate or keep, per stage, plus gate mapping and draft lesson skeleton
- `03-failure-cases-and-risks.md` — where AI-assisted design goes wrong
- `04-vietnam-market.md` — Vietnam evidence (thin) and what to validate
- `05-teaching-working-designers.md` — course design notes (thin evidence, hypotheses)
- `06-activity-flow-standard.md` — the generic method every activity follows
- `07-step-card-template.md` — generic step card format and checklist
- `08-measuring-design-success.md` — how to measure product outcome and the AI workflow itself; PO question kit
- `10-series-skeleton.md` — draft lesson names and learning objectives (10 lessons)
- `09-traceability-and-alignment.md` — outcome → opportunity → hypothesis → decision → principle → test; the alignment check
- `examples/competitor-analysis/` — first worked example (step cards; diagram and template are in `assets/`)
