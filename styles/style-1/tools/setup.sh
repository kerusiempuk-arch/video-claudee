#!/usr/bin/env bash
# Sediakan alat (sekali setiap sesi baru): venv dengan faster-whisper + sound effect.
set -euo pipefail
cd "$(dirname "$0")/../../.."
[ -x .venv-style1/bin/python ] || python3 -m venv .venv-style1
.venv-style1/bin/python -c "import faster_whisper" 2>/dev/null || .venv-style1/bin/pip install -q faster-whisper
ls styles/style-1/sfx/*.wav >/dev/null 2>&1 || python3 -I styles/style-1/sfx.py styles/style-1/sfx
command -v ffmpeg >/dev/null || { echo "ffmpeg tiada"; exit 1; }
echo "siap"
