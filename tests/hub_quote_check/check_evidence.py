"""Reference script for check-evidence-instruction.md.

Checks every quote in the interview note files against the raw transcript turn it points to,
and checks each note's fields and tags. Not used in class: it shows the instruction is
precise enough for a script to follow.
"""
import pathlib
import re
import sys
from dataclasses import dataclass

REQUIRED = ["outcome", "status", "confidence", "source", "tags"]
QUOTE_LINE = re.compile(r'^>\s*["“](.*)["”]\s*\((\w+),\s*turn\s*(\d+)\)\s*$')
NOTE_HEAD = re.compile(r"^##\s+(\S+)\s+·\s+(.*)$")
FIELD = re.compile(r"^-\s+(\w+):\s*(.*?)\s*$")
TAG_DEF = re.compile(r"^-\s+`([^`]+)`")


@dataclass
class Result:
    name: str
    problems: list

    @property
    def ok(self):
        return not self.problems


def norm(s):
    s = s.replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
    return re.sub(r"\s+", " ", s).strip().lower()


def read_turns(path):
    turns = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^(\d+)\s+(.*)$", line)
        if m:
            turns[int(m.group(1))] = m.group(2)
    return turns


def split_notes(text):
    """Yield (id, title, field dict, quote tuples) for each `## ID · title` block."""
    block = None
    for line in text.splitlines():
        h = NOTE_HEAD.match(line)
        if h:
            if block:
                yield block
            block = (h.group(1), h.group(2), {}, [])
        elif block:
            f, q = FIELD.match(line), QUOTE_LINE.match(line)
            if f:
                block[2][f.group(1)] = f.group(2)
            elif q:
                block[3].append(q.groups())
    if block:
        yield block


def check_dir(evidence_dir, raw_dir):
    evidence, raw = pathlib.Path(evidence_dir), pathlib.Path(raw_dir)
    tags_file = evidence / "tags.md"
    known = {m.group(1) for l in tags_file.read_text(encoding="utf-8").splitlines() if (m := TAG_DEF.match(l))} if tags_file.exists() else None
    seen, results = set(), []
    for f in sorted(p for p in evidence.glob("*.md") if p.name != "tags.md"):
        notes = list(split_notes(f.read_text(encoding="utf-8")))
        if not notes:
            results.append(Result(f.name, ["no notes found"]))
        for nid, _title, fm, quotes in notes:
            problems = [f"missing field {k}" for k in REQUIRED if not fm.get(k)]
            if nid in seen:
                problems.append(f"duplicate id {nid}")
            seen.add(nid)
            if fm.get("outcome") and nid.split("-")[0] != fm["outcome"]:
                problems.append("outcome does not match id prefix")
            if not quotes:
                problems.append("no quote lines")
            for quote, raw_name, turn in quotes:
                raw_file = raw / f"{raw_name}.txt"
                if not quote.strip():
                    problems.append("empty quote")
                elif not raw_file.exists():
                    problems.append(f"raw file {raw_name} not found")
                else:
                    turns = read_turns(raw_file)
                    if int(turn) not in turns:
                        problems.append(f"turn {turn} not found in {raw_name}")
                    elif norm(quote) not in norm(turns[int(turn)]):
                        problems.append(f"quote not in {raw_name} turn {turn}")
                if f"{raw_name} @ turn {turn}" not in fm.get("source", ""):
                    problems.append(f"source {raw_name} @ turn {turn} not in source field")
            if known is None:
                problems.append("tags.md not found")
            else:
                for t in (x.strip() for x in fm.get("tags", "").strip("[]").split(",") if x.strip()):
                    if t not in known:
                        problems.append(f"tag {t} not in tags.md")
            results.append(Result(nid, problems))
    return results


if __name__ == "__main__":
    out = check_dir(sys.argv[1], sys.argv[2])
    for r in out:
        print(("OK     " if r.ok else "NOT OK ") + r.name + ("" if r.ok else ": " + "; ".join(r.problems)))
    sys.exit(0 if all(r.ok for r in out) else 1)
