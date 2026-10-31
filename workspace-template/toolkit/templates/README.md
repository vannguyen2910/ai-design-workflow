# Templates

Empty templates for working documents, shared by every project in this workspace. **Do not fill them in here.** Most templates now sit inside the skill that uses them (`../skills/<skill>/templates/`); this folder keeps the one no skill uses.

## How to use

1. Copy a file into the `work/` of your project and rename it so it is easy to recognise (for example `work/pestel-analysis.md`).
2. Fill in the content. Change `status` to `verified` once you have checked it.
3. Rebuild the report; the document shows in the **Work** section.

Or ask the AI tool: *"Create a research plan document in `work/` from the template `toolkit/skills/interview/templates/research-plan.md`."*

> Templates for **items** (need, hypothesis, decision, evidence, finding, metric) live separately in `insights/_templates/` in each project, because `new-item.py` uses them to create items.

## Template in this folder (no skill uses it)

| Stage | Template | Use it to |
|---|---|---|
| All stages | `generic.md` | Any other kind of document |

## Templates inside each skill

| Skill | Templates (in `../skills/<skill>/templates/`) |
|---|---|
| `interview` | `research-plan.md`, `interview-guide.md`, `interview-synthesis.md` |
| `competitor-analysis` | `competitor-analysis.md` |
| `pestel-analysis` | `pestel-analysis.md` |
| `stakeholder-map` | `stakeholder-map.md` |
| `survey` | `survey-results.md` |
| `user-voice-synthesis` | `persona.md` |
| `framing` | `problem-brief.md`, `assumptions-map.md`, `opportunity-solution-tree.md` |
| `customer-journey-map` | `journey-map.md` |
| `ideation` | `options.md`, `prioritization.md` |
| `build-process-map` | `process-map.md`, `user-flow.md`, `ia-sitemap.md` |
| `prototype` | `prototype.md`, and the `starter/` folder (a small design system, a rules file and an empty page) |
| `user-testing` | `usability-test-script.md`, `test-report.md`, `heuristic-evaluation.md` |
| `handoff` | `measurement-plan.md` |
