#!/usr/bin/env bash
# Ukur purata kecerahan (YAVG 0-255) dan cadang patch media-treatment kalau gelap (< 105).
# Guna: brightness.sh <video>   -> cetak YAVG dan JSON patch (atau "ok")
set -euo pipefail
Y=$(ffmpeg -v error -i "$1" -vf "fps=1,scale=270:-1,signalstats,metadata=print:key=lavfi.signalstats.YAVG:file=-" -f null - 2>/dev/null \
  | grep -oE "YAVG=[0-9.]+" | cut -d= -f2 | awk '{s+=$1;n++} END {printf "%.1f", s/n}')
echo "YAVG=$Y"
python3 -I -c "
y=float('$Y')
if y>=105: print('ok')
else:
  e=max(0.15,min(0.8,(118-y)/85)); print('{\"adjust\":{\"exposure\":%.2f,\"shadows\":0.25,\"blacks\":0.08}}'%e)"
