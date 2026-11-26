# Seluar kargo (Drive 12TlggiFEJmDpdd4Or-plvkOK42sZJow8) — Style 3
# Bina: python3 -I styles/style-3/build.py work/v12tl/raw.mp4 styles/style-3/projects/seluar.py work/v12tl/hf

REMOVE = [
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

END = 31.59
HEADS = [
    dict(start=0.0, end=7.6, kicker="Seluar kargo", title="Banyak pilihan.",
         pills=[(3.33, "Ada warna lain"), (6.09, "Size pun banyak")]),
    dict(start=7.6, end=13.6, kicker="Poket", title="Banyak poket.",
         pills=[(8.06, "Belakang"), (9.38, "Peha · kanan kiri"), (11.51, "Depan · kanan kiri")]),
    dict(start=13.6, end=17.52, kicker="Zip dia", title="Heavy duty."),
    dict(start=17.52, end=21.16, kicker="Kain dia", title="Sangat tebal.", pills=[(17.6, "Tengok belah dalam")]),
    dict(start=21.16, end=28.19, kicker="Sesuai untuk", title="Kerja lasak.",
         pills=[(23.72, "Kerja kebun"), (24.80, "Camping"), (26.10, "Memancing")]),
]
IMAGES = []   # tiada gambar produk diberi
CTA = dict(start=28.19, text="Beli di beg kuning")
