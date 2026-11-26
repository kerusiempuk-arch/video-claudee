# Seluar kargo (Drive 12TlggiFEJmDpdd4Or-plvkOK42sZJow8) — Style 3
# Bina: python3 -I styles/style-3/build.py work/v12tl/raw.mp4 styles/style-3/projects/seluar.py work/v12tl/hf

REMOVE = [
    (2.88, 3.08),    # "haa" (selepas "aku pilih ni")
    (8.00, 8.24),    # "okay"
    (14.36, 14.58),  # "okay"
    (16.68, 17.05),  # "aa"
    (21.38, 21.63),  # "okay"
    (23.70, 23.98),  # "okay"
    (26.56, 26.72),  # "okay"
]
SRC_END = 38.75   # lepas tu dia jalan keluar frame
TAIL = 1.9

# Kepala di bahagian atas frame (y ~15–30 %) → tajuk, CTA & gradien di BAWAH.
POSITION = "bottom"

END = 31.39
HEADS = [
    dict(start=0.0, end=7.40, kicker="Seluar kargo", title="Banyak pilihan.",
         pills=[(3.13, "Ada warna lain"), (5.89, "Size pun banyak")]),
    dict(start=7.40, end=13.40, kicker="Poket", title="Banyak poket.",
         pills=[(7.86, "Belakang"), (9.18, "Peha · kanan kiri"), (11.31, "Depan · kanan kiri")]),
    dict(start=13.40, end=17.32, kicker="Zip dia", title="Heavy duty."),
    dict(start=17.32, end=20.96, kicker="Kain dia", title="Sangat tebal.", pills=[(17.40, "Tengok belah dalam")]),
    dict(start=20.96, end=27.99, kicker="Sesuai untuk", title="Kerja lasak.",
         pills=[(23.52, "Kerja kebun"), (24.60, "Camping"), (25.90, "Memancing")]),
]
IMAGES = []   # tiada gambar produk diberi
CTA = dict(start=27.99, text="Beli di beg kuning")
