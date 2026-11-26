#!/usr/bin/env bash
# Transkripsi "sedar pengisi" (aaa/emm/okay) + senarai jeda senyap.
# Guna: find-fillers.sh <video> <outdir>
# Output: <outdir>/fill.json (whisper-cli, perkataan demi perkataan) dan senarai di skrin.
set -euo pipefail
vid="$1"; out="$2"; mkdir -p "$out"
B=/root/.cache/hyperframes/whisper/whisper.cpp/build/bin
M=/root/.cache/hyperframes/whisper/models/ggml-small.bin
ffmpeg -v error -y -i "$vid" -ar 16000 -ac 1 "$out/a16k.wav"
LD_LIBRARY_PATH=$B $B/whisper-cli -m "$M" -f "$out/a16k.wav" -l ms -ml 1 -sow \
  --prompt "Aaa, okay, emm, aaa. Okay, jadi aaa, okay." -oj -of "$out/fill" >/dev/null 2>&1
python3 -I - "$out/fill.json" <<'PY'
import json,sys,re
d=json.load(open(sys.argv[1]))
F=re.compile(r'^(a+|aa+h?|e+m+|u+m+|okay|ok|oke|haa?)$',re.I)
print("== perkataan (* = pengisi) ==")
for s in d['transcription']:
    t=s['text'].strip()
    if not t: continue
    a,b=s['offsets']['from']/1000,s['offsets']['to']/1000
    mark='*' if F.match(re.sub(r'[^\w]','',t)) else ' '
    print(f"{mark} {a:6.2f}-{b:6.2f} {t}")
PY
echo "== jeda senyap >= 0.18 s (-32 dB) =="
ffmpeg -hide_banner -i "$vid" -af silencedetect=n=-32dB:d=0.18 -f null - 2>&1 | grep -oE "silence_(start|end): [0-9.]+" | paste - -
