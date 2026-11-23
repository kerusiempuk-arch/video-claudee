#!/usr/bin/env bash
# Muat turun video dari link Google Drive (set "Anyone with the link").
# Usage: tools/fetch_drive.sh <drive-link-atau-id> <output.mp4>
set -euo pipefail
LINK="$1"; OUT="$2"
ID=$(printf '%s' "$LINK" | sed -nE 's#.*/d/([A-Za-z0-9_-]+).*#\1#p; s#.*[?&]id=([A-Za-z0-9_-]+).*#\1#p' | head -1)
[ -z "$ID" ] && ID="$LINK"
mkdir -p "$(dirname "$OUT")"
curl -sSL -o "$OUT" "https://drive.usercontent.google.com/download?id=${ID}&export=download&confirm=t"
if ! file "$OUT" | grep -qiE 'ISO Media|QuickTime|Matroska|WebM|MPEG'; then
  echo "GAGAL: bukan fail video. Pastikan link di-share 'Anyone with the link'." >&2
  head -c 300 "$OUT" >&2; exit 1
fi
ffprobe -v error -show_entries format=duration:stream=codec_type,width,height:stream_side_data=rotation \
  -of default=nw=1 "$OUT"
