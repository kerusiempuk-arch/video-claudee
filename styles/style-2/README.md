# Style 2 — Talking head / review produk (TikTok, 9:16)

Cara guna: beri Claude **link Google Drive** video dan cakap **"edit style 2"**.
Claude akan ikut arahan dalam `.claude/skills/edit-style-2/SKILL.md`.

Contoh rujukan: video review boxer (`reference-project/`).

## Rupa
| Elemen | Gaya |
|---|---|
| Format | Menegak 1080×1920, 30 fps |
| Caption | Satu baris di **dada** (bawah dagu), Inter 700 56 px putih atas jalur gelap lut sinar; perkataan muncul satu-satu ikut suara (karaoke). Kata kunci: **kotak putih** atau *serif italik* (Playfair Display) |
| Hook | Pil putih "✳ review **topik**" dalam 3 saat pertama |
| Kad kelebihan | Kad putih bucu bulat di bahagian **bawah** (atas kaki, tak tutup muka/produk). Label kecil biru monospace (`01 · SELESA`), tajuk tebal + satu perkataan serif italik biru, ikon atau senarai ✓ |
| Garis progress | Garis biru menegak di kiri + label pil biru (`01 Selesa`, `02 Udara`…) turun setiap langkah |
| CTA | Footage digelapkan biru tua, ringkasan ✓ semua kelebihan, butang kuning **"Tekan *beg kuning*"** |
| Warna | Biru `#2F6BFF`, kuning `#FFC93C`, oren `#D97757`, putih, biru tua `rgba(14,22,52,.62)` |

## Suntingan (wajib)
- Buang **"aaa", "emm", "okay"**, perkataan **berulang** dan **gagap**.
- Jeda senyap > 0.3 s dipendekkan ke ~0.1 s.
- **Suara utama sahaja**: bunyi latar dibuang (`scripts/clean-voice.sh`, RNNoise), suara −14 LUFS.
- **Video gelap dicerahkan** (`scripts/brightness.sh` → `hyperframes media-treatment`).
- Setiap jump cut disilih dengan **punch-in** kecil (zoom 1.07, kepala tak terpotong).
- **Sound effect**: whoosh (kad masuk), pop (pil/ikon/chip), click (✓), sparkle (nama produk), ping (butang CTA).
- Gambar frame draf → preview video draf → render akhir selepas diluluskan.

## Fail
- `reference-project/` — projek HyperFrames penuh (tanpa video sumber) untuk disalin.
- `reference-project/assets/sfx/` — sound effect (pustaka terbina HyperFrames).
- `scripts/download-drive.sh` — muat turun dari Google Drive.
- `scripts/find-fillers.sh`, `scripts/energy.py` — cari "aaa/okay", jeda dan titik potong.
- `scripts/segments.mjs` — jana segmen video (dan suara bersih dengan `--voice`) selepas potongan + peta masa.
- `scripts/clean-voice.sh` — buang bunyi latar, kekalkan suara utama.
- `scripts/brightness.sh` — ukur kecerahan dan cadang patch kalau gelap.
- `scripts/gen-captions.mjs` — jana caption karaoke dari `transcript.json` + `captions.config.json`.
