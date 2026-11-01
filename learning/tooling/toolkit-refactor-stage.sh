#!/bin/sh
# Stage ONLY the toolkit refactor (2026-10-28) in workspace-template. Run from workspace-template/.
# Part 1 stages every file that belongs to the refactor and nothing else. It ends with `git status`, commits nothing.
# Part 2 (below, comments) lists the five files where your earlier edits and the refactor share one file.

cd "$(dirname "$0")/../workspace-template" || exit 1

git add -A -- \
  toolkit/skills toolkit/templates toolkit/tools toolkit/guides toolkit/README.md \
  .github README.md .claude/skills \
  demo-project/insights/README.md demo-project/standards/principle-checks.md demo-project/work/README.md \
  my-project/insights/README.md my-project/standards/principle-checks.md my-project/work/README.md \
  my-project/index.html \
  ':!toolkit/skills/diagram-design' \
  ':!toolkit/skills/customer-journey-map/SKILL.md' \
  ':!toolkit/skills/customer-journey-map/template.md' \
  ':!toolkit/skills/customer-journey-map/examples' \
  ':!toolkit/templates/generic.md'

# Note: pestel-analysis, stakeholder-map and survey moved into skills/<name>/templates/ and still carry your earlier edits,
# so they are staged with your changes inside them.
git status --short | head -5; echo "..."

# Part 2, run by hand with `git add -p <file>` (answer y or n per hunk; use s to split a hunk):
#   AGENTS.md                                  y, y, n   (3 hunks: the last one, "6. Write plain, clean content", is yours)
#   demo-project/AGENTS.md                     y x8, then n   (the last hunk, "Write content to be read by people", is yours)
#   my-project/AGENTS.md                       y x8, then n   (same last hunk)
#   demo-project/work/final-prototype/index.md n, y, n   (only the "Note: this is the version with compressed images" hunk is the refactor)
#   .gitignore                                 press s to split the hunk, then y for the comment line that now says toolkit/tools/build-report.py,
#                                              and n for the "Personal notes never leave your computer" lines (yours)
#
# Not part of the refactor, leave for your own commits:
#   demo-project/index.html (generated, 91 hunks mostly regenerated output; CI rebuilds it), toolkit/diagram-design/* (deleted),
#   toolkit/skills/diagram-design/, toolkit/skills/customer-journey-map/{SKILL.md,template.md,examples/},
#   toolkit/templates/generic.md, demo-project/work/*, demo-project/work/journey-map.md
