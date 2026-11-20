"""Reference script for check-evidence-instruction.md.

Checks every quote in the evidence notes against the raw transcript turn it points to,
and checks each note's frontmatter. Not used in class: it shows the instruction is
precise enough for a script to follow.
"""
import pathlib
import re
import sys
from dataclasses import dataclass

REQUIRED = ["id", "outcome", "status", "confidence", "source", "tags"]
QUOTE_LINE = re.compile(r'^>\s*["“](.*)["”]\s*\((\w+),\s*turn\s*(\d+)\)\s*$', re.M)


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


def check_dir(evidence_dir, raw_dir):
    evidence, raw = pathlib.Path(evidence_dir), pathlib.Path(raw_dir)
    seen, results = {}, []
    for f in sorted(evidence.glob("*.md")):
        text = f.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
        if not m:
            results.append(Result(f.name, ["no frontmatter"]))
            continue
        fm = dict(re.findall(r"^(\w+):\s*(.*?)\s*(?:#.*)?$", m.group(1), re.M))
        problems = [f"missing field {k}" for k in REQUIRED if not fm.get(k)]
        nid = fm.get("id", "")
        if nid in seen:
            problems.append(f"duplicate id {nid}")
        seen[nid] = f.name
        if fm.get("outcome") and nid.split("-")[0] != fm["outcome"]:
            problems.append("outcome does not match id prefix")
        quotes = QUOTE_LINE.findall(m.group(2))
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
        results.append(Result(f.name, problems))
    return results


if __name__ == "__main__":
    out = check_dir(sys.argv[1], sys.argv[2])
    for r in out:
        print(("OK     " if r.ok else "NOT OK ") + r.name + ("" if r.ok else ": " + "; ".join(r.problems)))
    sys.exit(0 if all(r.ok for r in out) else 1)
