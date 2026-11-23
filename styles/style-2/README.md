# Style 2 — Talking head / review produk (TikTok, 9:16)

Cara guna: beri Claude **link Google Drive** video dan cakap **"edit style 2"**.
Claude ikut `.claude/skills/edit-style-2/SKILL.md`. Dirender dengan **HyperFrames** melalui `build.py`:
video mentah + config projek (`projects/<nama>.py`) → projek HyperFrames → `hyperframes render`.

Contoh yang diluluskan: `projects/boxer.py` (review boxer lelaki). Templat: `projects/_template.py`.

## Rupa
| Elemen | Gaya |
|---|---|
| Format | Menegak 1080×1920, 30 fps |
| Caption | Satu baris di **dada** (bawah dagu), Inter 700 56 px putih atas jalur gelap lut sinar; perkataan muncul satu-satu ikut suara (karaoke). Kata kunci: **kotak putih** (`box`) atau *serif italik* (`serif`, Playfair Display) |
| Hook | Pil putih "✳ review **topik**" dalam 3 saat pertama |
| Kad | Kad putih bucu bulat di bahagian **bawah** (atas kaki, tak tutup muka/produk): `vs` (lama ~~dipangkah~~ → baru ✓), `icon` (tajuk + ikon), `check` (senarai ✓ ditanda ikut percakapan), `chips` (saiz & bulatan warna). Label kecil biru monospace (`01 · SELESA`), tajuk tebal + satu perkataan serif italik biru |
| Garis progress | Garis biru menegak di kiri + label pil biru (`01 Selesa`, `02 Udara`…) turun setiap langkah |
| CTA | Footage digelapkan biru tua, ringkasan ✓ semua kelebihan, butang kuning **"Tekan *beg kuning*"** |
| Warna | Biru `#2F6BFF`, kuning `#FFC93C`, oren `#D97757`, putih, biru tua `rgba(14,22,52,.62)` |

## Automatik dalam `build.py`
- **Potong senyap** > 0.3 s; bahagian dalam `REMOVE` (aaa / emm / okay / ulangan / gagap) dibuang.
- **Punch-in** 1.07 pada setiap jump cut (selang-seli, kepala tak terpotong).
- **Suara utama sahaja**: bunyi latar dibuang (highpass + RNNoise + lowpass), suara −14 LUFS.
- **Video gelap dicerahkan** (purata luma < 105 → `hyperframes media-treatment`).
- **Sound effect**: pop (pil/ikon/chip), whoosh (kad masuk), click (✓, pangkah), sparkle (nama produk), ping (butang CTA).

## Aliran kerja
Gambar frame draf → preview video draf → render akhir selepas diluluskan.

## Fail
- `build.py` — enjin Style 2.
- `projects/` — config setiap video (`boxer.py` contoh, `_template.py` templat).
- `sfx/` — sound effect (pustaka terbina HyperFrames).
- `scripts/download-drive.sh` — muat turun dari Google Drive.
- `scripts/find-fillers.sh`, `scripts/energy.py` — cari "aaa/okay", jeda dan titik potong.
