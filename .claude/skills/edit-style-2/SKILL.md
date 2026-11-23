---
name: edit-style-2
description: Edit a vertical talking-head / product-review video in the owner's "Style 2" (karaoke captions on the chest, blue progress rail, white feature cards at the bottom, CTA with checklist + yellow "beg kuning" button, punch-in jump cuts, UI sound effects) with HyperFrames. Use when the user says "edit style 2", "style 2", "gaya style 2" or gives a Google Drive link and asks to edit it like style 2.
---

# Edit Style 2

The owner writes in Malay; reply in Malay. They send a Google Drive link and say "edit style 2".
Reference implementation (the boxer review): `styles/style-2/reference-project/`. Read its
`index.html` and `compositions/*.html` before building; copy and adapt them, don't start from zero.
Design notes for humans: `styles/style-2/README.md`. Helper scripts: `styles/style-2/scripts/`.

## Owner's standing rules (non-negotiable)

1. Cut **every filler word** ("aaa", "emm", "okay"), **repeated words/phrases** (keep the last, cleanest take) and **stutters**.
2. Shorten **every pause > ~0.3 s** to ~0.1 s.
3. Alternate a **punch-in** (`scale(1.07)`, `transform-origin: 50% 4%` so the head is never cropped) on every other segment so jump cuts look intentional.
4. Add **sound effects** on every visual action (map below), volume 0.3–0.4, under the voice.
5. Send **draft frames first**, then a **draft preview video**; final high-quality render only after approval.
6. Never invent product facts (sizes, colours, prices). If the speaker doesn't say them, ask, or mark them clearly as placeholders.
7. Commit and push work to the session branch as you go.

## 0. Environment (fresh container)

- The "video-claudee" cloud environment has a setup script that already installs `hyperframes@0.9.85`, its skills, whisper.cpp and `ggml-small.bin`. Check with `which hyperframes` and `ls /root/.cache/hyperframes/whisper/models`; only do the manual steps below if they are missing.
- Network needs `drive.google.com`, `drive.usercontent.google.com`, `huggingface.co` (+ its CDN hosts). The owner's cloud environment **"video-claudee"** has them. If a host is refused, check `get_environment` and switch to / propose that environment.
- Install: `npm install -g hyperframes` then `hyperframes skills` (installs the `/hyperframes` and `/media-use` skills — load `/hyperframes` before writing compositions).
- Whisper model: `hyperframes transcribe` does **not** use the HTTPS proxy (fails with `ENOTFOUND huggingface.co`). Run it once (it builds whisper.cpp), then download the model with curl:
  `curl -sSL -o /root/.cache/hyperframes/whisper/models/ggml-small.bin https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-small.bin`
  and run transcribe again.
- CLI: `node ~/.claude/skills/hyperframes/scripts/plugin-cli.mjs <command>` (= `npx hyperframes <command>`).

## 1. Get the footage

```bash
S=styles/style-2/scripts
bash $S/download-drive.sh "<drive link>" /tmp/<name>.mp4
hyperframes init <name> --video /tmp/<name>.mp4 --skip-transcribe --non-interactive --skip-skills --skill=hyperframes
```
Phones record 1920×1080 with rotation −90 → the project is 1080×1920 portrait. Make a contact sheet
(`ffmpeg -vf "fps=1/2,scale=240:-1,tile=8x3"`) and a gridded strip (`drawgrid=w=0:h=60`) to see
where the **face**, the **product** and the **free areas** are.

## 2. Transcribe + find what to cut

```bash
cd <name>
hyperframes transcribe src.mp4 --model small --language ms --engine whisper   # -> transcript.json (word timings)
bash ../$S/find-fillers.sh src.mp4 /tmp/<name>-fill                            # filler-aware words (* = filler) + pauses
python3 -I ../$S/energy.py /tmp/<name>-fill/a16k.wav <from> <to>               # dB every 30 ms to place cuts
```
- Normal Whisper drops fillers; `find-fillers.sh` uses a filler prompt so "aaa/okay" show up. Confirm each one on the energy table (a sound burst bounded by dips below ~-40 dB) and, if unsure, transcribe the remainder alone (`ffmpeg -ss <cut_end>` → `whisper-cli`) to check the next word is still whole.
- Cut points sit inside the quiet dips, keeping ~0.03–0.05 s of air.
- Fix Whisper spelling for captions (e.g. boksir→boxer, lembuk→lembut, beg kuni→beg kuning). The speaker's words are the captions — don't drop words like "pun".

## 3. Build (copy from the reference project)

1. `node ../$S/segments.mjs <source_end> '<cuts json>' [source times…]` → `<video>` segment tags (punch-in alternates) + total duration + source→edit time map. Root `data-duration` = total. Add the `.seg` / `.seg.punch` CSS from the reference `index.html`.
2. Copy `reference-project/assets/sfx/*.mp3` into `assets/sfx/`.
3. Scenes (each its own file in `compositions/`, host in `index.html`, same id for host / root / timeline key):
   - `hook.html` — white pill "✳ <topic>" over the chest, 0.15 s → ~2.7 s.
   - `vs.html` — optional "old → new" comparison card (strike-through grey vs blue ✓ serif-italic).
   - `f1…fN.html` — one **feature card** per selling point, bottom band `left:120 top:1360–1390 width:760`, white, radius 30, kicker in JetBrains Mono blue 28 px (`01 · SELESA`), title Inter 700 46–50 px with one Playfair Display italic blue accent word, optional icon tile or ✓ checklist ticked on the spoken word.
   - `rail.html` — blue progress rail at x=58 with node + blue label pill (`01 Selesa`…) stepping down **Y = 318, 380, 442, 504** (beside the head, above the caption), visible only during the feature section.
   - `cta.html` — navy tint `rgba(14,22,52,.62)` over footage, ✓ recap of every feature, yellow `#FFC93C` pill button "🛒 Tekan *beg kuning*" (or whatever the speaker asks), basket wiggle.
   - `captions.html` — write `captions.config.json` (see the reference one) then `node ../$S/gen-captions.mjs .`. Chunks ≤ 4 words; `[word]` white box, `{word}` serif italic; `top` ≈ just below the chin (545 in the reference).
4. Time every card/tick/label to the **edited** time of the word that triggers it (use the map from step 1).
5. Cards must not cover the face or the product being shown; the bottom band over the legs is the default (TikTok safe-zone warnings there are accepted).
6. Avoid WebGL media treatments (blur/grade) — they make local renders ~10× slower without a GPU. Use the navy tint div instead.

### Sound effect map (`<audio id class-less data-start data-duration data-volume data-track-index>`)

| Moment | File | dur | vol |
|---|---|---|---|
| pill / icon / chip pops in | `pop.mp3` | 0.72 | 0.3–0.35 |
| card enters or swaps | `whoosh-short.mp3` | 0.57 | 0.3–0.35 |
| ✓ tick, strike-through | `click.mp3` | 0.37 | 0.35–0.4 |
| product name reveal | `sparkle.mp3` | 1.8 | 0.3 |
| CTA button lands | `ping.mp3` | 1.32 | 0.4 |

Always set `data-duration` on each `<audio>` (otherwise check thinks it runs to the end) and put overlapping ones on different `data-track-index` lanes.

## 4. Check, draft, preview, final

```bash
hyperframes check --json        # fix every error; warnings: safe-zone bottom + caption density are expected
hyperframes snapshot --at <t1>,<t2>,…   # hook, each card, each cut, CTA → combine with ffmpeg hstack/vstack → SendUserFile
hyperframes render -q draft -o ../<name>_preview.mp4   # run detached (setsid nohup … &) and wait with a background until-loop
```
- Verify the render: transcribe the output again with the filler prompt — no "aaa/okay" may remain.
- Send the preview with SendUserFile; list what was cut (times) and anything assumed.
- Final: `hyperframes render -q high -o ../<name>_final.mp4` after the owner approves.
