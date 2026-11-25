# Style 1 — "Product Explainer" (gaya UI moden)

Dirender dengan **HyperFrames** (HTML → MP4): `build.py` + config projek → projek HyperFrames → `hyperframes render`.

Rujukan asal: video facemask "lawak." (Drive `1F89dXsFD8GCP3JTsKQYwjflXe1zwCAkW`).
Contoh siap: `styles/style-1/projects/boxer.py` (boxer lelaki — versi yang diluluskan user).

## Struktur video
| Bahagian | Apa | Bila |
|---|---|---|
| **Hook** | kicker kecil (cth. "seluar dalam lelaki paling") + tajuk besar 1 perkataan bold hitam + **titik merah** (cth. "selesa."). Kad gelap gaya tetingkap macOS (titik merah/kuning/hijau + nama produk) dengan 2 pilihan `01`/`02` — pilihan bertukar biru tepat bila perkataan itu disebut (`select_at` ikut masa sebenar) | sepanjang ayat pembuka (~3–6s); **boleh dipanjangkan (cth. ~8s)** supaya kedua-dua pilihan sempat disebut — `HOOK.end` = hujung ayat yang sebut pilihan ke-2 |
| **Kelebihan 1/3, 2/3, 3/3** | progress bar biru nipis di atas + label monospace gelap `kelebihan 1 / 3` (nombor biru) + subtajuk pendek. Sticker putih condong sikit, bertindan ke bawah (kiri atas), keluar tepat bila disebut. Bulatan biru + label untuk tunjuk bahagian produk (pilihan) | ikut isi percakapan |
| **CTA** | tajuk besar ulang (cth. "selesa.") + kad gelap: nama produk, tag monospace `a · b · c` (**maks 3 tag, 1–2 perkataan setiap satu** — supaya tak terkeluar kad), butang. TikTok Shop → butang **kuning "Tekan bakul kuning ↓"** (teks gelap). Lain-lain → merah "Link dekat bawah ↓" | ~2s terakhir, simpan ~1.2s hujung untuk dibaca (`TAIL = 1.2`). Nama produk panjang → font kad mengecil sendiri |

## Kapsyen
- Ikut suara, **1–3 perkataan** satu masa, muncul ikut masa sebenar setiap perkataan (Whisper).
- Putih, Inter Bold 60, bayang lembut + outline nipis gelap.
- **Kedudukan: ATAS, paras dada, `CAPTION_Y = 680`** (pilihan user, video Tai Chi) — di bawah sticker/tajuk, tak tutup muka.
  Semak stills: kalau masih kena dagu/mulut, turunkan sikit (700–760). Projek lama (boxer, perancah) kekal 1780.
- Kata kunci diwarnakan: biru-ungu `(110,123,255)` secara default; **kuning `(255,212,59)` automatik** bila baju/latar biru di paras kapsyen (`build.py` kira piksel biru ≥ 15 %, cetak keputusannya). Paksa dengan `CAPTION_ACCENT = (…)` dalam config projek.

## Potongan (wajib setiap video)
- Buang **senyap > 0.3s** (auto, `build.py`).
- Buang **"aaa", "eh", "emm", "okay"** — semua filler.
- Bunyi pendek perlahan antara ayat ("ha", "okay" 0.1–0.3s) selalunya **tak dikesan** bila transkrip video asal (bising).
  Selepas `--cut-audio`, transkrip **suara bersih** dengan `--keep`: setiap `[FILLER]` dicetak bersama `REMOVE ≈ (asal_a, asal_b)` — masukkan dalam `REMOVE`, ulang sampai tiada filler.
- Buang **ulangan / gagap / ayat tak habis** — simpan sebutan TERAKHIR yang lengkap.
- **Ayat penutup/CTA diulang beberapa kali** ("berminat dengan … ni" ×3, "dapatkan" tak habis) → buang SEMUA cubaan awal dengan satu `REMOVE`, simpan hanya take terakhir yang lengkap sampai "… beg/bakul kuning".
- Setiap jump cut tukar zoom (punch-in 1.08) supaya nampak sengaja.
- Potong hujung bila orang keluar frame / kamera jatuh.

## Bunyi: suara utama sahaja (wajib)
- Bunyi latar yang tak perlu (angin, kipas, jalan raya, dengung, bunyi lain) **dibuang** — auto dalam `build.py`:
  highpass 80 Hz → RNNoise (`arnndn`) → lowpass 12 kHz → −14 LUFS. Video dibisukan; suara bersih main sebagai trek sendiri.
- Kalau masih ada bunyi lain yang kuat (muzik, orang lain bercakap), potong bahagian itu atau tanya user.

## Kecerahan (wajib)
- Video **gelap mesti dicerahkan**. `build.py` ukur purata luma (YAVG 0–255); bawah **105** → exposure/shadows dinaikkan
  melalui `hyperframes media-treatment` (exposure = (118 − YAVG)/85, had 0.15–0.8).
- Semak gambar frame: masih gelap atau terlalu putih → tetapkan `BRIGHTEN = {"exposure": …, "shadows": …, "blacks": …}` dalam config; `BRIGHTEN = None` untuk matikan.

## Visual lain
- Gradient putih lembut di atas (supaya tajuk gelap jelas), zoom perlahan 4–5% sepanjang video.
- Warna: hitam `INK`, putih, biru `BLUE (66,99,235)`, merah `RED (229,72,77)`.
- Font: Inter (Bold/Display Bold/SemiBold/Medium) + JetBrains Mono — dalam `fonts/`.

## Sound effect (auto)
whoosh = tajuk & setiap seksyen · click = pilihan kad bertukar · pop = sticker/bulatan · ding = kad CTA.
Bunyi sintetik (`sfx.py`, fail `.wav` dalam `sfx/`), bebas hak cipta, volume di bawah suara.

## Aliran kerja
1. Preview (render **draft**, tanpa watermark) → hantar ke user, senaraikan apa yang dipotong & teks yang perlu disemak.
2. Tunggu user cakap **"okay render"** → render final 1080×1920 (`hyperframes render -q high`).
