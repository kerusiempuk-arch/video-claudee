# Beg guni corak petak (Drive 13UP8lAA3jmCilSZnodOEbj9PlJ_5Z8y0) — Style 3
# Bina: python3 -I styles/style-3/build.py work/v1/raw.mp4 styles/style-3/projects/beg.py work/v1/hf

REMOVE = [
    (0.00, 18.32),   # pra-rakaman: bunyi latar / bersedia / "boleh"
    (22.97, 24.25),  # "aa ni"
    (29.72, 30.25),  # "aa"
    (31.45, 31.96),  # "aa"
    (34.80, 35.30),  # "aa"
    (37.90, 38.21),  # "aa"
    (39.95, 44.35),  # "bag ni sangat besar" (ulang) + "cara nak"
    (47.75, 48.19),  # "aa"
    (50.10, 50.62),  # "okay"
    (52.55, 53.40),  # "okay, aa"
    (55.70, 56.25),  # "okay"
]
SRC_END = 62.25
TAIL = 1.9

# Muka dalam jalur tajuk atas (y ~190–560) hampir sepanjang video → tajuk, CTA & gradien di BAWAH.
POSITION = "bottom"

END = 33.36
HEADS = [
    dict(start=0.0, end=4.45, kicker="Sekarang ni", title="Tiada plastik.",
         pills=[(1.32, "Pergi pasar raya"), (3.13, "Plastik tak disediakan")]),
    dict(start=4.45, end=9.75, kicker="Beg guni", title="Senang.",
         pills=[(5.40, "Letak dalam kereta"), (8.36, "Beli barang dapur")]),
    dict(start=9.75, end=13.8, kicker="Terus bawa", title="Isi barang.",
         pills=[(11.09, "Letak barang dalam beg"), (12.4, "Lagi memudahkan")]),
    dict(start=13.8, end=17.95, kicker="Kalau tak bawa", title="Terpaksa beli.",
         pills=[(16.2, "Simpan dalam kereta je")]),
    dict(start=17.95, end=20.6, kicker="Beg ni", title="Sangat besar.", pills=[(19.1, "Tahan berat")]),
    dict(start=20.6, end=22.95, kicker="Siap ada", title="Zip.", pills=[(21.2, "Dalam pun luas")]),
    dict(start=22.95, end=27.35, kicker="Kalis air", title="Waterproof.",
         pills=[(23.86, "Hujan tak basah"), (25.33, "Senang tutup")]),
    dict(start=27.35, end=31.24, kicker="Ada", title="Pelbagai corak.", pills=[(29.73, "Beg besar")]),
]
IMAGES = [  # frame beg paling jelas dari video (src 59.5 s), owner minta
    dict(src="work/v1/img/p1.png", start=4.45, end=7.0),
]
CTA = dict(start=31.24, text="Beli di beg kuning")
