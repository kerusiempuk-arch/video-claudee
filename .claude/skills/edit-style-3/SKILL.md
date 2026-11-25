---
name: edit-style-3
description: Edit a vertical talking-head product video in the owner's "Style 3" (top headline style — small spaced uppercase label + big bold title with a period at the top above the head, white pills popping in as things are said, big animated numbers like 3XL→5XL / 2×→3×, product-photo cards over a blurred background, yellow "Beli di beg kuning" pill with bouncing arrows, NO bottom subtitles, punch-in cuts, SFX) with HyperFrames via styles/style-3/build.py. Use when the user says "edit style 3", "style 3", "gaya style 3" and gives a Google Drive link.
---

# Edit Style 3 (HyperFrames, `build.py`)

Owner writes in Malay — reply in Malay. They send a Google Drive link and say "edit style 3".
`styles/style-3/build.py` turns raw video + project config (`styles/style-3/projects/<name>.py`) into a HyperFrames
project; `hyperframes check / snapshot / render` do the rest. Reference: `projects/boxer.py` (rebuilt from the owner's
reference video). Template: `projects/_template.py`. Design notes: `styles/style-3/README.md`.

## Owner's standing rules (non-negotiable)
1. Cut every filler ("aaa", "emm", "okay"), repeated words/phrases (keep the last, complete take) and stutters → `REMOVE`.
2. Pauses > 0.3 s are cut automatically; punch-in (1.07, origin top) alternates on each jump cut — automatic.
3. **Keep only the main voice** — automatic (RNNoise, −14 LUFS; video muted).
4. **Brighten dark footage** — automatic (mean luma < 105). Check stills; override with `BRIGHTEN`.
5. Sound effects — automatic (whoosh title / pop pill / click number / sparkle image / ping CTA).
6. **No bottom subtitles** in Style 3 (owner's choice). Text = headlines + pills only.
7. Send **draft frames first**, then a **draft preview video**; final `-q high` render only after approval.
8. Never invent product facts (sizes, colours, prices, combo count). Only what is said, or what the owner confirms.
9. **Style 3 is protected**: don't change `build.py`, fonts, sfx, README or this skill on `main` without the owner's explicit OK. Per-video tweaks go only in `projects/<name>.py`. After the final render, ask whether any change should be saved into Style 3.
10. Commit and push work as you go (videos and `work/` are git-ignored).

## Environment
Same as Style 2: `hyperframes`, whisper.cpp, `ggml-small.bin` (check `ls /root/.cache/hyperframes/whisper/models`; if missing:
`curl -sSL -o /root/.cache/hyperframes/whisper/models/ggml-small.bin https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-small.bin`).
`HF="node ~/.claude/skills/hyperframes/scripts/plugin-cli.mjs"`; `S=styles/style-3/scripts`.

## Steps (from repo root, `W=work/<name>`)
1. `bash $S/download-drive.sh "<link>" $W/raw.mp4` → contact sheet (`ffmpeg -vf "fps=1/2,scale=240:-1,tile=8x3"`) + gridded strip (`fps=1/3,scale=270:480,drawgrid=w=0:h=48,tile=9x1`, each line = 10 %): where is the head and the product.
   **Face check:** titles sit at y 190–530 px (10–28 %). If the face is in that band for most of the video (head near the top of the frame), set `POSITION = "bottom"` (titles y 1240, CTA y 1300, dark gradient at the bottom; example `projects/extension.py`) and say so with the draft frames. Keep titles off the product too.
   Ask the owner for **product photos** (TikTok Shop listing screenshots) if none were sent — the "Penyelesaian" / design / fabric moments use them. Without photos, skip `IMAGES`.
2. `bash $S/find-fillers.sh $W/raw.mp4 $W/fill` → words (`*` = filler) + pauses. Confirm on `python3 -I $S/energy.py $W/fill/a16k.wav <from> <to>`; verify boundaries next to kept words with a short whisper clip (Style 2 skill step 2 has the detail). Write `REMOVE`, `SRC_END`, `TAIL` in `projects/<name>.py` (copy `_template.py`).
3. `python3 -I styles/style-3/build.py $W/raw.mp4 <project> $W/hf --plan` → END. Then `--cut-audio $W/cut.wav` and transcribe:
   `B=/root/.cache/hyperframes/whisper/whisper.cpp/build/bin; LD_LIBRARY_PATH=$B $B/whisper-cli -m /root/.cache/hyperframes/whisper/models/ggml-small.bin -f $W/cut.wav -l ms -ml 1 -sow --prompt "Aaa, okay, emm." -oj -of $W/cutw`
   Verify no filler/repeat remains.
4. Fill the overlay config in **cut time**. Split the script into ideas; one `HEADS` entry per idea, back-to-back (each end = next start):
   kicker = 1–2 word context ("Setiap hari", "Sayang duit", "Boxer lama", "Penyelesaian", "Jangan risau", "Design", "Rasa dia", "Saiz · hingga", "Kain dia", "Nak jimat"),
   title = 1–3 words + period summarising the idea ("Lain warna.", "Dah koyak.", "Tiada brand.", "Lembut."). Pills = the spoken details, each timed to its word; keep each pill ≥ 1.4 s on screen.
   Sizes / quantities → `big=[(t, "3XL"), (t, "5XL")]` + `sub`. Product name moment → `IMAGES` card overlapping that head. Last head ends where the CTA line starts; `CTA.start` = start of "kalau nak dapatkan / tekan beg kuning".
5. `python3 -I styles/style-3/build.py $W/raw.mp4 <project> $W/hf` → `cd $W/hf && $HF check` (no errors; `outside_safe_zone` top-edge warnings are the design; fix `line_unread` by lengthening the head or `TAIL`).
6. `$HF snapshot --at …` (each head, each pill, each image, CTA) → send the contact sheet (SendUserFile).
7. `$HF render -q draft -o ../preview.mp4` with `run_in_background: true` → re-transcribe (no "aaa/okay") → SendUserFile with what was cut, notes and open questions.
8. After approval: `$HF render -q high -o ../final.mp4` (`run_in_background: true`) → SendUserFile **with the cover photo** → ask whether to save any change into Style 3.
   **Cover photo** (every style): with the final video, also send a TikTok cover — `python3 -I tools/cover/make_cover.py $W/raw.mp4 <t> $W/cover.png --title "<Nama produk>." --kicker "<2 kelebihan>" --pills "<a>,<b>,<c>" [--pos top]` (pick a sharp frame where the product is fully visible and the face looks at the camera; compare a few nearby times first; text off the face/product; only facts said in the video) → SendUserFile together with final.mp4. Use `--pos bottom` when the project uses `POSITION = "bottom"` (example: extension → t 11.0, "Extension Wire.", "Surge protector · SIRIM", "5 Soket,3 Pin,Wire panjang").
