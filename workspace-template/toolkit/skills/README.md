# Skills: step cards for the AI

Each skill is a folder with a `SKILL.md`, and, when it has them, `templates/` and `examples/`. `SKILL.md` is a **step card**: it defines an AI-assisted procedure as a file, so the AI tool can read it and the procedure is stored with the project. Each card is one workflow made of ordered steps, and each step says who does it (the AI or you), which files to read and where to write.

This folder is the source: edit the skills here. The scripts they use live in `../tools/`.

## Skills

| Skill | Stage | When to use | Status |
|---|---|---|---|
| [`competitor-analysis`](competitor-analysis/SKILL.md) | Discover | When you need to know what competitors are doing | Draft, not tried much |
| [`user-voice-synthesis`](user-voice-synthesis/SKILL.md) | Discover | When you have quotes or user interviews to synthesise | Draft, not tried much |
| [`pestel-analysis`](pestel-analysis/SKILL.md) | Discover | When a decision depends on the market, region or regulation around the product | Draft |
| [`stakeholder-map`](stakeholder-map/SKILL.md) | Discover | When you start a project, or a decision keeps stalling | Draft |
| [`survey`](survey/SKILL.md) | Discover | When you have survey responses to summarise | Draft |
| [`interview`](interview/SKILL.md) | Discover | When you plan interviews or need to summarise anonymised interview notes | Draft |
| [`framing`](framing/SKILL.md) | Define | When you have checked evidence and need to choose the problem, the opportunities and the hypotheses | Draft |
| [`ideation`](ideation/SKILL.md) | Develop | When you have a chosen opportunity and need to explore and compare solution directions | Draft |
| [`prototype`](prototype/SKILL.md) | Develop | When you have a chosen direction and want a clickable prototype built with your design system | Draft |
| [`build-process-map`](build-process-map/SKILL.md) | Develop | When you need a process map, swimlane or user flow drawn as a diagram (uses `diagram-design/`) | Draft |
| [`user-testing`](user-testing/SKILL.md) | Deliver | When you have a prototype and want to test it with real users and rate the findings | Draft |
| [`handoff`](handoff/SKILL.md) | Deliver | When the design is ready for developers and you need a handoff pack and a measurement plan | Draft |
| [`add-insights`](add-insights/SKILL.md) | Discover, Test | When there is new research (interview, survey, test results) to turn into items | Draft |
| [`add-media`](add-media/SKILL.md) | All stages | When there are images, video, PDFs or documents to put into the report | Draft |
| [`refresh-hub`](refresh-hub/SKILL.md) | All stages | When you want the AI to review where items are not linked or are missing | Draft |
| [`build-report`](build-report/SKILL.md) | All stages | When you need to see the hub in a browser or send it to someone | Draft |
| [`customer-journey-map`](customer-journey-map/SKILL.md) | Define | When you need a customer journey map across stages, touchpoints and emotions | Imported |
| [`diagram-design`](diagram-design/SKILL.md) | All stages | The drawing skill the diagram cards use | Imported |

How the hub works is explained in [`../guides/06-how-the-hub-works.md`](../guides/06-how-the-hub-works.md).

## How to run a step

1. Open the whole project folder in the AI tool. The tool reads `AGENTS.md` at the root by itself.
2. Commit first (if you use Git), so you can go back.
3. Tell the tool: *"Run step 5 of `../toolkit/skills/user-voice-synthesis/SKILL.md`."*
4. Read the result, then check it yourself in the next step. A step labelled **(YOU)** is the part you still do yourself.

## Card format

Each step has fixed lines:

| Line | Meaning |
|---|---|
| **Who** | `YOU` or `AI` |
| **Input** | The files this step may read, and only those files |
| **Instruction** | The prompt given to the AI (only on AI steps) |
| **Output** | The section or file that is written |
| **Check** | What you check before moving to the next step |
| **Failure sign** | The signal that this step has gone wrong |

## Add your own skill

Make a folder with your skill's name. Put a `SKILL.md` in it that starts with a short header (`name`, equal to the folder name, and a one-sentence `description` that says what it does and when to use it), then the card. Add `templates/` for documents it uses and `examples/` for filled-in samples. Keep to at most 8 steps, one working file, and two rules: the AI returns only its own section, and the AI draft is always kept apart from the version you checked.
