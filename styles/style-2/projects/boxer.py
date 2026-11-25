# Boxer lelaki (Drive 1gI1bGT7A2_I4DFTn-jw5PHQ8X-NKUNGH) — CONTOH STYLE 2 YANG DILULUSKAN
# --- potongan (build.py), masa ikut video ASAL
REMOVE = [
    (0.00, 0.31),    # "aaa" di permulaan
    (3.24, 3.58),    # "aaa" sebelum "kebanyakan"
    (12.95, 15.00),  # "getah dia pun lembut" pertama – diulang lepas tu
]
SRC_END = 22.4
TAIL = 0.7

# --- overlay (build.py), masa ikut video SELEPAS dipotong (transkripsi cut.wav)
END = 17.99
CAPTION_Y = 545   # dada, bawah dagu
CARD_TOP = 1360   # nilai asal sebelum default jadi 1500

# (tamat_kumpulan, [(perkataan, mula, gaya)]) — gaya: "" biasa, "box" kotak putih, "serif" serif italik. Max ~4 perkataan.
CAPTIONS = [
    (1.64, [("Zaman", 0.03, ""), ("sekarang", 0.26, ""), ("jarang", 0.80, ""), ("dah", 1.20, "")]),
    (2.80, [("pakai", 1.64, ""), ("spender", 2.07, "box"), ("biasa", 2.41, "")]),
    (4.76, [("kebanyakan", 2.80, ""), ("pakai", 3.94, ""), ("boxer", 4.27, "serif")]),
    (5.56, [("Sebab", 4.76, ""), ("apa?", 5.12, "")]),
    (6.86, [("Pakaian", 5.56, ""), ("boxer", 6.07, ""), ("ini", 6.58, "")]),
    (7.58, [("lebih", 6.86, ""), ("selesa", 7.09, "box")]),
    (9.56, [("pengudaraan", 7.58, "serif"), ("lebih", 8.47, ""), ("lancar", 8.85, "")]),
    (10.59, [("Lagi", 9.56, ""), ("satu,", 9.80, ""), ("kain", 10.17, ""), ("dia", 10.41, "")]),
    (11.76, [("pun", 10.59, ""), ("sangat", 10.77, ""), ("lembut", 11.21, "box")]),
    (13.12, [("Getah", 11.76, ""), ("dia", 12.12, ""), ("pun", 12.29, ""), ("lembut", 12.49, "serif")]),
    (14.44, [("ada", 13.12, ""), ("pelbagai", 13.35, ""), ("saiz", 13.96, "box")]),
    (15.51, [("ada", 14.44, ""), ("pelbagai", 14.64, ""), ("warna", 15.22, "box")]),
    (16.84, [("Berminat?", 15.51, ""), ("Dapatkan", 16.10, ""), ("di", 16.58, "")]),
    (17.99, [("beg kuning", 16.84, "serif")]),
]

HOOK = dict(start=0.15, end=2.75, text="review **boxer lelaki**", x=350, y=690)

CARDS = [  # kind: vs | icon | check | chips  (start/end = masa kad di skrin)
    dict(kind="vs", start=2.75, end=5.5, kicker="ZAMAN SEKARANG", old="Spender", new="Boxer", new_at=4.27),
    dict(kind="icon", start=5.5, end=7.55, kicker="01 · SELESA", title="Lebih *selesa*", icon="heart"),
    dict(kind="icon", start=7.55, end=9.5, kicker="02 · UDARA", title="Pengudaraan\n*lebih lancar*", icon="wind"),
    dict(kind="check", start=9.5, end=13.05, kicker="03 · LEMBUT", title="Sangat *lembut*",
         items=[("Kain lembut", 11.21), ("Getah pinggang lembut", 12.49)]),
    dict(kind="chips", start=13.05, end=15.45, kicker="04 · PILIHAN", title="Pelbagai saiz & warna",
         chips=["M", "L", "XL", "2XL"], chips_at=13.96,                 # ANDAIAN – sahkan dengan user
         colors=["#6E6A7C", "#2E7F86", "#1D1F22", "#E07A4F", "#8C93A1"], colors_at=14.9),
]
RAIL = dict(start=5.5, end=15.45, steps=[(5.5, "Selesa"), (7.55, "Udara"), (9.5, "Lembut"), (13.05, "Pilihan")])
CTA = dict(start=15.45, button_at=15.9, button="Tekan *beg kuning*",
           items=["Lebih selesa", "Pengudaraan lancar", "Kain & getah lembut", "Pelbagai saiz & warna"])
