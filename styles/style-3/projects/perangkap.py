# Perangkap serangga kuning (Drive 1WKTCMihIWBqwOVNgPOSyaco3WNR4HQ0t) — Style 3
# Bina: python3 -I styles/style-3/build.py work/v1/raw.mp4 styles/style-3/projects/perangkap.py work/v1/hf

REMOVE = [
    (2.93, 4.12),    # "aa" + "Dia ada," (ayat tak habis) → "Dia berpelekat"
    (6.44, 7.03),    # "aa"
    (9.43, 10.05),   # "dah" ulangan + "a"
    (13.49, 14.06),  # "aa"
    (17.55, 19.55),  # "ia selalu mengganggu pokok" (take pertama)
    (25.31, 25.96),  # "aa"
    (30.32, 31.10),  # "okey?"
    (37.45, 39.24),  # "Berminat" (take pertama)
]
SRC_END = 42.35
TAIL = 1.9

# Kepala di bahagian atas frame (y ~5–25 %) → tajuk, CTA & gradien di BAWAH.
POSITION = "bottom"

END = 31.33
HEADS = [
    dict(start=0.0, end=2.93, kicker="Ini nama dia", title="Perangkap serangga."),
    dict(start=2.93, end=5.5, kicker="Dua belah", title="Berpelekat.",
         pills=[(3.9, "Depan"), (4.55, "Belakang")]),
    dict(start=5.5, end=10.57, kicker="Senang pasang", title="Terus gantung.",
         pills=[(5.6, "Lubang siap"), (7.18, "Tali disediakan"), (8.01, "Masuk tali · gantung")]),
    dict(start=10.57, end=16.95, kicker="Masalah", title="Serangga.",
         pills=[(13.82, "Ganggu pokok"), (15.89, "Daun"), (16.40, "Buah")]),
    dict(start=16.95, end=23.45, kicker="Penyelesaian", title="Gantung je.",
         pills=[(19.36, "Pada ranting pokok"), (22.37, "Serangga melekat")]),
    dict(start=23.45, end=28.66, kicker="Sangat", title="Berkesan.",
         pills=[(24.43, "Tanpa racun"), (26.16, "Tanpa bahan kimia"), (27.88, "Lebih selamat")]),
]
IMAGES = []   # tiada gambar produk diberi
CTA = dict(start=28.66, text="Beli di beg kuning")
# Cover: python3 -I tools/cover/make_cover.py work/v1/raw.mp4 33.0 work/v1/cover.png --style 3 --title $' Perangkap Serangga. ' \
#   --kicker "Tanpa racun · Lebih selamat" --pills "Berpelekat 2 belah,Tali disediakan,Gantung je" --pos bottom --y 760
#   (NBSP di kiri/kanan tajuk = fon kecil sikit supaya tajuk panjang tak cecah tepi)
