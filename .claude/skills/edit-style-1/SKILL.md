---
name: edit-style-1
description: Edit a vertical product video in the owner's "Style 1" (modern UI "product explainer" — big one-word title with red dot, macOS-style dark option card, monospace "kelebihan 1 / 3" labels with blue progress bar, tilted white stickers, top (chest-level) word-by-word captions, dark CTA card with yellow "Tekan beg kuning" button, punch-in jump cuts, SFX) rendered with HyperFrames. Use when the user says "edit style 1", "style 1", "gaya style 1" and gives a Google Drive link.
---

# Edit Style 1 (HyperFrames)

Owner writes in Malay — reply in Malay. They send a Google Drive link and say "edit style 1".
Design rules: `styles/style-1/README.md`. Approved example: `styles/style-1/projects/boxer.py`.
Rendering is **HyperFrames** (HTML → MP4): `styles/style-1/build.py` turns raw video + project config into a
HyperFrames project; `hyperframes check / snapshot / render` do the rest. Transcription stays in Python (faster-whisper).

## Owner's standing rules (non-negotiable)
1. Cut every filler ("aaa", "eh", "emm", "okay"), repeated phrases / unfinished sentences (keep the complete take) and stutters.
2. Cut every pause > 0.3 s (automatic in `build.py`), punch-in alternates on each jump cut.
3. **Keep only the main voice.** Background noise (wind, fans, traffic, hum, other sounds) is removed — automatic in `build.py` (highpass + RNNoise `arnndn` + lowpass, −14 LUFS). If something still leaks through (music, another person), say so and cut that part or ask.
4. **Brighten dark footage.** `build.py` measures mean luma; below `DARK_Y` (100) it applies exposure/shadows through `hyperframes media-treatment`. Look at the stills: if it is still dark or now washed out, set `BRIGHTEN = {"exposure": …, "shadows": …, "blacks": …}` in the project config (or `BRIGHTEN = None` to switch off).
4b. **Cover vehicle number plates.** If a plate is visible anywhere (check the contact sheet), blur it in the raw footage first with `styles/style-1/tools/blur_plate.py` (template match + camera-motion tracking; `--anchor` for plates half out of frame; look at `--check` and at 0.2 s steps where the plate enters/leaves) and use the output as RAW for `build.py` and `cover.py`.
5. Captions at the **top, chest level** (`CAPTION_Y = 680`, owner's choice) — below the title/stickers, never over the face/mouth (check stills; nudge to 700–760 if it is; if the face sits low in the frame — seated speaker, high camera — go to chest level `CAPTION_Y = 900`). No watermark on previews.
6. Sound effects on every overlay action (automatic: whoosh / click / pop / ding). For water/kitchen products set `SFX_WHOOSH = "drop"` (water-drop "bloop" instead of whoosh).
7. Preview (draft render) first → wait for **"okay render"** → final render (`-q high`).
8. Don't invent product facts (prices, sizes, materials). Inferred items (e.g. colours visible on screen) must be listed for the owner to confirm.
9. **Style 1 itself is protected.** Never edit `styles/style-1/` build/sfx/tools/README or this skill on `main` without the owner's explicit OK. Per-video tweaks go only in `styles/style-1/projects/<name>.py`.
10. After sending the final render + cover photo, ask (in Malay) whether any change made for this video should be saved into Style 1 for future videos, listing the candidates. Only on a yes: update the style files, commit, push to `main`.

## Steps (run from repo root; `W=work/<name>`, `HF="node ~/.claude/skills/hyperframes/scripts/plugin-cli.mjs"`)
```bash
styles/style-1/tools/setup.sh                                   # hyperframes CLI + skills, venv .venv-style1 + faster-whisper, RNNoise model
styles/style-1/tools/fetch_drive.sh "<drive link>" $W/raw.mp4   # fails clearly if link isn't public
ffmpeg -v error -i $W/raw.mp4 -vf "fps=1,scale=240:-1,tile=8x4" $W/sheet.jpg   # look at it
.venv-style1/bin/python styles/style-1/tools/transcribe.py $W/raw.mp4
```
- Closing/CTA line repeated several times (e.g. "berminat dengan … ni" ×3 + an unfinished "dapatkan") → one `REMOVE` covering all earlier tries; keep only the last complete take through "… beg/bakul kuning". Re-transcribe that window if Whisper garbles it.
- `transcribe.py` flags `[FILLER]`, `[ULANG?]` (possible repeat — check, keep the complete take) and `[PANJANG]` (word > 0.9 s: Whisper merged a repeat; it re-transcribes that window and prints it). Also check isolated 0.1–0.3 s sound bursts between sentences on the energy (short "aa").
- If the link is the already-edited reference video, ask for the raw footage instead.

1. `cp styles/style-1/projects/_template.py styles/style-1/projects/<name>.py`; fill `REMOVE` (source times), `SRC_END`, `TAIL`.
2. `python3 -I styles/style-1/build.py $W/raw.mp4 styles/style-1/projects/<name>.py $W/hf --plan` → prints the kept segments and **END** (put END in the config).
3. `python3 -I styles/style-1/build.py $W/raw.mp4 <project> $W/hf --cut-audio $W/cut.wav` → clean, cut voice; transcribe it:
   `.venv-style1/bin/python styles/style-1/tools/transcribe.py $W/cut.wav --keep $W/cut.wav.keep.json` → the clean voice reveals short "ha"/"okay" the raw transcript missed; each `[FILLER]` prints `REMOVE ≈ (src_a, src_b)` → add to `REMOVE`; it also prints `# BUNYI PENDEK?` (0.06–0.45 s sound between words that Whisper did not write — an "okey"/"aa"/half-word; check, then add its `REMOVE`) and `# JEDA` (pause > 0.6 s that build.py kept because of background noise, or that Whisper hid inside a stretched word → add its `REMOVE`), redo `--plan`/`--cut-audio` until no filler/repeat remains → fill `CAPTIONS` (1–3 words, real word starts; `[]` = no captions), `HOOK` (2 or 3 options — use 3 when the opening line names 3 things; `select_at` = when each option word is spoken; `end` may run to ~8 s so the options are spoken while the card is up), `SECTIONS` (label "kelebihan", or "tip" for how-to/tip videos), `STICKERS` (when the speaker first lists problems of the ordinary product, add 3 "… ✗" problem stickers there before the sections, and echo them with "✓" in the matching kelebihan section — see README, `projects/lighter.py`) (a short list said in a row, e.g. "tak koyak / tak bocor / tak basah ✓" → 3 tiers y 260/340/420), `CIRCLES`, `BIG_WORDS` (big one-word flashes mid-video, e.g. "berbuih." — place where no sticker is up), `CTA` (CTA `title`: prefer a word said near the end, e.g. "murah" from "harga sangat murah", else repeat the hook title; CTA `tags`: max 3 short tags, 1–2 words each, or they overflow the card). All overlay times are **cut** times.
4. Build: `python3 -I styles/style-1/build.py $W/raw.mp4 <project> $W/hf` (prints the brightness decision).
5. `cd $W/hf && $HF check` — must have no errors (top/bottom safe-zone and small-text warnings are the approved design).
6. Stills: `$HF snapshot --at <t1>,<t2>,…` (hook, each option switch, each section, stickers, CTA) → check overlaps with face/product; the caption accent turns yellow automatically on a blue shirt/background (build prints `piksel biru … → KUNING`); if it still vanishes, force `CAPTION_ACCENT = (…)` in the project config.
7. Preview: `$HF render -q draft -o ../preview.mp4` (run detached: `setsid nohup … &`, wait with a background until-loop) → SendUserFile + table of texts/times + what was cut + brightness/noise notes + open questions.
8. After "okay render": `$HF render -q high -o ../final.mp4` → SendUserFile, **with the cover photo**. **Cover photo** (Style 1's own approved design, from the sabun video): fill `COVERS` in the project config — 2 options: A = product + face looking at the camera, B = the result (no face in the video → A = whole product from the sharpest frame, B = another angle/build with a kicker from another line, see `projects/ninja.py`); `at` = source time of a sharp frame (compare a few nearby times first); sticker text only from what was said — then `python3 -I styles/style-1/tools/cover.py $W/raw.mp4 <project> $W/cover` (white top + kicker + big black word with red square dot, photo shifted down so the title never covers the face, 2 tilted white stickers, dark mono pill — its label matches `SECTIONS`: "kelebihan 1-3 · …" for kelebihan videos, "tip 1-3 · …" for tip videos; the part after "·" may be the product name) → look at both PNGs → SendUserFile cover.png + cover2.png together with final.mp4. (`tools/cover/make_cover.py --style 1` is the older generic layout; use it only if the owner asks for the card-style cover.)
9. Commit the project config (videos and `work/` are git-ignored) and push.

## Environment notes
- Network: `drive.google.com`, `drive.usercontent.google.com`, `huggingface.co`, `us.aws.cdn.hf.co`, `raw.githubusercontent.com` (RNNoise model) — cloud environment **"video-claudee"** has the Drive/HF hosts; its setup script installs hyperframes + whisper.cpp.
- Whisper download: use `HF_HUB_DISABLE_XET=1` (the tool sets it). Pass numpy audio to faster-whisper (new PyAV breaks file paths).
- Phone video: 1920×1080 + rotation −90 → the browser and ffmpeg auto-rotate to 1080×1920.
- Never use WebGL blur on footage (very slow without GPU); the brightness treatment alone renders fine (~0.4 s/frame).
