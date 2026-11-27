# Style 1 — "Product Explainer" (gaya UI moden)

Dirender dengan **HyperFrames** (HTML → MP4): `build.py` + config projek → projek HyperFrames → `hyperframes render`.

Rujukan asal: video facemask "lawak." (Drive `1F89dXsFD8GCP3JTsKQYwjflXe1zwCAkW`).
Contoh siap: `styles/style-1/projects/boxer.py` (boxer lelaki — versi yang diluluskan user).

## Struktur video
| Bahagian | Apa | Bila |
|---|---|---|
| **Hook** | kicker kecil (cth. "seluar dalam lelaki paling") + tajuk besar 1 perkataan bold hitam + **titik merah** (cth. "selesa."). Kad gelap gaya tetingkap macOS (titik merah/kuning/hijau + nama produk) dengan **2 atau 3 pilihan** (3 pilihan bila ayat pembuka sebut 3 perkara — cth. "kapal / superhero / gabung mainan lain", kad sampai ~7s) `01`/`02`/`03` (kad tinggi sendiri ikut bilangan pilihan) — pilihan bertukar biru tepat bila perkataan itu disebut (`select_at` ikut masa sebenar) | sepanjang ayat pembuka (~3–6s); **boleh dipanjangkan (cth. ~8s)** supaya kedua-dua pilihan sempat disebut — `HOOK.end` = hujung ayat yang sebut pilihan ke-2 |
| **Kelebihan 1/3, 2/3, 3/3** | progress bar biru nipis di atas + label monospace gelap `kelebihan 1 / 3` atau **`tip 1 / 3`** (video tip / cara guna) (nombor biru) + subtajuk pendek. Sticker putih condong sikit, bertindan ke bawah (kiri atas), keluar tepat bila disebut. Senarai pendek yang disebut berturut (cth. "tak koyak / tak bocor / tak basah ✓") → **3 tingkat** y 260 / 340 / 420, sudut berselang 2 / −1.5 / 1.5. Bulatan biru + label untuk tunjuk bahagian produk (pilihan) | ikut isi percakapan |
| **CTA** | tajuk besar — **utamakan perkataan yang disebut di hujung video** (cth. "murah." bila dia kata "harga sangat murah"), kalau tiada baru ulang tajuk hook (cth. "selesa.") + kad gelap: nama produk, tag monospace `a · b · c` (**maks 3 tag, 1–2 perkataan setiap satu** — supaya tak terkeluar kad), butang. TikTok Shop → butang **kuning "Tekan beg kuning ↓"** (teks gelap). Lain-lain → merah "Link dekat bawah ↓" | ~2s terakhir, simpan ~1.2s hujung untuk dibaca (`TAIL = 1.2`). Nama produk panjang → font kad mengecil sendiri |

## Kapsyen
- **Tanpa kapsyen**: `CAPTIONS = []` (cth. video sabun – owner minta buang subtitle tengah).
- Ikut suara, **1–3 perkataan** satu masa, muncul ikut masa sebenar setiap perkataan (Whisper).
- Putih, Inter Bold 60, bayang lembut + outline nipis gelap.
- **Kedudukan: ATAS, paras dada, `CAPTION_Y = 680`** (pilihan user, video Tai Chi) — di bawah sticker/tajuk, tak tutup muka.
  Semak stills: kalau masih kena dagu/mulut, turunkan sikit (700–760 — cth. orang duduk tapi muka masih tinggi: 760, video sarung telefon); kalau muka rendah dalam frame (orang duduk, kamera tinggi), turunkan ke dada `CAPTION_Y = 900` (video kain lap dapur). Projek lama (boxer, perancah) kekal 1780.
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
- Video **gelap mesti dicerahkan**. `build.py` ukur purata luma (YAVG 0–255); bawah **100** (`DARK_Y`) → exposure/shadows dinaikkan
  melalui `hyperframes media-treatment` (exposure = (118 − YAVG)/85, had 0.15–0.8).
- Semak gambar frame: masih gelap atau terlalu putih → tetapkan `BRIGHTEN = {"exposure": …, "shadows": …, "blacks": …}` dalam config; `BRIGHTEN = None` untuk matikan.

## Plate nombor kenderaan (wajib tutup)
- Kalau plate kereta/lori/pikap nampak dalam footage, **kaburkan dulu** sebelum `build.py`:
  `.venv-style1/bin/python -I styles/style-1/tools/blur_plate.py <raw.mp4> <raw_noplate.mp4> --ref <saat plate jelas> --box x,y,w,h`
  (kotak huruf plate, piksel 1080×1920). Plate diikut dengan padanan templat + gerakan kamera; plate separuh di tepi frame
  → tambah `--anchor saat:x,y,w,h`. Lihat `--check check.jpg` dan semak setiap 0.2 s bila plate masuk/keluar frame.
- Guna `raw_noplate.mp4` sebagai RAW untuk `build.py` dan `cover.py`. Rujukan: `projects/bar_ratchet.py`.

## Bahagian "masalah" sebelum kelebihan (bila video banding produk biasa vs produk ni)
- Bila pembuat video sebut masalah produk biasa (cth. lighter gas: "habis gas, buang", "angin, tangan basah, api tak hidup"),
  letak **3 sticker masalah** (`STICKERS`, x 50/80/110, y 260/340/420) bertanda **✗** pada masa ia disebut — **sebelum** `SECTIONS` bermula.
- Dalam seksyen kelebihan yang menjawab masalah itu, ulang perkara sama dengan **✓** (cth. "tangan basah ✓", "tahan angin ✓").
- Teks hanya dari apa yang disebut. Rujukan: `projects/lighter.py`.

## Visual lain
- **Perkataan besar sekejap** di tengah video (`BIG_WORDS = [(mula, tamat, "berbuih", True)]`, `True` = titik merah): hitam bold 170px di atas (y ≈ 340), bunyi whoosh/drop automatik. Letak bila tiada sticker supaya tak bertindih (rujukan: video rak besi "store", "4 layer", "ngam.").
- **Kad hook** default `CARD_Y = 1420` (lebih rendah) supaya produk yang dipegang tak tertutup — semak stills, naikkan kalau kad tutup produk di bawah.
- Gradient putih lembut di atas (supaya tajuk gelap jelas), zoom perlahan 4–5% sepanjang video.
- Warna: hitam `INK`, putih, biru `BLUE (66,99,235)`, merah `RED (229,72,77)`.
- Font: Inter (Bold/Display Bold/SemiBold/Medium) + JetBrains Mono — dalam `fonts/`.

## Sound effect (auto)
whoosh = tajuk & setiap seksyen (atau `SFX_WHOOSH = "drop"` → titisan air, sesuai produk air/dapur) · click = pilihan kad bertukar · pop = sticker/bulatan · ding = kad CTA.
Bunyi sintetik (`sfx.py`, fail `.wav` dalam `sfx/`), bebas hak cipta, volume di bawah suara.

## Cover photo (wajib selepas render akhir)
`tools/cover.py` jana cover TikTok 1080×1920 PNG daripada `COVERS` dalam config projek (contoh: `projects/sabun.py`):
- Atas putih (gradient Style 1): kicker kecil + **tajuk besar + titik merah** (cth. "senang.").
- Gambar dari video **diturunkan** (`shift` 330px) supaya tajuk tak tutup muka; pilih frame muka + produk jelas (`at` = masa video ASAL).
- 2 sticker putih condong di kiri (y ≈ 1060) — ayat dari apa yang **disebut** dalam video, jangan reka dakwaan.
- Pil monospace gelap di bawah (cth. "tip 1-3 · cara cuci senang", nombor biru) — label ikut `SECTIONS`: video "kelebihan" → "kelebihan 1-3 · …", video tip → "tip 1-3 · …".
- Pil boleh juga guna **nama produk** selepas titik: "kelebihan 1-3 · <Nama Produk>" (video mainan Ninjago).
- Frame suram dicerahkan sendiri. Buat **2 pilihan** (cth. A = produk + muka, B = hasil) dan biar owner pilih.
- **Video tanpa muka** (tangan pegang produk sahaja): A = produk penuh dari frame paling tajam, B = sudut/binaan lain + kicker dari ayat lain (cth. "ganti telefon & TV,"). Rujukan: `projects/ninja.py`.

## Aliran kerja
1. Preview (render **draft**, tanpa watermark) → hantar ke user, senaraikan apa yang dipotong & teks yang perlu disemak.
2. Tunggu user cakap **"okay render"** → render final 1080×1920 (`hyperframes render -q high`).
3. Cover photo: `python3 -I styles/style-1/tools/cover.py <raw.mp4> projects/<nama>.py <out_dir>` → hantar cover.png + cover2.png.
