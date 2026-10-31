# Toolkit

Everything shared by the projects in this workspace. The home page that lists every project is the `index.html` at the workspace root. **You do not fill anything in here.** Each project (`my-project`, `demo-project`, your own) sits outside this folder.

| Folder | What it holds | When to open it |
|---|---|---|
| `guides/` | Step-by-step guides: the setup checklist (start here), get the folder onto your machine, set up a project, GitHub, share the report, Obsidian | The first time, or when you are stuck |
| `templates/` | The one template no skill uses (`generic.md`). The other templates sit inside each skill | When you start a new document |
| `skills/` | One folder per skill: the steps for the AI tool (`SKILL.md`), its templates and examples. Includes the `diagram-design` skill the AI tool uses to draw process maps, user flows and other diagrams | Rarely: the AI tool reads them itself |
| `tools/` | The scripts: `new-project.py` (create a project with one command), `build-report.py` and `build-home.py` (build the `index.html` pages), `new-item.py`, `serve-hub.py`, `flow-from-mermaid.py` | When you want a new project; the AI tool runs the others |

Create a new project (from the workspace root):

```
python3 toolkit/tools/new-project.py project-name
```

Details: [`guides/02-set-up-your-project.md`](guides/02-set-up-your-project.md).
