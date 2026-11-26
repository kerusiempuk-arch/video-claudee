# Kipas kereta triple fan (Drive 1g8ZMTWF2yN79W1swDyBpJ2pdVz95gKE0) — Style 3
# Bina: python3 -I styles/style-3/build.py work/v1/raw.mp4 styles/style-3/projects/kipas.py work/v1/hf

REMOVE = [
    (0.00, 0.63),    # "aa"
    (3.83, 4.10),    # "aa"
    (4.45, 4.79),    # "aa"
    (8.82, 10.85),   # "kelajuan pertama, aa" (ulang)
    (14.00, 14.27),  # "aa"
    (15.90, 16.74),  # "okay, aa"
    (22.30, 22.74),  # "aa"
    (24.92, 25.12),  # "aa"
    (26.29, 27.46),  # "okey, aa"
]
SRC_END = 39.4
TAIL = 1.9
# Kipas di separuh atas frame → tajuk & CTA di BAWAH supaya tak tutup produk.
POSITION = "bottom"

END = 33.21
HEADS = [
    dict(start=0.0, end=3.15, kicker="Kipas kereta", title="Triple fan.", pills=[(2.43, "3 kipas")]),
    dict(start=3.15, end=5.1, kicker="Tengok", title="Kertas melayang."),
    dict(start=5.1, end=12.3, kicker="Kipas ni ada", title="2 kelajuan.",
         pills=[(7.56, "Kelajuan 1 · dah melayang"), (10.0, "Kelajuan 2 · lagi kuat")]),
    dict(start=12.3, end=14.7, kicker="Boleh adjust", title="Depan & belakang."),
    dict(start=14.7, end=21.15, kicker="Lagi satu", title="Boleh pusing.",
         pills=[(16.32, "Orang sebelah"), (17.92, "Pemandu"), (19.12, "Belakang")]),
    dict(start=21.15, end=23.6, kicker="Pakai sendiri", title="Puas hati."),
    dict(start=23.6, end=28.85, kicker="Satu kereta", title="Rasa berangin.",
         pills=[(26.16, "Dibantu aircond"), (27.3, "Udara sejuk")]),
]
IMAGES = []
CTA = dict(start=28.85, text="Beli di beg kuning")
