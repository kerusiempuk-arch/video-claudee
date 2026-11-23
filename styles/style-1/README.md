# Style 1 — "Product Explainer" (gaya UI moden)

Rujukan asal: video facemask "lawak." (Drive `1F89dXsFD8GCP3JTsKQYwjflXe1zwCAkW`).
Contoh siap: `styles/style-1/projects/boxer.py` (boxer lelaki — versi yang diluluskan user).

## Struktur video
| Bahagian | Apa | Bila |
|---|---|---|
| **Hook** | kicker kecil (cth. "seluar dalam lelaki paling") + tajuk besar 1 perkataan bold hitam + **titik merah** (cth. "selesa."). Kad gelap gaya tetingkap macOS (titik merah/kuning/hijau + nama produk) dengan 2 pilihan `01`/`02` — pilihan bertukar biru tepat bila perkataan itu disebut | ayat pembuka, ~3–5s |
| **Kelebihan 1/3, 2/3, 3/3** | progress bar biru nipis di atas + label monospace gelap `kelebihan 1 / 3` (nombor biru) + subtajuk pendek. Sticker putih condong sikit, bertindan ke bawah (kiri atas), keluar tepat bila disebut. Bulatan biru + label untuk tunjuk bahagian produk (pilihan) | ikut isi percakapan |
| **CTA** | tajuk besar ulang (cth. "selesa.") + kad gelap: nama produk, tag monospace `a · b · c`, butang. TikTok Shop → butang **kuning "Tekan bakul kuning ↓"** (teks gelap). Lain-lain → merah "Link dekat bawah ↓" | ~2s terakhir, simpan ~0.7s hujung untuk dibaca |

## Kapsyen
- Ikut suara, **1–3 perkataan** satu masa, muncul ikut masa sebenar setiap perkataan (Whisper).
- Putih, Inter Bold 60, bayang lembut + outline nipis gelap.
- **Kedudukan: BAWAH, `CAPTION_Y = 1780`** (pilihan user — jangan letak tengah).
- Kata kunci diwarnakan: biru-ungu `(110,123,255)` secara default; **kuning `(255,212,59)`** bila latar/baju biru (contoh boxer).

## Potongan (wajib setiap video)
- Buang **senyap > 0.3s** (auto, `cut.py`).
- Buang **"aaa", "eh", "emm", "okay"** — semua filler.
- Buang **ulangan / gagap / ayat tak habis** — simpan sebutan TERAKHIR yang lengkap.
- Setiap jump cut tukar zoom (punch-in 1.08) supaya nampak sengaja.
- Potong hujung bila orang keluar frame / kamera jatuh.

## Visual lain
- Gradient putih lembut di atas (supaya tajuk gelap jelas), zoom perlahan 4–5% sepanjang video.
- Warna: hitam `INK`, putih, biru `BLUE (66,99,235)`, merah `RED (229,72,77)`.
- Font: Inter (Bold/Display Bold/SemiBold/Medium) + JetBrains Mono — dalam `fonts/`.

## Sound effect (auto)
whoosh = tajuk & setiap seksyen · click = pilihan kad bertukar · pop = sticker/bulatan · ding = kad CTA.
Bunyi sintetik (`sfx.py`), bebas hak cipta, volume di bawah suara. Suara dinormalkan −14 LUFS.

## Aliran kerja
1. Preview **540p tanpa watermark** → hantar ke user, senaraikan apa yang dipotong & teks yang perlu disemak.
2. Tunggu user cakap **"okay render"** → render final 1080×1920 (`engine.py` tanpa `--preview`).
