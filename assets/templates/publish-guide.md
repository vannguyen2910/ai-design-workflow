# Publish Your Hub: a Step-by-Step Guide

**For students. Optional. About 25 to 30 minutes. No coding and no Git commands: everything happens in your web browser.**
**Your hub is private by default.** Use this guide only if your case is free to share (a course case, or a cleaned-up version of your work). By the end you will have one web address for your hub. It opens on any device with no login, you can email it to anyone, and you can update it yourself. If your case is confidential, skip this guide and use the next section.

## Three ideas first
- **GitHub** is a website that stores folders of files online.
- A **repository** (people say "repo") is one such folder on GitHub.
- **GitHub Pages** turns a repository that contains a website into a live site at a web address.

## Before you start: what goes online
- **Only the contents of your `hub/` folder go online.** Your `00-context` files, notes, sources and working files stay on your computer.
- A free GitHub Pages site is **public to anyone who has the link**. Choose a case you are free to share. Leave out confidential company figures, unreleased details and users' personal data.
- Your GitHub username will appear in the address. If you prefer not to use your real name, pick a username you are comfortable showing.
- **You host this hub and you are responsible for it:** the link, what is on it, and what you choose to make public. The instructor does not host or upload hubs for you.
- If you do not want a GitHub account, use another free host that works by dragging a folder in (the options are in `hub/README.md`), and share that link instead.

## Sharing a private hub (the default)
If you use these templates on your employer's real project, **do not publish that hub.** It stays on your computer. To show a stakeholder:
- **PDF:** open the hub in a browser, print each key page to PDF (the Overview, the problem brief, the findings), and send the PDFs.
- **Zipped folder:** zip the `hub/` folder and send it; the recipient unzips it and opens `index.html`. Check that it opens on another device first.
- **Your company's own tools:** attach the PDFs to your company's wiki or document system.
A private web link would need a paid password plan or your company's own hosting; that is outside this course. Publish a hub only for a case you are free to share, such as a course case or a cleaned-up version of your work.

## Public or private repository?
- **The repository that publishes your hub must be public.** On a free GitHub account, Pages only publishes from a public repository. A private repository does **not** make the website private, and publishing from a private repository needs a paid plan.
- **You can still use a private repository, for a different job:** keep your *whole* case folder (context files, sources, working files) in a separate **private** repository as a backup with version history. Nothing in it is ever published. This is optional.
- A good habit: one **private** repository for the case, one **public** repository that contains only the hub.

The trade-off of this course: you need a GitHub account to publish. In return you get a free live link that you own and can update yourself.

## Steps

### 1. Create a free GitHub account
Go to github.com and choose **Sign up**. Use an email you check. Confirm the email when GitHub asks.

### 2. Create a public repository
1. Select **+** at the top right, then **New repository**.
2. Name it something like `my-case-hub` (lowercase, hyphens, no spaces).
3. Choose **Public**. (Free Pages sites need a public repository.)
4. Tick **Add a README file** so the repository is not empty.
5. Select **Create repository**.

### 3. Upload the contents of your hub folder
1. In your repository, choose **Add file → Upload files**.
2. Open your `hub/` folder on your computer, select **everything inside it** (`index.html`, the other pages, `hub.css`, `hub.js`, `hub-data.js`) and drag it into the browser window.
3. Check that `index.html` is at the top level of the list, not inside a folder. If it ends up inside a folder, the address will have an extra part and may not work.
4. Scroll down and select **Commit changes**.

A single upload takes up to 100 files, each up to 25 MB. Compress large images first.

### 4. Turn on GitHub Pages
1. In the repository, open **Settings**, then **Pages** in the left menu.
2. Under **Build and deployment**, set **Source** to **Deploy from a branch**.
3. Set **Branch** to **main** and the folder to **/ (root)**, then select **Save**.
4. Wait one to two minutes and refresh the page. A message appears: *Your site is live at* with your web address. It looks like `https://your-username.github.io/my-case-hub/`.

### 5. Check it like a stakeholder would
Open the address in a **private (incognito) window**. You should see your hub's Overview page, with the menu on the left. If you see an error page, see "If something goes wrong" below.

### 6. Update it, and prove you can
1. Change one small thing in `hub-data.js` on your computer, such as the case name.
2. In your repository, choose **Add file → Upload files** and drag the changed file in.
3. Select **Commit changes** and wait a minute.
4. Refresh your link. The same address now shows the change.

You will repeat this every time you add a page to the hub. The address does not change.

## Send it
Send the instructor your live link.

## If something goes wrong
| What you see | Likely cause | Fix |
|---|---|---|
| "404" or a blank page | `index.html` is not at the top level of the repository, or Pages is not on yet | Check step 3 (index.html at the top) and step 4; wait two minutes |
| The page shows but has no styling or menu | `hub.css` or `hub.js` was not uploaded, or was moved | Upload all hub files together, in the same place |
| The old version still shows after an update | Your browser kept a copy | Refresh again, or open it in a private window |
| The address changed | The repository was renamed | Do not rename the repository; if you must, share the new address |
| Upload fails | A file is over 25 MB or there are over 100 files in one go | Compress images; upload in two batches |

## You can change or remove it any time
To take it down, delete the repository in **Settings** (scroll to the bottom). To change what is shown, upload new versions of the files.

*GitHub's own steps may look slightly different over time. If a button has moved, the idea is the same: a public repository, the hub files at its top level, and Pages turned on for the main branch.*
