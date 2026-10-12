#!/usr/bin/env python3
"""Export the markdown hub of a case folder to ONE self-contained HTML file.

    python3 tools/export-hub.py                 # case = the folder that contains tools/ -> <case>/index.html
    python3 tools/export-hub.py --case PATH     # another case folder
    python3 tools/export-hub.py --out FILE.html # custom output path (e.g. a copy to send)

Why a script and not an AI tool: turning markdown into HTML and tracing links between items is
deterministic. A script gives the same output every time, invents nothing and sends no data anywhere.
Python 3.8+ standard library only.

The report is an OUTPUT. Never edit it by hand: change the markdown and export again.

Included : hub/*.md, hub/<type>/*.md, case-log.md, 00-context/principle-checks.md
Excluded : everything else (AI drafts, _personal/, sources/, AGENTS.md, how-the-hub-works.md)

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
VI_NAME = {"O": ("Nhu cầu của người dùng", "Opportunity"), "H": ("Giả thuyết", "Hypothesis"), "M": ("Chỉ số", "Metric"),
           "D": ("Quyết định thiết kế", "Design decision"), "T": ("Bài kiểm tra", "Test")}
VI_SHORT = {"O": "Nhu cầu", "H": "Giả thuyết", "M": "Chỉ số", "D": "Quyết định", "T": "Kiểm tra"}
PROP_LABEL = {"type": "Loại", "rank": "Thứ hạng", "evidence": "Bằng chứng", "serves": "Phục vụ nhu cầu", "metric": "Chỉ số",
              "tests": "Kiểm chứng giả thuyết", "follows": "Theo nguyên tắc", "pulls_against": "Đi ngược nguyên tắc",
              "measures": "Đo chỉ số", "status": "Trạng thái", "baseline": "Mức hiện tại (baseline)", "measured_by": "Đo bằng",
              "participants": "Số người tham gia", "result": "Kết quả"}
BACK_LABEL = {"serves": "Được phục vụ bởi giả thuyết", "metric": "Được dùng làm chỉ số của", "tests": "Được kiểm chứng bởi",
              "measures": "Được đo bởi", "follows": "Được theo bởi quyết định", "pulls_against": "Bị đi ngược bởi quyết định"}
STATUS_VI = {"open": "Đang mở", "passed": "Đạt", "failed": "Chưa đạt"}
AGREE_VI = {"agreed": "Đã thống nhất", "pending": "Đang chờ thống nhất", "not available": "Chưa có cơ hội thống nhất"}


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
                out = ('<img src="%s" alt="%s">' % (val, html.escape(label, quote=True))) if kind == "data" \
                    else '<span class="ext">[hình: %s]</span>' % (label or url)
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
    pc = os.path.join(case, "00-context", "principle-checks.md")
    if os.path.isfile(pc):
        ref.append(Page("principles", pc, "ref", "Principle checks"))
    cl = os.path.join(case, "case-log.md")
    if os.path.isfile(cl):
        ref.append(Page("case-log", cl, "ref", "Case log"))
    for letter, folder, _, _ in TYPES:
        d = os.path.join(hub, folder)
        if not os.path.isdir(d):
            continue
        for name in sorted(os.listdir(d), key=_natkey):
            if name.endswith(".md") and name != "README.md":
                p = Page(name[:-3], os.path.join(d, name), "item")
                p.letter = letter
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
                flag("no-need", [d], "Quyết định này chưa nối được về nhu cầu nào của người dùng")
        for d in self.D:
            for p in self.strains.get(d, []):
                flag("strain", [d], "Quyết định này đi ngược nguyên tắc %s: cân nhắc sửa, hoặc ghi lại vì sao chấp nhận" % p)
        for o in self.O:
            hs = [h for h in self.H if o in self.serves.get(h, [])]
            if not hs or not any(self.decisions_of(h) for h in hs):
                flag("unserved", [o], "Nhu cầu này chưa có quyết định thiết kế nào phục vụ")
        for h in self.H:
            if not self.tests_of(h):
                flag("untested", [h], "Giả thuyết này chưa có bài kiểm tra")
            if not self.metric.get(h):
                flag("nometric", [h], "Giả thuyết này chưa có chỉ số để biết đúng hay sai")
        empty = [p for p, (nm, chk) in principles.items() if not chk.strip() and not nm.startswith("(")]
        if empty:
            self.warnings.append(("principles", empty, "Nguyên tắc chưa có câu hỏi có/không để kiểm tra"))

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
.path{font-size:.88rem;color:var(--muted);margin:0 0 14px;display:flex;flex-wrap:wrap;gap:6px;align-items:center}
.backlinks{margin-top:30px;padding:14px 18px;background:var(--surface);border:1px solid var(--line);border-radius:var(--r)}
.backlinks h2{margin:0 0 8px;font-size:.95rem}
.backlinks .row{display:flex;gap:10px;align-items:baseline;flex-wrap:wrap;margin:6px 0}
.backlinks .lbl{font-size:.8rem;color:var(--muted);min-width:7em}
.back-tree{display:none}
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
  header.top,.skip,.pane-tree,.back,.pn,.subtabs,.back-tree,.themepick{display:none!important}
  .view,.journey .doc,.reference .doc,.pane-detail .doc{display:block!important}
  .jlist{display:none}
  .doc{break-before:page}
  .wrap{padding:0;max-width:none}
  .trace{display:block}
  a{color:inherit;text-decoration:none}
  table{font-size:.8rem}
  .banner{border:1px solid #000;background:none;color:#000}
}
"""

JS = r"""
(function(){
  var root=document.documentElement; root.classList.add('js');
  var VIEWS=['overview','journey','trace','reference'];
  function $(s,c){return (c||document).querySelector(s)}
  function $$(s,c){return [].slice.call((c||document).querySelectorAll(s))}
  var docs={}; $$('.doc').forEach(function(d){docs[d.id]=d});
  var caseName=document.body.getAttribute('data-case');
  function route(){
    var id=decodeURIComponent((location.hash||'').replace(/^#\/?/,''))||'overview';
    var doc=null, view='overview';
    if(VIEWS.indexOf(id)>-1){view=id}
    else if(docs[id]){doc=docs[id]; var v=doc.closest('.view'); view=v?v.id.slice(2):'overview'}
    if(view==='reference'&&!doc){doc=docs['gates']||docs['principles']||docs['case-log']||null}
    $$('.view').forEach(function(v){v.classList.toggle('on',v.id==='v-'+view)});
    $$('.tabs a').forEach(function(a){
      if(a.getAttribute('href')==='#/'+view){a.setAttribute('aria-current','page')}else{a.removeAttribute('aria-current')}
    });
    $$('.doc').forEach(function(d){d.classList.remove('on')});
    if(doc){doc.classList.add('on')}
    var j=$('#v-journey'); if(j){j.classList.toggle('has-doc',view==='journey'&&!!doc)}
    var t=$('#v-trace'); if(t){t.classList.toggle('has-item',view==='trace'&&!!doc)}
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
  function apply(){
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
    var c=$('#tcount'); if(c){c.textContent=any?(shown+' mục khớp'):''}
  }
  if(q){q.addEventListener('input',function(){if(gs){gs.value=q.value} apply()})}
  if(gs){gs.addEventListener('input',function(){
    if(q){q.value=gs.value}
    if(!/^#\/(trace|[OHMDT]\d+)$/.test(location.hash)){location.hash='#/trace'}
    apply();
  })}
  $$('.filters button').forEach(function(b){
    b.addEventListener('click',function(){
      var on=b.getAttribute('aria-pressed')!=='true';
      b.setAttribute('aria-pressed',on?'true':'false');
      if(b.getAttribute('data-warn')){warnOnly=on}
      else{var k=b.getAttribute('data-type'); if(on){types[k]=true}else{delete types[k]}}
      apply();
    });
  });
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


THEMES = [("notion", "Notion (xanh, gọn)"), ("classic", "Classic (tím)"), ("editorial", "Editorial (chữ có chân, giấy kem)"),
          ("swiss", "Swiss (đen trắng, khung rõ)"), ("calm", "Calm (xanh lá dịu)")]

# Each theme only overrides the colour tokens and a few details; layout is shared.
THEME_CSS = r"""
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


def esc(s):
    return html.escape(s, quote=True)


def build(case, out_path, theme="notion", switcher=False):
    problems = []
    overview, weekly, items, ref = collect(case)
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
            if is_img and os.path.getsize(target) < 1500000:
                mime = mimetypes.guess_type(target)[0] or "application/octet-stream"
                with open(target, "rb") as f:
                    return "data", "data:%s;base64,%s" % (mime, base64.b64encode(f.read()).decode())
            return "outside", os.path.relpath(target, case_abs)
        if os.path.isdir(target):
            return "outside", os.path.relpath(target, case_abs) + "/"
        return "broken", url

    # --- consistency checks
    for p in items:
        if not p.meta:
            problems.append("%s: thiếu khối properties (--- ... ---) ở đầu file" % os.path.basename(p.path))
        elif not p.meta.get("title"):
            problems.append("%s: thiếu property title" % os.path.basename(p.path))
        if not re.fullmatch(r"%s\d+" % p.letter, p.id):
            problems.append("%s nằm sai folder (loại %s)" % (p.id, LETTER_NAME[p.letter]))
        tp = str(p.meta.get("type", "")).lower()
        if p.meta and tp and tp != TYPE_WORD[p.letter]:
            problems.append("%s: property type là '%s' nhưng file nằm ở folder %s" % (p.id, tp, TYPE_WORD[p.letter]))
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
            if k == "title":
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

    # --- overview
    counts = "".join('<div class="card"><div class="num">%d</div><div class="lbl">%s<small>%s</small></div></div>' % (
        len(getattr(G, L)), VI_NAME[L][0], pl) for L, _, _, pl in TYPES)
    nwarn = len(G.warnings)
    counts += '<div class="card warnc"><div class="num">%d</div><div class="lbl">Điểm cần xem lại<small>xem danh sách bên dưới</small></div></div>' % nwarn
    gate_html = ""
    for g in gates:
        pct = int(100 * g["passed"] / g["total"]) if g["total"] else 0
        gate_html += '<div class="gate"><small>%s</small><strong>%s</strong><div class="st">%s</div><div class="bar"><i style="width:%d%%"></i></div><small>%d trên %d mục đã đạt</small></div>' % (
            esc(g["name"].split("(")[0].strip()), esc(g["name"].split("(")[-1].rstrip(")")) if "(" in g["name"] else "",
            STATUS_VI.get(g["status"], g["status"]), pct, g["passed"], g["total"])
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
    align = ('<div class="table-wrap"><table><thead><tr><th>Quyết định</th><th>Kiểm chứng giả thuyết</th><th>Phục vụ nhu cầu</th><th>Bài kiểm tra</th><th>Theo nguyên tắc</th><th>Đi ngược nguyên tắc</th></tr></thead><tbody>%s</tbody></table></div>' % rows) if rows else '<p class="ok">Chưa có quyết định thiết kế nào.</p>'
    if G.warnings:
        wl = "".join('<li>%s <span class="chips" style="display:inline-flex;vertical-align:middle">%s</span> <strong>%s</strong></li>' % (
            "⚠", "".join(chip(i) for i in ids), esc(text)) for _, ids, text in G.warnings)
        warn_html = '<ul class="warnlist">%s</ul>' % wl
    else:
        warn_html = '<p class="ok">Không có điểm nào cần xem lại: mọi quyết định đều lần ngược được về một nhu cầu, và mọi giả thuyết đều có bài kiểm tra và chỉ số.</p>'
    banner = ""
    if placeholders:
        banner = '<div class="banner" role="note"><strong>Báo cáo này còn nội dung mẫu hoặc chỗ chưa điền</strong> (khoảng %d chỗ, kể cả các mục có nhãn [EXAMPLE]). Hãy điền hoặc xoá trước khi gửi cho người khác.</div>' % placeholders
    howto = (
        '<details class="help" open><summary>Cách đọc báo cáo này</summary>'
        '<p>Báo cáo ghi lại một dự án thiết kế, từ câu hỏi của business đến prototype đã được kiểm tra. '
        'Điểm chính: <strong>mỗi quyết định thiết kế đều lần ngược được về nhu cầu của người dùng đứng sau nó</strong>.</p>'
        '<ul><li><strong>Tổng quan</strong> (trang này): tình trạng chung, các quyết định và những chỗ cần xem lại.</li>'
        '<li><strong>Hành trình</strong>: các trang theo giai đoạn, kể lại dự án từ câu hỏi ban đầu đến bàn giao.</li>'
        '<li><strong>Truy vết</strong>: chọn một nhu cầu hoặc một quyết định, rồi đi theo các liên kết để thấy lý do và bằng chứng. Có ô tìm kiếm và bộ lọc.</li>'
        '<li><strong>Tham chiếu</strong>: các cổng chất lượng, nguyên tắc thiết kế và nhật ký quyết định.</li></ul>'
        '<p>Chỉ có năm phút? Đọc bảng bên dưới, rồi mở các mục có dấu ⚠ trong tab Truy vết.</p></details>')
    glossary = (
        '<details class="help"><summary>Các từ khoá dùng trong báo cáo</summary><dl>'
        '<dt>Nhu cầu (Opportunity)</dt><dd>Điều người dùng cần hoặc đang gặp khó, có bằng chứng. Không phải một tính năng.</dd>'
        '<dt>Giả thuyết (Hypothesis)</dt><dd>Điều nhóm tin là đúng, kèm cách sẽ biết nó đúng hay sai.</dd>'
        '<dt>Quyết định thiết kế (Decision)</dt><dd>Một lựa chọn thiết kế cụ thể, kèm lý do.</dd>'
        '<dt>Bài kiểm tra (Test)</dt><dd>Cách kiểm chứng một giả thuyết với người dùng thật.</dd>'
        '<dt>Chỉ số (Metric)</dt><dd>Con số cho biết giả thuyết đúng hay sai. Nhãn <em>assumed</em> nghĩa là chưa được người phụ trách sản phẩm xác nhận.</dd>'
        '<dt>Nguyên tắc (Principle)</dt><dd>Quy tắc thiết kế mà mọi quyết định cần đạt, ví dụ 10 usability heuristics của Nielsen (P1 đến P10).</dd>'
        '<dt>Cổng chất lượng (Gate)</dt><dd>Bước kiểm tra trước khi sang giai đoạn sau. Mỗi cổng gồm vài mục nhỏ.</dd>'
        '<dt>Alignment</dt><dd>Mức độ mỗi quyết định nối được về nhu cầu của người dùng và đạt các nguyên tắc.</dd>'
        '</dl></details>')
    v_overview = (
        '<section class="view" id="v-overview"><div class="wrap">%s<h1>%s</h1><p class="lede">Trạng thái thống nhất với product và business: <strong>%s</strong></p>'
        '%s<div class="cards">%s</div>'
        '<h2>Cổng chất lượng (Gates)</h2><p class="lede">Mỗi giai đoạn có một cổng kiểm tra trước khi sang giai đoạn sau.</p><div class="gatecards">%s</div>'
        '<h2>Mỗi quyết định dựa trên nhu cầu nào? (Alignment)</h2><p class="lede">Mỗi dòng là một quyết định thiết kế. Ô ghi <em>chưa có</em> là chỗ chưa nối được về giả thuyết, nhu cầu hoặc bài kiểm tra.</p>%s'
        '<h2>Điểm cần xem lại</h2><p class="lede">Đây không phải lỗi. Mỗi điểm dưới đây là chỗ cần một quyết định rõ ràng: sửa, giữ lại có chủ đích, hoặc bỏ đi.</p>%s'
        '%s</div></section>'
    ) % (banner, esc(name), esc(AGREE_VI.get((agreement or "").lower(), agreement or "chưa ghi")), howto, counts, gate_html, align, warn_html, glossary)

    # --- journey
    def doc_html(p, extra_pre="", extra_post="", reading=True):
        r = Renderer(p.path, resolver, problems)
        body = r.render(p.md)
        return body

    jcards, jdocs = "", ""
    for k, p in enumerate(weekly):
        wk, desc, label = winfo.get(p.id, ("", "", p.heading))
        jcards += '<a class="jcard" href="#/%s"><span class="wk">%s</span><h3>%s</h3><p>%s</p></a>' % (
            p.id, esc(wk if wk else "Trang"), esc(p.heading), esc(desc))
        prev = '<a href="#/%s">← %s</a>' % (weekly[k - 1].id, esc(weekly[k - 1].heading)) if k else "<span></span>"
        nxt = '<a href="#/%s">%s →</a>' % (weekly[k + 1].id, esc(weekly[k + 1].heading)) if k + 1 < len(weekly) else "<span></span>"
        jdocs += '<section class="doc" id="%s" data-title="%s"><a class="back" href="#/journey">← Hành trình</a><div class="reading">%s</div><nav class="pn" aria-label="Trang trước và sau">%s%s</nav></section>' % (
            p.id, esc(p.heading), doc_html(p), prev, nxt)
    v_journey = '<section class="view journey" id="v-journey"><div class="wrap"><div class="jlist"><h1>Hành trình</h1><p class="lede">Các trang theo giai đoạn, mỗi trang kể lại một phần của dự án.</p><div class="jcards">%s</div></div>%s</div></section>' % (jcards, jdocs)

    # --- reference
    subtabs = "".join('<a href="#/%s">%s</a>' % (p.id, esc(p.label)) for p in ref)
    rdocs = "".join('<section class="doc" id="%s" data-title="%s"><div class="reading">%s</div></section>' % (p.id, esc(p.label), doc_html(p)) for p in ref)
    v_reference = '<section class="view reference" id="v-reference"><div class="wrap"><h1>Tham chiếu</h1><p class="lede">Các tài liệu để tra cứu: cổng chất lượng, nguyên tắc thiết kế và nhật ký quyết định.</p><div class="subtabs" role="navigation" aria-label="Tài liệu tham chiếu">%s</div>%s</div></section>' % (subtabs, rdocs)

    # --- trace: tree
    def tnode(i, kids="", cnt="", leaf=True, opened=False):
        p = G.items[i]
        w = i in G.warn
        a = '<a class="node" href="#/%s" data-id="%s"><span class="idc t-%s">%s</span><span class="nt">%s%s</span>%s</a>' % (
            i, i, p.letter, i, esc(p.title), ('<span class="cnt">%s</span>' % cnt) if cnt else "",
            ('<span class="wb" title="%s" aria-label="có điểm cần xem lại">⚠</span>' % esc("; ".join(G.warn[i]))) if w else "")
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
            cnt = " · ".join(s for s in ["%d quyết định" % len(ds) if ds else "", "%d kiểm tra" % len(ts) if ts else "", "%d chỉ số" % len(ms) if ms else ""] if s) or "chưa có quyết định hay bài kiểm tra"
            hk += tnode(h, kids, cnt)
        n_h = len(G.hyps_of(o))
        top += tnode(o, hk, ("%d giả thuyết" % n_h) if n_h else "chưa có giả thuyết", opened=(k == first_open))
    loose = [i for i in sorted(G.items, key=_natkey) if i not in placed]
    if loose:
        lk = "".join(tnode(i) for i in loose)
        top += '<li class="n" data-type="" data-warn="0" data-text=""><details open><summary><span class="gh">Chưa nối vào nhu cầu nào (%d)</span></summary><ul>%s</ul></details></li>' % (len(loose), lk)
    filters = "".join('<button type="button" aria-pressed="false" data-type="%s">%s</button>' % (L, VI_SHORT[L]) for L, _, _, pl in TYPES)
    filters += '<button type="button" aria-pressed="false" data-warn="1">⚠ Chỉ điểm cần xem lại</button>'

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
            path = '<p class="path"><span>Từ nhu cầu đến mục này:</span>%s</p>' % " ".join(
                '<span class="chips">%s</span>' % " › ".join(chip(x) for x in c) for c in chains[:3])
        bl = ""
        if G.back.get(i):
            groups = {}
            for src, label in G.back[i]:
                groups.setdefault(label, []).append(src)
            rows_ = "".join('<div class="row"><span class="lbl">%s</span><span class="chips">%s</span></div>' % (
                esc(BACK_LABEL.get(lb, lb.replace("_", " "))), "".join(chip(s) for s in sorted(srcs, key=_natkey))) for lb, srcs in groups.items())
            bl = '<aside class="backlinks"><h2>Những mục nối tới mục này</h2>%s</aside>' % rows_
        idocs += ('<section class="doc" id="%s" data-title="%s"><a class="back back-tree" href="#/trace">← Về cây truy vết</a>'
                  '<header class="ihead"><span class="idtag t-%s">%s</span><div><p class="kind">%s · %s</p><h1>%s</h1></div></header>%s%s<div class="reading">%s</div>%s</section>') % (
            i, esc(i + " " + p.title), p.letter, i, VI_NAME[p.letter][0], VI_NAME[p.letter][1], esc(p.title), warn, path, body, bl)
    v_trace = (
        '<section class="view" id="v-trace"><div class="wrap"><div class="trace">'
        '<div class="pane-tree"><input id="tsearch" class="tsearch" type="search" placeholder="Tìm theo mã hoặc tên" aria-label="Tìm trong cây truy vết">'
        '<div class="filters" role="group" aria-label="Lọc theo loại">%s</div><p class="tcount" id="tcount" aria-live="polite"></p>'
        '<ul class="tree" id="tree">%s</ul></div>'
        '<div class="pane-detail">%s<div class="empty"><p><strong>Chọn một mục ở cây bên trái.</strong></p>'
        '<p>Cây đọc từ trên xuống: nhu cầu, rồi giả thuyết, rồi quyết định, bài kiểm tra và chỉ số.</p></div></div>'
        '</div></div></section>'
    ) % (filters, top or '<li class="n"><span class="nt">Chưa có mục nào.</span></li>', idocs)

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
<div class="brand">{{NAME}}<small>Báo cáo case · tạo ngày {{NOW}}</small></div>
<nav class="tabs" aria-label="Các phần của báo cáo"><a href="#/overview">Tổng quan</a><a href="#/journey">Hành trình</a><a href="#/trace">Truy vết</a><a href="#/reference">Tham chiếu</a></nav>
<input id="gsearch" class="gsearch" type="search" placeholder="Tìm theo mã hoặc từ khoá (ví dụ D2)" aria-label="Tìm trong báo cáo">
{{THEME_SELECT}}
</div></header>
<main id="main">
{{V_OVERVIEW}}
{{V_JOURNEY}}
{{V_TRACE}}
{{V_REFERENCE}}
<div class="wrap" style="padding-top:0"><footer class="foot">Trang này được tạo tự động từ các file Markdown của case. Muốn đổi nội dung, hãy sửa file gốc rồi tạo lại trang (nhờ AI tool chạy python3 tools/export-hub.py).</footer></div>
</main>
<script>{{JS}}</script>
</body>
</html>
""").replace("{{NAME}}", esc(name)).replace("{{NOW}}", now).replace("{{V_OVERVIEW}}", v_overview) \
        .replace("{{V_JOURNEY}}", v_journey).replace("{{V_TRACE}}", v_trace).replace("{{V_REFERENCE}}", v_reference) \
        .replace("{{CSS}}", CSS + theme_rules(theme, switcher)).replace("{{JS}}", JS).replace("{{THEME}}", theme).replace("{{THEME_SELECT}}", theme_select)

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(doc)
    return G, weekly, ref, problems, placeholders, name


def main():
    ap = argparse.ArgumentParser(description="Export the markdown hub to one self-contained HTML file.")
    ap.add_argument("--case", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--out", default=None)
    ap.add_argument("--theme", default="notion", choices=[k for k, _ in THEMES], help="visual theme of the report")
    ap.add_argument("--preview-themes", action="store_true", help="add a theme switcher to the report (for choosing a theme)")
    a = ap.parse_args()
    case = os.path.abspath(a.case)
    out = a.out or os.path.join(case, "index.html")
    G, weekly, ref, problems, placeholders, name = build(case, out, a.theme, a.preview_themes)
    print("Case: %s" % name)
    print("Đã đưa vào báo cáo: %d trang giai đoạn, %d tài liệu tham chiếu, %d item (O %d, H %d, M %d, D %d, T %d)" % (
        len(weekly), len(ref), len(G.items), len(G.O), len(G.H), len(G.M), len(G.D), len(G.T)))
    if G.warnings:
        print("Điểm cần xem lại (%d):" % len(G.warnings))
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
