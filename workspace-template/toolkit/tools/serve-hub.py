#!/usr/bin/env python3
"""Preview the hub on your own computer and see edits without re-running the export.

    python3 serve-hub.py            # http://127.0.0.1:8000
    python3 serve-hub.py --port 9000

Edit any Markdown file in the project, then reload the page: index.html is rebuilt first when a file changed.
Only your computer can reach this address. Stop with Ctrl+C.
Python 3.8+ standard library only.
"""
import argparse
import http.server
import os
import subprocess
import sys
import functools

def find_case(start=None):
    """The project folder: the nearest folder, from `start` (default: the current folder) upwards,
    that has AGENTS.md next to insights/ or work/. Falls back to the folder above this script
    (a copy of this script in the workspace's toolkit/tools/ folder)."""
    p = os.path.abspath(start or os.getcwd())
    while True:
        if os.path.isfile(os.path.join(p, "AGENTS.md")) and (
                os.path.isdir(os.path.join(p, "insights")) or os.path.isdir(os.path.join(p, "work"))):
            return p
        parent = os.path.dirname(p)
        if parent == p:
            break
        p = parent
    legacy = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if os.path.isdir(os.path.join(legacy, "insights")):
        return legacy
    return None


CASE = None
EXPORTER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "build-report.py")
INDEX = None
SKIP = {".git", "node_modules", "_raw-private", "_personal"}


def newest_source():
    newest = os.path.getmtime(EXPORTER)
    for dp, dn, fn in os.walk(CASE):
        dn[:] = [d for d in dn if d not in SKIP]
        for f in fn:
            if f.endswith((".md", ".html", ".png", ".jpg", ".svg", ".css")) and f != "index.html" or dp == CASE and f == "AGENTS.md":
                try:
                    newest = max(newest, os.path.getmtime(os.path.join(dp, f)))
                except OSError:
                    pass
    return newest


def rebuild_if_needed():
    if not os.path.isfile(INDEX) or newest_source() > os.path.getmtime(INDEX):
        r = subprocess.run([sys.executable, EXPORTER, "--project", CASE], capture_output=True, text=True)
        print("  rebuilt index.html" + ("" if r.returncode == 0 else " (error)\n" + r.stdout + r.stderr))


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.split("?")[0] in ("/", "/index.html"):
            rebuild_if_needed()
        super().do_GET()

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt, *args):
        pass


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8000)
    ap.add_argument("--project", "--case", dest="case", default="", help="project folder (default: the project you are standing in)")
    a = ap.parse_args()
    global CASE, INDEX
    CASE = os.path.abspath(a.case) if a.case else find_case()
    if not CASE:
        sys.exit("Project folder not found. Run inside a project (a folder with AGENTS.md and insights/), or pass --project <path>.")
    INDEX = os.path.join(CASE, "index.html")
    rebuild_if_needed()
    handler = functools.partial(Handler, directory=CASE)
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", a.port), handler)
    print("Hub: http://127.0.0.1:%d   (Ctrl+C to stop)" % a.port)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
