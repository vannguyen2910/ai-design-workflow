---
type: "prototype"
title: "Prototype"
stage: "Develop"
status: "planned"
summary: "Where the prototype lives: a starter design system and the rules file for the AI coding tool."
supports: []
---
# Prototype starter

A small design system, a rules file and an empty page, so you can build your first version without setting anything up. **If you have your own design system in Figma, build it as code (step 3 of `SKILL.md`) and use this starter only as a pattern.**

| File | What it is |
|---|---|
| `design-system/tokens.css` | The variables: colour, type, spacing, radius, touch target |
| `design-system/components.css` | Button, field, radio card, card, badge, alert, step indicator |
| `design-system/components.html` | Every component and state, on one page |
| `design-system/README.md` | The design system notes, written for an AI coding tool |
| `project-rules.md` | The rules file: give it to your AI coding tool |
| `index.html` | An empty page to build on |

## Steps
1. Copy this whole folder into your project as `work/prototype/` (the AI tool can do it: *"Copy `toolkit/skills/prototype/starter` to `work/prototype`"*). Work in the copy, not here.
2. Open `design-system/components.html` in a browser and look at what exists.
3. Decide your rules, your shell (the frame around every screen) and 2 or 3 templates, and write them in `project-rules.md` and in `index.md` under `## Shell and templates` (see `toolkit/skills/prototype/SKILL.md`, step 2).
4. Have the AI coding tool build your design system from Figma, then the empty shell, and check each one at a phone and a desktop width (steps 3 and 4). Build patterns only if a group of components repeats (step 5, optional).
5. Give the tool `project-rules.md`, your flow and your content notes, and have it build the whole journey in one pass. Then review every screen yourself.
6. Save a working copy after each check you are happy with.
