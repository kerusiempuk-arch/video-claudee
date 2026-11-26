# Laundry Detergent DIY Kit (Drive 1Cy4tc-bkyyC9HIOEmv1PTncvZpmVRxPJ) — Style 3
# Bina: python3 -I styles/style-3/build.py work/new/raw.mp4 styles/style-3/projects/detergent.py work/new/hf

REMOVE = [
    (0.0, 0.80),     # "aa"
    (1.72, 2.62),    # "aa"
    (3.95, 5.74),    # "DIY kit" (owner: buang) + "aa"
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

END = 23.95
HEADS = [
    dict(start=0.0, end=2.37, kicker="Baru sampai", title="DIY Kit.", pills=[(1.71, "Laundry detergent")]),
    dict(start=2.37, end=5.47, kicker="Cuba sendiri", title="Buat sabun.", pills=[(3.63, "Sabun sendiri")]),
    dict(start=5.47, end=9.27, kicker="Dalam pek", title="Semua ada.", pills=[(7.41, "Semua bahan disediakan")]),
    dict(start=9.27, end=14.57, kicker="Belakang pek · step", big=[(11.57, "1"), (13.93, "6")],
         sub="langkah demi langkah"),
    dict(start=14.57, end=16.97, kicker="Cara buat", title="Sangat senang."),
    dict(start=16.97, end=19.35, kicker="Caranya", title="Campur je.",
         pills=[(17.07, "Campur semua bahan"), (17.87, "Dalam baldi saja")]),
]
IMAGES = [  # screenshot listing dari owner (crop: scripts/crop-listing.py)
    dict(src="work/new/img/p2.jpg", start=2.60, end=5.40),    # 1 set 15–16 liter, sabun siap dibancuh
    dict(src="work/new/img/p1.jpg", start=5.70, end=9.20),    # kuasa cucian lebih kuat
    dict(src="work/new/img/p3.jpg", start=14.70, end=16.90),  # buih melimpah
    dict(src="work/new/img/p4.jpg", start=17.10, end=19.30),  # bancuh sendiri di rumah (langkah)
]
CTA = dict(start=19.35, text="Beli di beg kuning")
