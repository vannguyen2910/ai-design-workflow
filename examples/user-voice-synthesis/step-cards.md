# Step Cards — User-Voice Synthesis

**Created:** 2026-10-05 · **Status: draft, untested.** Second worked example of the standard in `../../02-method.md` Part 1, using the card format in `../../02-method.md` Part 2. Pattern: A Investigate. Diagram: `../../assets/diagrams/user-voice-synthesis-activity-flow.svg`. The AI instructions are my design and have not been run in a class. Uses generic labels per CLAUDE.md.

**Why this is the main Discover example.** Competitor analysis shows what rivals do. It cannot show why users behave as they do. User voice (what real people say in reviews, forums and interviews) is the evidence designers most need and most often synthesise badly. This flow keeps the AI on real quotes and makes every theme traceable.

## What counts as user voice
| Source | Primary or secondary | Good for | Watch out for |
|---|---|---|---|
| **Public reviews and forum or community posts** (app stores, review sites, user forums) | Secondary, real words | Pains, expectations, vocabulary, at scale | Skew to extremes and to people who write; fake reviews; no context about the person |
| **Short interviews** (3 to 5 people who use the product, 15 to 20 minutes) | Primary | The why behind behaviour, past events, context | Small sample; friends are polite; leading questions; **personal data**, so consent and anonymising |
| **Support tickets and feedback** (if you have access) | Secondary or internal | Real problems in the wild | Data safety: usually personal or internal; anonymise and use an approved tool only |
| **Survey open-text** (if you ran one) | Primary | Many short answers | Shallow; self-selected |

For the default outside-in case, use public reviews and forum posts plus 3 to 5 short interviews with people who use the product. Aim for at least 30 quotes from at least 3 sources or people, so a theme can be judged.

## Pairing rule (Discover as a whole)
Every Discover evidence pack combines **"what others do"** (competitor analysis or desk research) with **"what users say or do"** (this flow). Each answers a different question and covers the other's blind spot.

## The working file (one file, one folder)
```
user-voice-synthesis-[product]/
├── user-voice-synthesis.md     ← the one working file; each step fills one section
├── sources/                    ← anonymised quotes with IDs (R01…, I01-01…), interview notes, consent notes
```
| Section | Filled in step | By |
|---|---|---|
| `## Scope` (question, who, beliefs) | 1 | You |
| `## Sources and guide` | 2 and 3 | Step 2: AI suggestions go in, labelled. Step 3: your final list of sources and interview guide |
| `sources/` (quotes with IDs) | 4 | You: collect and anonymise |
| `## Coding (AI draft)` | 5 | AI. **Never edit.** |
| `## Coding (verified)` | 6 | You: a copy you correct |
| `## Themes` (counts, counter-quotes) | 7 | AI |
| `## Opportunities + limits` | 8 | You |

Same two safety rules as every flow: the AI returns only its own section, and the AI draft and your verified copy stay separate.

## If a gate fails
| Gate | After step | Supports stage check | If the answer is no |
|---|---|---|---|
| A: right voices? | 3 | (local to this activity) | Go back to step 2 and widen the sources |
| B: word for word and traceable? | 6 | 1b, 1c | Rerun step 5 with a tighter instruction (many errors), then verify again |
| C: weighed, not counted? | 8 | 1b, and 2a when the opportunity feeds the brief | Go back to step 7 and redo the synthesis |

Stage checks are in `../../02-method.md` Part 3, §2.

---

## Step 1 — Frame the question (YOU)
**Goal:** Know whose voice you need and what you want to learn, and write down what you already believe.
**Do:** Fill `## Scope`: the question from your scope; who you need to hear from (which users, what situation); what you hope to learn (a behaviour or a pain, not a feature); what you already believe (3 to 5 statements, to test in step 7).
**Check:** Is the question about people's past behaviour and problems, not about whether they would like your idea?
**Failure sign:** "What do users think of feature X?" with no situation or behaviour.
**Output:** `## Scope`

## Step 2 — Suggest (AI)
**Goal:** Widen where you listen and sharpen what you ask.
**Give the AI:** the `## Scope` section only.
**Instruction essentials:**
> Using only the scope below, suggest where real users of this product talk about it in public (types of source, not specific invented pages), and draft eight interview questions. Questions must ask about past behaviour and real situations ("tell me about the last time…"), not opinions about ideas, and must not lead. Do not invent sources or quote anyone. Say what you are unsure about. Return only the two lists.

**Check:** Any source you cannot actually find? Any question that suggests an answer?
**Failure sign:** Invented forum names; questions like "would you use…".
**Output:** AI suggestions pasted under `## Sources and guide`, labelled

## Step 3 — Review the voices (YOU) · Gate A
**Goal:** Decide whose voice you will hear, and who you are missing.
**Do:** Edit into your final list of sources and your interview guide, with a reason for each. Add voices the AI missed. Agree consent for interviews: people know it is for a course project, and that you will remove names.
**Gate A questions:**
- Who is missing? (Light users, people who left, people who never signed up.)
- Is the sample skewed (only angry reviews, only friends, only one segment)?
- Is consent clear and recorded?

**Failure sign:** Everyone you chose thinks like you; no consent note.
**Output:** final `## Sources and guide`

## Step 4 — Collect + anonymise (YOU)
**Goal:** Gather the raw quotes and make them safe and checkable.
**Do:** Export or copy at least 30 quotes from public sources and run 3 to 5 short interviews (record with permission; take notes or transcribe). **Anonymise before the AI sees anything:** remove names, usernames, emails, company names (find and replace on your computer, not by asking the AI). Give every quote an ID (R01… for reviews, I01-01… for interview 1, quote 1) and keep it word for word. Save to `sources/`.
**Data safety (from the first lesson):** reviews are public but usernames can identify people; interviews are personal data. If the case is real work at your company, keep the files private and use only an approved tool.
**Failure sign:** Quotes paraphrased "to tidy them up"; no IDs; names left in.
**Output:** files in `sources/`

## Step 5 — Code (AI)
**Goal:** Group the quotes into themes without inventing any.
**Give the AI:** the `## Scope` section and the anonymised quotes in `sources/`.
**Instruction essentials:**
> Using only the quotes below, group them into themes. For each theme give a short name, then list the ID and the exact text of every quote in it, word for word. Never paraphrase, shorten or invent a quote. Put quotes that fit nowhere in "unclassified". If a theme has fewer than three quotes, or quotes from fewer than two sources or people, label it "weak". If you cannot tell, say "unknown". Return only the table.

**Failure sign:** Quotes that do not appear in the source; no "unclassified"; every theme "strong".
**Output:** `## Coding (AI draft)` (do not edit)

## Step 6 — Verify (YOU) · Gate B
**Goal:** Confirm the coding is true to the quotes.
**Do:** Copy the draft to `## Coding (verified)`. (1) Check **every quote cited for your top three themes** is word for word: search the text in `sources/`. (2) Check a random 20% of the rest. (3) Read ten quotes from "unclassified" and ten from other themes: did the AI leave out or misplace something important? (4) Fix errors; note the count of misquotes and misplaced quotes, and the error rate, at the top.
**Better still, once:** code 20 quotes yourself first, then compare with the AI's grouping.
**Gate B questions:**
- Is every quote word for word, with an ID?
- Do the themes survive a sample you read yourself?
- Is the error rate acceptable? If many are wrong, go back (see the table above).

**Failure sign:** You only checked the first few; no error rate recorded.
**Output:** `## Coding (verified)`

## Step 7 — Synthesise + test (AI)
**Goal:** Turn themes into needs and pains, then test them.
**Give the AI:** the `## Scope` section (with your beliefs) and `## Coding (verified)` only, **not** the AI draft.
**Instruction essentials:**
> From the verified coding, list the needs and pains that matter for the question in the scope. For each: how many quotes and from how many sources or people, one example quote with its ID, and a counter-quote if there is one. Then, for each, give the strongest argument that it is wrong or misleading, and say what evidence would change your mind. Go through my beliefs one by one and say whether the quotes support, contradict or do not address each. Do not recommend actions yet. Say what this sample cannot tell us. Return only this section.

**Failure sign:** Generic needs ("users want simplicity"); no counter-quotes; every belief "supported".
**Output:** `## Themes`

## Step 8 — Interpret + decide (YOU) · Gate C
**Goal:** Turn themes into opportunities, weighed by what matters.
**Do:** Weigh each theme by **severity** (how bad when it happens), **context** (who, when) and **reach** (how many different people), not only by how many quotes mention it. Write 3 to 5 opportunity statements as user needs, not features, each with its quote IDs. State the limits of the sample. Add the page to your hub (Evidence), with opportunities that will feed the problem brief.
**Gate C questions:**
- Does each opportunity rest on severity and context, not only on count?
- Could you defend it by showing the quotes?
- Have you said what this sample cannot tell you?

**Failure sign:** The top theme by count becomes the top opportunity without thought; quote IDs missing.
**Output:** `## Opportunities + limits`, and the Evidence page in the hub → feeds **Define**.

---

## Limits to say out loud
This shows what people **say**, not what they **do**. Reviews lean to extremes, friends are polite, samples are small. Treat themes as hypotheses. Test them with real users later in the series.

## To test before teaching
1. Run it on one case with at least 30 quotes and 3 interviews; time each step. Step 4 (collect and anonymise) will probably take longest.
2. Measure the misquote rate in the AI's coding. If above about 5%, tighten the step 5 instruction. *(The threshold is my guess.)*
3. Compare the AI's themes with your own coding of 20 quotes. How much do they agree?
4. Check whether the step 7 counter-argument is a real argument or a token sentence.
5. Check anonymising really removed identifiers (try searching for a name).
