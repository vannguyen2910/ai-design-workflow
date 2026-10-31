#!/usr/bin/env python3
"""Check the toolkit: every skill folder has a SKILL.md named like the folder, and every
`toolkit/...` path or Markdown link written in the workspace text files points at a file that exists.
Reports only; exit 1 if anything is wrong.

    python3 toolkit/tools/check-toolkit.py
"""
import os
import re
import sys

WS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # the workspace root
SKIP = {".git", "node_modules", "diagram-design", "_raw-private", "_personal"}
PATH_RX = re.compile(r"(?:\.\./)?toolkit/(?:skills|templates|guides|tools|diagram-design)/[\w./-]*[\w]")
LINK_RX = re.compile(r"\]\(([^)#\s]*(?:SKILL\.md|guides/[^)#\s]+|templates/[^)#\s]+))(?:#[^)]*)?\)")  # links into the toolkit only
OLD_RX = re.compile(r"toolkit/skills/[\w-]+\.(?:md|py)\b")  # the layout before skills became folders
errors = []

skills = os.path.join(WS, "toolkit", "skills")
for d in sorted(os.listdir(skills)):
    if os.path.isdir(os.path.join(skills, d)):
        card = os.path.join(skills, d, "SKILL.md")
        head = open(card, encoding="utf-8").read(400) if os.path.isfile(card) else ""
        if not re.search(r"^name:\s*%s\s*$" % re.escape(d), head, re.M):
            errors.append("skills/%s: no SKILL.md whose name is %s" % (d, d))

for root, dirs, files in os.walk(WS):
    dirs[:] = [d for d in dirs if d not in SKIP]
    for f in files:
        if not f.endswith((".md", ".py", ".yml")):
            continue
        p = os.path.join(root, f)
        rel = os.path.relpath(p, WS)
        for i, line in enumerate(open(p, encoding="utf-8", errors="ignore"), 1):
            for m in OLD_RX.finditer(line):
                if not m.group(0).endswith("README.md"):
                    errors.append("%s:%d old path %s" % (rel, i, m.group(0)))
            for m in PATH_RX.finditer(line):
                target = os.path.join(WS, m.group(0).replace("../", "", 1) if m.group(0).startswith("../") else m.group(0))
                if "<" not in m.group(0) and not os.path.exists(target):
                    errors.append("%s:%d missing %s" % (rel, i, m.group(0)))
            if f.endswith(".md"):
                for m in LINK_RX.finditer(line):
                    url = m.group(1)
                    if re.match(r"[a-z]+:", url) or url.startswith("/"):
                        continue
                    if not os.path.exists(os.path.normpath(os.path.join(root, url))):
                        errors.append("%s:%d broken link %s" % (rel, i, url))

print("\n".join(errors) if errors else "toolkit OK")
sys.exit(1 if errors else 0)
