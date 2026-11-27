# Charger 120W + kabel Type-C (Drive 16Gl94gtBkansxxvIjVV9RTpELujfXthX) — Style 3
# Bina: python3 -I styles/style-3/build.py work/v1/raw.mp4 styles/style-3/projects/charger.py work/v1/hf

REMOVE = [
    (4.40, 6.95),    # "okay. Aa, wire dia, ada," — ambil take kedua "wire kabel dia"
    (9.82, 10.62),   # "okay. Aa,"
    (12.08, 13.10),  # "okay. Aa,"
    (15.76, 16.64),  # "okay. Aa,"
    (20.77, 21.33),  # "aa"
]
SRC_END = 31.3
TAIL = 1.9

# Kepala di bahagian atas frame (y ~5–30 %) → tajuk, CTA & gradien di BAWAH.
POSITION = "bottom"

END = 21.87
HEADS = [
    dict(start=0.0, end=3.45, kicker="Charger ni", title="Boleh lipat.",
         pills=[(0.7, "Buka · tutup"), (2.0, "Jimat ruang")]),
    dict(start=3.45, end=6.5, kicker="Wire kabel", title="Pelbagai saiz."),
    dict(start=6.5, end=9.6, kicker="Kabel", title="Type-C."),
    dict(start=9.6, end=11.6, kicker="Kuasa", big=[(9.8, "120W")], sub="pengecas laju."),
    dict(start=11.6, end=15.1, kicker="Balik kampung", title="Tak ada masalah.", pills=[(11.8, "Charge telefon")]),
    dict(start=15.1, end=19.79, kicker="Bateri", title="Cepat penuh.", pills=[(18.3, "Super fast charging")]),
]
IMAGES = []   # tiada gambar produk diberi
CTA = dict(start=19.79, text="Beli di beg kuning")
