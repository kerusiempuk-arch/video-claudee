# Laundry Detergent DIY Kit (Drive 1Cy4tc-bkyyC9HIOEmv1PTncvZpmVRxPJ) — Style 3
# Bina: python3 -I styles/style-3/build.py work/new/raw.mp4 styles/style-3/projects/detergent.py work/new/hf

REMOVE = [
    (0.0, 2.62),     # "aa, aku baru dapat ni, aa" — owner: ayat pertama terus "Laundry detergent DIY kit"
    (5.38, 5.74),    # "aa"
    (7.16, 8.16),    # "aa"
    (9.27, 9.79),    # "okey"
    (10.62, 11.02),  # "dia" berulang ("dia, dia dah siap")
    (12.18, 12.42),  # "dia" berulang ("bagi, dia semua")
    (14.62, 14.95),  # "aa"
    (15.66, 16.34),  # "aa"
    (17.60, 18.17),  # "aa"
    (21.45, 21.80),  # "aa"
    (24.05, 26.78),  # "okey" + "nah ya"
    (29.62, 39.38),  # "okey, aa" + "berminat…" pertama + "berminat dengan ... yang tak jadi" (ulangan)
]
SRC_END = 42.5   # buang "apa akan dia bagi…" (tak jelas)
TAIL = 1.9

# Kepala di bahagian atas frame → tajuk, CTA & gradien di BAWAH.
POSITION = "bottom"

END = 22.24
HEADS = [
    dict(start=0.00, end=2.88, kicker="Laundry Detergent", title="DIY Kit."),
    dict(start=2.88, end=5.98, kicker="Cuba sendiri", title="Buat sabun.", pills=[(4.14, "Sabun sendiri")]),
    dict(start=5.98, end=9.14, kicker="Dalam pek", title="Semua ada.", pills=[(7.28, "Semua bahan disediakan")]),
    dict(start=9.14, end=14.44, kicker="Belakang pek · step", big=[(11.44, "1"), (13.80, "6")],
         sub="langkah demi langkah"),
    dict(start=14.44, end=16.84, kicker="Cara buat", title="Sangat senang."),
    dict(start=16.84, end=19.22, kicker="Caranya", title="Campur je.",
         pills=[(16.94, "Campur semua bahan"), (17.74, "Dalam baldi saja")]),
]
IMAGES = [  # screenshot listing dari owner (crop: scripts/crop-listing.py)
    dict(src="work/new/img/p2.jpg", start=3.11, end=5.91),    # 1 set 15–16 liter, sabun siap dibancuh
    dict(src="work/new/img/p1.jpg", start=6.21, end=9.07),    # kuasa cucian lebih kuat
    dict(src="work/new/img/p3.jpg", start=14.57, end=16.77),  # buih melimpah
    dict(src="work/new/img/p4.jpg", start=16.97, end=19.17),  # bancuh sendiri di rumah (langkah)
]
CTA = dict(start=19.22, text="Beli di beg kuning")
