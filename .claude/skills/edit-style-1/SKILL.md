---
name: edit-style-1
description: Edit a vertical product video in the owner's "Style 1" (modern UI "product explainer" — big one-word title with red dot, macOS-style dark option card, monospace "kelebihan 1 / 3" labels with blue progress bar, tilted white stickers, bottom word-by-word captions, dark CTA card with yellow "Tekan bakul kuning" button, punch-in jump cuts, synthetic SFX) with Python + ffmpeg. Use when the user says "edit style 1", "style 1", "gaya style 1" and gives a Google Drive link.
---

# Edit Style 1

Owner writes in Malay — reply in Malay. They send a Google Drive link and say "edit style 1".
Design rules: `styles/style-1/README.md`. Approved example: `styles/style-1/projects/boxer.py`.
Everything is plain Python (Pillow, numpy) + ffmpeg — no HyperFrames/Node needed.

## Owner's standing rules (non-negotiable)
1. Cut every filler ("aaa", "eh", "emm", "okay"), repeated phrases / unfinished sentences (keep the complete take) and stutters.
2. Cut every pause > 0.3 s (automatic in `cut.py`), punch-in alternates on each jump cut.
3. Captions at the **bottom** (`CAPTION_Y = 1780`), never in the middle. No watermark on previews.
4. Sound effects on every overlay action (automatic: whoosh / click / pop / ding).
5. Preview (540p) first → wait for **"okay render"** → final 1080×1920.
6. Don't invent product facts (prices, sizes, materials). Inferred items (e.g. colours visible on screen) must be listed for the owner to confirm.

## Steps (run from repo root; `W=work/<name>`)
```bash
styles/style-1/tools/setup.sh                                   # venv .venv-style1 + faster-whisper
styles/style-1/tools/fetch_drive.sh "<drive link>" $W/raw.mp4   # fails clearly if link isn't public
ffmpeg -v error -i $W/raw.mp4 -vf "fps=1,scale=240:-1,tile=8x4" $W/sheet.jpg   # look at it
.venv-style1/bin/python styles/style-1/tools/transcribe.py $W/raw.mp4
```
- `transcribe.py` flags `[FILLER]`, `[ULANG?]` (possible repeat — check, keep the complete take) and `[PANJANG]` (word > 0.9 s: Whisper merged a repeat; it re-transcribes that window and prints it). Also check isolated 0.1–0.3 s sound bursts between sentences on the energy (short "aa").
- If the link is the already-edited reference video, ask for the raw footage instead.

1. `cp styles/style-1/projects/_template.py styles/style-1/projects/<name>.py`; fill `REMOVE` (source times), `SRC_END`, `TAIL`.
2. `python3 -I styles/style-1/cut.py $W/raw.mp4 $W/cut.mp4 styles/style-1/projects/<name>.py`
3. Transcribe `$W/cut.mp4` again → confirm no filler/repeat remains → fill `CAPTIONS` (1–3 words, real word starts), `HOOK` (`select_at` = when each option word is spoken), `SECTIONS`, `STICKERS`, `CTA`, `END` (= cut duration). All overlay times are **cut.mp4** times.
4. Check stills for overlaps (face/product): `python3 -I styles/style-1/engine.py $W/cut.mp4 $W/s.png <project> --preview --still <t>`; use a gridded frame to place circles. If the accent colour vanishes on the background (e.g. light-blue shirt), set `CAPTION_ACCENT` to yellow.
5. Preview: `python3 -I styles/style-1/engine.py $W/cut.mp4 $W/preview.mp4 <project> --preview` → SendUserFile + table of texts/times + what was cut + open questions.
6. After "okay render": same command without `--preview` → `$W/final.mp4` → SendUserFile.
7. Commit the project config (videos are git-ignored) and push.

## Environment notes
- Network: `drive.google.com`, `drive.usercontent.google.com`, `huggingface.co`, `us.aws.cdn.hf.co` — cloud environment **"video-claudee"** has them.
- Whisper download: use `HF_HUB_DISABLE_XET=1` (the tool sets it). Pass numpy audio to faster-whisper (new PyAV breaks file paths).
- Phone video: 1920×1080 + rotation −90 → ffmpeg auto-rotates to 1080×1920.
