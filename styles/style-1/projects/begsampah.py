# Beg sampah / trash bag (Drive 1v1U82uI0PxsByx804c_kQY6YWgObLubn)
# ---------- potongan (build.py) – masa ikut video ASAL
REMOVE = [
    (2.95, 3.90),    # "okay"
    (5.45, 12.15),   # "okay tengok" + "okay yang spesialnya" (ayat tak habis)
    (17.00, 17.33),  # "okay"
    (24.80, 25.15),  # "aa"
    (26.15, 27.90),  # "okey"
]
SRC_END = 34.65
TAIL = 0.7
PUNCH_Y = 0.25

END = 23.58
CAPTION_Y = 1780
CARD_Y = 1180
ZOOM = 0.04
CAPTION_ACCENT = (255, 212, 59, 255)   # baju biru muda

CAPTIONS = [  # (group_end, [(perkataan, mula, highlight)])
    (1.46, [("Trash", 0.74, False), ("bag", 1.24, False)]),
    (2.10, [("ataupun", 1.46, False)]),
    (2.98, [("beg", 2.10, False), ("sampah", 2.28, True)]),
    (3.98, [("100", 3.10, True), ("pieces", 3.36, False)]),
    (4.60, [("semua", 3.98, False)]),
    (5.16, [("Yang", 4.72, False), ("spesial", 4.80, False)]),
    (6.30, [("beg", 5.16, False), ("sampah", 5.30, False), ("ni", 5.76, False)]),
    (7.16, [("dia", 6.52, False), ("tebal", 6.70, True)]),
    (7.88, [("Ada", 7.24, False), ("pelbagai", 7.46, False)]),
    (8.80, [("saiz", 7.88, True)]),
    (9.50, [("Susah", 8.98, False), ("nak", 9.38, False)]),
    (10.80, [("koyak", 9.50, True), ("biasa", 10.06, False)]),
    (11.50, [("Beg", 10.88, False), ("sampah", 11.00, False)]),
    (12.14, [("kalau", 11.54, False), ("kita", 11.64, False), ("beli", 11.86, False)]),
    (13.40, [("kat", 12.14, False), ("kedai", 12.28, False), ("biasa", 12.62, False)]),
    (14.48, [("dia", 13.54, False), ("senang", 13.62, False), ("bocor", 13.96, True)]),
    (15.45, [("senang", 14.54, False), ("koyak", 14.86, True)]),
    (16.10, [("Jadi", 15.60, False), ("ini", 15.68, False)]),
    (17.08, [("dia", 16.12, False), ("spesial", 16.34, True)]),
    (18.40, [("Dengan", 17.16, False), ("banyak", 17.88, True)]),
    (18.95, [("macam", 18.40, False), ("ni", 18.64, False)]),
    (19.70, [("100", 19.10, True), ("pieces", 19.28, False)]),
    (20.25, [("macam", 19.70, False), ("ni", 19.96, False)]),
    (21.24, [("harga", 20.44, False), ("sangat", 20.94, False)]),
    (22.00, [("berbaloi", 21.24, True)]),
    (22.98, [("Berminat", 22.10, False), ("dapatkan", 22.56, False)]),
    (23.58, [("di", 22.98, False), ("beg", 23.10, False), ("kuning", 23.22, True)]),
]
HOOK = dict(end=3.0, y=100, kicker="beg sampah paling", title="tebal",
            options=[("Senang koyak", "01"), ("Susah nak koyak", "02")], select_at=[1.0, 2.0])
SECTIONS = [  # (mula, tamat, "kelebihan", "1 / 3", subtajuk)
    (3.0, 8.8, "kelebihan", "1 / 3", "tebal & pelbagai saiz"),
    (8.8, 15.5, "kelebihan", "2 / 3", "susah nak koyak"),
    (15.5, 20.3, "kelebihan", "3 / 3", "banyak dalam satu pek"),
]
STICKERS = [  # (mula, tamat, teks, x, y, sudut)
    (3.2, 8.7, "100 pieces", 70, 300, 2.0),
    (6.6, 8.7, "plastik tebal", 110, 370, -1.5),
    (7.6, 8.7, "pelbagai saiz", 150, 440, 1.5),
    (9.4, 15.4, "susah koyak", 70, 300, -2.0),
    (13.6, 15.4, "tak mudah bocor", 110, 370, 1.5),
    (16.3, 20.2, "banyak isi", 70, 300, 2.0),
    (19.1, 20.2, "100 pcs", 110, 370, -1.5),
]
CIRCLES = []
CTA = dict(title="tebal", title_at=20.3, title_y=230, card_at=21.0, card_y=1180,
           card_label="Beg Sampah", name="Beg Sampah 100 pcs", tags="tebal · pelbagai saiz · susah koyak",
           button="Tekan bakul kuning ↓", button_color=(255, 200, 40, 255), button_text_color=(22, 22, 26, 255))
