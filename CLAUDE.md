# video-claudee

Video editing for TikTok — all styles render with HyperFrames (HTML → MP4). The owner writes in Malay — reply in Malay.

## Saved styles

| Trigger | What to do |
|---|---|
| "edit style 1" + Google Drive link | Follow `.claude/skills/edit-style-1/SKILL.md` (product explainer, HyperFrames via `styles/style-1/build.py`: big title with red dot, dark macOS-style option card, monospace "kelebihan 1 / 3" + blue progress bar, tilted white stickers, top (chest-level) captions, dark CTA card with yellow "Tekan beg kuning" button, punch-in cuts, SFX). Reference: `styles/style-1/` (approved example `projects/boxer.py`). |
| "edit style 2" + Google Drive link | Follow `.claude/skills/edit-style-2/SKILL.md` (talking-head / product review, HyperFrames via `styles/style-2/build.py`: chest karaoke captions, blue rail, bottom feature cards, yellow "beg kuning" CTA, punch-in cuts, SFX). Reference: `styles/style-2/` (approved example `projects/boxer.py`). |
| "edit style 3" + Google Drive link | Follow `.claude/skills/edit-style-3/SKILL.md` (top headlines, HyperFrames via `styles/style-3/build.py`: small spaced label + big bold title with period above the head, white pills, big animated numbers (3XL→5XL, 2×→3×), product-photo cards over blurred footage, yellow "Beli di beg kuning" pill + bouncing arrows, **no bottom subtitles**, punch-in cuts, SFX). Reference: `styles/style-3/` (example `projects/boxer.py`). |

General style notes from the first reference video: `STYLE_GUIDE.md`.

## Owner's editing rules (all styles)
- Remove every filler ("aaa", "emm", "okay"), repeated phrases and stutters; shorten pauses > 0.3 s.
- **Keep only the main voice**: remove background noise / unwanted sounds (RNNoise denoise, −14 LUFS).
- **Brighten dark footage** (mean luma < 100 → `hyperframes media-treatment` exposure/shadows).
- **Cover vehicle number plates** (Style 1: `styles/style-1/tools/blur_plate.py` before build).
- Add fitting sound effects.
- Send draft frames → draft preview video → final render after approval.
- **Every time the final video is sent, send a cover photo with it** (frame showing the product + product name), **text in that style's own font and look** (`tools/cover/make_cover.py --style N`) — see each style's skill.
- Commit and push work as you go.

## Saved styles are protected (owner's rule)
- **Never change a saved style on `main`** (`styles/style-N/`, `.claude/skills/edit-style-N/`, its README/build/tools) unless the owner explicitly says so ("simpan dalam style 1", "update style 1 di main", …).
- Tweaks for one video go **only** in that video's project config (e.g. `styles/style-1/projects/<nama>.py`) on the session branch.
- **At the end of every edit** (after the final render is sent), ask in Malay whether any change made for this video should be saved into the style for future videos — list the candidate changes briefly. Only on a yes: apply them to the style files, commit, and push to `main`.
