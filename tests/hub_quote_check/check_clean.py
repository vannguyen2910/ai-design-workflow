"""Reference script for check-clean-instruction.md.

Compares a cleaned transcript with the anonymised draft it came from, turn by turn.
The only allowed differences are formatting and the filler words the learner declared.
Not used in class: it shows the instruction is precise enough for a script to follow.
"""
import pathlib
import re
import sys
from dataclasses import dataclass

DRAFT_LINE = re.compile(r"^\[\d\d:\d\d:\d\d\]\s+([^:\s]+):\s*(.*)$")
CLEAN_LINE = re.compile(r"^(\d+)\s+([^:\s]+):\s*(.*)$")
QMARK = "[?]"


@dataclass
class Result:
    name: str
    problems: list

    @property
    def ok(self):
        return not self.problems


def words(text, drop=()):
    text = text.replace("’", "'").replace(QMARK, " ")
    found = re.findall(r"[\w']+", text.lower())
    return [w for w in found if w not in drop]


def check_clean(draft_path, clean_path, fillers, names=()):
    fillers = {f.lower() for f in fillers}
    draft = [m.groups() for l in pathlib.Path(draft_path).read_text(encoding="utf-8").splitlines() if (m := DRAFT_LINE.match(l))]
    clean = [m.groups() for l in pathlib.Path(clean_path).read_text(encoding="utf-8").splitlines() if (m := CLEAN_LINE.match(l))]
    if len(draft) != len(clean):
        return [Result("file", [f"draft has {len(draft)} lines, clean has {len(clean)} turns"])]
    results = []
    for i, ((d_spk, d_text), (num, c_spk, c_text)) in enumerate(zip(draft, clean), 1):
        problems = []
        if int(num) != i:
            problems.append(f"turn number {num} should be {i}")
        if d_spk != c_spk:
            problems.append(f"speaker differs: draft {d_spk}, clean {c_spk}")
        d_words, c_words = words(d_text, fillers), words(c_text)
        if d_words != c_words:
            diff = next((j for j, (a, b) in enumerate(zip(d_words, c_words)) if a != b), min(len(d_words), len(c_words)))
            problems.append(f"words differ at word {diff + 1}: draft '{' '.join(d_words[diff:diff + 3])}', clean '{' '.join(c_words[diff:diff + 3])}'")
        if QMARK in c_text:
            problems.append("marked [?]: listen to the recording and fix")
        for name in names:
            if re.search(rf"(?<!\w){re.escape(name)}(?!\w)", c_text, re.I):
                problems.append(f"name {name} still present")
        results.append(Result(f"turn {int(num):02d}", problems))
    return results


if __name__ == "__main__":
    # usage: check_clean.py draft.txt clean.txt "um,uh" [names.txt]
    names = pathlib.Path(sys.argv[4]).read_text(encoding="utf-8").split("\n") if len(sys.argv) > 4 else []
    out = check_clean(sys.argv[1], sys.argv[2], sys.argv[3].split(","), [n for n in names if n.strip()])
    for r in out:
        print(("OK     " if r.ok else "NOT OK ") + r.name + ("" if r.ok else ": " + "; ".join(r.problems)))
    sys.exit(0 if all(r.ok for r in out) else 1)
