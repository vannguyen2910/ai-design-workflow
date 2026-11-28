"""Reference script for check-clean-instruction.md.

Compares a cleaned transcript with the anonymised draft it came from, turn by turn.
The only allowed differences are formatting and the filler words the learner declared
(each filler is a single word).
Not used in class: it shows the instruction is precise enough for a script to follow.
"""
import pathlib
import re
import sys
import unicodedata
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


def nfc(text):
    # Vietnamese tone marks in decomposed form are not matched by \w, so compose first.
    return unicodedata.normalize("NFC", text)


def read_turns(path, pattern):
    """Only the first line (a note) and blank lines may differ from the turn format."""
    lines = nfc(pathlib.Path(path).read_text(encoding="utf-8")).splitlines()
    turns, stray, note = [], [], ""
    for number, line in enumerate(lines, 1):
        if m := pattern.match(line):
            turns.append(m.groups())
        elif number == 1:
            note = line
        elif line.strip():
            stray.append(number)
    return turns, stray, note


def leaked(text, names):
    return [f"name {n} still present" for n in names if re.search(rf"(?<!\w){re.escape(n)}(?!\w)", text, re.I)]


def check_clean(draft_path, clean_path, fillers, names=()):
    fillers = {nfc(f).strip().lower() for f in fillers}
    names = [nfc(n).strip() for n in names if n.strip()]
    draft, draft_stray, _ = read_turns(draft_path, DRAFT_LINE)
    clean, clean_stray, note = read_turns(clean_path, CLEAN_LINE)
    broken = [f"draft line {n} is not a turn" for n in draft_stray] + [f"clean line {n} is not a turn" for n in clean_stray]
    if not draft or not clean:
        broken.append("no turns found")
    if len(draft) != len(clean):
        broken.append(f"draft has {len(draft)} lines, clean has {len(clean)} turns")
    if broken:
        return [Result("file", broken)]
    results = [Result("file", leaked(note, names))] if leaked(note, names) else []
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
        problems += leaked(f"{c_spk}: {c_text}", names)
        results.append(Result(f"turn {int(num):02d}", problems))
    return results


if __name__ == "__main__":
    # usage: check_clean.py draft.txt clean.txt "um,uh" [names.txt]
    names = pathlib.Path(sys.argv[4]).read_text(encoding="utf-8").split("\n") if len(sys.argv) > 4 else []
    out = check_clean(sys.argv[1], sys.argv[2], sys.argv[3].split(","), names)
    for r in out:
        print(("OK     " if r.ok else "NOT OK ") + r.name + ("" if r.ok else ": " + "; ".join(r.problems)))
    sys.exit(0 if all(r.ok for r in out) else 1)
