# Course site: one link per student hub

Every student hub has one permanent web address that opens anywhere, with no login, and can be sent by email. Student projects are public by design (decided 2026-10-05).

**How hubs get published (decided 2026-10-05):** students publish their own hub on GitHub Pages in their **own public repository** (guide: `../publish-guide.md`, Assignment 2 of the first lesson), so they own the link and update it themselves. This course site is the **landing page** that lists the hubs, and the **fallback host** for students who do not want a GitHub account.

## Set up once (instructor)
1. On GitHub, create a **public** repository, for example `ai-design-workflow-hubs`.
2. Upload the contents of this `course-site/` folder to the repository root: `index.html`, `hubs.js`, `.nojekyll`, `README.md`, and the empty `hubs/` folder (add a placeholder file such as `hubs/.gitkeep` because GitHub does not keep empty folders).
3. In the repository: **Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch: `main`, folder `/ (root)` → Save.**
4. After a minute the site is live at `https://<your-account>.github.io/<repository>/`.
   A student hub at `hubs/<slug>/` is then at `https://<your-account>.github.io/<repository>/hubs/<slug>/`.
   (If you create a repository named `<your-account>.github.io`, the address has no repository part.)

## List a student hub
**Student-hosted hub (the default):** the student sends you their live link. Add one line to `hubs.js` with `url` set to that link, and `consent: true` once they agree to be listed. Nothing needs uploading.

**Fallback, hosted by you (student has no GitHub account):** follow the steps below, then add the line to `hubs.js` without `url`.

1. The student sends the hub **folder** (zipped, or in a shared drive folder). It contains `index.html`, the other pages, `hub.css`, `hub.js`, `hub-data.js`.
2. Put it in `hubs/<slug>/`. Choose a lowercase slug with no spaces. Use a pseudonym slug if the student prefers, because the address is public.
3. In `hubs.js`, add one line for the student and set `consent: true` **only after they agreed to a public link** (and to how their name is shown).
4. Commit. The link is live in about a minute. Email that link to the student, who can send it to stakeholders.

How to upload without Git (browser only): open the repository → **Add file → Upload files** → drag the files in → **Commit changes**. A browser upload takes up to 100 files per commit, each up to 25 MB ([GitHub docs on adding files](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository)). A hub is about 13 files plus the prototype, so one upload is usually enough. For nested folders, drag the folder itself.

## Update or remove
- **Student-hosted:** the student updates their own repository; the listed link does not change. To remove from the list, delete the line in `hubs.js`; the student can delete their repository themselves.
- **Hosted by you:** upload the changed files into the same `hubs/<slug>/` folder. To remove, delete the folder and its line in `hubs.js`. Cached copies can last a few minutes.

## Limits and checks
- A published Pages site may be no larger than 1 GB, with a soft bandwidth limit of 100 GB a month ([GitHub Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits)). Ask students to compress large images and keep each file under 25 MB. 30 hubs at 30 MB each is about 1 GB, so watch the total.
- Free Pages publishing needs a **public** repository. A private repository does not make a Pages site private (see `../hub/README.md`).
- Pages carry a no-index tag, which asks search engines not to list them. It does not hide the link.
- **Before publishing:** open the link in a private browser window to see what a stakeholder sees; check the hub shows no employer confidential data; check the student agreed.

## Student rules (said in the first lesson, written in the guide)
- The hub is public to anyone with the link. Choose a case you are free to share.
- Only the contents of `hub/` go online. Anything you do not want public (real company figures, unreleased details, personal data of users) stays out.
- You can change or remove it any time.

## Later (optional)
A GitHub Action could publish any hub folder a student uploads without you touching it, and each student could own a repository of their own for a portfolio. Both need more setup than the first version needs; not built.
