---
name: prototype
description: Build a clickable prototype of the chosen direction from your Figma design system and designed screens. Rules first, then the design system in code, the shell, optional patterns, then the whole journey in one pass, then review. Use when you have a chosen direction, a flow and a design system in Figma.
---

# Workflow: Prototype

Build a clickable prototype of the direction you chose. Set the rules first, turn your Figma design system into code, build the shell every screen sits in, feed in your flow, let the AI build the whole journey in one pass, then review. The order is: **rules, design system, shell, patterns (optional), flow, build, review.** The AI builds, you check.

*Status: draft. Try it on a real project and adjust it before you rely on it.*

| | |
|---|---|
| Working folder | `work/prototype/` (copy `../toolkit/skills/prototype/starter/` if it is not there). `work/prototype/index.md` holds the scope, shell, screen plan and known gaps |
| Sources | Your design system and designed screens in Figma, `work/options.md`, `work/problem-brief.md`, `work/user-flow.md` (your flow: the AI does not invent it), `context/design-system-notes.md`, `standards/principle-checks.md` |
| Rules file | `work/prototype/project-rules.md` (give it to the AI coding tool at every build step) |
| Original data | `work/sources/_raw-private/` (the AI does not read it) |
| Output | A prototype that runs in a browser, plus `index.md` with the scope and known gaps |
| Related | `../toolkit/skills/ideation/SKILL.md` before; `../toolkit/skills/add-media/SKILL.md` to show it in the report |

The prototype is a **reference for developers and a thing to test with users**, not production code. The AI must not invent colours, components or sizes.

## Sections of `work/prototype/index.md`

| Section | Step | By |
|---|---|---|
| `## Scope` | 1 | YOU |
| `## Shell and templates` | 2 | YOU |
| `## Screen plan` | 6 | YOU |
| `## Plan check (AI)` | 6 | AI. **Do not edit** |
| `## Build log` | 3, 4, 5, 7 and 8 | AI lists changed files, YOU write the verdict |
| `## Rule check (AI)` | 8 | AI. **Do not edit** |
| `## Known gaps` | 9 | YOU |

Two rules: the AI changes only the files for the step you asked for, and you never accept "done" until you have opened the page yourself.

## Step 1: Scope

**Who:** YOU · **Output:** `## Scope`

Write: the one flow (start, goal, end); 3 to 6 screens that are already designed in Figma; clickable HTML with real content; the real content the screens need (names, labels, messages).

**Check:** Can someone finish the flow in one sitting? **Failure sign:** "The whole app"; no real content.

## Step 2: Rules, shell and templates

**Who:** YOU · **Output:** `## Shell and templates`, and the same rules in `project-rules.md`

The rules come first, because they decide everything the AI builds. The **shell** is the frame around every screen. A **template** is the layout of one kind of screen. Fix all three now, so the screens do not each invent their own.

- **Rules.** Start from the ten rules in `project-rules.md`: five about the system, five about how you and the tool work. Read each rule: can you check it by opening a file? Rewrite the vague ones. Add your content voice (rule 5): how labels, messages and terms are written, so the same thing always has the same name.
- **Shell.** Read it off your designed screens. Answer: header or not; side navigation or not; product name; the navigation items; where the main action goes; what happens on a narrow screen.
- **Templates.** Pick 2 or 3, for example Home, List, Detail, Form. For each: when to use it, its areas (main, side, actions), and which components it holds.

**Check:** Can you say which template each screen of your flow will use? **Failure sign:** "Each screen can look different"; a navigation you have not decided.

## Step 3: Build the design system · Gate A

**Who:** AI, then YOU · **Output:** `tokens.css`, `components.css`, `components.html`, and a line in `## Build log`

Your design system exists in Figma. Here it becomes code, so every later step can use it and nothing else.

> Read `project-rules.md` first. From my Figma design system, build `tokens.css` (colour, type, spacing, radius) and `components.css` with `components.html`, one example of every component in every state. Use only the tokens and components I list below. If something is missing or unclear, say so and stop. Do not touch any file I did not name. List every file you changed and everything you were unsure about.
>
> *(Paste your token list and component list, or give the Figma link if your tool can read it.)*

Then you check. Open `components.html` and compare each component and state with Figma. Search the files for raw values (`#` colours, `px` sizes outside the tokens). Send fixes back in **one list**. If it is right, say **"Lưu lại"** (the AI saves a checkpoint). Record the notes in `context/design-system-notes.md`.

**Gate A:** Does every component and state match Figma? Is every colour and size a token? Is every missing piece written down?
**Failure sign:** A component you did not list; a hard-coded colour; a state that Figma has and the page does not.

## Step 4: Build the shell · Gate B

**Who:** AI, then YOU · **Output:** the shell files (header, navigation, empty main area), and a line in `## Build log`

This is screen 0. The shell is put together from your tokens and components, and it is built only here: later screens never add navigation.

> Read `project-rules.md` first. Build only the shell from my `## Shell and templates`: header, navigation and an empty main area. Use only the variables in `tokens.css` and the components in `components.css`. If a component you need is missing, say so and stop. Make it work with the keyboard, with a visible focus. Do not touch any file I did not name. List every file you changed and everything you were unsure about.

Then you check. Tab through the navigation with the keyboard. Open it at a phone width and a desktop width. Search the files the AI touched for raw values. If it is right, say **"Lưu lại"**. If not, send back the fix and check again.

**Gate B:** Does the shell match your answers in step 2 and the shell in your Figma screens? Does it work with a keyboard and at both widths? Is every colour and size from the design system?
**Failure sign:** A new CSS file; a hard-coded colour; navigation items you did not list.

## Step 5: Build experience patterns (optional)

**Who:** AI, then YOU · **Output:** the experience patterns in `components.css` and `components.html`, and a line in `## Build log`

Do this only when the same group of components appears on two or more screens, for example search, navigation, a sign-in form, a list with filters, a confirmation box or an empty state. Skip it when each group appears once.

> Read `project-rules.md` first. Build these experience patterns from existing components only: [list]. Add no new component. Show each pattern in `components.html`. List every file you changed and everything you were unsure about.

**Check:** Is each experience pattern used on at least two screens? Is it made only of existing components? **Failure sign:** A new component hidden inside a pattern; a pattern used once.

## Step 6: Feed the flow · Gate C

**Who:** YOU, then AI, then YOU · **Output:** `## Screen plan`, `## Plan check (AI)`

First you write the plan from your own flow (`work/user-flow.md`) and your designed screens, one row per screen: name, template, content (real, not "lorem ipsum"), states (empty, loading, error, success), and where the user goes next.

Then the AI checks the plan against your design system. It does not change the plan.

> Check my `## Screen plan` against my design system. Do not change the plan. For each screen list: the components it needs that are not in `components.css`, marked "MISSING"; the content that is missing, marked "unknown"; the states with no content. Say what you are unsure about. Return only this section.

Then you decide each "MISSING": use an existing component, or add it yourself to the design system, and update `context/design-system-notes.md` and `project-rules.md` in the same go. The AI does not add it for you.

**Gate C:** Can the flow be finished with these screens? Does each screen have a template? Is every component either existing or decided?
**Failure sign:** A plan the AI wrote for you; "MISSING" components left for the AI to improvise.

## Step 7: Build the journey

**Who:** AI · **Output:** the screen files, and lines in `## Build log`

One pass for the whole journey, because the rules, the design system and the shell now constrain the result.

> Read `project-rules.md` first. Build the whole journey from my `## Screen plan`: every screen inside the shell, each one following its template. Use only the variables in `tokens.css` and the components in `components.css`. Use my real content; where something is missing, write "unknown" and list it at the end. Do not add navigation. Make everything work with the keyboard, with a visible focus, and move focus to the new heading when the screen changes. Do not touch any file I did not name. List every file you changed and everything you were unsure about.

**Failure sign:** Navigation of its own on a screen; a new CSS file; a hard-coded colour; a component you did not list; a screen not in the plan.

## Step 8: Review · Gate D

**Who:** AI, then YOU · **Output:** `## Rule check (AI)`, your verdict in `## Build log`

The AI checks first, so you start from a list.

> Check the prototype against `project-rules.md` and the principle checks, without changing any file. List every place that breaks a rule, with file and line: raw colour or size values; components not in the design system; a screen outside the shell or with navigation of its own; a screen that does not follow a listed template; an input without a visible label; an error without a message beside the field; meaning carried by colour alone; a touch target under 44 px; more than one `<h1>`; focus not moved on a screen change. Say what you could not check. Do not fix anything.

Then you review. This is the longest step and where your design judgement lives.

- Open three of the places the AI listed: are they real?
- Open every screen and use it: click every control, tab through it, open it at a phone and a desktop width. Compare with the plan, with your Figma screens and with `components.html`.
- Send fixes back in **one list**. An error that repeats across screens usually sits below the screens: fix it at the broadest layer the symptom is still true at (token, component, pattern, shell, template, rules file), then rebuild. An error on one screen is fixed on that screen.
- Rewrite each rule the AI broke or that was missing, in your own words, and update `context/design-system-notes.md` and `project-rules.md`.

When it is right, say **"Lưu lại"** (the AI saves a checkpoint).

**Gate D:** Does it match the plan? Does it work with a keyboard and at both widths? Is every colour and size from the design system? Is every broken rule fixed or written down?
**Failure sign:** You read the AI's report instead of opening the page; "no issues found" without saying what was checked.

## Step 9: Known gaps · Gate E

**Who:** YOU · **Output:** `## Known gaps`, and decisions

Fix the breaks that matter, or write them down. Write what the prototype does **not** do (states not built, content faked, screens missing), so nobody tests or hands off something that looks finished but is not. Record choices as decisions: `new-item.py D --title "..." --reason "..." --state proposed`. Add the prototype to the report with `../toolkit/skills/add-media/SKILL.md`.

**Gate E:** Can a tester finish the flow? Is every gap written down?

## If a gate is not met

| Gate | If no |
|---|---|
| A | Fix the design system before building the shell: every later step uses it |
| B | Fix the shell before building any screen: a wrong shell spreads to every screen |
| C | Cut screens until one flow can be finished |
| D | Send back one fix list, then check again |
| E | Write the gaps down, or fix them before testing |

---

A prototype that runs shows the idea **can** work, not that it **does**. The proof is the page you opened and used yourself.
