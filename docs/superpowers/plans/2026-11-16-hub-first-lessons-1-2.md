# Hub-first Lessons 1 and 2 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rewrite Lessons 1 and 2 (lesson, practice, slide outline, live deck) so the course teaches the hub as the AI's shared memory, a machine quote check, a blind synthesis demo, and the multi-hub idea.

**Architecture:** Content project, not software. Two small verified assets come first (a reference quote-check script with tests, and a blind synthesis prompt pair with saved outputs) because the lessons teach what they prove. Then lesson, practice and outline files for Lesson 1, then Lesson 2 (plus one line in Lesson 3), then a Vietnamese and house-rule pass, then Winnie's review, then the live decks.

**Tech Stack:** Markdown lesson files; Python 3 standard library for the reference script and its `unittest` tests; Slides artifacts edited through the Artifact tool; Vietnamese editing skills (`vi-voice`, `translationese-cleaner-vi`, `style-guide-vi`, `grammar-checker-vi`).

**Spec:** `docs/superpowers/specs/2026-11-16-hub-first-lessons-1-2-design.md` (approved). Read it first; the "Calls made by the author" section settles formats.

## Global Constraints

- Learner view; lean; no prescribed folders; no topic name inside practice files; no company constraints on AI use.
- Trade terms stay English (hub, schema, ingest, source notes, insight, evidence, assumption, hypothesis, scope, package). Practice headings follow the existing pattern: "Phần C · …", "Step 9 · …". Lesson section titles stay English.
- No em dash anywhere. No AI tool names (use "AI chat tool", "AI coding tool"). No employer or client name; say "large companies".
- Note format `ID | text`, IDs like `I01-03`; citation row `insight | note IDs | one word-for-word quote`. Example prefixes BIZ, DES, TEC are illustrations only.
- Lesson, practice, outline and deck agree on step names and counts. Lesson 1 keeps its "Career directions" section and objective 1.
- Live decks: Lesson 1 `Dmc6zgaZrHQYunwHCeCVXa`, Lesson 2 `5imC8V6rhuh6XrztMw32F6`; edit one slide at a time; publish with the slide as `file_path`; after a refusal do a bare `read` of the artifact URL, redo the edit, publish.

## Review Focus

1. A quote that differs only by curly versus straight quotes, extra spaces or line breaks must still pass; a quote with one changed word must fail.
2. A cited ID that does not exist in the notes must fail with its own message, not crash.
3. A quote that is real but cited against the wrong note ID must fail.
4. The blind synthesis outputs may not differ visibly on some runs; the lesson must not claim a difference that the saved outputs do not show.
5. A learner whose notes are not in `ID | text` form (extra spaces, missing ID, duplicate ID) gets a clear message from the check instruction, not a silent pass.

---

### Task 0: Commit the pending work first

**Files:** the eight modified lesson files already in the working tree.

- [ ] **Step 1:** Run `git status --short` and confirm only Lesson 1 to 3 lesson, practice and outline files are modified.
- [ ] **Step 2:** Commit them in one commit: `git add lessons/ && git commit -m "Sync Lessons 1 to 3 practice, lesson and outline with live decks; keep trade terms in English"`. This keeps later diffs readable.

### Task 1: Reference quote check, with tests

**Files:**
- Create: `tests/hub_quote_check/check_quotes.py`
- Create: `tests/hub_quote_check/test_check_quotes.py`
- Create: `tests/hub_quote_check/fixtures.py` (notes and rows, built from `assets/starter-files/course-case/source-notes.md`)

**Interfaces:**
- Produces: `parse_notes(text: str) -> dict[str, str]` (reads `ID | text` rows; raises `ValueError` naming the line on a missing ID, empty text or duplicate ID); `check_rows(notes: dict[str, str], rows: list[tuple[str, list[str], str]]) -> list[Result]` where `Result` is a dataclass `(row_index: int, status: "pass" | "fail", reason: str)`. A row is `(insight, note_ids, quote)`.
- Consumes: nothing.

- [ ] **Step 1: Write failing tests** in `test_check_quotes.py`: `test_pass_exact_quote`, `test_pass_curly_vs_straight_quotes_and_whitespace`, `test_fail_one_word_changed`, `test_fail_unknown_id` (reason contains the ID), `test_fail_quote_in_wrong_note`, `test_parse_notes_rejects_missing_id`, `test_parse_notes_rejects_duplicate_id`. Use real notes from the sample file; the changed-word case alters R03 or F04.
- [ ] **Step 2:** Run `python3 -m unittest discover -s tests/hub_quote_check -v`. Expected: all fail with import errors.
- [ ] **Step 3:** Implement both functions in `check_quotes.py`. Normalise by unifying quotation marks, collapsing whitespace and lowercasing before a substring test; a row passes only if the quote is in every cited note.
- [ ] **Step 4:** Run the same command. Expected: all pass.
- [ ] **Step 5:** Commit: `git add tests/hub_quote_check && git commit -m "Add reference quote check used to verify the Lesson 2 instruction"`.

### Task 2: Quote-check instruction for learners, verified

**Files:**
- Create: `assets/starter-files/course-case/check-quotes-instruction.md`

**Interfaces:**
- Consumes: Task 1 behaviour (it defines what the instruction must ask for).
- Produces: the instruction text quoted in Practice 2 Step 9.

- [ ] **Step 1:** Write the instruction in Vietnamese for an AI coding tool: read a notes file in `ID | text` form and a citations table in `insight | note IDs | quote` form; for every row confirm the quote appears in each cited note, ignoring whitespace and quotation-mark style; print a pass or fail list with a reason per failure; stop with a clear message if a note has no ID, is empty, or repeats an ID.
- [ ] **Step 2:** Verify it works: give the instruction to an AI coding tool in a scratch folder with the sample notes and a citations table that contains one altered quote. Expected: exactly that row fails, nothing else. If it silently passes a bad note format, tighten the instruction and repeat.
- [ ] **Step 3:** Commit.

### Task 3: Blind synthesis prompt pair and saved outputs

**Files:**
- Create: `assets/starter-files/course-case/blind-synthesis.md`

**Interfaces:**
- Consumes: `assets/starter-files/course-case/source-notes.md` (24 notes).
- Produces: two prompts (no hypothesis; hypothesis "the team believes price is the main reason customers leave"), the saved output of each, and a short comparison table (what each run says about price; which note IDs it cites).

- [ ] **Step 1:** Write the two prompts. They differ only by the hypothesis sentence.
- [ ] **Step 2:** Run each prompt in a fresh, separate session with only the 24 notes attached, and save both outputs verbatim under the prompts.
- [ ] **Step 3:** Compare. Expected: run 2 gives price more weight than the notes support (2 of 24). If the difference is not visible, rewrite the hypothesis sentence or the question and repeat Steps 2 and 3, up to three times; if still not visible, stop and report to Winnie, because the lesson cannot claim the effect.
- [ ] **Step 4:** Add the comparison table and one line stating the sample limits (24 notes, one app). Commit.

### Task 4: Lesson 1 theory

**Files:**
- Modify: `lessons/01-design-process-with-ai/materials/design-process-with-ai-lesson.md`

**Interfaces:**
- Produces: section titles and counts that the outline (Task 6) and deck (Task 12) copy.

- [ ] **Step 1:** Shorten sections 1, 3 and 4 by about one third; every kept paragraph answers "what does AI do here, and how does the result reach the hub". Keep section 2 (Career directions) unchanged.
- [ ] **Step 2:** Expand section 6 into the main section: three layers, three rules, index and log files, schema file short and specific.
- [ ] **Step 3:** Add a section "One hub or many" with the five points in the spec (why per-function hubs; shared-ID thread with a worked chain; three ID rules; owner, status, version; two risks). Say "large companies"; no company name; no exercise. Present it as a pattern companies are trying, not a standard.
- [ ] **Step 4:** Update "Nội dung buổi học" and "Sau buổi học, bạn có thể" so each objective maps to a section; add objectives for the three layers and the multi-hub idea.
- [ ] **Step 5:** Verify: `grep -n "—" <file>` returns nothing; `grep -niE "claude|chatgpt|cursor|copilot|NAB" <file>` returns nothing. Commit.

### Task 5: Lesson 1 practice

**Files:**
- Modify: `lessons/01-design-process-with-ai/materials/design-process-with-ai-practice.md` (Step 4 only; update Output and Self-check lines that mention `AGENTS.md`)

- [ ] **Step 1:** Make the last bullet of Step 4 a normal part of the step: the AI drafts `AGENTS.md`; the learner checks that it states the three hub rules and rewrites them in their own words; the file stays short.
- [ ] **Step 2:** Add one self-check line: "Can you say what each of the three rules protects?". Verify no other step changed (`git diff --stat` shows one file, edits only in Step 4 and the lists). Commit.

### Task 6: Lesson 1 slide outline

**Files:**
- Modify: `lessons/01-design-process-with-ai/materials/design-process-with-ai-slide-outline.md`

- [ ] **Step 1:** Rewrite the outline to match Task 4's sections: slide titles at most 6 words, kickers not repeating titles, speaker notes in the bullet-plus-"Câu hỏi cho lớp" frame. Add slides for the three layers, the three rules, "One hub or many" (one or two slides, with the chain example).
- [ ] **Step 2:** Verify: slide count and section order equal the lesson; no em dash; no tool or company name. Commit.

### Task 7: Lesson 2 theory

**Files:**
- Modify: `lessons/02-discover-the-problem/materials/discover-the-problem-lesson.md`

- [ ] **Step 1:** Shorten sections 1 to 4 by about one third, same rule as Task 4.
- [ ] **Step 2:** Add section "Ingest: from transcript to source notes" (cutting into notes with IDs, word-for-word quotes, the machine check explained as a plain string comparison, pass or fail list, a program not another AI judgement).
- [ ] **Step 3:** Add section "Blind synthesis" using Task 3's saved outputs and table as the worked demonstration; state the 24-note limit.
- [ ] **Step 4:** In section 5 add one line: the learner's outputs use IDs under the same convention. Update the contents list and objectives (add: explain what the quote check proves; describe what blind synthesis shows).
- [ ] **Step 5:** Verify as in Task 4, Step 5. Commit.

### Task 8: Lesson 2 practice and the Lesson 3 pointer

**Files:**
- Modify: `lessons/02-discover-the-problem/materials/discover-the-problem-practice.md`
- Modify: `lessons/03-research-you-can-trust/materials/research-you-can-trust-practice.md` (Step 1 only)

**Interfaces:**
- Consumes: Task 2's instruction text.
- Produces: Step 9 and Output lines that Lesson 3 Step 1 refers to.

- [ ] **Step 1:** Add "Phần C · Ingest vào hub" and "Step 9 · Ingest: transcript thành source notes" with the four parts (cut, cite, check, fix), the sample-extract fallback, and the plain statement that the check verifies the AI's quotes, not the learner's notes. Quote the Task 2 instruction. Add a one-line pointer to repeat the blind comparison on their own notes in Lesson 3.
- [ ] **Step 2:** Update Goal, Output and Self-check to include source notes and a clean check.
- [ ] **Step 3:** In Lesson 3 Step 1, change "cut transcripts into notes" to "start from the source notes from Practice 2, and repeat the blind comparison on your own notes". Change nothing else in Lesson 3. Verify with `git diff --stat` that only these lines moved.
- [ ] **Step 4:** Commit.

### Task 9: Lesson 2 slide outline

**Files:**
- Modify: `lessons/02-discover-the-problem/materials/discover-the-problem-slide-outline.md`

- [ ] **Step 1:** Rewrite to match Task 7: new slides for ingest, the quote check, blind synthesis run 1 and run 2 (saved outputs), and the comparison. Same title, kicker and notes rules as Task 6.
- [ ] **Step 2:** Verify slide count and order equal the lesson. Commit.

### Task 10: Vietnamese and house-rule pass

**Files:** all Task 2, 3, 4, 5, 6, 7, 8, 9 files.

- [ ] **Step 1:** Run the three Vietnamese editing skills in order (`translationese-cleaner-vi`, `style-guide-vi`, `grammar-checker-vi`) on every new or changed Vietnamese passage. Keep trade terms in English.
- [ ] **Step 2:** Run `grep -rn "—" lessons/01-* lessons/02-* assets/starter-files/course-case` (nothing expected in changed files) and the tool and company name grep from Task 4. Fix any hit.
- [ ] **Step 3:** Check that each practice step name appears identically in the lesson, outline and Output list. Commit.

### Task 11: Winnie reviews the written files (gate)

- [ ] **Step 1:** Link the changed files to Winnie, with the Task 3 comparison table and Task 2 result. Do not start the decks until Winnie says the files are right. Apply requested changes; if a change alters a section title or step count, repeat Task 10, Step 3.

### Task 12: Live deck, Lesson 1

**Files:** slides of Artifact `Dmc6zgaZrHQYunwHCeCVXa`, edited in a scratchpad copy.

- [ ] **Step 1:** Read `project/deck.json` and the slides to change. Edit and add slides to match Task 6, in the deck's existing style (v4 inline or v5 classes, whichever the deck uses); speaker notes in the project note format; Vietnamese editing as in Task 10.
- [ ] **Step 2:** Publish one slide at a time; send `deck.json` only when order or slide set changes. After each publish, read the slide back and compare with the outline.
- [ ] **Step 3:** Confirm the practice slide matches Practice 1 Step 4. Report the link; the deck stays private until Winnie shares it.

### Task 13: Live deck, Lesson 2

**Files:** slides of Artifact `5imC8V6rhuh6XrztMw32F6`.

- [ ] **Step 1 to 3:** Same as Task 12, against Task 9 and Practice 2 Step 9. The blind synthesis slides show the saved outputs from Task 3 side by side, with the price lines highlighted. Report the link.

---

## Self-review (run once)

- Spec coverage: goals 1 to 4 map to Tasks 4, 7 (layers and rules, multi-hub, ingest and check, blind synthesis); the Lesson 3 dependency to Task 8; outputs 1 to 5 to Tasks 2, 3, 4 to 9, 12, 13. The spec's success criteria map to Task 3 Step 3 (visible difference), Task 2 Step 2 (altered quote), Task 10 Step 3 (agreement).
- Step scan: code appears only as signatures and test names; no step says "handle edge cases".
- Types: `parse_notes` and `check_rows` names are used identically in Tasks 1 and 2.
- Proportion: the plan is shorter than the work it describes and shorter than the combined spec and sources.
