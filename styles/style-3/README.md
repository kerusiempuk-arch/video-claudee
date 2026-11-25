# Style 3 — Tajuk atas / product talking head (TikTok, 9:16)

Cara guna: beri Claude **link Google Drive** video mentah dan cakap **"edit style 3"** (hantar sekali gambar produk jika mahu kad gambar).
Claude ikut `.claude/skills/edit-style-3/SKILL.md`. Dirender dengan **HyperFrames** melalui `build.py`:
video mentah + config projek (`projects/<nama>.py`) → projek HyperFrames → `hyperframes render`.

Rujukan: video boxer (Drive `1hHKM5lkYPdj2YYQVw6qiHSPtgzrcHYP5`), dibina semula dalam `projects/boxer.py`. Templat: `projects/_template.py`.

## Rupa
| Elemen | Gaya |
|---|---|
| Format | Menegak 1080×1920, 30 fps, font **Plus Jakarta Sans** (`fonts/`) |
| Gradien | Gelap lembut di atas (0–820 px) sepanjang video supaya tajuk putih jelas |
| Tajuk (`HEADS`) | Tengah atas, atas kepala: **label kecil** huruf besar berjarak (`S E T I A P  H A R I`, 28 px) + **tajuk besar bertitik** (800, 96 px, "Lain warna."). Tukar setiap ayat/idea. Masuk blur→tajam, keluar tajam→blur |
| Pil | Pil putih teks hitam di bawah tajuk, muncul satu-satu bila disebut ("Ahad · Hijau", "Tak tulis brand") |
| Nombor besar | Ganti tajuk dengan nilai besar (210 px) yang bertukar ikut suara: "3XL → 5XL", "2× → 3×" + ayat kecil + (pilihan) garis hijau |
| Kad gambar produk (`IMAGES`) | Gambar listing produk bucu bulat di tengah (lebar 1000 px), footage di belakang blur + digelapkan |
| CTA | Pil kuning **"Beli di beg kuning"** di atas + anak panah ⌄⌄ kuning melantun, hingga tamat |
| Subtitle | **Tiada subtitle bawah** (arahan owner) |
| Warna | Putih, kuning `#FFD21F`, hijau `#22C55E`, gelap `#12141A` |

## Struktur biasa
Hook (masalah/situasi + pil) → masalah → **Penyelesaian** (nama produk + kad gambar) → kelebihan (satu tajuk setiap satu, pil untuk butiran) → saiz (nombor besar) → combo/jimat (nombor besar) → CTA.

## Automatik dalam `build.py`
- **Potong senyap** > 0.3 s; bahagian dalam `REMOVE` (aaa / emm / okay / ulangan / gagap) dibuang.
- **Punch-in** 1.07 pada setiap jump cut (selang-seli, kepala tak terpotong).
- **Suara utama sahaja** (highpass + RNNoise + lowpass), −14 LUFS.
- **Video gelap dicerahkan** (purata luma < 105 → `hyperframes media-treatment`).
- **Sound effect**: whoosh (tajuk baru), pop (pil), click (nombor bertukar), sparkle (kad gambar), ping (CTA).

## Aliran kerja
Gambar frame draf → preview video draf → render akhir selepas diluluskan.

## Fail
- `build.py` — enjin Style 3.
- `projects/` — config setiap video (`boxer.py` contoh, `_template.py` templat).
- `fonts/` — Plus Jakarta Sans (OFL). `sfx/` — sound effect.
- `scripts/download-drive.sh`, `scripts/find-fillers.sh`, `scripts/energy.py` — muat turun, cari "aaa/okay", jeda dan titik potong.
