"""Reference trace check for Lesson 3. Learners' AI coding tool writes its own; this one verifies the instruction."""
from check_quotes import Result


def parse_rows(text: str) -> list[tuple[str, list[str]]]:
    """Parse lines 'line ID | insight IDs' (IDs comma separated). Raises ValueError with the line number."""
    rows = []
    for n, line in enumerate(text.splitlines(), 1):
        if not line.strip():
            continue
        item, sep, ids = line.partition("|")
        if not sep or not item.strip():
            raise ValueError(f"line {n}: expected 'line ID | insight IDs'")
        rows.append((item.strip(), [x.strip() for x in ids.split(",") if x.strip()]))
    return rows


def check_trace(valid_ids: set[str], rows: list[tuple[str, list[str]]]) -> list[Result]:
    valid = {v.upper() for v in valid_ids}
    results = []
    for i, (_item, ids) in enumerate(rows):
        ids = [x.upper() if x.lower() != "assumption" else "assumption" for x in ids]
        if not ids:
            results.append(Result(i, "fail", "no insight ID"))
        elif ids == ["assumption"]:
            results.append(Result(i, "pass", ""))
        elif "assumption" in ids:
            results.append(Result(i, "fail", "assumption mixed with insight IDs"))
        else:
            missing = [x for x in ids if x not in valid]
            results.append(Result(i, "fail", f"unknown insight ID: {', '.join(missing)}") if missing else Result(i, "pass", ""))
    return results
