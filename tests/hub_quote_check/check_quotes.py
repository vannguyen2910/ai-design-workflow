"""Reference quote check for Lesson 2. Learners' AI coding tool writes its own; this one verifies the instruction."""
import re
from dataclasses import dataclass

_QUOTES = {"‘": "'", "’": "'", "“": '"', "”": '"'}


def _norm(s: str) -> str:
    for k, v in _QUOTES.items():
        s = s.replace(k, v)
    return re.sub(r"\s+", " ", s).strip().lower()


@dataclass
class Result:
    row_index: int
    status: str  # "pass" | "fail"
    reason: str


def parse_notes(text: str) -> dict[str, str]:
    notes: dict[str, str] = {}
    for n, line in enumerate(text.splitlines(), 1):
        if not line.strip():
            continue
        note_id, sep, body = line.partition("|")
        note_id, body = note_id.strip(), body.strip()
        if not sep or not note_id or not body:
            raise ValueError(f"line {n}: expected 'ID | text'")
        if note_id in notes:
            raise ValueError(f"line {n}: duplicate ID {note_id}")
        notes[note_id] = body
    return notes


def check_rows(notes: dict[str, str], rows: list[tuple[str, list[str], str]]) -> list[Result]:
    results = []
    for i, (_insight, ids, quote) in enumerate(rows):
        q = _norm(quote)
        if len(q) >= 2 and q[0] == '"' and q[-1] == '"':
            q = q[1:-1].strip()  # AI tools often wrap a quote in quotation marks
        if not ids:
            results.append(Result(i, "fail", "no note ID"))
            continue
        if not q:
            results.append(Result(i, "fail", "empty quote"))
            continue
        missing = [x for x in ids if x not in notes]
        if missing:
            results.append(Result(i, "fail", f"unknown note ID: {', '.join(missing)}"))
            continue
        bad = [x for x in ids if q not in _norm(notes[x])]
        results.append(Result(i, "fail", f"quote not found in {', '.join(bad)}") if bad else Result(i, "pass", ""))
    return results
