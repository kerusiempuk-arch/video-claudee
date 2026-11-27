# Paip tangan robot / paip mekanikal (Drive 1WfT1JZHO3yhyuK3X5n8vZ18jj7NGoHOi) — Style 3
# Bina: python3 -I styles/style-3/build.py work/vid1127/raw.mp4 styles/style-3/projects/paip_robot.py work/vid1127/hf3

REMOVE = [
    (6.24, 6.72),    # "okey"
    (12.88, 13.45),  # "okey"
    (18.42, 20.90),  # "Aku pusing ni" (cubaan pertama – ulang)
    (23.25, 24.12),  # "Okay"
    (26.22, 27.66),  # "Oke, nah,"
    (30.85, 31.45),  # "Kita," (mula semula)
    (32.70, 33.88),  # "kita boleh nak laras," (ulang – simpan "kita boleh nak adjust")
    (34.84, 37.26),  # "okey, nak basuh," (cubaan pertama)
    (39.75, 40.34),  # "okay"
]
SRC_END = 53.1
TAIL = 1.9

# Paip (produk) di separuh atas frame (y ~12–50 %) → tajuk, CTA & gradien di BAWAH.
POSITION = "bottom"

# --- overlay, masa ikut video SELEPAS dipotong. TIADA subtitle bawah.
END = 35.57
HEADS = [
    dict(start=0.0, end=5.5, kicker="Baru pasang", title="Paip robot.",
         pills=[(3.10, "Tangan robot"), (4.66, "Paip mekanikal")]),
    dict(start=5.5, end=10.4, kicker="Boleh gerak", title="Ikut suka.",
         pills=[(5.82, "Dongak ke atas"), (7.00, "Turun ke bawah"), (8.92, "Pusing 360°")]),
    dict(start=10.4, end=16.86, kicker="Air keluar", title="Semua lubang.",
         pills=[(13.10, "Keseluruhan lubang"), (15.34, "Pusing kepala paip")]),
    dict(start=16.86, end=19.32, kicker="Atau", title="Lubang tengah.", pills=[(17.00, "Air mengalir")]),
    dict(start=19.32, end=27.46, kicker="Jangkauan air", title="Boleh adjust.",
         pills=[(22.00, "Basuh sekitar singki"), (24.42, "Dongak"), (25.94, "Air pergi lebih jauh")]),
    dict(start=27.46, end=31.94, kicker="Walaupun kecil", title="Sangat mudah.",
         pills=[(27.98, "Cuci pinggan"), (29.02, "Cuci singki")]),
]
IMAGES = []   # tiada gambar produk diberi
CTA = dict(start=31.94, text="Beli di beg kuning")
