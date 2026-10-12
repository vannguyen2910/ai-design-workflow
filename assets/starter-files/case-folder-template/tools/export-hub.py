#!/usr/bin/env python3
"""Export the markdown hub of a case folder to ONE self-contained HTML file.

    python3 tools/export-hub.py                 # case = the folder that contains tools/ -> <case>/index.html
    python3 tools/export-hub.py --case PATH     # another case folder
    python3 tools/export-hub.py --out FILE.html # custom output path (e.g. a copy to send)

Why a script and not an AI tool: turning markdown into HTML and tracing links between items is
deterministic. A script gives the same output every time, invents nothing and sends no data anywhere.
Python 3.8+ standard library only.

The report is an OUTPUT. Never edit it by hand: change the markdown and export again.

Included : hub/*.md (pages and items O1, H1, D1...), case-log.md, learnings/context-principle-checks.md
Excluded : everything else (AI drafts, _personal/, learnings/sources/, AGENTS.md, how-the-hub-works.md)

Layout: four tabs (Overview, Journey, Trace, Reference). Items (O, H, M, D, T) are not in the menu:
they live in the Trace tab as a tree  Opportunity > Hypothesis > Decision / Test / Metric, with search
and filters, so the report still works with hundreds of items.
"""
import argparse
import base64
import datetime
import html
import mimetypes
import os
import re
import sys
import csv
import shutil
import urllib.parse

TYPES = [
    # letter, folder, singular, plural
    ("O", "opportunities", "Opportunity", "Opportunities"),
    ("H", "hypotheses", "Hypothesis", "Hypotheses"),
    ("M", "metrics", "Metric", "Metrics"),
    ("D", "decisions", "Design decision", "Decisions"),
    ("T", "tests", "Test", "Tests"),
]
LETTER_NAME = {t[0]: t[2] for t in TYPES}
EXCLUDE_HUB_FILES = {"how-the-hub-works.md"}
VI_NAME = {"O": ("Opportunity", "Opportunity"), "H": ("Hypothesis", "Hypothesis"), "M": ("Metric", "Metric"),
           "D": ("Decision", "Design decision"), "T": ("Test", "Test")}
VI_SHORT = {"O": "Opportunity", "H": "Hypothesis", "M": "Metric", "D": "Decision", "T": "Test"}
PROP_LABEL = {"type": "Type", "rank": "Rank", "evidence": "Evidence", "serves": "Serves", "metric": "Metric",
              "tests": "Tests", "follows": "Follows", "pulls_against": "Pulls against",
              "measures": "Measures", "status": "Status", "baseline": "Baseline", "measured_by": "Measured by",
              "participants": "Participants", "result": "Result", "participants_type": "Participants type"}
BACK_LABEL = {"serves": "Served by", "metric": "Used as metric by", "tests": "Tested by",
              "measures": "Measured by", "follows": "Followed by", "pulls_against": "Pulled against by"}
STATUS_VI = {"open": "Open", "passed": "Passed", "failed": "Failed"}
AGREE_VI = {"agreed": "Agreed", "pending": "Pending", "not available": "Not available"}


# --------------------------------------------------------------------------- markdown (subset)
def _split_row(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|") and not line.endswith("\\|"):
        line = line[:-1]
    cells, cur, in_code = [], "", False
    i = 0
    while i < len(line):
        ch = line[i]
        if ch == "\\" and i + 1 < len(line) and line[i + 1] == "|":
            cur += "|"
            i += 2
            continue
        if ch == "`":
            in_code = not in_code
        if ch == "|" and not in_code:
            cells.append(cur.strip())
            cur = ""
        else:
            cur += ch
        i += 1
    cells.append(cur.strip())
    return cells


def _is_sep(line):
    s = line.strip()
    return s.startswith("|") and re.fullmatch(r"\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?", s) is not None


class Renderer(object):
    def __init__(self, src_path, resolver, problems):
        self.src = src_path
        self.resolve = resolver
        self.problems = problems

    def inline(self, text):
        text = html.escape(text, quote=False)
        codes, links = [], []

        def stash_code(m):
            codes.append("<code>%s</code>" % m.group(1))
            return "\x00C%d\x00" % (len(codes) - 1)

        text = re.sub(r"`([^`]+)`", stash_code, text)

        def stash_link(m):
            label, url = m.group(1), html.unescape(m.group(2)).strip()
            is_img = m.group(0).startswith("!")
            kind, val = self.resolve(self.src, url, is_img)
            inner = self._emph(label)
            if is_img:
                if kind == "file":
                    out = '<a href="%s" target="_blank" rel="noopener"><img loading="lazy" src="%s" alt="%s"></a>' % (val, val, html.escape(label, quote=True))
                elif kind == "data":
                    out = '<img src="%s" alt="%s">' % (val, html.escape(label, quote=True))
                else:
                    out = '<span class="ext">[hình: %s]</span>' % (label or url)
            elif kind == "file":
                out = '<a href="%s" target="_blank" rel="noopener">%s</a>' % (val, inner)
            elif kind == "page":
                out = '<a href="#/%s">%s</a>' % (val, inner)
            elif kind == "web":
                out = '<a href="%s" target="_blank" rel="noopener">%s</a>' % (html.escape(val, quote=True), inner)
            elif kind == "anchor":
                out = '<span class="ext">%s</span>' % inner
            elif kind == "outside":
                out = '<span class="ext" title="Nằm ngoài báo cáo: %s">%s</span>' % (html.escape(val, quote=True), inner)
            else:
                self.problems.append("Link hỏng trong %s: %s" % (os.path.basename(self.src), url))
                out = '<span class="broken" title="Link hỏng: %s">%s</span>' % (html.escape(url, quote=True), inner)
            links.append(out)
            return "\x00L%d\x00" % (len(links) - 1)

        text = re.sub(r"!?\[([^\]]*)\]\(([^)\s]+)\)", stash_link, text)
        text = self._emph(text)
        text = re.sub(r"\x00L(\d+)\x00", lambda m: links[int(m.group(1))], text)
        text = re.sub(r"\x00C(\d+)\x00", lambda m: codes[int(m.group(1))], text)
        return text

    @staticmethod
    def _emph(text):
        text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
        return re.sub(r"(?<![\*\w])\*(?!\s)(.+?)(?<!\s)\*(?![\*\w])", r"<em>\1</em>", text)

    def render(self, md):
        lines = md.replace("\r\n", "\n").split("\n")
        out, i, n = [], 0, len(lines)
        while i < n:
            s = lines[i].strip()
            if not s:
                i += 1
                continue
            if s.startswith("<!--") and s.endswith("-->"):
                i += 1
                continue
            if s.startswith("```"):
                buf = []
                i += 1
                while i < n and not lines[i].strip().startswith("```"):
                    buf.append(lines[i])
                    i += 1
                i += 1
                out.append("<pre><code>%s</code></pre>" % html.escape("\n".join(buf), quote=False))
                continue
            m = re.match(r"(#{1,6})\s+(.*)", s)
            if m:
                lvl = len(m.group(1))
                out.append("<h%d>%s</h%d>" % (lvl, self.inline(m.group(2)), lvl))
                i += 1
                continue
            if re.fullmatch(r"-{3,}|\*{3,}", s):
                out.append("<hr>")
                i += 1
                continue
            if s.startswith(">"):
                buf = []
                while i < n and lines[i].strip().startswith(">"):
                    buf.append(re.sub(r"^\s*>\s?", "", lines[i]))
                    i += 1
                if re.match(r"\s*\*\*Cách điền", "\n".join(buf)):
                    continue  # authoring hint for the writer, not for the reader of the report
                out.append("<blockquote>%s</blockquote>" % self.render("\n".join(buf)))
                continue
            if s.startswith("|") and i + 1 < n and _is_sep(lines[i + 1]):
                head = _split_row(lines[i])
                i += 2
                rows = []
                while i < n and lines[i].strip().startswith("|"):
                    rows.append(_split_row(lines[i]))
                    i += 1
                thead = ""
                if any(c.strip() for c in head):
                    thead = "<thead><tr>%s</tr></thead>" % "".join('<th scope="col">%s</th>' % self.inline(c) for c in head)
                body = ""
                for r in rows:
                    r = (r + [""] * len(head))[: len(head)]
                    body += "<tr>%s</tr>" % "".join("<td>%s</td>" % self.inline(c) for c in r)
                out.append('<div class="table-wrap"><table>%s<tbody>%s</tbody></table></div>' % (thead, body))
                continue
            if re.match(r"([-*]|\d+\.)\s+", s):
                block, i = self._list(lines, i)
                out.append(block)
                continue
            buf = []
            while i < n and lines[i].strip() and not re.match(r"(#{1,6}\s|```|>|\||([-*]|\d+\.)\s+|-{3,}$)", lines[i].strip()):
                buf.append(lines[i].strip())
                i += 1
            if not buf:
                buf.append(lines[i].strip())
                i += 1
            out.append("<p>%s</p>" % self.inline(" ".join(buf)))
        return "\n".join(out)

    def _list(self, lines, i):
        n = len(lines)
        items = []
        while i < n:
            line = lines[i]
            m = re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)", line)
            if m:
                items.append([len(m.group(1).replace("\t", "    ")), m.group(2)[0].isdigit(), m.group(3)])
                i += 1
            elif line.strip() and items and re.match(r"^\s{2,}\S", line):
                items[-1][2] += " " + line.strip()
                i += 1
            else:
                break

        def build(pos, indent):
            parts, ordered = [], items[pos][1]
            while pos < len(items) and items[pos][0] >= indent:
                ind, _, text = items[pos]
                if ind > indent:
                    sub, pos = build(pos, ind)
                    if parts:
                        parts[-1] = parts[-1][:-5] + sub + "</li>"
                    continue
                cb = re.match(r"\[( |x|X)\]\s+(.*)", text)
                li = self.inline(cb.group(2)) if cb else self.inline(text)
                if cb:
                    li = '<span class="box" aria-hidden="true">%s</span> %s' % ("☑" if cb.group(1) != " " else "☐", li)
                parts.append("<li>%s</li>" % li)
                pos += 1
            tag = "ol" if ordered else "ul"
            return "<%s>%s</%s>" % (tag, "".join(parts), tag), pos

        block, _ = build(0, items[0][0])
        return block, i


# --------------------------------------------------------------------------- model
class Page(object):
    def __init__(self, pid, path, kind, label=None):
        self.id, self.path, self.kind = pid, path, kind
        self.md = open(path, encoding="utf-8").read()
        m = re.search(r"^#\s+(.+)$", self.md, flags=re.M)
        self.heading = m.group(1).strip() if m else pid
        self.label = label or self.heading
        self.letter = None
        self.title = self.heading
        self.meta = {}
        self.rank = 999


def _unq(s):
    s = s.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        s = s[1:-1]
    return s


def _csv(s):
    out, cur, q = [], "", None
    for ch in s:
        if q:
            cur += ch
            if ch == q:
                q = None
        elif ch in "\"'":
            q = ch
            cur += ch
        elif ch == ",":
            out.append(cur)
            cur = ""
        else:
            cur += ch
    if cur.strip():
        out.append(cur)
    return out


def _front(md):
    """YAML front matter (small subset: scalars, inline lists, '- item' lists) -> (dict, body)"""
    m = re.match(r"---[ \t]*\n(.*?)\n---[ \t]*\n?", md, flags=re.S)
    if not m:
        return {}, md
    data, key = {}, None
    for line in m.group(1).split("\n"):
        if not line.strip() or line.strip().startswith("#"):
            continue
        li = re.match(r"^\s+-\s+(.*)$", line)
        if li and key is not None:
            if not isinstance(data.get(key), list):
                data[key] = []
            data[key].append(_unq(li.group(1)))
            continue
        kv = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if kv:
            key, val = kv.group(1).lower(), kv.group(2).strip()
            if val == "":
                data[key] = []
            elif val.startswith("[") and val.endswith("]"):
                inner = val[1:-1].strip()
                data[key] = [_unq(x) for x in _csv(inner)] if inner else []
            else:
                data[key] = _unq(val)
    return data, md[m.end():]


REL_KEYS = ("serves", "metric", "tests", "measures", "follows", "pulls_against")
TYPE_WORD = {"O": "opportunity", "H": "hypothesis", "M": "metric", "D": "decision", "T": "test"}


def _ids(value):
    if isinstance(value, list):
        value = " ".join(value)
    v = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", value or "")
    v = re.sub(r"\[\[([^\]]+)\]\]", r"\1", v)
    v = re.sub(r"\]\([^)]*\)", "]", v)
    return re.findall(r"\b([OHMDTP]\d+)\b", v)


def _natkey(s):
    return [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", s)]


def collect(case):
    hub = os.path.join(case, "hub")
    ov = os.path.join(hub, "README.md")
    if not os.path.isfile(ov):
        sys.exit("Không tìm thấy hub/README.md trong %s" % case)
    overview = Page("overview", ov, "overview")
    weekly, items, ref = [], [], []
    for name in sorted(os.listdir(hub)):
        if re.match(r"\d\d-.*\.md$", name) and name not in EXCLUDE_HUB_FILES:
            weekly.append(Page(name[:-3], os.path.join(hub, name), "week"))
    gates = os.path.join(hub, "gates.md")
    if os.path.isfile(gates):
        ref.append(Page("gates", gates, "ref", "Gates"))
    pc = os.path.join(case, "learnings", "context-principle-checks.md")
    if os.path.isfile(pc):
        ref.append(Page("principles", pc, "ref", "Principle checks"))
    cl = os.path.join(case, "case-log.md")
    if os.path.isfile(cl):
        ref.append(Page("case-log", cl, "ref", "Case log"))
    letters = {t[0] for t in TYPES}
    for name in sorted(os.listdir(hub), key=_natkey):
        m = re.match(r"([A-Z])\d+\.md$", name)
        if m and m.group(1) in letters:
            p = Page(name[:-3], os.path.join(hub, name), "item")
            p.letter = m.group(1)
            p.meta, p.body = _front(p.md)
            hm = re.search(r"^#\s+(?:[A-Z]\d+:\s*)?(.+)$", p.body, flags=re.M)
            p.title = str(p.meta.get("title") or (hm.group(1) if hm else name[:-3])).strip()
            r = re.search(r"\d+", str(p.meta.get("rank", "")))
            p.rank = int(r.group(0)) if r else 999
            items.append(p)
    return overview, weekly, items, ref


def case_info(overview_md, case):
    name = os.path.basename(os.path.abspath(case))
    m = re.search(r"^\|\s*Tên case\s*\|\s*(.+?)\s*\|\s*$", overview_md, flags=re.M)
    if m and not m.group(1).startswith("["):
        name = re.sub(r"[*`]", "", m.group(1))
    status = ""
    m = re.search(r"^\|\s*Agreement status\s*\|\s*(.+?)\s*\|\s*$", overview_md, flags=re.M)
    if m:
        status = re.sub(r"\*.*?\*|[*`]", "", m.group(1)).strip()
    return name, status


def week_info(overview_md):
    """slug -> (week, description) from the Pages table in hub/README.md"""
    info = {}
    for line in overview_md.split("\n"):
        m = re.match(r"\|\s*\[([^\]]+)\]\((\d\d-[^)]+)\.md\)\s*\|\s*([^|]*)\|\s*([^|]*)\|", line)
        if m:
            info[m.group(2)] = (m.group(3).strip(), m.group(4).strip(), m.group(1).strip())
    return info


def parse_gates(md):
    out, cur = [], None
    for line in md.split("\n"):
        h = re.match(r"##\s+Gate\s+\d+:\s*(.+)", line)
        if h:
            cur = {"name": h.group(1).strip(), "checks": []}
            out.append(cur)
            continue
        if cur and line.strip().startswith("|"):
            c = _split_row(line)
            if len(c) >= 3 and re.fullmatch(r"\d[a-z]", c[0]):
                cur["checks"].append((c[0], c[1], c[2].strip().lower()))
    for g in out:
        st = [c[2] for c in g["checks"]]
        g["passed"] = sum(1 for s in st if s == "passed")
        g["total"] = len(st)
        g["status"] = "failed" if "failed" in st else ("passed" if st and all(s == "passed" for s in st) else "open")
    return out


def parse_principles(md):
    out = {}
    for line in md.split("\n"):
        if line.strip().startswith("|"):
            c = _split_row(line)
            if len(c) >= 3 and re.fullmatch(r"P\d+", c[0]):
                out[c[0]] = (c[1], c[2].strip())
    return out


# --------------------------------------------------------------------------- graph
class Graph(object):
    def __init__(self, items, principles):
        self.items = {p.id: p for p in items}
        self.principles = principles
        g = lambda i, k: _ids(self.items[i].meta.get(k, ""))
        self.serves = {i: [x for x in g(i, "serves") if x in self.items] for i, p in self.items.items() if p.letter == "H"}
        self.metric = {i: [x for x in g(i, "metric") if x in self.items] for i, p in self.items.items() if p.letter == "H"}
        self.tests = {i: [x for x in g(i, "tests") if x in self.items] for i, p in self.items.items() if p.letter in "DT"}
        self.measures = {i: [x for x in g(i, "measures") if x in self.items] for i, p in self.items.items() if p.letter == "T"}
        self.follows = {i: g(i, "follows") for i, p in self.items.items() if p.letter == "D"}
        self.strains = {i: g(i, "pulls_against") for i, p in self.items.items() if p.letter == "D"}
        letters = lambda L: sorted([i for i, p in self.items.items() if p.letter == L], key=_natkey)
        self.O, self.H, self.M, self.D, self.T = [letters(L) for L in "OHMDT"]
        self.O.sort(key=lambda i: (self.items[i].rank, _natkey(i)))
        self.back = {}
        for src, p in self.items.items():
            for label, val in p.meta.items():
                if label not in REL_KEYS:
                    continue
                for t in _ids(val):
                    if t in self.items and t != src:
                        e = (src, label)
                        if e not in self.back.setdefault(t, []):
                            self.back[t].append(e)
        self.warn = {}
        self.warnings = []  # (kind, [ids], text)

        def flag(kind, ids, text):
            self.warnings.append((kind, ids, text))
            for i in ids:
                self.warn.setdefault(i, []).append(text)

        for d in self.D:
            hs = self.tests.get(d, [])
            if not hs or all(not self.serves.get(h) for h in hs):
                flag("no-need", [d], "Decision này chưa nối được về opportunity nào")
        for d in self.D:
            for p in self.strains.get(d, []):
                flag("strain", [d], "Decision này đi ngược principle %s: cân nhắc sửa, hoặc ghi lại vì sao chấp nhận" % p)
        for o in self.O:
            hs = [h for h in self.H if o in self.serves.get(h, [])]
            if not hs or not any(self.decisions_of(h) for h in hs):
                flag("unserved", [o], "Opportunity này chưa có decision nào phục vụ")
        for h in self.H:
            if not self.tests_of(h):
                flag("untested", [h], "Hypothesis này chưa có test")
            if not self.metric.get(h):
                flag("nometric", [h], "Hypothesis này chưa có metric để biết đúng hay sai")
        # Evidence quality: a test can be planned (not run) or run with simulated participants. Neither counts as evidence.
        def kind(t):
            m = self.items[t].meta
            if str(m.get("status", "")).lower() == "planned":
                return "planned"
            if str(m.get("participants_type", "")).lower() == "simulated":
                return "simulated"
            return "real"
        for t in self.T:
            k = kind(t)
            if k == "planned":
                flag("planned", [t], "Test này mới ở dạng kế hoạch, chưa chạy")
            elif k == "simulated":
                flag("simulated", [t], "Test này dùng người mô phỏng, không phải người dùng thật: chưa tính là evidence")
        for h in self.H:
            ts = self.tests_of(h)
            if ts and not any(kind(t) == "real" for t in ts):
                flag("no-real-evidence", [h], "Hypothesis này chưa có evidence từ người dùng thật")
        empty = [p for p, (nm, chk) in principles.items() if not chk.strip() and not nm.startswith("(")]
        if empty:
            self.warnings.append(("principles", empty, "Principle chưa có câu hỏi có/không để kiểm tra"))

    def hyps_of(self, o):
        return [h for h in self.H if o in self.serves.get(h, [])]

    def decisions_of(self, h):
        return [d for d in self.D if h in self.tests.get(d, [])]

    def tests_of(self, h):
        return [t for t in self.T if h in self.tests.get(t, [])]

    def paths(self, i, depth=0):
        """chains from an Opportunity down to item i (list of id lists)"""
        p = self.items[i]
        if p.letter == "O":
            return [[i]]
        parents = []
        if p.letter == "H":
            parents = self.serves.get(i, [])
        elif p.letter in "DT":
            parents = self.tests.get(i, [])
        elif p.letter == "M":
            parents = [h for h in self.H if i in self.metric.get(h, [])]
        res = []
        for par in parents:
            for chain in self.paths(par, depth + 1):
                res.append(chain + [i])
        return res


# --------------------------------------------------------------------------- html
CSS = r"""
:root{--ink:#14121c;--bg:#fff;--surface:#faf9ff;--muted:rgba(20,18,28,.66);--line:rgba(20,18,28,.13);--purple:#6B3FEE;--link:#5530d4;--tint:rgba(107,63,238,.10);--tint2:rgba(107,63,238,.18);--on-purple:#fff;--r:12px;color-scheme:light}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;overflow-x:hidden}
a{color:var(--link)}
a:focus-visible,button:focus-visible,input:focus-visible,summary:focus-visible{outline:3px solid var(--purple);outline-offset:2px;border-radius:6px}
.skip{position:absolute;left:-999px;top:0;background:var(--purple);color:var(--on-purple);padding:8px 14px;z-index:30}
.skip:focus{left:8px;top:8px}
header.top{position:sticky;top:0;z-index:20;background:var(--bg);border-bottom:1px solid var(--line)}
.top-in{max-width:1280px;margin:0 auto;padding:10px 24px;display:flex;gap:18px;align-items:center;flex-wrap:wrap}
.brand{font-weight:800;letter-spacing:-.01em;margin-right:auto}
.brand small{display:block;font-weight:500;color:var(--muted);font-size:.74rem;letter-spacing:0}
.tabs{display:flex;gap:4px;overflow-x:auto}
.tabs a{padding:8px 14px;border-radius:999px;text-decoration:none;color:var(--ink);font-weight:600;font-size:.92rem;white-space:nowrap}
.tabs a:hover{background:var(--tint)}
.tabs a[aria-current=page]{background:var(--purple);color:var(--on-purple)}
.themepick{font-size:.8rem;color:var(--muted);display:flex;gap:6px;align-items:center}
.themepick select{font:inherit;padding:6px 8px;border:1px solid var(--line);border-radius:8px;background:var(--surface);color:var(--ink)}
.gsearch{border:1px solid var(--line);background:var(--surface);color:var(--ink);border-radius:999px;padding:8px 14px;font:inherit;font-size:.9rem;width:220px}
.view{display:none}
.view.on{display:block}
.wrap{max-width:1280px;margin:0 auto;padding:28px 24px 80px}
h1{font-size:1.8rem;line-height:1.25;margin:0 0 8px;letter-spacing:-.015em}
h2{font-size:1.1rem;margin:34px 0 12px;letter-spacing:-.005em}
h3{font-size:1rem;margin:22px 0 6px}
.lede{color:var(--muted);margin:0 0 22px}
.banner{background:var(--ink);color:var(--bg);border-radius:var(--r);padding:12px 16px;margin:0 0 22px;font-size:.92rem}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin:8px 0 8px}
.card{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);padding:14px 16px}
.card .num{font-size:1.9rem;font-weight:800;line-height:1.1;letter-spacing:-.02em}
.card .lbl{color:var(--muted);font-size:.85rem}
.card.warnc .num::after{content:" ⚠";font-size:1rem}
.gatecards{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:12px}
.gate{border-radius:var(--r);padding:14px 16px;background:var(--ink);color:var(--bg)}
.gate small{display:block;opacity:.8}
.gate .st{margin-top:8px;font-weight:700}
.gate .bar{height:6px;border-radius:99px;background:rgba(255,255,255,.25);margin-top:8px;overflow:hidden}
.gate .bar i{display:block;height:100%;background:#fff}
.table-wrap{overflow-x:auto;margin:12px 0}
table{border-collapse:collapse;width:100%;font-size:.92rem}
th,td{text-align:left;padding:9px 12px;border-bottom:1px solid var(--line);vertical-align:top}
th{background:var(--tint);font-weight:700}
table.props th{background:none;color:var(--muted);font-weight:600;width:11em}
.missing{font-weight:700;color:var(--muted);font-style:italic}
.card .lbl small{display:block;font-size:.74rem;opacity:.85}
details.help{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);padding:12px 18px;margin:0 0 22px}
details.help summary{cursor:pointer;font-weight:700}
details.help ul,details.help dl{margin:10px 0 4px}
details.help dt{font-weight:700;margin-top:10px}
details.help dd{margin:2px 0 0;color:var(--muted)}
.chip,.idc,.idtag{display:inline-block;font-weight:800;font-size:.8rem;line-height:1;padding:4px 8px;border-radius:7px;text-decoration:none;letter-spacing:.03em;vertical-align:middle;border:2px solid transparent;white-space:nowrap}
.t-O{background:var(--purple);color:var(--on-purple)}
.t-H{border-color:var(--purple);color:var(--link)}
.t-D{background:var(--ink);color:var(--bg)}
.t-T{border-color:var(--ink);color:var(--ink)}
.t-M{background:var(--tint2);color:var(--ink)}
.t-P{border:2px dashed var(--muted);color:var(--ink)}
a.chip:hover{filter:brightness(1.1)}
.chips{display:flex;flex-wrap:wrap;gap:6px}
.warnlist{list-style:none;margin:0;padding:0}
.warnlist li{padding:10px 14px;margin:8px 0;border-radius:var(--r);background:var(--tint);border-left:4px solid var(--purple)}
.ok{padding:10px 14px;border-radius:var(--r);background:var(--tint)}
/* journey */
.jcards{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:14px}
.jcard{display:block;background:var(--surface);border:1px solid var(--line);border-radius:var(--r);padding:16px 18px;text-decoration:none;color:var(--ink)}
.jcard:hover{border-color:var(--purple);box-shadow:0 2px 0 var(--purple)}
.jcard .wk{font-size:.75rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--link)}
.jcard h3{margin:4px 0 6px;font-size:1.05rem}
.jcard p{margin:0;color:var(--muted);font-size:.9rem}
.has-doc .jlist{display:none}
.journey .doc,.reference .doc{display:none}
.journey .doc.on,.reference .doc.on{display:block}
.reading{max-width:76ch}
.pn{display:flex;justify-content:space-between;gap:16px;margin-top:40px;padding-top:16px;border-top:1px solid var(--line);flex-wrap:wrap}
.back{display:inline-block;margin:0 0 16px;font-size:.9rem}
.subtabs{display:flex;gap:6px;margin:0 0 18px;flex-wrap:wrap}
.subtabs a{padding:6px 12px;border-radius:999px;border:1px solid var(--line);text-decoration:none;color:var(--ink);font-size:.9rem;font-weight:600}
.subtabs a[aria-current=page]{background:var(--ink);color:var(--bg);border-color:var(--ink)}
/* trace */
.trace{display:grid;grid-template-columns:minmax(300px,380px) minmax(0,1fr);gap:28px;align-items:start}
.pane-tree{position:sticky;top:76px;max-height:calc(100vh - 96px);overflow:auto;border:1px solid var(--line);border-radius:var(--r);background:var(--surface);padding:12px}
.filters{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 10px}
.filters button{border:1px solid var(--line);background:var(--bg);color:var(--ink);border-radius:999px;padding:5px 11px;font:inherit;font-size:.8rem;font-weight:700;cursor:pointer}
.filters button[aria-pressed=true]{background:var(--purple);border-color:var(--purple);color:var(--on-purple)}
.tsearch{width:100%;border:1px solid var(--line);background:var(--bg);color:var(--ink);border-radius:10px;padding:8px 12px;font:inherit;font-size:.9rem;margin:0 0 10px}
.tcount{font-size:.8rem;color:var(--muted);margin:0 0 8px}
.tree,.tree ul{list-style:none;margin:0;padding:0}
.tree ul{margin-left:14px;padding-left:10px;border-left:1px solid var(--line)}
.tree li[hidden]{display:none}
.tree summary{cursor:pointer;display:flex;align-items:flex-start;gap:6px;padding:3px 0;list-style:none}
.tree summary::-webkit-details-marker{display:none}
.tree summary::before{content:"▸";color:var(--muted);width:1em;flex:none;font-size:.8rem;margin-top:5px}
.tree details[open]>summary::before{content:"▾"}
.tree li.leaf{padding-left:1.35em}
.tree a.node{display:flex;gap:8px;align-items:flex-start;text-decoration:none;color:var(--ink);padding:4px 6px;border-radius:8px;flex:1;min-width:0;font-size:.9rem}
.tree a.node:hover{background:var(--tint)}
.tree a.node.sel{background:var(--tint2);font-weight:700}
.tree .idc{font-size:.72rem;padding:3px 6px;flex:none;margin-top:2px}
.tree .nt{overflow-wrap:anywhere}
.tree .wb{margin-left:auto;flex:none}
.tree .cnt{display:block;color:var(--muted);font-size:.75rem;font-weight:500}
.tree .gh{font-size:.8rem;font-weight:800;color:var(--muted);padding:8px 0 2px}
.pane-detail .doc{display:none}
.pane-detail .doc.on{display:block}
.empty{color:var(--muted);border:1px dashed var(--line);border-radius:var(--r);padding:28px;text-align:center}
.pane-detail .doc.on~.empty{display:none}
.ihead{display:flex;gap:14px;align-items:flex-start;margin:0 0 14px}
.ihead .idtag{font-size:1rem;padding:7px 12px;flex:none;margin-top:2px}
.ihead .kind{margin:0;color:var(--muted);font-size:.8rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase}
.ihead h1{margin:2px 0 0;font-size:1.5rem}
.warnbox{margin:0 0 14px;padding:10px 14px;border-radius:var(--r);background:var(--tint);border-left:4px solid var(--purple);font-size:.92rem}
.path{font-size:.88rem;color:var(--muted);margin:0 0 14px}
.path .chain{margin:6px 0 0;align-items:center}
.path .more{display:block;margin-top:6px}
.backlinks{margin-top:30px;padding:14px 18px;background:var(--surface);border:1px solid var(--line);border-radius:var(--r)}
.backlinks h2{margin:0 0 8px;font-size:.95rem}
.backlinks .row{display:flex;gap:10px;align-items:baseline;flex-wrap:wrap;margin:6px 0}
.backlinks .lbl{font-size:.8rem;color:var(--muted);min-width:7em}
.back-tree{display:none}
.acards{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:14px;margin-top:6px}
.acard{display:flex;flex-direction:column;gap:6px;background:var(--surface);border:1px solid var(--line);border-radius:var(--r);padding:0 0 14px;text-decoration:none;color:var(--ink);overflow:hidden}
.acard[hidden]{display:none}
.acard:hover{border-color:var(--purple);box-shadow:0 2px 0 var(--purple)}
.acard .thumb{width:100%;height:150px;object-fit:cover;object-position:top;border-bottom:1px solid var(--line);background:var(--tint)}
.acard>*:not(.thumb){margin-left:16px;margin-right:16px}
.acard:not(:has(.thumb))>.atype{margin-top:14px}
.atype{font-size:.72rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--link)}
.acard h3{margin:0;font-size:1.02rem}
.acard p{margin:0;color:var(--muted);font-size:.88rem}
.ameta{font-size:.78rem;color:var(--muted)}
.st{display:inline-block;padding:1px 8px;border-radius:999px;font-weight:700;font-size:.72rem;background:var(--tint2);color:var(--ink)}
.st-simulated,.st-planned,.st-draft{background:var(--ink);color:var(--bg)}
.ahead .sum{font-size:1.05rem;color:var(--muted);margin:6px 0 10px}
.ahead .kind{margin:0;color:var(--muted);font-size:.8rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase}
.supports{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin:6px 0 14px}
.supports .lbl{font-size:.8rem;color:var(--muted)}
.figs{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:14px;margin:8px 0}
.fig{margin:0;border:1px solid var(--line);border-radius:var(--r);overflow:hidden;background:#fff}
.fig img{display:block;width:100%;height:auto}
.fig figcaption,.mcard .cap{font-size:.8rem;color:var(--muted);padding:6px 12px}
.mcard{border:1px solid var(--line);border-radius:var(--r);margin:12px 0;overflow:hidden;background:var(--surface)}
.mhead{display:flex;gap:10px;align-items:center;flex-wrap:wrap;padding:10px 14px}
.mtag{font-size:.72rem;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:.06em}
.btn{margin-left:auto;padding:5px 12px;border-radius:999px;background:var(--purple);color:var(--on-purple);text-decoration:none;font-size:.82rem;font-weight:700}
.mcard iframe{display:block;width:100%;height:560px;border:0;border-top:1px solid var(--line);background:#fff}
.mcard video{display:block;width:100%}
.achip{display:inline-flex;gap:8px;align-items:baseline;padding:6px 12px;border:1px solid var(--line);border-radius:10px;text-decoration:none;color:var(--ink);background:var(--surface);font-size:.9rem}
.achip:hover{border-color:var(--purple)}
.achip .atype{font-size:.66rem}
.sgroup{margin:10px 0}
.sgroup h3{margin:0 0 6px;font-size:.8rem;text-transform:uppercase;letter-spacing:.08em;color:var(--muted)}
.t-A{background:var(--tint2);color:var(--ink);border-color:transparent}
details.draft{margin:14px 0;border:1px dashed var(--muted);border-radius:var(--r);padding:10px 14px;background:var(--surface)}
details.draft>summary{cursor:pointer;font-weight:700;color:var(--muted)}
.srcnote{margin-top:24px;font-size:.82rem;color:var(--muted)}
.docs .doc{display:none}
.docs .doc.on{display:block}
.has-doc .jlist{display:none}
blockquote{margin:16px 0;padding:10px 16px;background:var(--tint);border-left:4px solid var(--purple);border-radius:0 10px 10px 0}
blockquote p{margin:6px 0}
code{font:.88em ui-monospace,Menlo,Consolas,monospace;background:var(--tint);padding:1px 5px;border-radius:5px}
pre{background:var(--tint);padding:12px 14px;border-radius:10px;overflow-x:auto}
pre code{background:none;padding:0}
hr{border:0;border-top:1px solid var(--line);margin:28px 0}
ul,ol{padding-left:1.4em}
li{margin:4px 0}
.box{font-family:ui-monospace,Menlo,Consolas,monospace}
.ext{color:var(--muted);border-bottom:1px dotted var(--muted);cursor:help}
.broken{color:#9b1c1c;text-decoration:underline wavy}
img{max-width:100%}
footer.foot{margin-top:56px;color:var(--muted);font-size:.85rem;border-top:1px solid var(--line);padding-top:14px}
@media (max-width:900px){
  .trace{grid-template-columns:1fr}
  .pane-tree{position:static;max-height:none}
  .has-item .pane-tree{display:none}
  .has-item .back-tree{display:inline-block}
  .gsearch{width:100%;order:3}
  .wrap{padding:20px 16px 60px}
}
@media print{
  header.top,.skip,.pane-tree,.back,.pn,.subtabs,.back-tree,.themepick,.filters,.tsearch{display:none!important}
  .view,.journey .doc,.reference .doc,.docs .doc,.pane-detail .doc{display:block!important}
  .jlist{display:none}
  .doc{break-before:page}
  .wrap{padding:0;max-width:none}
  .trace{display:block}
  a{color:inherit;text-decoration:none}
  table{font-size:.8rem}
  .banner{border:1px solid #000;background:none;color:#000}
}
"""

NAV_CSS = r"""
/* sidebar layout (mirrors the website structure: one page per document, nested menu on the left) */
.shell{display:grid;grid-template-columns:300px minmax(0,1fr);max-width:1480px;margin:0 auto;align-items:start}
.side{position:sticky;top:61px;height:calc(100vh - 61px);overflow:auto;border-right:1px solid var(--line);padding:16px 12px 48px;font-size:.9rem;background:var(--bg)}
.side nav{display:block}
.side a{display:block;text-decoration:none;color:var(--ink);padding:5px 10px;border-radius:8px;overflow-wrap:anywhere}
.side a:hover{background:var(--tint)}
.side a[aria-current=page]{background:var(--purple);color:var(--on-purple);font-weight:700}
.side .s-top{font-weight:700}
.side details{margin:0}
.side summary{cursor:pointer;list-style:none;font-weight:800;padding:7px 10px;border-radius:8px;display:flex;gap:6px;align-items:baseline}
.side summary::-webkit-details-marker{display:none}
.side summary::before{content:"▸";color:var(--muted);font-size:.75rem;width:.9em;flex:none}
.side details[open]>summary::before{content:"▾"}
.side summary:hover{background:var(--tint)}
.side .grp{margin-top:6px}
.side .grp>.sub{margin-left:12px;border-left:1px solid var(--line);padding-left:6px}
.side .sub summary{font-weight:700;color:var(--ink);font-size:.88rem}
.side .sub .cnt{margin-left:auto;font-weight:500;color:var(--muted);font-size:.78rem}
.side .sub a{font-size:.85rem;color:var(--ink)}
.side .sub a .idc{font-size:.66rem;padding:2px 5px;margin-right:6px}
.side .sub a[aria-current=page] .idc{border-color:var(--on-purple);background:transparent;color:var(--on-purple)}
.side .menu>summary{display:none}
.shell .wrap{max-width:1000px;padding:28px 40px 80px}
/* one page at a time: the trace tree is its own page, items are pages of their own */
.trace{display:block}
.pane-tree{position:static;max-height:none;overflow:visible;border:0;background:none;padding:0}
#v-trace.has-item .pane-tree{display:none}
#v-trace:not(.has-item) .pane-detail{display:none}
#v-trace .back-tree{display:inline-block}
#v-reference .wrap>h1,#v-reference .wrap>.lede,#v-reference .subtabs{display:none}
@media (max-width:900px){
  .shell{display:block}
  .side{position:static;height:auto;border-right:0;border-bottom:1px solid var(--line);padding:8px 12px;max-height:none}
  .side .menu>summary{display:block;cursor:pointer;font-weight:800;padding:8px 10px;list-style:none}
  .side .menu[open]>summary{border-bottom:1px solid var(--line);margin-bottom:6px}
  .shell .wrap{padding:20px 16px 60px}
}
@media print{.side{display:none!important}.shell{display:block}.shell .wrap{max-width:none;padding:0}}
"""
CSS += NAV_CSS

MIN_CSS = r"""
/* minimalist layer: fewer boxes, more air, one accent */
body{font-size:15.5px;line-height:1.7}
header.top{border-bottom:1px solid var(--line)}
.top-in{padding:12px 24px}
.brand{font-weight:700}
.brand small{display:none}
h1{font-size:1.75rem;font-weight:700}
h2{font-size:.8rem;font-weight:700;letter-spacing:.09em;text-transform:uppercase;color:var(--muted);margin:44px 0 12px}
.lede{margin:0 0 26px}
.stats{display:flex;flex-wrap:wrap;gap:6px 28px;margin:6px 0 4px;padding:14px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.stats span{color:var(--muted);font-size:.92rem}
.stats b{display:inline-block;margin-right:6px;font-size:1.35rem;font-weight:700;color:var(--ink);letter-spacing:-.01em}
.stats .w b::after{content:" ⚠";font-size:.9rem}
.glist{margin:0;border-top:1px solid var(--line)}
.grow{display:grid;grid-template-columns:minmax(0,1.4fr) 110px minmax(80px,1fr) 70px;gap:16px;align-items:center;padding:11px 0;border-bottom:1px solid var(--line)}
.grow .gn small{display:block;color:var(--muted);font-size:.78rem}
.grow .gn strong{font-weight:600}
.grow .gs{font-size:.85rem;font-weight:600}
.grow .gs.ok{color:#1a7f4b}
.grow .gs.no{color:#a33}
.grow .gb{height:4px;border-radius:99px;background:var(--line);overflow:hidden}
.grow .gb i{display:block;height:100%;background:var(--purple)}
.grow .gc{font-size:.82rem;color:var(--muted);text-align:right}
.warnlist li{background:none;border-left:0;border-top:1px solid var(--line);border-radius:0;padding:10px 0;margin:0}
.warnlist li:last-child{border-bottom:1px solid var(--line)}
.warnlist strong{font-weight:500}
.ok{background:none;padding:0;color:var(--muted)}
table{font-size:.9rem}
th{background:none;font-size:.78rem;letter-spacing:.04em;text-transform:uppercase;color:var(--muted);border-bottom:1px solid var(--ink)}
td{border-bottom:1px solid var(--line)}
.chip,.idc,.idtag{font-weight:700;font-size:.74rem;padding:3px 7px}
details.help{background:none;border:0;border-top:1px solid var(--line);border-radius:0;padding:14px 0;margin:44px 0 0}
details.help summary{font-weight:600;color:var(--muted)}
.banner{background:var(--tint);color:var(--ink);font-size:.88rem;border-radius:var(--r);padding:10px 14px}
.side{font-size:.88rem}
.jcard,.acard{background:none}
.reading{max-width:70ch}
footer.foot{margin-top:48px}
@media (max-width:640px){.grow{grid-template-columns:1fr 1fr;gap:6px 12px}.grow .gb{grid-column:1/-1}}
/* sidebar: five sections; each opens a page of cards */
.side{padding:14px 12px}
.nav2 a{display:flex;align-items:center;gap:8px;padding:9px 12px;font-weight:600;font-size:.95rem}
.nav2 a .nm{margin-left:auto;font-weight:500;font-size:.78rem;color:var(--muted)}
.nav2 a[aria-current=page] .nm{color:var(--on-purple);opacity:.85}
/* item page */
.ihead{display:block;margin:0 0 6px}
.ihead .idtag{display:inline-block;font-size:.78rem;padding:3px 8px;margin:0 0 10px}
.ihead .kind{display:inline-block;margin:0 0 0 8px;font-size:.74rem;font-weight:600;letter-spacing:.06em;color:var(--muted);vertical-align:middle}
.ihead h1{font-size:1.6rem;margin:0;line-height:1.3}
.ihead>div{display:inline}
.path{margin:14px 0 18px;font-size:.84rem}
.path>span:first-child{display:block;margin-bottom:4px}
.warnbox{background:none;border:0;border-left:2px solid var(--purple);border-radius:0;padding:2px 0 2px 12px;margin:0 0 10px;font-size:.88rem}
table.props{margin:0 0 8px}
table.props th{width:11em;padding:7px 12px 7px 0;font-size:.82rem;text-transform:none;letter-spacing:0;font-weight:500;color:var(--muted);border-bottom:1px solid var(--line)}
table.props td{padding:7px 0}
.backlinks{background:none;border:0;border-top:1px solid var(--line);border-radius:0;padding:14px 0 0;margin-top:36px}
.backlinks h2{font-size:.78rem;letter-spacing:.09em;text-transform:uppercase;color:var(--muted);margin:0 0 6px}
.backlinks .lbl{font-weight:500}
.reading h2{margin-top:30px}
/* trace tree */
.pane-tree{margin-top:0}
.tsearch{background:none;border:0;border-bottom:1px solid var(--line);border-radius:0;padding:8px 0;font-size:.95rem}
.filters{margin:2px 0 14px;gap:4px}
.filters button{border:0;background:none;color:var(--muted);padding:4px 10px;font-weight:600}
.filters button:hover{background:var(--tint)}
.filters button[aria-pressed=true]{background:var(--ink);color:var(--bg)}
.tree ul{margin-left:11px;padding-left:12px;border-left:1px solid var(--line)}
.tree a.node{padding:4px 6px;font-size:.92rem}
.tree a.node:hover{background:var(--tint)}
.tree a.node.sel{background:var(--tint);font-weight:600}
.tree .cnt{display:inline;margin-left:8px;font-size:.76rem;color:var(--muted)}
.tree .idc{font-size:.68rem;padding:2px 5px;border-width:1px}
.tree summary{padding:2px 0}
.tree .gh{font-weight:700;font-size:.78rem;letter-spacing:.06em;text-transform:uppercase}
/* cards: documents, journey pages, insights */
.acards,.jcards,.icards{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:12px;margin-top:6px;border:0}
.acard,.jcard,.icard{display:flex;flex-direction:column;gap:4px;padding:16px;border:1px solid var(--line);border-radius:var(--r);background:none;text-decoration:none;color:var(--ink);overflow:hidden;min-height:112px}
.acard:hover,.jcard:hover,.icard:hover{border-color:var(--ink);box-shadow:none;background:none}
.acard[hidden],.icard[hidden]{display:none}
.acard>*:not(.thumb),.icard>*{margin:0}
.acard:not(:has(.thumb))>.atype{margin:0}
.acard .thumb{display:block;align-self:stretch;width:auto;max-width:none;margin:-16px -16px 10px;height:110px;object-fit:cover;object-position:top;border-bottom:1px solid var(--line);background:var(--tint)}
.acard .atype,.jcard .wk,.icard .itype{font-size:.7rem;font-weight:700;letter-spacing:.09em;text-transform:uppercase;color:var(--muted)}
.acard h3,.jcard h3,.icard h3{margin:2px 0 0;font-size:1rem;line-height:1.35}
.acard p,.jcard p,.icard p{margin:0;color:var(--muted);font-size:.86rem;line-height:1.5}
.acard .ameta{font-size:.76rem;color:var(--muted);margin-top:auto;padding-top:8px}
.icard .top{display:flex;align-items:center;gap:8px}
.icard .top .w{margin-left:auto}
.st{background:none;border:1px solid var(--line);color:var(--muted);font-weight:600;padding:0 7px}
.st-simulated,.st-planned,.st-draft{background:none;border:1px solid var(--ink);color:var(--ink)}
.ahead .kind{font-size:.74rem;letter-spacing:.09em}
.ahead h1{margin:4px 0 6px}
.ahead .sum{font-size:1rem;margin:0 0 12px}
.ahead p:has(.st){margin:0 0 10px}
.supports{margin:10px 0 0}
.mcard{background:none;margin:14px 0}
.mhead{padding:10px 14px}
.btn{background:none;color:var(--link);padding:0;font-weight:600;border-radius:0}
.btn:hover{text-decoration:underline}
.mcard iframe{height:520px}
.fig{border-radius:var(--r)}
.srcnote{margin-top:32px;font-size:.8rem}
.vmode{display:inline-flex;gap:2px;margin:0 0 14px;border:1px solid var(--line);border-radius:var(--r);padding:2px}
.vmode button{border:0;background:none;font:inherit;font-size:.82rem;font-weight:600;color:var(--muted);padding:4px 12px;border-radius:calc(var(--r) - 2px);cursor:pointer}
.vmode button[aria-pressed=true]{background:var(--ink);color:var(--bg)}
#v-trace .tree{display:none}
.tabs2{display:flex;gap:2px;border-bottom:1px solid var(--line);margin:0 0 14px;overflow-x:auto}
.tabs2 button{border:0;background:none;font:inherit;font-weight:600;font-size:.9rem;color:var(--muted);padding:10px 14px;margin-bottom:-1px;border-bottom:2px solid transparent;cursor:pointer;white-space:nowrap}
.tabs2 button:hover{color:var(--ink)}
.tabs2 button[aria-selected=true]{color:var(--ink);border-bottom-color:var(--purple)}
.tabs2 .n{margin-left:7px;font-size:.72rem;font-weight:700;padding:1px 7px;border-radius:99px;background:rgba(145,158,171,.16);color:var(--muted)}
.tabs2 button[aria-selected=true] .n{background:var(--tint2);color:var(--link)}
#v-trace.mode-tree .tree{display:block}
#v-trace.mode-tree .icards{display:none}
/* reference and journey pages */
html[data-theme] th{background:none}
.reference .reading,.journey .reading{max-width:none}
.reference .reading>p,.journey .reading>p,.journey .reading>ul,.journey .reading>ol{max-width:72ch}
.reference .reading>p>em:only-child,.journey .reading>p>em:only-child{font-style:normal;color:var(--muted)}
.reference .reading h2,.journey .reading h2{margin-top:36px}
.reference table,.journey table{margin:8px 0 0}
.journey td a{text-decoration:none;font-weight:600}
.journey td a:hover{text-decoration:underline}
.journey .reading>blockquote{max-width:72ch}
.back{display:inline-block;margin:0 0 18px;font-size:.8125rem;font-weight:600;color:var(--muted);text-decoration:none}
.back:hover{color:var(--ink)}
.journey .reading>p>em:only-child{font-size:.875rem}
.journey .reading>p:first-child{font-size:1rem}
.journey .doc>.reading>h1:first-child{margin-bottom:6px}
.journey .reading code{font-size:.84em}
.pn{border-top:1px solid var(--line);margin-top:32px;padding-top:14px}
.pn a{text-decoration:none;font-weight:600}
.pn a:hover{text-decoration:underline}
.reference td:first-child{white-space:nowrap;color:var(--muted);font-weight:600;width:1%}
.gst{font-size:.82rem;font-weight:600;white-space:nowrap}
.gst::before{content:"";display:inline-block;width:7px;height:7px;border-radius:50%;margin-right:7px;background:var(--muted);vertical-align:middle}
.gst-passed::before{background:#1a7f4b}
.gst-failed{color:#a33}
.gst-failed::before{background:#a33}
.dash{color:var(--muted)}
"""
CSS += MIN_CSS

JS = r"""
(function(){
  var root=document.documentElement; root.classList.add('js');
  var VIEWS=['overview','journey','docs','trace','reference'];
  function $(s,c){return (c||document).querySelector(s)}
  function $$(s,c){return [].slice.call((c||document).querySelectorAll(s))}
  var docs={}; $$('.doc').forEach(function(d){docs[d.id]=d});
  $$('.nback').forEach(function(b){b.addEventListener('click',function(){showPanel('root')})});
  var caseName=document.body.getAttribute('data-case');
  function route(){
    var id=decodeURIComponent((location.hash||'').replace(/^#\/?/,''))||'overview';
    var doc=null, view='overview';
    if(VIEWS.indexOf(id)>-1){view=id}
    else if(docs[id]){doc=docs[id]; var v=doc.closest('.view'); view=v?v.id.slice(2):'overview'}
    $$('.view').forEach(function(v){v.classList.toggle('on',v.id==='v-'+view)});
    $$('.side a[data-nav]').forEach(function(a){
      if(a.getAttribute('data-nav')===view){a.setAttribute('aria-current','page')}else{a.removeAttribute('aria-current')}
    });
    var mn=$('.side details.menu'); if(mn&&window.innerWidth<=900){mn.open=false}
    $$('.doc').forEach(function(d){d.classList.remove('on')});
    if(doc){doc.classList.add('on')}
    var j=$('#v-journey'); if(j){j.classList.toggle('has-doc',view==='journey'&&!!doc)}
    var t=$('#v-trace'); if(t){t.classList.toggle('has-item',view==='trace'&&!!doc)}
    var rv=$('#v-reference'); if(rv){rv.classList.toggle('has-doc',view==='reference'&&!!doc)}
    var dv=$('#v-docs'); if(dv){dv.classList.toggle('has-doc',view==='docs'&&!!doc)}
    $$('.subtabs a').forEach(function(a){
      if(doc&&a.getAttribute('href')==='#/'+doc.id){a.setAttribute('aria-current','page')}else{a.removeAttribute('aria-current')}
    });
    $$('.tree a.node').forEach(function(a){
      var on=view==='trace'&&doc&&a.getAttribute('data-id')===doc.id;
      a.classList.toggle('sel',!!on);
    });
    var sel=$('.tree a.node.sel');
    if(sel){var p=sel.parentElement; while(p&&p.id!=='tree'){if(p.tagName==='DETAILS'){p.open=true} p=p.parentElement}}
    document.title=(doc?doc.getAttribute('data-title')+' · ':'')+caseName;
    window.scrollTo(0,0);
  }
  window.addEventListener('hashchange',route);
  // tree filtering
  var tree=$('#tree'), q=$('#tsearch'), gs=$('#gsearch'), types={}, warnOnly=false;
  function applyCards(){
    var s=(q&&q.value||'').trim().toLowerCase(), any=!!s||warnOnly||Object.keys(types).length>0, n=0;
    $$('.icard').forEach(function(c){
      var ok=(!s||c.getAttribute('data-text').indexOf(s)>-1)&&(Object.keys(types).length===0||types[c.getAttribute('data-type')])&&(!warnOnly||c.getAttribute('data-warn')==='1');
      c.hidden=!ok; if(ok){n++}
    });
    var t=$('#tcount'); if(t){t.textContent=any?(n+' mục khớp'):''}
  }
  $$('.vmode button').forEach(function(b){b.addEventListener('click',function(){
    var tv=$('#v-trace'); tv.classList.toggle('mode-tree',b.getAttribute('data-vmode')==='tree');
    $$('.vmode button').forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false')});
  })});
  function apply(){
    applyCards();
    if(!tree) return;
    var s=(q.value||'').trim().toLowerCase(), any=!!s||warnOnly||Object.keys(types).length>0, shown=0;
    function walk(ul){
      var vis=false;
      [].slice.call(ul.children).forEach(function(li){
        var own=(!s||(li.getAttribute('data-text')||'').indexOf(s)>-1)
          &&(Object.keys(types).length===0||types[li.getAttribute('data-type')])
          &&(!warnOnly||li.getAttribute('data-warn')==='1');
        var sub=li.querySelector(':scope > details > ul')||li.querySelector(':scope > ul');
        var cv=sub?walk(sub):false;
        var isItem=!!li.getAttribute('data-type');
        if(own&&isItem&&any){shown++}
        var show=(own&&(!sub||!any||true))||cv;
        if(any&&!own&&!cv){show=false}
        li.hidden=!show;
        if(any&&cv){var d=li.querySelector(':scope > details'); if(d){d.open=true}}
        vis=vis||show;
      });
      return vis;
    }
    walk(tree);
    var c=$('#tcount'); if(c&&$('#v-trace').classList.contains('mode-tree')){c.textContent=any?(shown+' mục khớp'):''}
  }
  if(q){q.addEventListener('input',function(){if(gs){gs.value=q.value} apply()})}
  if(gs){gs.addEventListener('input',function(){
    if(q){q.value=gs.value}
    if(!/^#\/(trace|[OHMDT]\d+)$/.test(location.hash)){location.hash='#/trace'}
    apply();
  })}
  $$('#v-trace .filters button').forEach(function(b){
    b.addEventListener('click',function(){
      var on=b.getAttribute('aria-pressed')!=='true';
      b.setAttribute('aria-pressed',on?'true':'false');
      if(b.getAttribute('data-warn')){warnOnly=on}
      else{var k=b.getAttribute('data-type'); if(on){types[k]=true}else{delete types[k]}}
      apply();
    });
  });
  var cards=$$('#acards .acard'), fs={}, ft={};
  function applyDocs(){
    var q=(($('#dsearch')||{}).value||'').trim().toLowerCase(), n=0;
    cards.forEach(function(c){
      var ok=(!q||c.getAttribute('data-text').indexOf(q)>-1)&&(!Object.keys(ft).length||ft[c.getAttribute('data-type')])&&(!Object.keys(fs).length||fs[c.getAttribute('data-stage')]);
      c.hidden=!ok; if(ok){n++}
    });
    var c=$('#dcount'); if(c){c.textContent=(q||Object.keys(ft).length||Object.keys(fs).length)?(n+' tài liệu khớp'):''}
  }
  var ds=$('#dsearch'); if(ds){ds.addEventListener('input',applyDocs)}
  $$('#v-docs .filters button').forEach(function(b){
    b.addEventListener('click',function(){
      var on=b.getAttribute('aria-pressed')!=='true'; b.setAttribute('aria-pressed',on?'true':'false');
      var k=b.getAttribute('data-ftype');
      if(k){if(on){ft[k]=true}else{delete ft[k]}}
      applyDocs();
    });
  });
  function tabGroup(sel,onPick){
    $$(sel+' button').forEach(function(b){
      b.addEventListener('click',function(){
        $$(sel+' button').forEach(function(x){x.setAttribute('aria-selected',x===b?'true':'false')});
        onPick(b);
      });
    });
  }
  tabGroup('#v-docs .tabs2',function(b){fs={}; var s=b.getAttribute('data-fstage'); if(s){fs[s]=true} applyDocs()});
  tabGroup('#v-trace .tabs2',function(b){types={}; var t=b.getAttribute('data-type'); if(t){types[t]=true} apply()});
  var sel=$('#themeselect');
  if(sel){
    try{var saved=localStorage.getItem('hub-theme'); if(saved){sel.value=saved; root.setAttribute('data-theme',saved)}}catch(e){}
    sel.addEventListener('change',function(){
      root.setAttribute('data-theme',sel.value);
      try{localStorage.setItem('hub-theme',sel.value)}catch(e){}
    });
  }
  route();
})();
"""


THEMES = [("minimal", "Minimal (MUI, xanh lá)"), ("notion", "Notion (xanh, gọn)"), ("classic", "Classic (tím)"), ("editorial", "Editorial (chữ có chân, giấy kem)"),
          ("swiss", "Swiss (đen trắng, khung rõ)"), ("calm", "Calm (xanh lá dịu)")]

# Each theme only overrides the colour tokens and a few details; layout is shared.
THEME_CSS = r"""
/* minimal: the Minimal UI kit look on top of Material UI: green primary, soft cards, dashed rules, soft "label" chips */
[data-theme=minimal]{--ink:#1c252e;--bg:#fff;--surface:#f4f6f8;--muted:#637381;--line:rgba(145,158,171,.28);--purple:#00a76f;--link:#007867;--tint:rgba(0,167,111,.08);--tint2:rgba(0,167,111,.16);--on-purple:#fff;--r:8px}
[data-theme=minimal] body{font-family:"Public Sans",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif}
[data-theme=minimal] h1{font-weight:800;letter-spacing:-.01em}
[data-theme=minimal] h2{font-weight:700;color:#637381}
[data-theme=minimal] header.top{background:rgba(255,255,255,.86);backdrop-filter:blur(6px);border-bottom:1px dashed var(--line)}
[data-theme=minimal] .brand{font-weight:800;letter-spacing:-.01em}
[data-theme=minimal] .brand::before{content:"";display:inline-block;width:10px;height:10px;border-radius:3px;background:#00a76f;margin-right:10px}
[data-theme=minimal] .gsearch,[data-theme=minimal] .tsearch{background:#fff;border:1px solid rgba(145,158,171,.32);border-radius:8px;padding:9px 14px;color:var(--ink)}
[data-theme=minimal] .gsearch:focus,[data-theme=minimal] .tsearch:focus{outline:0;border-color:#1c252e;box-shadow:0 0 0 1px #1c252e}
[data-theme=minimal] .side{border-right:1px dashed var(--line)}
[data-theme=minimal] .nav2 a{border-radius:8px;min-height:44px;font-weight:500;font-size:.9rem;color:#637381}
[data-theme=minimal] .nav2 a:hover{background:rgba(145,158,171,.08)}
[data-theme=minimal] .nav2 a[aria-current=page]{background:rgba(0,167,111,.08);color:#007867;font-weight:700}
[data-theme=minimal] .nav2 a[aria-current=page] .nm{color:#007867;opacity:1}
[data-theme=minimal] .acard,[data-theme=minimal] .jcard,[data-theme=minimal] .icard{border:0;border-radius:16px;background:#fff;box-shadow:0 0 2px 0 rgba(145,158,171,.2),0 12px 24px -4px rgba(145,158,171,.12);transition:box-shadow .2s,transform .2s}
[data-theme=minimal] .acard:hover,[data-theme=minimal] .jcard:hover,[data-theme=minimal] .icard:hover{border:0;box-shadow:0 0 2px 0 rgba(145,158,171,.24),0 20px 40px -4px rgba(145,158,171,.24);transform:translateY(-2px)}
[data-theme=minimal] .acard .thumb{border-radius:0}
[data-theme=minimal] .acard .atype,[data-theme=minimal] .jcard .wk,[data-theme=minimal] .icard .itype{color:#919eab}
[data-theme=minimal] .acard h3,[data-theme=minimal] .jcard h3,[data-theme=minimal] .icard h3{font-weight:700}
[data-theme=minimal] .stats{border:0;background:#f4f6f8;border-radius:16px;padding:18px 24px}
[data-theme=minimal] .stats b{font-weight:800;color:#1c252e}
[data-theme=minimal] .glist{border-top:0}
[data-theme=minimal] .grow{border-bottom:1px dashed var(--line)}
[data-theme=minimal] .grow .gb{height:6px;background:rgba(0,167,111,.16)}
[data-theme=minimal] .grow .gb i{background:#00a76f;border-radius:99px}
[data-theme=minimal] .grow .gs,[data-theme=minimal] .gst{display:inline-block;justify-self:start;font-size:.75rem;font-weight:700;line-height:24px;padding:0 8px;border-radius:6px;background:rgba(255,171,0,.16);color:#b76e00}
[data-theme=minimal] .grow .gs.ok,[data-theme=minimal] .gst-passed{background:rgba(34,197,94,.16);color:#118d57}
[data-theme=minimal] .grow .gs.no,[data-theme=minimal] .gst-failed{background:rgba(255,86,48,.16);color:#b71d18}
[data-theme=minimal] .gst::before{display:none}
[data-theme=minimal] table th{background:#f4f6f8;color:#637381;font-weight:600;font-size:.8125rem;text-transform:none;letter-spacing:0;border-bottom:0}
[data-theme=minimal] table th:first-child{border-radius:8px 0 0 8px}
[data-theme=minimal] table th:last-child{border-radius:0 8px 8px 0}
[data-theme=minimal] table td{border-bottom:1px dashed var(--line)}
[data-theme=minimal] table.props th{background:none;color:#637381;font-weight:500;border-radius:0;border-bottom:1px dashed var(--line)}
[data-theme=minimal] .chip,[data-theme=minimal] .idc,[data-theme=minimal] .idtag{border-radius:6px;font-weight:700;font-size:.75rem;border:1px solid transparent}
[data-theme=minimal] .t-O{background:#00a76f;color:#fff}
[data-theme=minimal] .t-H{background:transparent;border-color:rgba(0,167,111,.5);color:#007867}
[data-theme=minimal] .t-D{background:#1c252e;color:#fff}
[data-theme=minimal] .t-T{background:transparent;border-color:rgba(28,37,46,.35);color:#1c252e}
[data-theme=minimal] .t-M{background:rgba(145,158,171,.16);color:#454f5b}
[data-theme=minimal] .t-P{background:transparent;border:1px dashed rgba(145,158,171,.8);color:#637381}
[data-theme=minimal] .t-A{background:rgba(0,184,217,.16);color:#006c9c}
[data-theme=minimal] .filters button{border:1px solid rgba(145,158,171,.32);border-radius:8px;background:#fff;color:#454f5b;font-weight:600;padding:5px 12px}
[data-theme=minimal] .filters button:hover{background:rgba(145,158,171,.08)}
[data-theme=minimal] .filters button[aria-pressed=true]{background:#1c252e;border-color:#1c252e;color:#fff}
[data-theme=minimal] .tabs2 button[aria-selected=true]{color:#007867;border-bottom-color:#00a76f}
[data-theme=minimal] .vmode{border:1px solid rgba(145,158,171,.32);border-radius:8px;padding:3px}
[data-theme=minimal] .vmode button{border-radius:6px;font-weight:700}
[data-theme=minimal] .vmode button[aria-pressed=true]{background:#1c252e;color:#fff}
[data-theme=minimal] .btn{background:#1c252e;color:#fff;border-radius:8px;padding:6px 14px;font-weight:700;font-size:.8125rem}
[data-theme=minimal] .btn:hover{text-decoration:none;background:#454f5b}
[data-theme=minimal] .banner,[data-theme=minimal] .warnbox{background:rgba(255,171,0,.12);color:#7a4100;border:0;border-radius:8px;padding:12px 16px}
[data-theme=minimal] .warnlist li{border-top:0;border-bottom:1px dashed var(--line)}
[data-theme=minimal] details.help{border:1px dashed var(--line);border-radius:16px;padding:14px 20px}
[data-theme=minimal] .backlinks{border-top:1px dashed var(--line)}
[data-theme=minimal] .mcard{border:0;border-radius:16px;box-shadow:0 0 2px 0 rgba(145,158,171,.2),0 12px 24px -4px rgba(145,158,171,.12);background:#fff;overflow:hidden}
[data-theme=minimal] .fig{border:0;border-radius:16px;box-shadow:0 0 2px 0 rgba(145,158,171,.2),0 12px 24px -4px rgba(145,158,171,.12)}
[data-theme=minimal] .st{border:0;border-radius:6px;background:rgba(145,158,171,.16);color:#454f5b;font-weight:700;line-height:22px}
[data-theme=minimal] .st-verified{background:rgba(34,197,94,.16);color:#118d57}
[data-theme=minimal] .st-draft{background:rgba(255,171,0,.16);color:#b76e00;border:0}
[data-theme=minimal] .st-simulated,[data-theme=minimal] .st-planned{background:rgba(0,184,217,.16);color:#006c9c;border:0}
[data-theme=minimal] .pn{border-top:1px dashed var(--line)}
[data-theme=minimal] code{background:rgba(145,158,171,.16);border-radius:6px}
[data-theme=minimal] footer.foot{border-top:1px dashed var(--line)}
[data-theme=minimal] .tree ul{border-left:1px dashed var(--line)}

/* notion: neutral grey, one blue accent, small radius, almost no fill */
[data-theme=notion]{--ink:#37352f;--bg:#fff;--surface:#f7f6f3;--muted:rgba(55,53,47,.65);--line:rgba(55,53,47,.13);--purple:#2383e2;--link:#0b6bcb;--tint:rgba(35,131,226,.08);--tint2:rgba(35,131,226,.15);--r:6px}
[data-theme=notion] h1{font-size:2.1rem;font-weight:700}
[data-theme=notion] .tabs a{border-radius:6px;font-weight:500}
[data-theme=notion] .card,[data-theme=notion] .jcard,[data-theme=notion] details.help{background:transparent}
[data-theme=notion] .gate{background:var(--surface);color:var(--ink);border:1px solid var(--line)}
[data-theme=notion] .gate .bar{background:var(--line)}
[data-theme=notion] .gate .bar i{background:var(--purple)}
[data-theme=notion] .banner{background:var(--tint2);color:var(--ink)}
[data-theme=notion] th{background:var(--surface);font-weight:600}
[data-theme=notion] .chip,[data-theme=notion] .idc,[data-theme=notion] .idtag{border-radius:4px}

/* editorial: serif text on warm paper, terracotta accent, thin rules */
[data-theme=editorial]{--ink:#201c17;--bg:#fbf8f3;--surface:#f3eee5;--muted:rgba(32,28,23,.68);--line:rgba(32,28,23,.18);--purple:#9a3412;--link:#9a3412;--tint:rgba(154,52,18,.08);--tint2:rgba(154,52,18,.15);--r:2px}
[data-theme=editorial] body{font-family:Georgia,"Times New Roman",serif;font-size:17px}
[data-theme=editorial] h1,[data-theme=editorial] h2,[data-theme=editorial] h3{font-family:Georgia,"Times New Roman",serif;font-weight:700;letter-spacing:-.01em}
[data-theme=editorial] header.top{border-bottom:2px solid var(--ink)}
[data-theme=editorial] .tabs a{border-radius:0;text-transform:uppercase;letter-spacing:.08em;font-size:.78rem;font-family:-apple-system,"Segoe UI",Helvetica,Arial,sans-serif}
[data-theme=editorial] .card,[data-theme=editorial] .jcard,[data-theme=editorial] details.help,[data-theme=editorial] .pane-tree{background:transparent;border-color:var(--ink)}
[data-theme=editorial] .gate{background:transparent;color:var(--ink);border:1px solid var(--ink)}
[data-theme=editorial] .gate .bar{background:var(--line)}
[data-theme=editorial] .gate .bar i{background:var(--purple)}
[data-theme=editorial] .banner{background:var(--ink);color:var(--bg)}
[data-theme=editorial] .chip,[data-theme=editorial] .idc,[data-theme=editorial] .idtag,[data-theme=editorial] .filters button,[data-theme=editorial] .tsearch,[data-theme=editorial] .gsearch,[data-theme=editorial] table,[data-theme=editorial] .tree a.node,[data-theme=editorial] .card .lbl,[data-theme=editorial] .ihead .kind,[data-theme=editorial] .jcard .wk{font-family:-apple-system,"Segoe UI",Helvetica,Arial,sans-serif}
[data-theme=editorial] th{background:transparent;border-bottom:2px solid var(--ink)}
[data-theme=editorial] .gsearch{border-radius:0}

/* swiss: black on white, hard 1px frames, one signal colour, no rounding */
[data-theme=swiss]{--ink:#000;--bg:#fff;--surface:#fff;--muted:rgba(0,0,0,.62);--line:#000;--purple:#ff3b00;--link:#000;--tint:#f1f1f1;--tint2:#e3e3e3;--r:0}
[data-theme=swiss] body{font-family:"Helvetica Neue",Helvetica,Arial,sans-serif}
[data-theme=swiss] h1{font-size:2.3rem;font-weight:800;letter-spacing:-.03em}
[data-theme=swiss] h2{text-transform:uppercase;font-size:.85rem;letter-spacing:.1em;border-top:2px solid #000;padding-top:10px}
[data-theme=swiss] header.top{border-bottom:2px solid #000}
[data-theme=swiss] .tabs a{border-radius:0;text-transform:uppercase;font-size:.78rem;letter-spacing:.06em}
[data-theme=swiss] .tabs a[aria-current=page]{background:#000;color:#fff}
[data-theme=swiss] .gsearch,[data-theme=swiss] .tsearch,[data-theme=swiss] .filters button{border-radius:0;border-color:#000}
[data-theme=swiss] .filters button[aria-pressed=true]{background:#000;border-color:#000}
[data-theme=swiss] .card,[data-theme=swiss] .jcard,[data-theme=swiss] details.help,[data-theme=swiss] .pane-tree,[data-theme=swiss] .backlinks{border:1px solid #000}
[data-theme=swiss] .jcard:hover{border-color:var(--purple);box-shadow:4px 4px 0 var(--purple)}
[data-theme=swiss] .gate{background:#000;color:#fff}
[data-theme=swiss] .gate .bar{background:rgba(255,255,255,.3)}
[data-theme=swiss] .gate .bar i{background:var(--purple)}
[data-theme=swiss] .banner{background:var(--purple);color:#000;font-weight:700}
[data-theme=swiss] th{background:transparent;border-bottom:2px solid #000;text-transform:uppercase;font-size:.75rem;letter-spacing:.06em}
[data-theme=swiss] td{border-bottom:1px solid #000}
[data-theme=swiss] .warnlist li,[data-theme=swiss] blockquote{background:#f1f1f1;border-left:6px solid var(--purple)}
[data-theme=swiss] .t-H{color:#000;border-color:#000}
[data-theme=swiss] .t-T{border-color:#000}

/* calm: soft sage green, generous radius, quiet shadows */
[data-theme=calm]{--ink:#1f2a24;--bg:#fbfcfa;--surface:#f1f5f0;--muted:rgba(31,42,36,.66);--line:rgba(31,42,36,.12);--purple:#2f7d5b;--link:#256a4b;--tint:rgba(47,125,91,.10);--tint2:rgba(47,125,91,.18);--r:16px}
[data-theme=calm] h1{font-weight:700;letter-spacing:-.02em}
[data-theme=calm] .card,[data-theme=calm] .jcard,[data-theme=calm] details.help{box-shadow:0 1px 2px rgba(31,42,36,.06),0 4px 14px rgba(31,42,36,.04);border-color:transparent;background:#fff}
[data-theme=calm] .pane-tree{border-color:transparent;box-shadow:0 1px 2px rgba(31,42,36,.06),0 4px 14px rgba(31,42,36,.04);background:#fff}
[data-theme=calm] .gate{background:var(--purple);color:#fff}
[data-theme=calm] .banner{background:#fff;color:var(--ink);border:1px solid var(--line);border-left:6px solid var(--purple)}
[data-theme=calm] th{background:var(--surface)}
[data-theme=calm] .tabs a[aria-current=page]{box-shadow:0 2px 8px rgba(47,125,91,.35)}
"""


def theme_rules(theme, all_themes=False):
    """CSS overrides for one theme (or every theme when previewing with the switcher)."""
    keep = []
    for line in THEME_CSS.split("\n"):
        m = re.match(r"\[data-theme=(\w+)\]", line)
        if m and (all_themes or m.group(1) == theme):
            keep.append(line)
    return "\n" + "\n".join(keep) + "\n"


PLACEHOLDER_RE = re.compile(r"\[(?:EXAMPLE\]|[A-Z][A-Z0-9 ]{2,}[^\]]*\])")



# --------------------------------------------------------------------------- artifacts
ART_TYPES = {
    "competitor-analysis": "Competitor analysis", "persona": "Persona", "survey-results": "Survey results",
    "interview-synthesis": "Interview synthesis", "user-flow": "User flow", "ia-sitemap": "Information architecture",
    "prototype": "Prototype", "test-plan": "Test plan", "test-report": "Test report",
    "requirements": "Requirements (PRD)", "solution-pool": "Solution pool", "generic": "Document",
}
STAGES = ["Setup", "Discover", "Define", "Develop", "Deliver"]
ART_STATUS = {"verified": "Verified", "draft": "Draft", "simulated": "Simulated", "planned": "Planned"}
IMG_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}
VIDEO_EXT = {".mp4", ".webm", ".mov"}
PRIVATE_PARTS = ("_raw-private", "_personal", "/.git/", "_templates")
DRAFT_RE = re.compile(r"\bAI draft\b", re.I)


def _is_private(abs_path):
    n = abs_path.replace(os.sep, "/")
    return any(x in n for x in PRIVATE_PARTS) or os.path.basename(n) in ("AGENTS.md", ".DS_Store")


def _aslist(v):
    if v is None or v == "":
        return []
    return list(v) if isinstance(v, list) else [v]


class Artifact(object):
    def __init__(self, slug, md_path, folder):
        self.id, self.path, self.folder = slug, md_path, folder
        raw = open(md_path, encoding="utf-8").read()
        self.meta, self.body = _front(raw)
        hm = re.search(r"^#\s+(.+)$", self.body, flags=re.M)
        self.title = str(self.meta.get("title") or (hm.group(1) if hm else slug)).strip()
        self.type = str(self.meta.get("type") or "generic").strip().lower()
        self.stage = str(self.meta.get("stage") or "").strip()
        self.status = str(self.meta.get("status") or "").strip().lower()
        self.summary = str(self.meta.get("summary") or "").strip()
        self.takeaways = [str(x) for x in _aslist(self.meta.get("takeaways"))]
        self.supports = _ids(_aslist(self.meta.get("supports")))
        self.source = str(self.meta.get("source") or "").strip()
        self.links = [str(x) for x in _aslist(self.meta.get("links"))]
        self.media = [str(x) for x in _aslist(self.meta.get("media"))]
        self.embed = str(self.meta.get("embed") or "").lower() in ("true", "yes", "1")
        self.embed_url = str(self.meta.get("embed_url") or "").strip()


def collect_artifacts(case):
    base = os.path.join(case, "hub", "artifacts")
    out = []
    if not os.path.isdir(base):
        return out
    for name in sorted(os.listdir(base), key=_natkey):
        if name.startswith(("_", ".")) or name.lower() == "readme.md":
            continue
        full = os.path.join(base, name)
        if os.path.isfile(full) and name.endswith(".md"):
            out.append(Artifact(name[:-3], full, None))
        elif os.path.isdir(full):
            for cand in ("index.md", "README.md", name + ".md"):
                if os.path.isfile(os.path.join(full, cand)):
                    out.append(Artifact(name, os.path.join(full, cand), full))
                    break
    return out


def media_kind(path):
    ext = os.path.splitext(path)[1].lower()
    if ext in IMG_EXT:
        return "image"
    if ext in VIDEO_EXT:
        return "video"
    if ext == ".pdf":
        return "pdf"
    if ext in (".html", ".htm"):
        return "html"
    if ext == ".csv":
        return "csv"
    if ext == ".md":
        return "doc"
    return "file"


def render_md(md, src, resolver, problems, team=False):
    """Render markdown; sections whose H2 mentions 'AI draft' are dropped (default) or folded (team mode)."""
    segs, cur = [], []
    for line in md.replace("\r\n", "\n").split("\n"):
        if re.match(r"##\s+\S", line):
            segs.append(cur)
            cur = [line]
        else:
            cur.append(line)
    segs.append(cur)
    out = []
    for seg in segs:
        if not any(l.strip() for l in seg):
            continue
        head = seg[0] if re.match(r"##\s+\S", seg[0]) else ""
        draft = bool(head and DRAFT_RE.search(head))
        if draft and not team:
            continue
        h = Renderer(src, resolver, problems).render("\n".join(seg))
        if draft:
            h = '<details class="draft"><summary>Bản nháp AI, chưa kiểm tra: %s</summary>%s</details>' % (
                html.escape(re.sub(r"^#+\s*", "", head), quote=False), h)
        out.append(h)
    return "\n".join(out)


def plural(n, one, many):
    return "%d %s" % (n, one if n == 1 else many)


def esc(s):
    return html.escape(s, quote=True)


def build(case, out_path, theme="minimal", switcher=False, team=False, bundle=False):
    problems = []
    overview, weekly, items, ref = collect(case)
    arts = collect_artifacts(case)
    A = {a.id: a for a in arts}
    used_media = set()
    name, agreement = case_info(overview.md, case)
    winfo = week_info(overview.md)
    pr_md = next((p.md for p in ref if p.id == "principles"), "")
    gates_md = next((p.md for p in ref if p.id == "gates"), "")
    principles = parse_principles(pr_md)
    gates = parse_gates(gates_md)
    G = Graph(items, principles)

    pages = weekly + ref + items
    by_path = {os.path.normcase(os.path.abspath(p.path)): p.id for p in pages}
    by_path[os.path.normcase(os.path.abspath(overview.path))] = "overview"
    case_abs = os.path.abspath(case)
    out_dir = os.path.dirname(os.path.abspath(out_path))
    for a in arts:
        by_path[os.path.normcase(os.path.abspath(a.path))] = a.id
    for a in arts:  # a link to a working file that backs an artifact opens that artifact
        if a.source:
            sp = os.path.normcase(os.path.abspath(os.path.join(os.path.dirname(a.path), a.source)))
            by_path.setdefault(sp, a.id)

    media_abs = set()
    for a in arts:
        for m in a.media:
            media_abs.add(os.path.abspath(os.path.normpath(os.path.join(os.path.dirname(a.path), m))))

    def href_for(abs_path):
        used_media.add(abs_path)
        base = case_abs if bundle else out_dir
        return urllib.parse.quote(os.path.relpath(abs_path, base).replace(os.sep, "/"), safe="/")

    def resolver(src, url, is_img):
        if re.match(r"(https?:|mailto:)", url):
            return "web", url
        if url.startswith("#"):
            return "anchor", url
        target = os.path.normpath(os.path.join(os.path.dirname(src), url.split("#")[0]))
        key = os.path.normcase(os.path.abspath(target))
        if key in by_path:
            return "page", by_path[key]
        if os.path.isfile(target):
            if _is_private(target):
                return "outside", os.path.relpath(target, case_abs)
            if target.lower().endswith(".md") and os.path.abspath(target) not in media_abs:
                # raw working files are not published unless an artifact lists them in `media`
                return "outside", os.path.relpath(target, case_abs)
            if not os.path.abspath(target).startswith(case_abs + os.sep):
                return "outside", os.path.basename(target)
            return "file", href_for(os.path.abspath(target))
        if os.path.isdir(target):
            return "outside", os.path.relpath(target, case_abs) + "/"
        return "broken", url

    # --- consistency checks
    for p in items:
        if not p.meta:
            problems.append("%s: thiếu khối properties (--- ... ---) ở đầu file" % os.path.basename(p.path))
        elif not p.meta.get("title"):
            problems.append("%s: thiếu property title" % os.path.basename(p.path))
        tp = str(p.meta.get("type", "")).lower()
        if p.meta and tp and tp != TYPE_WORD[p.letter]:
            problems.append("%s: property type là '%s' nhưng mã %s thuộc loại %s" % (p.id, tp, p.id, TYPE_WORD[p.letter]))
    seen = {}
    for p in pages:
        if p.id in seen:
            problems.append("ID trùng: %s" % p.id)
        seen[p.id] = 1
    for i, p in G.items.items():
        for label, val in p.meta.items():
            if label not in REL_KEYS:
                continue
            for t in _ids(val):
                if t not in G.items and t not in principles:
                    problems.append("%s trỏ tới %s nhưng không có file hoặc dòng principle tương ứng" % (i, t))

    def chip(i, cls="chip"):
        if i in A:
            return '<a class="%s t-A" href="#/%s" title="%s">%s</a>' % (cls, i, esc(A[i].title), esc(A[i].title if len(A[i].title) < 28 else A[i].title[:26] + "…"))
        if i in G.items:
            p = G.items[i]
            return '<a class="%s t-%s" href="#/%s" title="%s">%s</a>' % (cls, p.letter, i, esc(p.title), i)
        if i in principles:
            return '<a class="%s t-P" href="#/principles" title="%s">%s</a>' % (cls, esc(principles[i][0]), i)
        return '<span class="%s">%s</span>' % (cls, esc(i))

    def val_html(x, r):
        def link(m):
            tid = (m.group(2) or m.group(1)).strip()
            return chip(tid) if (tid in G.items or tid in principles) else esc(tid)
        if re.search(r"\[\[", x):
            return re.sub(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", lambda m: "\x00" + link(m) + "\x00", esc(x)).replace("\x00", "")
        return r.inline(x)

    def prop_table(p, r):
        rows_ = ""
        for k, v in p.meta.items():
            if k in ("title", "type"):  # both already shown in the page header
                continue
            vals = v if isinstance(v, list) else [v]
            if k == "type" and p.letter in VI_NAME:
                vals = [VI_NAME[p.letter][0]]
            cell = " ".join(val_html(str(x), r) for x in vals if str(x).strip()) or "—"
            rows_ += '<tr><th scope="row">%s</th><td>%s</td></tr>' % (esc(PROP_LABEL.get(k, k.replace("_", " ").capitalize())), cell)
        return ('<div class="table-wrap"><table class="props"><tbody>%s</tbody></table></div>' % rows_) if rows_ else ""

    def chips(ids):
        return '<span class="chips">%s</span>' % "".join(chip(i) for i in ids) if ids else '<span class="missing">chưa có</span>'

    placeholders = sum(len(PLACEHOLDER_RE.findall(p.md)) for p in [overview] + pages)

    art_for = {}
    for a in arts:
        for s in a.supports:
            if s in G.items:
                art_for.setdefault(s, []).append(a.id)
            elif s not in principles:
                problems.append("Tài liệu %s trỏ tới %s nhưng không có item đó" % (a.id, s))
        if a.id in seen:
            problems.append("ID trùng: %s (tài liệu và trang)" % a.id)
        if not a.supports:
            G.warnings.append(("art-orphan", [a.id], "Document này chưa nối với item nào (property supports đang trống)"))

    def media_of(a):
        """(kind, abs, name) in a stable order: explicit `media` first, then files dropped in the artifact folder."""
        seen_, out = set(), []
        base = os.path.dirname(a.path)
        for m in a.media:
            ab = os.path.abspath(os.path.normpath(os.path.join(base, m)))
            if not os.path.isfile(ab):
                problems.append("Tài liệu %s: không tìm thấy tệp media %s" % (a.id, m))
                continue
            if _is_private(ab):
                problems.append("Tài liệu %s: bỏ qua tệp nằm trong vùng riêng tư (%s)" % (a.id, m))
                continue
            if ab not in seen_:
                seen_.add(ab)
                out.append((media_kind(ab), ab, os.path.basename(ab)))
        if a.folder:
            for fn in sorted(os.listdir(a.folder), key=_natkey):
                ab = os.path.abspath(os.path.join(a.folder, fn))
                if os.path.isfile(ab) and ab != os.path.abspath(a.path) and not fn.startswith(".") and ab not in seen_ and not _is_private(ab):
                    seen_.add(ab)
                    out.append((media_kind(ab), ab, fn))
        order = {"image": 0, "html": 1, "video": 2, "pdf": 3, "csv": 4, "doc": 5, "file": 6}
        return sorted(out, key=lambda x: order.get(x[0], 9))

    # --- overview
    nwarn = len(G.warnings)
    stats = "".join('<span><b>%d</b>%s</span>' % (len(getattr(G, L)), pl.lower()) for L, _, _, pl in TYPES)
    stats += '<span class="w"><b>%d</b>warnings</span>' % nwarn
    gate_html = ""
    for g in gates:
        pct = int(100 * g["passed"] / g["total"]) if g["total"] else 0
        stc = "ok" if g["status"] == "passed" else ("no" if g["status"] == "failed" else "")
        gate_html += ('<div class="grow"><div class="gn"><small>%s</small><strong>%s</strong></div><div class="gs %s">%s</div>'
                      '<div class="gb"><i style="width:%d%%"></i></div><div class="gc">%d/%d checks</div></div>') % (
            esc(g["name"].split("(")[0].strip()), esc(g["name"].split("(")[-1].rstrip(")")) if "(" in g["name"] else "",
            stc, STATUS_VI.get(g["status"], g["status"]), pct, g["passed"], g["total"])
    rows = ""
    for d in G.D:
        hs = G.tests.get(d, [])
        os_ = []
        for h in hs:
            for o in G.serves.get(h, []):
                if o not in os_:
                    os_.append(o)
        ts = []
        for h in hs:
            for t_ in G.tests_of(h):
                if t_ not in ts:
                    ts.append(t_)
        rows += "<tr><td>%s %s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (
            chip(d), esc(G.items[d].title), chips(hs), chips(os_), chips(ts),
            chips(G.follows.get(d, [])) if G.follows.get(d) else "—",
            chips(G.strains.get(d, [])) if G.strains.get(d) else "—")
    align = ('<div class="table-wrap"><table><thead><tr><th>Decision</th><th>Hypothesis</th><th>Opportunity</th><th>Test</th><th>Follows</th><th>Pulls against</th></tr></thead><tbody>%s</tbody></table></div>' % rows) if rows else '<p class="ok">Chưa có decision nào.</p>'
    if G.warnings:
        merged = []  # warnings with the same wording become one line that lists every item it applies to
        for _, ids, text in G.warnings:
            for m_ in merged:
                if m_[1] == text:
                    m_[0].extend(i for i in ids if i not in m_[0])
                    break
            else:
                merged.append([list(ids), text])
        wl = "".join('<li>%s <span class="chips" style="display:inline-flex;vertical-align:middle">%s</span> <strong>%s</strong></li>' % (
            "⚠", "".join(chip(i) for i in ids), esc(text)) for ids, text in merged)
        warn_html = '<ul class="warnlist">%s</ul>' % wl
    else:
        warn_html = '<p class="ok">Không có warning nào: mọi decision đều lần ngược được về một opportunity, và mọi hypothesis đều có test và metric.</p>'
    banner = ""
    if placeholders:
        banner = '<div class="banner" role="note"><strong>Báo cáo này còn nội dung mẫu hoặc chỗ chưa điền</strong> (khoảng %d chỗ, kể cả các mục có nhãn [EXAMPLE]). Hãy điền hoặc xoá trước khi gửi cho người khác.</div>' % placeholders
    howto = (
        '<details class="help"><summary>Cách đọc báo cáo và các từ khoá</summary>'
        '<p>Điểm chính: <strong>mỗi decision đều lần ngược được về user need đứng sau nó.</strong> '
        'Dùng menu bên trái để đi tới từng trang. Mở các mục có dấu ⚠ trong Insights để thấy chỗ cần xem lại.</p>'
        '<dl><dt>Opportunity</dt><dd>Điều người dùng cần hoặc đang gặp khó, có evidence. Không phải một feature.</dd>'
        '<dt>Hypothesis</dt><dd>Điều nhóm tin là đúng, kèm cách sẽ biết nó đúng hay sai.</dd>'
        '<dt>Decision</dt><dd>Một lựa chọn thiết kế cụ thể, kèm lý do.</dd>'
        '<dt>Test</dt><dd>Cách kiểm chứng một hypothesis với người dùng thật.</dd>'
        '<dt>Metric</dt><dd>Con số cho biết hypothesis đúng hay sai. Nhãn <em>assumed</em> nghĩa là chưa được người phụ trách sản phẩm xác nhận.</dd>'
        '<dt>Principle</dt><dd>Quy tắc thiết kế mà mọi decision cần đạt, ví dụ 10 usability heuristics của Nielsen (P1 đến P10).</dd>'
        '<dt>Gate</dt><dd>Bước kiểm tra trước khi sang giai đoạn sau.</dd>'
        '<dt>Alignment</dt><dd>Mức độ mỗi decision nối được về opportunity và đạt các principle.</dd></dl></details>')
    docs_section = ""
    v_overview = (
        '<section class="view" id="v-overview"><div class="wrap">%s<h1>%s</h1><p class="lede">Agreement với product và business: <strong>%s</strong></p>'
        '<div class="stats">%s</div>'
        '<h2>Gates</h2><div class="glist">%s</div>'
        '<h2>Warnings</h2>%s'
        '<h2>Alignment</h2>%s'
        '%s</div></section>'
    ) % (banner, esc(name), esc(AGREE_VI.get((agreement or "").lower(), agreement or "chưa ghi")), stats, gate_html, warn_html, align, howto)

    # --- journey
    def doc_html(p, extra_pre="", extra_post="", reading=True):
        return render_md(p.md, p.path, resolver, problems, team)

    jcards, jdocs = "", ""
    for k, p in enumerate(weekly):
        wk, desc, label = winfo.get(p.id, ("", "", p.heading))
        jcards += '<a class="jcard" href="#/%s"><span class="wk">%s</span><h3>%s</h3><p>%s</p></a>' % (
            p.id, "%02d · %s" % (k + 1, esc(wk if wk else "Trang")), esc(p.heading), esc(desc))
        prev = '<a href="#/%s">← %s</a>' % (weekly[k - 1].id, esc(weekly[k - 1].heading)) if k else "<span></span>"
        nxt = '<a href="#/%s">%s →</a>' % (weekly[k + 1].id, esc(weekly[k + 1].heading)) if k + 1 < len(weekly) else "<span></span>"
        jdocs += '<section class="doc" id="%s" data-title="%s"><a class="back" href="#/journey">← Journey</a><div class="reading">%s</div><nav class="pn" aria-label="Trang trước và sau">%s%s</nav></section>' % (
            p.id, esc(p.heading), doc_html(p), prev, nxt)
    v_journey = '<section class="view journey" id="v-journey"><div class="wrap"><div class="jlist"><h1>Journey</h1><p class="lede">Các trang theo giai đoạn, mỗi trang kể lại một phần của dự án.</p><div class="jcards">%s</div></div>%s</div></section>' % (jcards, jdocs)

    # --- reference
    ref_desc = {"gates": "Bốn gate và các check của từng gate", "principles": "Design principle mà mọi decision cần đạt", "case-log": "Mỗi decision một dòng, kèm lý do"}
    rcards = "".join('<a class="jcard" href="#/%s"><span class="wk">Reference</span><h3>%s</h3><p>%s</p></a>' % (
        p.id, esc(p.label), esc(ref_desc.get(p.id, ""))) for p in ref)
    def ref_html(p):
        h = doc_html(p)
        # status words become quiet coloured labels; empty cells show a dash instead of a hole
        h = re.sub(r"<td>\s*(passed|open|failed)\s*</td>", lambda m: '<td><span class="gst gst-%s">%s</span></td>' % (m.group(1), STATUS_VI[m.group(1)]), h)
        return h.replace("<td></td>", '<td class="dash">—</td>')
    rdocs = "".join('<section class="doc" id="%s" data-title="%s"><a class="back" href="#/reference">← Reference</a><div class="reading">%s</div></section>' % (p.id, esc(p.label), ref_html(p)) for p in ref)
    v_reference = ('<section class="view reference" id="v-reference"><div class="wrap"><div class="jlist"><h1>Reference</h1>'
                   '<p class="lede">Các tài liệu để tra cứu: gates, design principles và case log.</p><div class="jcards">%s</div></div>%s</div></section>') % (rcards, rdocs)


    # --- documents (artifacts)
    def domain_label(url):
        host = urllib.parse.urlparse(url).netloc.lower().replace("www.", "")
        names = {"figma.com": "Figma", "miro.com": "Miro", "notion.so": "Notion", "docs.google.com": "Google Docs",
                 "drive.google.com": "Google Drive", "github.com": "GitHub", "loom.com": "Loom", "youtube.com": "YouTube"}
        for k, v in names.items():
            if host.endswith(k):
                return v
        return host or "Link"

    def media_html(a):
        parts = []
        figs = []
        for kind, ab, nm in media_of(a):
            href = href_for(ab)
            label = esc(nm)
            if kind == "image":
                figs.append('<figure class="fig"><a href="%s" target="_blank" rel="noopener"><img loading="lazy" src="%s" alt="%s"></a><figcaption>%s</figcaption></figure>' % (href, href, label, label))
            elif kind == "html":
                emb = ('<iframe loading="lazy" src="%s" title="%s"></iframe>' % (href, label)) if a.embed else ""
                parts.append('<div class="mcard"><div class="mhead"><strong>%s</strong><span class="mtag">Prototype / trang HTML</span>'
                             '<a class="btn" href="%s" target="_blank" rel="noopener">Mở ở tab mới ↗</a></div>%s</div>' % (label, href, emb))
            elif kind == "video":
                parts.append('<div class="mcard"><video controls preload="metadata" src="%s"></video><p class="cap">%s</p></div>' % (href, label))
            elif kind == "pdf":
                emb = ('<iframe loading="lazy" src="%s" title="%s"></iframe>' % (href, label)) if a.embed else ""
                parts.append('<div class="mcard"><div class="mhead"><strong>%s</strong><span class="mtag">PDF</span>'
                             '<a class="btn" href="%s" target="_blank" rel="noopener">Mở PDF ↗</a></div>%s</div>' % (label, href, emb))
            elif kind == "csv":
                try:
                    with open(ab, encoding="utf-8", newline="") as f:
                        rows_ = list(csv.reader(f))[:41]
                    th = "".join("<th>%s</th>" % esc(c) for c in rows_[0]) if rows_ else ""
                    tb = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % esc(c) for c in r) for r in rows_[1:])
                    parts.append('<div class="mcard"><div class="mhead"><strong>%s</strong><span class="mtag">CSV table</span><a class="btn" href="%s" target="_blank" rel="noopener">Tải về ↗</a></div><div class="table-wrap"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div></div>' % (label, href, th, tb))
                except Exception:
                    parts.append('<div class="mcard"><div class="mhead"><strong>%s</strong><a class="btn" href="%s" target="_blank" rel="noopener">Tải về ↗</a></div></div>' % (label, href))
            else:
                tag = "Source document" if kind == "doc" else "Attachment"
                parts.append('<div class="mcard"><div class="mhead"><strong>%s</strong><span class="mtag">%s</span><a class="btn" href="%s" target="_blank" rel="noopener">Mở ↗</a></div></div>' % (label, tag, href))
        for ln in a.links:
            lab, _, url = ln.partition("|")
            url = (url or lab).strip(); lab = lab.strip() if "|" in ln else domain_label(url)
            parts.append('<div class="mcard"><div class="mhead"><strong>%s</strong><span class="mtag">%s</span>'
                         '<a class="btn" href="%s" target="_blank" rel="noopener">Mở link ↗</a></div></div>' % (esc(lab), esc(domain_label(url)), esc(url)))
        if a.embed_url:
            parts.append('<div class="mcard"><iframe loading="lazy" src="%s" title="%s" allowfullscreen></iframe></div>' % (esc(a.embed_url), esc(a.title)))
        out = ""
        if figs:
            out += '<div class="figs">%s</div>' % "".join(figs)
        return out + "".join(parts)

    def art_card(a):
        thumb = ""
        for kind, ab, nm in media_of(a):
            if kind == "image":
                thumb = '<img class="thumb" loading="lazy" src="%s" alt="">' % href_for(ab)
                break
        n_media = len(media_of(a)) + len(a.links)
        badge = ('<span class="st st-%s">%s</span>' % (a.status, esc(ART_STATUS.get(a.status, a.status)))) if a.status else ""
        return ('<a class="acard" href="#/%s" data-type="%s" data-stage="%s" data-text="%s">%s<span class="atype">%s</span><h3>%s</h3><p>%s</p>'
                '<span class="ameta">%s%s%s</span></a>') % (
            a.id, esc(a.type), esc(a.stage), esc((a.title + " " + a.summary + " " + a.type).lower()), thumb,
            esc(ART_TYPES.get(a.type, a.type.replace("-", " ").capitalize())), esc(a.title), esc(a.summary),
            esc(a.stage) if a.stage else "", (" · " + badge) if badge else "", (" · %d tệp/link" % n_media) if n_media else "")

    adocs = ""
    for a in arts:
        label = ART_TYPES.get(a.type, a.type.replace("-", " ").capitalize())
        badge = ('<span class="st st-%s">%s</span>' % (a.status, esc(ART_STATUS.get(a.status, a.status)))) if a.status else ""
        warn = ""
        if a.status in ("simulated", "draft", "planned"):
            warn = '<p class="warnbox">⚠ Document này ở trạng thái <strong>%s</strong>: %s</p>' % (esc(ART_STATUS.get(a.status, a.status)),
                {"simulated": "kết quả đến từ người mô phỏng, không phải người dùng thật.", "draft": "nội dung chưa được kiểm tra.", "planned": "mới ở dạng kế hoạch, chưa thực hiện."}[a.status])
        take = ("<h2>Key takeaways</h2><ul>%s</ul>" % "".join("<li>%s</li>" % Renderer(a.path, resolver, problems).inline(x) for x in a.takeaways)) if a.takeaways else ""
        sup = ('<div class="supports"><span class="lbl">Supports</span><span class="chips">%s</span></div>' % "".join(chip(s) for s in a.supports)) if a.supports else ""
        med = media_html(a)
        med = ("<h2>Media</h2>%s" % med) if med else ""
        src_note = ('<p class="srcnote">Source: <code>%s</code></p>' % esc(a.source)) if a.source else ""
        own = re.sub(r"^\s*#\s+.*\n", "", a.body, count=1)
        body_html = render_md(own, a.path, resolver, problems, team) if own.strip() else ""
        if a.source:
            sp = os.path.abspath(os.path.join(os.path.dirname(a.path), a.source))
            if os.path.isfile(sp):
                sraw = open(sp, encoding="utf-8").read()
                _, sbody = _front(sraw)
                sbody = re.sub(r"^\s*#\s+.*\n", "", sbody, count=1)
                body_html += ("<h2>Full content</h2>" if body_html else "") + render_md(sbody, sp, resolver, problems, team)
            else:
                problems.append("Tài liệu %s: không tìm thấy source %s" % (a.id, a.source))
        adocs += ('<section class="doc" id="%s" data-title="%s"><a class="back" href="#/docs">← Documents</a>'
                  '<header class="ahead"><p class="kind">%s%s</p><h1>%s</h1>%s</header>%s%s%s%s<div class="reading">%s</div>%s</section>') % (
            esc(a.id), esc(a.title), esc(label), (" · " + esc(a.stage)) if a.stage else "", esc(a.title),
            ('<p class="sum">%s</p>' % esc(a.summary)) if a.summary else "", ('<p>%s</p>' % badge) if (badge and not warn) else "", warn, sup,
            take + med, body_html, src_note)

    stage_order = {s: i for i, s in enumerate(STAGES)}
    arts_sorted = sorted(arts, key=lambda a: (stage_order.get(a.stage, 99), a.title.lower()))
    types_present = sorted({a.type for a in arts})
    stages_present = [s for s in STAGES if any(a.stage == s for a in arts)]
    dfilters = "".join('<button type="button" aria-pressed="false" data-ftype="%s">%s</button>' % (esc(x), esc(ART_TYPES.get(x, x.replace("-", " ").capitalize()))) for x in types_present)
    sfilters = '<button type="button" role="tab" aria-selected="true" data-fstage="">All<span class="n">%d</span></button>' % len(arts)
    sfilters += "".join('<button type="button" role="tab" aria-selected="false" data-fstage="%s">%s<span class="n">%d</span></button>' % (
        esc(s), esc(s), sum(1 for a in arts if a.stage == s)) for s in stages_present)
    if arts_sorted:
        grid = '<div class="acards" id="acards">%s</div>' % "".join(art_card(a) for a in arts_sorted)
    else:
        grid = '<div class="empty"><p><strong>Chưa có tài liệu nào.</strong></p><p>Thêm một file vào <code>hub/artifacts/</code> (xem <code>hub/artifacts/README.md</code>).</p></div>'
    v_docs = ('<section class="view docs" id="v-docs"><div class="wrap"><div class="jlist"><h1>Documents</h1>'
              '<p class="lede">Các output làm ra trong dự án: phân tích, persona, survey, flow, prototype. Mỗi document nối với các decision mà nó hỗ trợ.</p>'
              '<input id="dsearch" class="tsearch" type="search" placeholder="Tìm tài liệu" aria-label="Tìm tài liệu">'
              '<div class="tabs2" role="tablist" aria-label="Lọc theo giai đoạn">%s</div>'
              '<p class="tcount" id="dcount" aria-live="polite"></p>%s</div>%s</div></section>') % (sfilters, grid, adocs)

    # --- trace: tree
    def tnode(i, kids="", cnt="", leaf=True, opened=False):
        p = G.items[i]
        w = i in G.warn
        a = '<a class="node" href="#/%s" data-id="%s"><span class="idc t-%s">%s</span><span class="nt">%s%s</span>%s</a>' % (
            i, i, p.letter, i, esc(p.title), ('<span class="cnt">%s</span>' % cnt) if cnt else "",
            ('<span class="wb" title="%s" aria-label="có warning">⚠</span>' % esc("; ".join(G.warn[i]))) if w else "")
        attrs = 'class="n%s" data-type="%s" data-warn="%s" data-text="%s"' % (" leaf" if not kids else "", p.letter, "1" if w else "0", esc((i + " " + p.title).lower()))
        if kids:
            return '<li %s><details%s><summary>%s</summary><ul>%s</ul></details></li>' % (attrs, " open" if opened else "", a, kids)
        return "<li %s>%s</li>" % (attrs, a)

    placed = set()
    top = ""
    first_open = next((k for k, o in enumerate(G.O) if G.hyps_of(o)), 0)
    for k, o in enumerate(G.O):
        placed.add(o)
        hk = ""
        for h in G.hyps_of(o):
            placed.add(h)
            ds, ts, ms = G.decisions_of(h), G.tests_of(h), G.metric.get(h, [])
            kids = ""
            for x in ds + ts + ms:
                placed.add(x)
                kids += tnode(x)
            cnt = " · ".join(s for s in [plural(len(ds), "decision", "decisions") if ds else "", plural(len(ts), "test", "tests") if ts else "", plural(len(ms), "metric", "metrics") if ms else ""] if s) or "chưa có decision hay test"
            hk += tnode(h, kids, cnt)
        n_h = len(G.hyps_of(o))
        top += tnode(o, hk, plural(n_h, "hypothesis", "hypotheses") if n_h else "chưa có hypothesis", opened=(k == first_open))
    loose = [i for i in sorted(G.items, key=_natkey) if i not in placed]
    if loose:
        lk = "".join(tnode(i) for i in loose)
        top += '<li class="n" data-type="" data-warn="0" data-text=""><details open><summary><span class="gh">Chưa nối vào opportunity nào (%d)</span></summary><ul>%s</ul></details></li>' % (len(loose), lk)
    ttabs = '<button type="button" role="tab" aria-selected="true" data-type="">All<span class="n">%d</span></button>' % len(G.items)
    ttabs += "".join('<button type="button" role="tab" aria-selected="false" data-type="%s">%s<span class="n">%d</span></button>' % (
        L, pl, len(getattr(G, L))) for L, _, _, pl in TYPES)
    filters = '<button type="button" aria-pressed="false" data-warn="1">⚠ Warnings only</button>'

    # --- trace: item docs
    idocs = ""
    for i in sorted(G.items, key=_natkey):
        p = G.items[i]
        r = Renderer(p.path, resolver, problems)
        body = re.sub(r"^<h1>.*?</h1>\n?", "", r.render(getattr(p, "body", p.md)), count=1)
        body = prop_table(p, r) + body
        warn = "".join('<p class="warnbox">⚠ %s</p>' % esc(w) for w in G.warn.get(i, []))
        chains = G.paths(i)
        path = ""
        if chains and p.letter != "O":
            more = ('<span class="more">và %d đường khác</span>' % (len(chains) - 3)) if len(chains) > 3 else ""
            path = '<div class="path"><span>From opportunity:</span>%s%s</div>' % ("".join(
                '<span class="chips chain">%s</span>' % " › ".join(chip(x) for x in c) for c in chains[:3]), more)
        bl = ""
        if G.back.get(i):
            groups = {}
            for src, label in G.back[i]:
                groups.setdefault(label, []).append(src)
            rows_ = "".join('<div class="row"><span class="lbl">%s</span><span class="chips">%s</span></div>' % (
                esc(BACK_LABEL.get(lb, lb.replace("_", " "))), "".join(chip(s) for s in sorted(srcs, key=_natkey))) for lb, srcs in groups.items())
            bl = '<aside class="backlinks"><h2>Linked from</h2>%s</aside>' % rows_
        if art_for.get(i):
            bl += '<aside class="backlinks"><h2>Related documents</h2><div class="row"><span class="chips">%s</span></div></aside>' % "".join(chip(x) for x in art_for[i])
        idocs += ('<section class="doc" id="%s" data-title="%s"><a class="back back-tree" href="#/trace">← Insights</a>'
                  '<header class="ihead"><span class="idtag t-%s">%s</span><div><p class="kind">%s</p><h1>%s</h1></div></header>%s%s<div class="reading">%s</div>%s</section>') % (
            i, esc(i + " " + p.title), p.letter, i, VI_NAME[p.letter][0], esc(p.title), warn, path, body, bl)
    def icard(i):
        p = G.items[i]
        w = i in G.warn
        meta = ""
        if p.letter == "O":
            n_h = len(G.hyps_of(i))
            meta = plural(n_h, "hypothesis", "hypotheses") if n_h else "chưa có hypothesis"
        elif p.letter == "H":
            ds_, ts_, ms_ = G.decisions_of(i), G.tests_of(i), G.metric.get(i, [])
            meta = " · ".join(x for x in [plural(len(ds_), "decision", "decisions") if ds_ else "", plural(len(ts_), "test", "tests") if ts_ else "", plural(len(ms_), "metric", "metrics") if ms_ else ""] if x) or "chưa có decision hay test"
        else:
            for k_ in REL_KEYS:
                ids_ = _ids(p.meta.get(k_, ""))
                if ids_:
                    meta = "%s: %s" % (PROP_LABEL.get(k_, k_), ", ".join(ids_))
                    break
        if w:
            meta = G.warn[i][0]
        return ('<a class="icard" href="#/%s" data-type="%s" data-warn="%s" data-text="%s"><span class="top"><span class="idc t-%s">%s</span>'
                '<span class="itype">%s</span>%s</span><h3>%s</h3><p>%s</p></a>') % (
            i, p.letter, "1" if w else "0", esc((i + " " + p.title).lower()), p.letter, i, esc(VI_SHORT[p.letter]),
            '<span class="w" title="có warning">⚠</span>' if w else "", esc(p.title), esc(meta))
    icards = "".join(icard(i) for L, _, _, _pl in TYPES for i in sorted(getattr(G, L), key=_natkey))
    v_trace = (
        '<section class="view" id="v-trace"><div class="wrap"><div class="trace">'
        '<div class="pane-tree"><h1>Insights</h1><p class="lede">Opportunity, hypothesis, decision, test và metric, nối với nhau. Lọc theo loại, hoặc xem dạng cây để thấy chuỗi lý do.</p>'
        '<input id="tsearch" class="tsearch" type="search" placeholder="Tìm theo mã hoặc tên" aria-label="Tìm insight">'
        '<div class="tabs2" role="tablist" aria-label="Lọc theo loại">%s</div>'
        '<div class="vmode" role="group" aria-label="Cách xem"><button type="button" data-vmode="cards" aria-pressed="true">Cards</button><button type="button" data-vmode="tree" aria-pressed="false">Tree</button></div>'
        '<p class="tcount" id="tcount" aria-live="polite"></p>'
        '<div class="icards">%s</div>'
        '<ul class="tree" id="tree">%s</ul></div>'
        '<div class="pane-detail">%s</div>'
        '</div></div></section>'
    ) % (ttabs, icards or '<div class="empty"><p><strong>Chưa có mục nào.</strong></p></div>', top or '<li class="n"><span class="nt">Chưa có mục nào.</span></li>', idocs)

    # --- sidebar (same structure as the website: Overview, Journey, Documents by stage, Trace by type, Reference)
    def nlink(target, inner, cls=""):
        return '<a%s href="#/%s" data-nav="%s">%s</a>' % ((' class="%s"' % cls) if cls else "", esc(target), esc(target), inner)

    sec_counts = {"journey": len(weekly), "docs": len(arts), "trace": len(items), "reference": len(ref)}
    nav = "".join('<a href="#/%s" data-nav="%s">%s%s</a>' % (
        k, k, t, ('<span class="nm">%d</span>' % sec_counts[k]) if k in sec_counts else "")
        for k, t in [("overview", "Overview"), ("journey", "Journey"), ("docs", "Documents"), ("trace", "Insights"), ("reference", "Reference")])
    sidebar = '<details class="menu" open><summary>Menu</summary><nav class="nav2" aria-label="Các phần của báo cáo">%s</nav></details>' % nav

    now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    theme_select = ""
    if switcher:
        theme_select = '<label class="themepick">Giao diện <select id="themeselect" aria-label="Chọn giao diện">%s</select></label>' % "".join(
            '<option value="%s"%s>%s</option>' % (k, " selected" if k == theme else "", esc(v)) for k, v in THEMES)
    doc = ("""<!doctype html>
<html lang="vi" data-theme="{{THEME}}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{{NAME}} · Báo cáo case</title>
<style>{{CSS}}</style>
</head>
<body data-case="{{NAME}}">
<a class="skip" href="#main">Bỏ qua menu</a>
<header class="top"><div class="top-in">
<div class="brand">{{NAME}}</div>
<input id="gsearch" class="gsearch" type="search" placeholder="Tìm theo mã hoặc từ khoá (ví dụ D2)" aria-label="Tìm trong báo cáo">
{{THEME_SELECT}}
</div></header>
<div class="shell">
<aside class="side">{{SIDEBAR}}</aside>
<main id="main">
{{V_OVERVIEW}}
{{V_JOURNEY}}
{{V_DOCS}}
{{V_TRACE}}
{{V_REFERENCE}}
<div class="wrap" style="padding-top:0"><footer class="foot">Tạo tự động từ các file Markdown của case, ngày {{NOW}}{{MODE}}. Muốn đổi nội dung, sửa file gốc rồi chạy lại <code>python3 tools/export-hub.py</code>.</footer></div>
</main>
</div>
<script>{{JS}}</script>
</body>
</html>
""").replace("{{NAME}}", esc(name)).replace("{{NOW}}", now).replace("{{MODE}}", " · bản dành cho team (có bản nháp AI)" if team else "").replace("{{V_OVERVIEW}}", v_overview) \
        .replace("{{V_JOURNEY}}", v_journey).replace("{{V_DOCS}}", v_docs).replace("{{V_TRACE}}", v_trace).replace("{{V_REFERENCE}}", v_reference) \
        .replace("{{CSS}}", CSS + theme_rules(theme, switcher)).replace("{{JS}}", JS).replace("{{THEME}}", theme).replace("{{THEME_SELECT}}", theme_select).replace("{{SIDEBAR}}", sidebar)

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(doc)
    return G, weekly, ref, problems, placeholders, name, arts, used_media


def main():
    ap = argparse.ArgumentParser(description="Export the markdown hub to one self-contained HTML file.")
    ap.add_argument("--case", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--out", default=None)
    ap.add_argument("--theme", default="minimal", choices=[k for k, _ in THEMES], help="visual theme of the report")
    ap.add_argument("--preview-themes", action="store_true", help="add a theme switcher to the report (for choosing a theme)")
    ap.add_argument("--team", action="store_true", help="team version: show AI-draft sections, folded and labelled")
    ap.add_argument("--bundle", default=None, metavar="DIR", help="write a clean folder (index.html + only the files it uses) to send to others")
    ap.add_argument("--zip", action="store_true", help="with --bundle: also make DIR.zip")
    a = ap.parse_args()
    case = os.path.abspath(a.case)
    bundle_dir = os.path.abspath(a.bundle) if a.bundle else None
    if bundle_dir:
        os.makedirs(bundle_dir, exist_ok=True)
        out = os.path.join(bundle_dir, "index.html")
    else:
        out = a.out or os.path.join(case, "index.html")
    G, weekly, ref, problems, placeholders, name, arts, used = build(case, out, a.theme, a.preview_themes, a.team, bool(bundle_dir))
    if bundle_dir:
        total = os.path.getsize(out)
        for ab in sorted(used):
            if not os.path.isfile(ab):
                continue
            dest = os.path.join(bundle_dir, os.path.relpath(ab, case))
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            shutil.copy2(ab, dest)
            total += os.path.getsize(ab)
        print("Bundle: %s (%d tệp, %.1f MB)" % (bundle_dir, len(used) + 1, total / 1048576.0))
        if a.zip:
            z = shutil.make_archive(bundle_dir, "zip", bundle_dir)
            print("Zip: %s (%.1f MB)" % (z, os.path.getsize(z) / 1048576.0))
    print("Case: %s" % name)
    print("Đã đưa vào báo cáo: %d trang giai đoạn, %d tài liệu tham chiếu, %d tài liệu (artifact), %d item (O %d, H %d, M %d, D %d, T %d)" % (
        len(weekly), len(ref), len(arts), len(G.items), len(G.O), len(G.H), len(G.M), len(G.D), len(G.T)))
    if a.team:
        print("  Bản dành cho team: có hiện các section AI draft (gấp lại). Đừng gửi bản này cho stakeholder.")
    if G.warnings:
        print("Warnings (%d):" % len(G.warnings))
        for _, ids, text in G.warnings:
            print("  - %s: %s" % (", ".join(ids), text))
    for p in problems:
        print("  ! %s" % p)
    if placeholders:
        print("  ! Còn ít nhất %d chỗ dữ liệu mẫu hoặc chưa điền" % placeholders)
    print("Đã ghi: %s" % out)
    print("Mở file index.html bằng trình duyệt (bấm đúp) để xem hub.")


if __name__ == "__main__":
    main()
