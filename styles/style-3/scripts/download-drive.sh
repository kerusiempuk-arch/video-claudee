#!/usr/bin/env bash
# Muat turun fail Google Drive (link "file/d/<ID>/view" atau ID sahaja).
# Guna: download-drive.sh <link-atau-id> <output.mp4>
set -euo pipefail
in="$1"; out="$2"
id=$(printf '%s' "$in" | sed -nE 's#.*/d/([A-Za-z0-9_-]+).*#\1#p')
[ -z "$id" ] && id=$(printf '%s' "$in" | sed -nE 's#.*[?&]id=([A-Za-z0-9_-]+).*#\1#p')
[ -z "$id" ] && id="$in"
curl -sSL -o "$out" -w '%{http_code} %{content_type} %{size_download}\n' \
  "https://drive.usercontent.google.com/download?id=${id}&export=download&confirm=t"
file "$out"
ffprobe -v error -show_entries format=duration:stream=codec_type,width,height,r_frame_rate:stream_side_data=rotation -of compact "$out"
