# Setup Checklist (Session 0)

Do this **before the first session**, on your own, in about 45 minutes. Each step ends with a **Done when** line: check it on your screen before you move on. If a step does not match what you see, stop there and send a screenshot with the step number. Do not skip ahead.

You do not need to know Git. You click buttons once to set things up, then the AI tool saves your work for you (step 9).

**What you need:** a Mac or Windows computer, an internet connection, and the AI coding tool the programme uses.

---

## 1. Create a GitHub account

1. Go to [github.com](https://github.com) and click **Sign up**. The free plan is enough.
2. Confirm your email.

**Done when:** you are signed in on github.com and see your profile picture at the top right.

## 2. Install GitHub Desktop

1. Download it from [desktop.github.com](https://desktop.github.com). It is **not** in the App Store.
2. Mac: if the page asks which version, check your chip first: Apple menu → **About This Mac**. "Chip: Apple M…" means **Apple silicon**; "Processor: Intel…" means **Intel**.
3. Open the app and sign in with the GitHub account from step 1.

**Done when:** GitHub Desktop opens, and **Settings → Accounts** (Windows: **File → Options → Accounts**) shows your GitHub name.

## 3. Install your AI coding tool

1. Install the AI coding tool the programme uses and sign in.
2. Find the menu item that opens a folder (usually **File → Open Folder**). You will use it in step 6.

**Done when:** the tool opens and you know where **Open Folder** is.

## 4. Create your own repo from the template

1. Open the template link you received.
2. Click the green **Use this template** button → **Create a new repository**.
3. Name it, for example `my-design-workflow`, and choose **Private**.
4. Click **Create repository**.

**Done when:** your browser shows `github.com/<your-name>/<repo-name>`, the folders `my-project`, `demo-project` and `toolkit` are listed, and the word **Private** is next to the repo name.

No **Use this template** button? Message the person who shared the link. Do not download the original repo instead.

## 5. Bring the repo to your machine (clone)

1. In GitHub Desktop: **File → Clone repository**.
2. On the **GitHub.com** tab, choose the repo from step 4.
3. In **Local path**, choose `Documents`. **Not** Google Drive, iCloud, OneDrive or Dropbox: a syncing folder can break files while the AI writes them.
4. Click **Clone**.

**Done when:** `Documents/<repo-name>` exists, and inside it you see `README.md`, `toolkit`, `my-project` and `demo-project`.

## 6. Open the workspace in your AI tool

1. In the AI tool: **File → Open Folder**, then choose `Documents/<repo-name>` (the whole workspace, not `my-project`).

**Done when:** the file list in the AI tool shows `AGENTS.md`, `toolkit`, `my-project` and `demo-project`.

## 7. Create your project

1. In the AI tool's chat, type: *"Tạo một dự án mới tên …"* (or *"Create a new project called …"*), with your project name.
2. Mac only: if a window asks to install "command line developer tools", click **Install**, wait, then ask again.

**Done when:** a new folder with your project name appears next to `my-project`, and the AI tells you the path of the new folder.

## 8. Open the report

1. Double-click `index.html` at the workspace root.
2. Click the card of your project.

**Done when:** your browser shows a card with your project name, and clicking it opens the **Overview** of your project.

## 9. Save and publish your work

1. In the AI tool: **File → Open Folder**, then choose **your project folder** (from step 7). From now on you always open the project folder, not the workspace.
2. In the chat, type: *"Lưu và đăng lên"* (or *"Save and publish"*).
3. The AI lists the files it will save and sends them to GitHub.

**Done when:** on github.com your repo shows your project folder, and GitHub Desktop says **No local changes**.

Two phrases are all you need from now on:

| You say | The AI does |
|---|---|
| *"Lưu lại"* / *"Save"* | Saves a checkpoint on your machine (a commit), with a one-line note |
| *"Lưu và đăng lên"* / *"Save and publish"* | Saves a checkpoint and sends it to GitHub (commit and push) |

---

## When something goes wrong

| You see | Do this |
|---|---|
| GitHub Desktop is not in the App Store | That is normal: download it from desktop.github.com (step 2) |
| The repo is in Google Drive or iCloud | In GitHub Desktop: **Repository → Remove**, then clone again into `Documents` (step 5) |
| The AI cannot find `new-project.py` | You opened `my-project` instead of the workspace. Open the workspace folder (step 6) |
| A page opens but tables and links look raw | You opened a `.md` file. Open `index.html` instead (step 8) |
| "Push" or "authentication" error | Open GitHub Desktop, check you are signed in (step 2), then say *"Lưu và đăng lên"* again |
| Anything else | Screenshot + the step number, sent to the person running the programme |

## Not in Session 0

Branches, pull requests and a public link (GitHub Pages) come later, when you have work to share. See [`03-github-basics.md`](03-github-basics.md) and [`04-share-your-hub.md`](04-share-your-hub.md).
