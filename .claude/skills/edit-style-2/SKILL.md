---
name: edit-style-2
description: Edit a vertical talking-head / product-review video in the owner's "Style 2" (karaoke captions on the chest, blue progress rail, white feature cards at the bottom, CTA with checklist + yellow "beg kuning" button, punch-in jump cuts, UI sound effects) with HyperFrames via styles/style-2/build.py. Use when the user says "edit style 2", "style 2", "gaya style 2" or gives a Google Drive link and asks to edit it like style 2.
---

# Edit Style 2 (HyperFrames, `build.py`)

Owner writes in Malay — reply in Malay. They send a Google Drive link and say "edit style 2".
`styles/style-2/build.py` turns raw video + project config (`styles/style-2/projects/<name>.py`) into a HyperFrames
project; `hyperframes check / snapshot / render` do the rest. Approved example: `projects/boxer.py`.
Template: `projects/_template.py`. Design notes: `styles/style-2/README.md`.

## Owner's standing rules (non-negotiable)
1. Cut every filler ("aaa", "emm", "okay"), repeated words/phrases (keep the last, complete take) and stutters → `REMOVE`.
2. Pauses > 0.3 s are cut automatically; punch-in (1.07, origin top) alternates on each jump cut — automatic.
3. **Keep only the main voice** — automatic (highpass + RNNoise `arnndn` + lowpass, −14 LUFS; video muted). If music or another person is still audible, cut it or ask.
4. **Brighten dark footage** — automatic (mean luma < 105 → `hyperframes media-treatment`). Check stills; if still dark or washed out set `BRIGHTEN = {...}` (or `None`).
5. Sound effects on every visual action — automatic (pop / whoosh-short / click / sparkle / ping).
6. Send **draft frames first**, then a **draft preview video**; final `-q high` render only after approval.
7. Never invent product facts (sizes, colours, prices). Unspoken items are placeholders the owner must confirm.
8. **Style 2 is protected**: don't change `build.py`, sfx, README or this skill on `main` without the owner's explicit OK. Per-video tweaks go only in `projects/<name>.py`. After the final render, ask whether any change should be saved into Style 2.
9. Commit and push work as you go (videos and `work/` are git-ignored).

## Environment
- The "video-claudee" cloud environment allows Drive + Hugging Face, and its setup script installs `hyperframes@0.9.85`, its skills, whisper.cpp and `ggml-small.bin` (check `which hyperframes`, `ls /root/.cache/hyperframes/whisper/models`). Manual fallback: `npm i -g hyperframes@0.9.85 && hyperframes skills`; run `hyperframes transcribe` once to build whisper.cpp, then
  `curl -sSL -o /root/.cache/hyperframes/whisper/models/ggml-small.bin https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-small.bin` (the CLI's own download ignores the proxy).
- RNNoise model is fetched by `build.py` from raw.githubusercontent.com into `~/.cache/style1/cb.rnnn`.
- `HF="node ~/.claude/skills/hyperframes/scripts/plugin-cli.mjs"`; `S=styles/style-2/scripts`.

## Steps (from repo root, `W=work/<name>`)
1. `bash $S/download-drive.sh "<link>" $W/raw.mp4` → contact sheet (`ffmpeg -vf "fps=1/2,scale=240:-1,tile=8x3"`) and a gridded strip (`drawgrid=w=0:h=60`) to find the **face**, the **product** and free areas.
2. `bash $S/find-fillers.sh $W/raw.mp4 $W/fill` → words (`*` = filler) + pauses. Confirm each filler/repeat on `python3 -I $S/energy.py $W/fill/a16k.wav <from> <to>`; cut inside the quiet dips. Write `REMOVE`, `SRC_END`, `TAIL` in `projects/<name>.py` (copy `_template.py`). Set `SRC_END` ~0.6 s after the last word (into the trailing silence) so the CTA stays on screen ≥ 2 s — `TAIL` alone does not lengthen END; `hyperframes check` must show no `line_unread`.
3. `python3 -I styles/style-2/build.py $W/raw.mp4 <project> $W/hf --plan` → END. Then `--cut-audio $W/cut.wav` and transcribe it word-by-word:
   `B=/root/.cache/hyperframes/whisper/whisper.cpp/build/bin; LD_LIBRARY_PATH=$B $B/whisper-cli -m /root/.cache/hyperframes/whisper/models/ggml-small.bin -f $W/cut.wav -l ms -ml 1 -sow --prompt "Aaa, okay, emm." -oj -of $W/cutw`
   Verify no filler/repeat remains (else extend `REMOVE` and redo).
4. Fill the overlay config in **cut time**: `CAPTIONS` (≤ 4 words, fix Whisper spelling — boksir→boxer, lembuk→lembut, beg kuni/begkorni/begkondi→beg kuning, berkarak→berkarat, anti-order→anti-odour — and keep every spoken word), `HOOK`, `CARDS` (vs / icon / check / chips, each timed to the word that triggers it; `vs` old/new 1–2 short words so they stay on one line, e.g. "Nipis" → "Tebal"), `RAIL` steps, `CTA`. `CAPTION_Y` just below the chin (default 600, hook y 760); CTA `button_at` is clamped to END − 2.2 s automatically; cards stay off the face and the product.
5. `python3 -I styles/style-2/build.py $W/raw.mp4 <project> $W/hf` → `cd $W/hf && $HF check` (no errors; safe-zone / density warnings are the design).
6. `$HF snapshot --at …` (hook, each card, each cut, CTA) → combine (ffmpeg hstack/vstack) → SendUserFile.
7. `$HF render -q draft -o ../preview.mp4` detached (`setsid nohup … &`, wait with a background until-loop) → re-transcribe the output with the filler prompt (no "aaa/okay" may remain) → SendUserFile with what was cut, brightness/noise notes and open questions.
8. After approval: `$HF render -q high -o ../final.mp4` → SendUserFile → ask whether to save any change into Style 2.
