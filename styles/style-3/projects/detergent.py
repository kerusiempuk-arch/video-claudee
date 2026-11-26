# Laundry Detergent DIY Kit (Drive 1Cy4tc-bkyyC9HIOEmv1PTncvZpmVRxPJ) — Style 3
# Bina: python3 -I styles/style-3/build.py work/new/raw.mp4 styles/style-3/projects/detergent.py work/new/hf

REMOVE = [
    (0.0, 2.62),     # "aa, aku baru dapat ni, aa" — owner: ayat pertama terus "Laundry detergent DIY kit"
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

END = 24.46
HEADS = [
    dict(start=0.0, end=2.88, kicker="Laundry Detergent", title="DIY Kit."),
    dict(start=2.88, end=5.98, kicker="Cuba sendiri", title="Buat sabun.", pills=[(4.14, "Sabun sendiri")]),
    dict(start=5.98, end=9.78, kicker="Dalam pek", title="Semua ada.", pills=[(7.92, "Semua bahan disediakan")]),
    dict(start=9.78, end=15.08, kicker="Belakang pek · step", big=[(12.08, "1"), (14.44, "6")],
         sub="langkah demi langkah"),
    dict(start=15.08, end=17.48, kicker="Cara buat", title="Sangat senang."),
    dict(start=17.48, end=19.86, kicker="Caranya", title="Campur je.",
         pills=[(17.58, "Campur semua bahan"), (18.38, "Dalam baldi saja")]),
]
IMAGES = [  # screenshot listing dari owner (crop: scripts/crop-listing.py)
    dict(src="work/new/img/p2.jpg", start=3.11, end=5.91),    # 1 set 15–16 liter, sabun siap dibancuh
    dict(src="work/new/img/p1.jpg", start=6.21, end=9.71),    # kuasa cucian lebih kuat
    dict(src="work/new/img/p3.jpg", start=15.21, end=17.41),  # buih melimpah
    dict(src="work/new/img/p4.jpg", start=17.61, end=19.81),  # bancuh sendiri di rumah (langkah)
]
CTA = dict(start=19.86, text="Beli di beg kuning")
