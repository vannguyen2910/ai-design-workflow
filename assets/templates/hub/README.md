# Experience Hub template

One hub per case: a folder of linked pages that stores every output of the project and lets you cross-check them. This is the series' final report.

## Files
| File | You edit it? | What it is |
|---|---|---|
| `hub-data.js` | **Yes** | The list of every item (O opportunity, H hypothesis, D decision, P principle, T test, M metric), what each links to, the gate status, and the agreement status |
| `index.html` … `case-log.html` (9 pages) | **Yes (content)** | One page per lesson. Write your content; keep the structure |
| `hub.css` | No | The look: black, white and purple only |
| `hub.js` | No | Builds the menu, turns IDs into links, shows what each item connects to, and builds the alignment table and warnings |

## How it works
1. Write each item on its page as `<article class="item" id="O1">`. Use the ID everywhere (O1, H1, D1, P1, T1, M1).
2. Add the same ID to `hub-data.js` with its `links`. Use `{ id: "P8", rel: "strains" }` when a decision pulls against a principle.
3. Open `index.html`. The alignment table and warnings (decisions with no user need behind them, opportunities no decision serves, untested hypotheses, a decision pulling against a principle, missing principles, broken links) build themselves.
4. Any ID you type in the text of a page becomes a link automatically.

## One page per lesson
Scope (shape the brief) → Evidence (discover) → Problem brief (define) → Options, flows, prototype (develop) → Alignment check → Findings (deliver) → Handoff and measurement → Case log. The Overview fills itself.


## Gates
The four gates and their lettered checks (1a to 4d) are the series' single gate list (`../../02-method.md` Part 3, §2). They are written in `hub-data.js` under `gates`. Set each check's `status` to `open`, `passed` or `failed`; the gate's status is worked out for you (all checks passed means passed; any failed means failed; otherwise open). Do not rename the checks; change only the status.

## If the hub shows a setup problem
The hub checks `hub-data.js` and each page, and lists problems in a box at the top of the page. It no longer goes blank.

| What the box says | What it means | Fix |
|---|---|---|
| "hub-data.js could not be read" | A typing mistake in `hub-data.js`: usually a missing comma between two items, a missing quote, or an unclosed bracket. The menu still works, but links and the matrix are off | Undo your last change, or give the file to your AI tool and ask it to find and fix the mistake. A missing comma is often reported on the line after it |
| "Duplicate ID" | Two items share an ID | Give one of them a new number |
| "bad ID" | An ID that is not a letter (O, H, D, P, T, M) and a number | Rename it, for example D3 |
| "Broken link" | An item links to an ID that is not defined | Add the missing item, or correct the ID |
| "the type should be…" | The ID's letter and the type disagree (for example D with "metric") | Fix the type; the hub already uses the right one |
| "its page … is not one of the pages" | An item's `page` is not in the `pages` list | Correct the file name |
| "is listed … for this page but is not written here" | Listed in `hub-data.js`, but the page has no matching block | Add the item block to that page |
| "is written on this page but is missing from hub-data.js" | A block on the page has no entry, so it has no links | Add it to `hub-data.js` |
| "is written twice" | The same ID appears twice on one page | Remove one |
| status or access "must be…" | A gate status or the agreement status has an unknown value | Use open, passed or failed; or agreed, pending, not available |

## Editing hub-data.js safely
- **Keep a copy** of `hub-data.js` before each edit.
- Add items one at a time, and refresh the page after each. The box tells you straight away if something is wrong.
- If you ask an AI tool to edit it, give it the **whole file** and say: *"Add these items. Keep the structure and every key name exactly as it is. Return the complete file, valid JavaScript, with commas between items and no other changes."* Then check the result in the browser before you publish.
- If you ask it to build the entries from your markdown working files, ask it to list any item it is unsure about instead of guessing a link.

## Notes
- The data in `hub-data.js` and the items marked `[EXAMPLE]` are there so you can see it work. Delete them and replace with your own.
- Open `index.html` in a browser; no server needed.
- Use an AI coding tool to turn your markdown working files into page content. Give it this README, `hub-data.js` and one page as a pattern, and ask it to return only the page content and the new `hub-data.js` entries.
- Principles P1 to P10 are Nielsen's 10 heuristics. Add your organisation's principles as P11 onwards.

## Share your hub (private by default; a live link is optional)
A folder on your computer cannot be opened by a stakeholder directly, so you either send it (PDF or zip) or, for a case free to share, publish it as a live link.

**In this course (revised 2026-10-05): your hub is private by default.** It lives in your case folder. To show a stakeholder, export the key pages to PDF or send the folder zipped (see `../publish-guide.md`, "Sharing a private hub"). **Publishing is optional** and only for a case that is free to share. If you publish, you use **GitHub Pages** in your own public repository and update it yourself; the guide is `../publish-guide.md` (optional homework in the first lesson). Your published hub is public to anyone with the link, and you upload only the contents of this `hub/` folder. **The repository that publishes the hub must be public** (free Pages cannot publish from a private one). You may keep your full case folder in a separate private repository as a backup; only the hub repository is published. **You host it and you are responsible for it.** The instructor does not host, upload or moderate hubs. If you do not want a GitHub account, use another free static host from the list below and share the link.

**Outside the course** (your own portfolio or another project), put the whole folder on a free static host yourself:

| Host | How | Free? | Good for | Watch out |
|---|---|---|---|---|
| **Netlify Drop** | Go to app.netlify.com/drop, drag the hub folder in. You get a random web address | Free to publish. **Password protection is paid** (Pro plan) | The simplest path for non-technical designers | Check whether a drop made without an account expires, and make an account to keep it |
| **Cloudflare Pages** | Create a Pages project, choose "Drag and drop your files", upload the folder. You get a `name.pages.dev` address | Free for static sites. Its Access feature can add a login, free for up to 50 users, but takes more setup | Students comfortable with a few more steps, or when a login is needed | More screens to click through than Netlify Drop |
| **GitHub Pages** | Needs a GitHub account and a repository | Free only for **public** sites. Private publishing needs a paid enterprise plan | Not recommended for non-technical designers | A private repository does **not** make the site private |

**Update the link:** upload the folder again to the same project; the address stays the same.
**Open the link in a private browser window before sharing**, to see what a stakeholder sees.

### Privacy: read before you publish
- A free hosted hub is **public to anyone who has the link**, and the link can be forwarded. The pages ask search engines not to index them, but that does not stop people who have the link.
- **Do not publish a client's or employer's confidential data** (real metrics, unreleased product details, user data) unless your company allows it. Check the policy first.
- For the course, use **anonymised or fictional data** for anything you publish.
- If you need it private: a paid password plan (for example Netlify Pro), Cloudflare Access, or your company's own internal hosting. If a login is not possible, share a **PDF export** of the pages instead (print each page to PDF) or send the folder zipped.
- Never put passwords, personal data of users, or unreleased financial figures in the hub.
