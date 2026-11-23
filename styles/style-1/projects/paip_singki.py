# Paip saluran singki (Drive 1HpNmreNbNDTsiQxYSTCGny_-kL03_mbE)
# ---------- potongan (build.py) – masa ikut video ASAL
REMOVE = [
    (8.62, 9.50),    # "okey"
    (15.22, 16.00),  # "okey"
    (17.00, 17.38),  # "okey"
    (22.60, 23.30),  # "okey"
    (24.60, 27.00),  # "bahagian tabung untuk..." – ayat tak habis, diulang
    (37.82, 38.45),  # "okay"
]
SRC_END = 42.4
TAIL = 0.7
PUNCH_Y = 0.25

END = 32.39
CAPTION_Y = 1780
CARD_Y = 1180
ZOOM = 0.04

CAPTIONS = [  # (group_end, [(perkataan, mula, highlight)]) – masa SELEPAS potong
    (1.30, [("Ini", 0.00, False), ("saluran", 0.80, False)]),
    (2.66, [("paip", 1.30, False), ("singki", 1.62, True), ("rumah", 1.92, False)]),
    (3.50, [("aku,", 2.22, False), ("dah", 2.68, False), ("lama", 2.94, True)]),
    (4.50, [("Sekarang", 3.54, False), ("aku", 4.08, False), ("dah", 4.36, False)]),
    (5.10, [("ada", 4.52, False), ("yang", 4.72, False), ("ni", 4.92, False)]),
    (5.90, [("Aku", 5.14, False), ("nak", 5.32, False), ("tukar", 5.46, False)]),
    (7.05, [("kepada", 5.92, False), ("yang", 6.26, False), ("baru", 6.46, True)]),
    (8.50, [("Lagi", 7.24, False), ("berkualiti", 7.50, True)]),
    (9.24, [("Boleh", 8.58, False), ("adjust", 8.98, True)]),
    (10.90, [("panjang,", 9.24, True), ("pendek", 10.34, True)]),
    (12.62, [("ikut", 10.92, False), ("kesesuaian", 10.98, False)]),
    (14.05, [("jarak", 12.64, False), ("lubang", 12.96, False), ("singki", 13.24, True)]),
    (14.80, [("Specialnya", 14.12, False)]),
    (15.55, [("kepala", 14.82, False), ("ni", 15.20, False)]),
    (16.38, [("anti", 15.56, False), ("odor", 15.86, True)]),
    (17.45, [("anti", 16.40, False), ("serangga", 16.68, True)]),
    (18.44, [("Bau", 17.48, True), ("tak", 17.70, False), ("masuk", 17.88, False)]),
    (19.04, [("serangga", 18.46, True), ("pun", 18.90, False)]),
    (19.76, [("tak", 19.04, False), ("masuk", 19.20, False)]),
    (20.76, [("Lagi", 19.78, False), ("satu", 20.02, False)]),
    (21.76, [("bahagian", 20.78, False), ("tabung", 21.04, True)]),
    (22.48, [("bawah", 21.36, False), ("ni", 21.78, False)]),
    (23.60, [("sekiranya", 22.50, False), ("dah", 23.24, False)]),
    (24.78, [("tersumbat", 23.62, True), ("ke", 24.34, False)]),
    (25.60, [("dah", 24.80, False), ("mendap", 24.96, True)]),
    (26.10, [("dah", 25.42, False), ("banyak", 25.62, False), ("ke", 25.90, False)]),
    (26.86, [("kita", 26.12, False), ("boleh", 26.32, False), ("nampak", 26.48, True)]),
    (28.00, [("Jadinya", 26.88, False), ("senang", 27.52, False)]),
    (29.10, [("kita", 28.02, False), ("nak", 28.20, False), ("cuci", 28.40, True)]),
    (30.36, [("Harga", 28.82, False), ("pun", 29.12, False), ("sangat", 29.46, False), ("murah", 29.80, True)]),
    (31.70, [("Berminat?", 30.38, False), ("dapatkan", 31.08, False), ("di", 31.62, False)]),
    (32.39, [("beg", 31.72, True), ("kuning", 31.90, True)]),
]
HOOK = dict(end=8.4, y=100, kicker="paip singki paling", title="berkualiti",
            options=[("Paip lama", "01"), ("Paip baru", "02")], select_at=[2.94, 6.46])
SECTIONS = [
    (8.4, 14.0, "kelebihan", "1 / 3", "boleh adjust"),
    (14.0, 19.7, "kelebihan", "2 / 3", "anti bau & serangga"),
    (19.7, 28.8, "kelebihan", "3 / 3", "senang cuci"),
]
STICKERS = [  # (mula, tamat, teks, x, y, sudut)
    (9.24, 13.9, "adjust panjang / pendek", 50, 250, 2.0),
    (12.64, 13.9, "ikut jarak singki", 80, 320, -1.5),
    (15.86, 19.6, "anti bau", 50, 250, 2.0),
    (16.68, 19.6, "anti serangga", 80, 320, -1.5),
    (24.0, 28.7, "nampak bila tersumbat", 50, 250, -2.0),
    (27.52, 28.7, "senang cuci", 80, 320, 1.5),
]
CIRCLES = []
YELLOW = (255, 200, 40, 255)
CTA = dict(title="berkualiti", title_at=28.8, title_y=230, card_at=29.1, card_y=1180,
           card_label="Paip Singki", name="Paip Saluran Singki",
           tags="boleh adjust · anti bau · senang cuci",
           button="Tekan bakul kuning ↓", button_color=YELLOW, button_text_color=(22, 22, 26, 255))
