# Hub-first redesign of Lessons 1 and 2

Date: 2026-11-16. Status: draft for approval. Scope: Lesson 1 and Lesson 2 only. Lessons 3 to 6 follow the same method later, one at a time.

## Intent and why

A learner of batch 1 told Winnie, after reading the landing page, that the course looked like an ordinary design project and that mid and senior people already know the basic process. They want to learn how to use AI well at each step.

Winnie's vision is unchanged: teach the end-to-end design workflow, centralised in a Knowledge Hub that becomes the shared "brain" an AI reads from and writes to, in the way Andrej Karpathy describes an LLM-maintained wiki (raw sources that never change, a wiki the AI writes, a schema file that tells the AI how to work). What changes is the emphasis. The basic design process is recalled quickly. The time goes to what senior people do not yet know: how to set up the hub, how to get trustworthy material into it, and how to check what the AI produces.

The landing page (live since 2026-11-16) already promises this, so the lessons must catch up before batch 1 starts on 2026-12-10.

## Goals

After Lesson 1 and 2, a learner can:

1. Explain the three layers of a hub (raw sources, wiki, schema) and the three rules that keep it trustworthy: raw sources are never edited by AI, every note has an ID, every quote is word for word.
2. Explain, in two sentences, why a company may keep one hub per function (business, technical, design) and connect them through shared IDs, and name three ID rules (stable, never reused, a prefix per function).
3. Turn their own interview transcripts into source notes with IDs, and run a machine check that every quote the AI cites really exists in the note it cites.
4. Describe what blind synthesis shows: the same notes, summarised once without a hypothesis and once with the team's hypothesis in the prompt, and why the second version leans toward the hypothesis.

## Non-goals

- No team exercise. Learners practise alone; the multi-hub idea is theory only.
- No new tool or paid service. The machine check is a small script an AI coding tool writes and runs for the learner.
- No redesign of Lessons 3 to 6 in this document, except the one dependency named below.
- No claims about measured gains from the hub pattern. Sources quoted in blogs are vendor claims and are not used.

## Anti-goals (a failure even if it technically works)

- The lessons sound like AI hype. The landing page was already toned down; the lessons keep that tone.
- A learner leaves able to run the commands but not able to say why the check matters.
- Basic design process content is deleted so completely that a junior reader of the sample case gets lost. It is shortened, not removed.

## Constraints (house rules already agreed with Winnie)

- Written from the learner's view; lean; no prescribed folder structure; no topic name inside practice files (the practice topic may change per batch); no company constraints on AI use (learners use their own accounts and may use AI freely).
- Trade terms stay in English (hub, schema, ingest, source notes, insight, evidence, assumption, hypothesis, scope, package). Vietnamese editing follows the vi-voice rules.
- No em dash. No specific AI tool names in lesson content: use "AI chat tool" and "AI coding tool".
- No employer or client name in lesson content. The multi-hub idea comes from a discussion with practitioners at a large financial company; the lessons say "large companies" or "some large companies".
- Lesson file, practice file, slide outline and the live slide deck must agree. Live decks are Slides artifacts (Lesson 1: Dmc6zgaZrHQYunwHCeCVXa; Lesson 2: 5imC8V6rhuh6XrztMw32F6) and are edited one slide at a time.

## Evidence used

From the Karpathy gist (April 2026): the three layers, the ingest, query and lint operations, and the argument that maintenance cost approaches zero when an AI does the bookkeeping. A commenter's benchmark found wiki-only retrieval weaker than retrieval with the source documents; this is self-reported and unverified, so the lessons teach "keep raw sources and check back to them".

From practitioner and academic writing on AI research synthesis: the common failures are invented themes (a pattern seen in 2 of 20 interviews presented as dominant), fabricated quotes that read better than real ones, lost outliers, and confirmation bias when the hypothesis is in the prompt. UX researchers report low trust in AI insights mainly because of missing traceability.

From writing on context files (AGENTS.md or similar): keep them short and specific, add a line when the AI repeats a mistake. A 2026 arXiv study found modest gains and about 20% higher inference cost, which supports "write less and test it".

From requirements traceability and data mesh writing: stable IDs that are never reused, a unique ID on every layer, forward and backward checks, a small set of shared fields (owner, status, version), and a rule that joining on shared IDs can fail silently when schemas differ. None of these sources is a standard for design hubs; the lessons present the multi-hub idea as a pattern companies are trying.

## Approaches considered

- **A. Add an "advanced AI" block to each lesson, keep the structure.** Cheapest, but the course still reads as process plus some AI, so the feedback is not addressed.
- **B. Re-spine the course around hub operations (schema, ingest, query, lint), keep the weekly topics.** Chosen. Each week teaches one hub operation through one design stage.
- **C. Change the landing page only.** Rejected: the learner would be disappointed in week 2.

Placement choices made with Winnie: blind synthesis happens in Lesson 2 on the course's sample data, not in Lesson 3 on the learner's own data. The machine quote check happens in Lesson 2, at the moment the learner's own transcripts become source notes.

## Design

### Lesson 1: schema and hub

Theory (`design-process-with-ai-lesson.md`):

- Keep and shorten the sections on background, the four stages and the core AI concepts. Target: about one third shorter, and every kept section answers "what does AI do here, and how does the result reach the hub".
- Expand section 6 (workspace and hub) into the main section of the lesson: the three layers, the three rules (raw never edited by AI, every note has an ID, every quote word for word), the index and log files, and why a schema file should be short and specific.
- Add a new section "One hub or many": why a function may own its hub; the shared-ID thread (a chain from business goal to opportunity to decision to technical constraint to test, each item carrying an ID and pointing to the one above); the three ID rules; the small shared fields owner, status and version; and two risks (a join can be silently wrong when structures differ; the AI is fast but a person still opens both sources to check). The course's own IDs (source IDs such as I01-03, insight IDs such as IN-01) are shown as a small example of the same idea. Example prefixes such as BIZ, DES and TEC are the author's illustration, not a standard.
- This section is theory only. No exercise.

Practice (`design-process-with-ai-practice.md`): change only Step 4 (README do AI soạn). Its last bullet today offers `AGENTS.md` as optional. It becomes a normal part of the step: the AI drafts `AGENTS.md`, and the learner checks that it states the three hub rules (raw sources are never edited, every note has an ID, every quote is word for word) and rewrites them in their own words. The file stays short. No new step, no new folder requirement. Step 5 (the saved-file comparison) is unchanged.

### Lesson 2: ingest

Theory (`discover-the-problem-lesson.md`):

- Keep Discover, principles, Break the brief and interviews, shortened in the same way as Lesson 1.
- Add a section "Ingest: from transcript to source notes". It covers: cutting a transcript into notes with one idea and one ID each; why quotes must be word for word; and the machine check, explained as a plain string comparison: for every cited ID, the quoted text must appear in that note. A pass or fail list is the result. The check is by a program, not by another AI judgement.
- Add a section "Blind synthesis". Demonstration on the sample data (`assets/starter-files/course-case/source-notes.md`, 24 notes). Run 1: ask an AI chat tool to summarise the main reasons customers leave, with no hypothesis. Run 2: same notes, with "the team believes price is the main reason" in the prompt. The sample data already contains the setup: only 2 of 24 notes mention price (IN-04 and IN-07 in `insight-set.md`). The point for learners: compare what each run says about price and which notes each run cites.
- Section 5 ("What goes into the hub") gains one line: the learner's own outputs use IDs under the same convention.

Practice (`discover-the-problem-practice.md`): add Part C after Part B.

- Heading follows the existing pattern of the file: "Phần C · Ingest vào hub" and "Step 9 · Ingest: transcript thành source notes". Section titles in the lesson stay in English, as in the current lesson.
- Step 9 · Ingest, in four parts:
  1. **Cut:** cut each anonymised transcript into source notes, one idea per note, one ID per note in the form `I01-03` (interview number, note number). Notes are stored one per row as `ID | text`. This format is fixed so the check can read it; folders stay free.
  2. **Cite:** ask an AI chat tool for three candidate insights, each as a row `insight | note IDs | one word-for-word quote`. This is a mini-step to produce something checkable. The full synthesis stays in Lesson 3.
  3. **Check:** ask an AI coding tool to write and run a small check: for every row, confirm the quoted text appears in each cited note (ignoring differences in whitespace and quotation marks), and print a pass or fail list.
  4. **Fix:** fix every failure by hand, or ask the AI chat tool again with the failing IDs listed, then re-run. Put the notes and the clean check result in the hub.
- Learners with fewer than 2 interviews, or none, use the sample interview extracts in the course case pack (the same fallback Lesson 3 already uses) and say so in the hub.
- With 2 interviews there are only 10 to 20 notes. That is enough, because the thing being checked is the AI's quotes, not the learner's notes; the lesson says this plainly.
- Output and self-check lines are updated to include source notes and a clean check.
- Blind synthesis is not a practice step here. A one-line pointer sends the learner to repeat it on their own notes in Lesson 3.

### Dependency on Lesson 3

Lesson 3 Practice Step 1 currently cuts transcripts into source notes with IDs. After this change that work is done in Lesson 2. The builder changes Lesson 3 Step 1 to "start from the source notes from Practice 2, and repeat the blind comparison on your own notes". Nothing else in Lesson 3 changes in this scope; a full Lesson 3 pass is the next brainstorm.

### Outputs to produce

1. Revised lesson, practice and slide-outline files for Lessons 1 and 2, in sync.
2. Edited live slides for Lessons 1 and 2 (new and changed slides only; speaker notes in the project's note format).
3. The one-line Lesson 3 Step 1 change above.
4. A prepared pair of prompts for the blind synthesis demo (no-hypothesis and hypothesis), stored with the sample data.
5. The quote-check instruction text for the learner to give their AI coding tool.

## Success criteria

- A reader who has not seen the old lessons can say, from Lesson 1 alone, what the three layers and three rules are.
- The blind synthesis demo, run on the sample data before it is taught, produces a visible difference between the two runs. If it does not, the demo is rewritten before it goes into the lesson. This must be run, not assumed.
- The quote check, run on the sample notes with one deliberately altered quote, reports exactly that quote as a failure.
- Lesson, practice, outline and deck agree on step names and counts.

## Calls made by the author (after the builder check)

These settle questions a builder would otherwise have had to guess. Winnie can overrule any of them.

- Transcripts and fallback: learners with fewer than 2 transcripts use the sample extracts and label them as sample.
- Citation format: a row of `insight | note IDs | one word-for-word quote`, produced by a mini-step in Step 9, not by a full synthesis.
- Note and ID format: fixed and minimal (`ID | text`, IDs like `I01-03`). The "no prescribed folders" rule covers folders only, not this format.
- Blind synthesis demo: run once before class on the sample data, and show the saved outputs of both runs on slides. A live re-run is optional for the instructor. If the two outputs do not differ visibly, the prompt pair is rewritten before the lesson goes out.
- Naming: practice files keep the current Vietnamese pattern (Phần C, Step 9); lesson section titles stay in English.
- Order of work: lesson, practice and outline files first, reviewed by Winnie; live decks last, one slide at a time, each read back after publishing; Winnie reviews the decks before any link is shared.

## Left to the builder

- The exact cut list for the basic sections, within the "about one third shorter" target.
- Slide counts and the order of new slides.
- The wording of the quote-check instruction and the script it produces (a string comparison that ignores differences in whitespace and quotation marks).
- Whether the multi-hub section is one slide or two.

## Open items for Winnie

- Lesson 1 still contains a theory section "Career directions" and a learning objective about it, although the practice step was removed. Keep it as theory, or cut it as part of the shortening? This document assumes cut; say if you want it kept.
- Whether the blind synthesis demo should also appear as an optional hands-on step later (this document says no).

## Sources

Karpathy gist (April 2026); articles on LLM wiki as agent memory; literature review on generative AI for UX research; practitioner guides on AI research synthesis; guides on AGENTS.md and the arXiv study on context files; guides on requirements traceability; writing on data mesh federated governance. Full links were given in the brainstorming conversation and can be restored on request.
