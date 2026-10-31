# Project rules (give this file to your AI coding tool)

*Most AI coding tools read a rules file from the project folder every time. Your tool may expect a particular file name (check its documentation); copy this text into that file, or keep this one and tell the tool to read it first. These are ten starter rules: rewrite them in your own words after your first build.*

## What you are building
A clickable prototype of the flow in `work/options.md`, as plain HTML, CSS and a little JavaScript. It is a reference for developers, not production code.

## System rules
1. **Only use components from the inventory** (`design-system/components.css`, shown in `design-system/components.html`). If a component you need is missing, **say so and stop**: ask me to add it to the inventory first, then build. Do not add libraries, frameworks, fonts or images from other sites.
2. **No raw values, ever.** Use only the variables in `design-system/tokens.css`, and flag what does not exist. Do not write raw colours, font sizes or spacing values.
3. **Screens inherit the template and sit inside the shell; they do not fork either.** The shell and the templates are in `index.md` (`## Shell and templates`). Do not add navigation of your own. If no template fits, say so and stop.
4. **Every build carries the flow context:** the flow in `work/user-flow.md` and where this screen sits in it.
5. **Real content in one voice, never lorem ipsum.** Use the content notes in `work/options.md` and the content voice written in `index.md` or `context/design-system-notes.md`. If content is missing, write "unknown" and ask.

## Working rules
6. **One layer per edit, named in the prompt:** token, component, shell, template or screen.
7. **Attach only the files the step needs.** Do not change files I did not ask you to change.
8. **Flag, don't invent.** Every build ends with the files you changed and everything you could not do or were unsure about.
9. **Save before a structural edit.** I will say "Lưu lại" when a checkpoint should be saved.
10. **WCAG 2.1 AA on every screen:** contrast, visible focus, target size (at least 44 px). Also:
    - One `<h1>` per screen, inside `<main>`. Every input has a visible `<label>`.
    - Everything works with a keyboard; focus moves to the new heading when the screen changes.
    - Errors say what went wrong and how to fix it, are shown next to the field, and are announced (`role="alert"`).
    - Meaning is never carried by colour alone.
