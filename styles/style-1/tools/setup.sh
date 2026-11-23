#!/usr/bin/env bash
# Sediakan alat Style 1 (sekali setiap sesi baru): HyperFrames, faster-whisper, model RNNoise.
set -euo pipefail
cd "$(dirname "$0")/../../.."
command -v ffmpeg >/dev/null || { echo "ffmpeg tiada"; exit 1; }
command -v hyperframes >/dev/null || npm install -g hyperframes@0.9.85
[ -f ~/.claude/skills/hyperframes/scripts/plugin-cli.mjs ] || hyperframes skills >/dev/null 2>&1 || true
[ -x .venv-style1/bin/python ] || python3 -m venv .venv-style1
.venv-style1/bin/python -c "import faster_whisper" 2>/dev/null || .venv-style1/bin/pip install -q faster-whisper
ls styles/style-1/sfx/*.wav >/dev/null 2>&1 || python3 -I styles/style-1/sfx.py styles/style-1/sfx
M=~/.cache/style1/cb.rnnn
[ -s "$M" ] || { mkdir -p "$(dirname "$M")"; curl -sSL -o "$M" https://raw.githubusercontent.com/GregorR/rnnoise-models/master/conjoined-burgers-2018-08-28/cb.rnnn; }
echo "siap"
