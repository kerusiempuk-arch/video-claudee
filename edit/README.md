# TikTok edit (gaya "product explainer")

Aliran kerja untuk setiap video baru:

1. **Potong** – `python3 edit/cut.py raw.mp4 cut.mp4 edit/projects/<nama>.py`
   - Senyap > 0.3s dipotong automatik (paras `SILENCE_DB`).
   - Ulangan / gagap / salah cakap: masukkan dalam `REMOVE` (masa video asal).
   - Setiap jump cut tukar zoom (punch-in) supaya nampak sengaja.
2. **Transkripsi semula** `cut.mp4` (faster-whisper, model `medium`, bahasa `ms`) untuk masa perkataan.
3. **Isi config** `edit/projects/<nama>.py`: kapsyen, hook, kelebihan 1/2/3, sticker, CTA.
4. **Preview** – `python3 edit/engine.py cut.mp4 out.mp4 edit/projects/<nama>.py --preview` (540p + tanda PREVIEW).
5. **Final** (lepas diluluskan) – sama, tanpa `--preview` (1080x1920).

Sound effect (`edit/sfx/`, dijana oleh `sfx.py`) dimasukkan automatik:
whoosh = tajuk/seksyen, click = pilihan kad, pop = sticker/bulatan, ding = kad CTA.
