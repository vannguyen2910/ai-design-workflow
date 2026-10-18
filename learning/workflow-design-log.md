# Workflow design log

*Updated 2026-10-12. For instructors and for the pitch: why the workspace behind this course is built the way it is, and what went wrong on the way. Students get the shorter `assets/templates/workflow-kit/`.*

## Decisions

| Decision | Why | Alternative rejected | Taught in |
|---|---|---|---|
| Stage pages are built from the work files and the item tables | Copying a verified file into a second page made two versions that drifted | A hand-written page per stage | Module 1, 3 |
| One file per item, relationships declared in one direction | Both directions would disagree sooner or later; the reverse is derived | A table kept in sync by hand | Module 3 |
| Propose first, then create | The student keeps the decision; the AI cannot add an unchecked claim | The AI creates items directly | Module 2 |
| Plain-language prompts, not commands | The students are designers, not developers; the AI picks the right step card | A command reference | Module 1 |
| Warnings in three tiers; a new case starts clean | Twenty equal warnings train people to ignore all of them | One flat list | Module 6 |
| Metrics get a target, a result and a verdict; a Learning page | The chain ended at hand-off; outcomes were never read back | Stop at the measurement plan | Module 7 |
| The report shell is in English; content stays in the author's language | Tool wording stays stable; the author writes for their own readers | Translate everything | Module 1 |
| Generated files carry no timestamp | The same input must give the same output, or merges conflict | A "generated on" footer | Hygiene checklist |

## Failures worth keeping

| What happened | Cause | Fix |
|---|---|---|
| Every merge conflicted on the generated report | A timestamp in the footer | Remove it; output is a pure function of the input |
| A whole menu section went empty with no message | An old-format table row was skipped silently | Name the bad row and the fix |
| A step card told the AI to write into blocks that no longer existed | Rules were not updated with the workflow | Rewrite the card; add a documentation sweep to the hygiene checklist |
| A query "worked" on the author's case and failed on a fresh one | The template relied on sample data | Always test on a case created from scratch |
| A diagram tool refused a flow of eleven steps in one row | A deliberate readability limit | Split the flow, build a scrolling view, or switch tool; weigh what leaves the machine |

## Open

- Whether the lab is its own session, folded into module 6, or a take-home task.
- A facilitation note for the lab (not written).
