# <Nama produk> (Drive <ID>) — salin fail ni, isi ikut video. Contoh lengkap: styles/style-3/projects/boxer.py
# Bina: python3 -I styles/style-3/build.py <raw.mp4> <fail ini> <work_dir>   (--plan / --cut-audio <wav>)

# --- potongan, masa ikut video ASAL. Senyap > 0.3 s dipotong automatik.
REMOVE = [
    # (mula, tamat),  # "aaa" / "emm" / "okay" / ulangan pertama / gagap / ayat tak habis
]
SRC_END = 99.0        # ~0.6 s+ selepas perkataan terakhir supaya CTA >= 2 s di skrin; potong SEBELUM orang jalan keluar frame
TAIL = 1.9            # hujung tak dipotong senyap — masa baca CTA
# PUNCH = 1.07        # punch-in segmen selang-seli
# BRIGHTEN = "auto"   # atau {"exposure": 0.4, "shadows": 0.25, "blacks": 0.08}; None = matikan
# DENOISE = True
# POSITION = "top"   # "bottom" bila kepala di atas frame (tajuk tutup muka) → tajuk, CTA & gradien di bawah (contoh projects/extension.py)
# HEAD_Y = 190        # atas label kecil (bottom: 1240); IMG_TOP = 470 (bottom: 190); IMG_W = 1000

# --- overlay, masa ikut video SELEPAS dipotong (transkripsi cut.wav dari --cut-audio). TIADA subtitle bawah.
END = 0.0             # dari --plan
HEADS = [  # satu tajuk setiap idea, bersambung tanpa jurang; tajuk pendek 1–3 perkataan + titik
    # dict(start=0.0, end=, kicker="Setiap hari", title="Lain warna.", pills=[(<bila disebut>, "Ahad · Hijau"), ...]),
    # dict(start=, end=, kicker="Penyelesaian", title="<Produk>."),          # + kad gambar dalam IMAGES
    # dict(start=, end=, kicker="Saiz · hingga", big=[(<t>, "3XL"), (<t>, "5XL")], sub="ikut saiz yang korang pakai"),
    # dict(start=, end=, kicker="Nak jimat", big=[(<t>, "2×"), (<t>, "3×")], sub="beli combo terus.", line=True),
    # JANGAN reka fakta (saiz, harga, warna) – hanya apa yang disebut
]
IMAGES = [  # gambar produk dari owner (screenshot listing → scripts/crop-listing.py), dalam work/<nama>/img/
    # dict(src="work/<nama>/img/p1.png", start=, end=),
]
CTA = dict(start=0, text="Beli di beg kuning")
# EXTRA_SFX = [(masa, "pop"|"whoosh-short"|"click"|"sparkle"|"ping", volume), ...]
