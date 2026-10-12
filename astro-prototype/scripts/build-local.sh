#!/usr/bin/env bash
# Builds the site in a LOCAL folder, because node_modules (tens of thousands of files) must not live in a cloud-synced folder.
#   scripts/build-local.sh            build
#   scripts/build-local.sh preview    build, then serve the result
#   HUB_TEAM=1 scripts/build-local.sh   include AI-draft sections (folded)
set -euo pipefail
SRC="$(cd "$(dirname "$0")/.." && pwd)"
WORK="${HUB_SITE_WORK:-$HOME/.cache/hub-site}"
export HUB_CASE_DIR="${HUB_CASE_DIR:-$(cd "$SRC/../workspace/demo-case" && pwd)}"
mkdir -p "$WORK"
rsync -a --delete --exclude node_modules --exclude dist --exclude .astro --exclude public/hub-assets "$SRC/" "$WORK/"
cd "$WORK"
npm install --no-audit --no-fund --loglevel=error
npm run build
echo "Built: $WORK/dist"
if [ "${1:-}" = "preview" ]; then npm run preview -- --host 127.0.0.1 --port 4321; fi
