---
name: build-report
description: Build the index.html report, then view or send it. Use when you need to see the hub in a browser or send it to someone.
---

# Workflow: Build the report

Export the hub as **one self-contained HTML file** to view in a browser and send to stakeholders, with no AI tool or any other tool needed to read it.

*Status: draft.*

| | |
|---|---|
| When | When you need to see the hub in a browser, or send it to someone |
| Before | Save the files you just edited. The tables rebuild every run, no other step is needed |
| Command | `python3 ../toolkit/tools/build-report.py` |
| Output | `index.html` at the root of the project folder |

## Why a script, not the AI

Turning Markdown into HTML is a deterministic transformation. The script gives the same result every time, does not invent content, sends no data anywhere, and uses no AI quota. The AI tool can only **run the command** for you.

## What goes in the report and what does not

| In | Not in |
|---|---|
| `README.md`, `context/`, `stages/`, `work/`, `insights/`, `standards/` | Sections with "(AI draft)" in the heading, `work/sources/` |
| Every item file (O, H, M, D, E) | `_personal/`, `work/sources/`, `AGENTS.md`, `../toolkit/skills/*.md` |
| `insights/project-log.md`, `standards/principle-checks.md` | `../toolkit/guides/06-how-the-hub-works.md` (a guide for the writer) |

The "How to fill" blocks are left out of the report. Links to files outside the report show as dotted-underlined text and cannot be clicked.

## How the report is organised

The menu sections (Overview, Context, Stages, Work, Insights, Standards) are described in `../toolkit/guides/06-how-the-hub-works.md`, "Where to see the hub".

Items are not in the left menu but in the Insights section, so the report still works with dozens of items. An item not linked to any opportunity is gathered separately at the end of the tree.

**The alignment table and the warnings in the report are computed by the script** from the relationship lines in the item files (the properties `serves`, `metric`, `tests`, `measures`, `follows`, `pulls_against`), from nowhere else, so they always match the item files.

Each item has its own trace (for example O1 › H1 › D2) and a **"Referenced by"** section, because item files declare relationships in one direction only.

## Send to others: a compact bundle

A report is a folder: `index.html` plus the files it uses (images, HTML prototypes...). To send it, make a compact version:

```
python3 ../toolkit/tools/build-report.py --bundle send-to-stakeholders --zip
```

The bundle holds only `index.html` and **exactly the files the documents declare** (`media:` or dropped in the document's folder). It does not hold raw working files, `_raw-private/` or `_personal/`. Images are referenced, not embedded in the HTML, so `index.html` stays light.

## Team version: see the AI drafts too

A working file keeps two sections: `(AI draft)` and `(verified)`. By default the report **hides** every section with `AI draft` in the heading. When you need to see them again (for example to measure the AI's error rate):

```
python3 ../toolkit/tools/build-report.py --team
```

This version folds the drafts and labels them "not checked". **Do not send the `--team` version outside.**

## Step 1: Export

**Who:** YOU (or the AI tool, only to run the command)
**Input:** `README.md`, `context/`, `stages/`, `work/`, `insights/`, `standards/`
**Output:** `index.html` at the root of the project folder

```
python3 ../toolkit/tools/build-report.py
```

The script prints the number of pages, the number of items, and the problems (broken links, IDs that do not match the file name, the number of places that still have sample data).

**Failure sign:** A `!` line about a broken link or an ID that does not match.

## Step 2: Check before sending

**Who:** YOU
**Input:** The HTML file just exported
**Output:** None

Open the file in a browser and check:

- [ ] The black bar "sample data or blanks remain" at the top of the Overview is gone
- [ ] There is no sample content or empty place left
- [ ] The agreement status is correct
- [ ] There is no confidential information or personal data (read every page; the report holds only the hub, but you are the one who wrote the hub)
- [ ] Try opening it on another device

**Failure sign:** You send the report while the black bar is still at the top of the page.

## Naming

The file is always called `index.html` and sits at the root of the project folder, as the **home page of the hub**: double-click to open. The template already has a version built from sample data, so you can see the hub from day one. Each time you edit the hub, rebuild it so the home page matches the new content.

**When you send it to others,** copy the file out and rename it so it is easy to recognise, for example `onboarding-redesign-report-2026-10-11.html`. A file called `index.html` sitting alone in the recipient's inbox says nothing about its content. You can also build the file to send directly with `python3 ../toolkit/tools/build-report.py --out file-name.html`.
