#!/usr/bin/env bash
# Buang bunyi latar, kekalkan suara utama sahaja: highpass -> RNNoise (arnndn) -> lowpass -> -14 LUFS.
# Guna: clean-voice.sh <video> <projek>/voice.m4a
set -euo pipefail
M=~/.cache/style1/cb.rnnn
[ -s "$M" ] || { mkdir -p "$(dirname "$M")"; curl -sSL -o "$M" https://raw.githubusercontent.com/GregorR/rnnoise-models/master/conjoined-burgers-2018-08-28/cb.rnnn; }
ffmpeg -v error -y -i "$1" -vn -af "highpass=f=80,arnndn=m=$M,lowpass=f=12000,loudnorm=I=-14:TP=-2" -ar 48000 -ac 2 -c:a aac -b:a 192k "$2"
echo "-> $2"
