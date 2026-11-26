# Beg terapi garam (Drive 13I5wAe24-5bTfD5j3INOjSfojUI138vq) — Style 3
# Bina: python3 -I styles/style-3/build.py work/new3/raw.mp4 styles/style-3/projects/garam.py work/new3/hf

REMOVE = [
    (0.0, 0.40),     # "aa"
    (1.98, 2.80),    # "okey"
    (3.30, 3.79),    # "aa"
    (4.70, 5.66),    # "aa, ni kat zip ni" (gagap)
    (6.26, 6.99),    # "ni, aa, dia"
    (7.83, 8.76),    # "dah pek" (ulangan)
    (10.39, 10.69),  # "aa"
    (12.40, 13.35),  # "okey, aa"
    (15.58, 17.32),  # "pelak dia aa ni" (ulangan)
    (20.20, 21.91),  # "okey, kita boleh nak kontrol" (ulangan)
    (26.09, 26.87),  # "okey, aa"
    (28.85, 30.20),  # "aku letak, okey"
    (35.89, 38.20),  # "okey, macam ni. okey"
    (39.70, 40.41),  # "okey"
    (44.40, 50.00),  # take pertama "dengan adanya ni ... tak panas" (ulang di 50.0)
    (53.75, 54.05),  # "okey"
    (59.50, 59.71),  # "okey"
]
SRC_END = 65.8
TAIL = 1.9

# Kepala di bahagian atas frame → tajuk, CTA & gradien di BAWAH.
POSITION = "bottom"

END = 39.46
HEADS = [
    dict(start=0.0, end=2.0, kicker="Ini dia", title="Beg terapi garam."),
    dict(start=2.0, end=7.1, kicker="Dalam dia", title="Isi garam.",
         pills=[(2.98, "Zip · dah packing"), (4.35, "Kemas · cantik"), (5.9, "Tutup je zip")]),
    dict(start=7.1, end=14.49, kicker="Siap ada plug", title="Boleh kontrol.",
         pills=[(11.19, "Suhu"), (12.65, "Berapa lama nak pakai")]),
    dict(start=14.49, end=21.0, kicker="Cara pakai", title="Letak je.",
         pills=[(16.9, "Kat bahu · sambil baring"), (19.07, "Kat belakang")]),
    dict(start=21.0, end=22.24, kicker="Rasa dia", title="Sangat selesa."),
    dict(start=22.24, end=25.9, kicker="Orang dulu-dulu", title="Panaskan garam.",
         pills=[(23.57, "Terapi garam")]),
    dict(start=25.9, end=29.6, kicker="Dengan beg ni", title="Tak payah lagi.",
         pills=[(28.29, "Panaskan garam")]),
    dict(start=29.6, end=33.56, kicker="Cuma", title="Sambung plug.",
         pills=[(32.25, "Boleh kontrol")]),
    dict(start=33.56, end=37.18, kicker="Membantu", title="Aliran darah.",
         pills=[(34.55, "Lancarkan peredaran")]),
]
IMAGES = [  # screenshot listing owner (crop-listing.py)
    dict(src="work/new3/img/p1.jpg", start=0.2, end=2.0),     # Pemanas bahu & leher
    dict(src="work/new3/img/p3.jpg", start=8.5, end=11.9),    # alat kawalan
    dict(src="work/new3/img/p2.jpg", start=17.0, end=20.7),   # cara pakai (bahu & belakang)
    dict(src="work/new3/img/p4.jpg", start=22.4, end=25.8),   # garam / tradisional
]
CTA = dict(start=37.18, text="Beli di beg kuning")
