#!/usr/bin/env bash
# Bấm đúp file này để build và mở hub trong trình duyệt. Đóng cửa sổ Terminal để tắt.
cd "$(dirname "$0")"
( sleep 12; open "http://127.0.0.1:4321/" ) &
bash scripts/build-local.sh preview
