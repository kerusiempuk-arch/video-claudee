# Charger 120W + kabel Type-C (Drive 16Gl94gtBkansxxvIjVV9RTpELujfXthX) — Style 3
# Bina: python3 -I styles/style-3/build.py work/v1/raw.mp4 styles/style-3/projects/charger.py work/v1/hf

REMOVE = [
    (0.0, 0.61),     # "aa" pembuka
    (4.40, 6.95),    # "okay. Aa, wire dia, ada," — ambil take kedua "wire kabel dia"
    (9.82, 10.62),   # "okay. Aa,"
    (12.08, 13.10),  # "okay. Aa,"
    (15.76, 16.86),  # "okay. Aa,"
    (20.77, 21.64),  # "aa"
]
SRC_END = 31.3
TAIL = 1.9

# Kepala di bahagian atas frame (y ~5–30 %) → tajuk, CTA & gradien di BAWAH.
POSITION = "bottom"

END = 21.11
HEADS = [
    dict(start=0.0, end=2.85, kicker="Charger ni", title="Boleh lipat.",
         pills=[(0.15, "Buka · tutup"), (1.4, "Jimat ruang")]),
    dict(start=2.85, end=5.9, kicker="Wire kabel", title="Pelbagai saiz."),
    dict(start=5.9, end=9.0, kicker="Kabel", title="Type-C."),
    dict(start=9.0, end=10.8, kicker="Kuasa", big=[(9.2, "120W")], sub="pengecas laju."),
    dict(start=10.8, end=14.1, kicker="Balik kampung", title="Tak ada masalah.", pills=[(10.9, "Charge telefon")]),
    dict(start=14.1, end=18.75, kicker="Bateri", title="Cepat penuh.", pills=[(17.3, "Super fast charging")]),
]
IMAGES = []   # tiada gambar produk diberi
CTA = dict(start=18.75, text="Beli di beg kuning")
