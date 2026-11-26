# Laundry Detergent DIY Kit (Drive 1Cy4tc-bkyyC9HIOEmv1PTncvZpmVRxPJ) — Style 3
# Bina: python3 -I styles/style-3/build.py work/new/raw.mp4 styles/style-3/projects/detergent.py work/new/hf

REMOVE = [
    (0.0, 0.80),     # "aa"
    (1.72, 2.62),    # "aa"
    (5.38, 5.74),    # "aa"
    (7.16, 8.16),    # "aa"
    (9.27, 9.79),    # "okey"
    (14.62, 14.95),  # "aa"
    (15.66, 16.34),  # "aa"
    (17.60, 18.17),  # "aa"
    (21.45, 21.80),  # "aa"
    (24.05, 26.78),  # "okey" + "nah ya"
    (29.62, 39.38),  # "okey, aa" + "berminat…" pertama + "berminat dengan ... yang tak jadi" (ulangan)
]
SRC_END = 44.3
TAIL = 1.9

# Kepala di bahagian atas frame → tajuk, CTA & gradien di BAWAH.
POSITION = "bottom"

END = 25.38
HEADS = [
    dict(start=0.0, end=3.80, kicker="Baru sampai", title="DIY Kit.", pills=[(1.71, "Laundry detergent")]),
    dict(start=3.80, end=6.90, kicker="Cuba sendiri", title="Buat sabun.", pills=[(5.06, "Sabun sendiri")]),
    dict(start=6.90, end=10.70, kicker="Dalam pek", title="Semua ada.", pills=[(8.84, "Semua bahan disediakan")]),
    dict(start=10.70, end=16.00, kicker="Belakang pek · step", big=[(13.00, "1"), (15.36, "6")],
         sub="langkah demi langkah"),
    dict(start=16.00, end=18.40, kicker="Cara buat", title="Sangat senang."),
    dict(start=18.40, end=20.78, kicker="Caranya", title="Campur je.",
         pills=[(18.50, "Campur semua bahan"), (19.30, "Dalam baldi saja")]),
]
IMAGES = []   # tiada gambar produk diberi
CTA = dict(start=20.78, text="Beli di beg kuning")
# Cover: python3 -I tools/cover/make_cover.py work/new/raw.mp4 34 work/new/cover.png --style 3 --title "Laundry Detergent." \
#   --kicker "DIY Kit · Buat sabun sendiri" --pills "Semua bahan ada,Step 1–6,Sangat senang" --pos bottom --y 760
