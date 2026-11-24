# Colgate Total Enamel Strength + berus gigi + cooling towel (Drive 1bLYwfdFrdA1xGE5kbk8LNlGi1CZu6FQ8)
# ---------- potongan (build.py) – masa ikut video ASAL
REMOVE = [
    (3.70, 4.12),     # "okay"
    (6.72, 6.98),     # "okay"
    (10.10, 10.90),   # "okay"
    (12.20, 13.58),   # "harga" ulang + "okay"
    (18.84, 19.04),   # "okay"
    (19.90, 22.90),   # "Harga pun sangat-sangat murah" pertama (ulang — simpan yang kedua)
]
SRC_END = 26.30       # buang "Berapa dah video ni?" di hujung
TAIL = 1.2
PUNCH_Y = 0.25

# ---------- overlay (build.py) – masa ikut video SELEPAS dipotong
END = 17.80
CAPTION_Y = 1780
CARD_Y = 1320
ZOOM = 0.04
CAPTION_ACCENT = (255, 212, 59, 255)   # kuning: baju biru

CAPTIONS = [  # (group_end, [(perkataan, mula, highlight)])
    (1.44, [("Colgate", 0.00, True), ("Total", 0.88, True)]),
    (2.78, [("Enamel", 1.46, False), ("Strength", 2.06, False)]),
    (3.50, [("Beli", 2.80, False), ("ni", 3.10, False)]),
    (4.70, [("dia", 3.32, False), ("bagi", 3.52, False), ("berus gigi", 3.86, True)]),
    (5.42, [("sangat", 4.72, False), ("lembut", 5.02, True)]),
    (6.24, [("dan", 5.44, False), ("dia", 5.66, False), ("bagi", 5.80, False)]),
    (7.10, [("cooling", 6.26, True), ("towel", 6.62, True)]),
    (8.60, [("dengan", 7.20, False), ("satu", 7.68, False), ("harga", 8.10, True)]),
    (9.30, [("Barang", 8.72, False), ("pun", 8.90, False), ("sangat", 9.00, False)]),
    (10.10, [("berkualiti", 9.32, True)]),
    (11.54, [("untuk", 10.14, False), ("nak", 10.50, False), ("memperkuatkan", 10.76, True)]),
    (12.40, [("gigi", 11.56, False)]),
    (13.80, [("nak", 12.48, False), ("memutihkan", 12.56, True), ("gigi", 13.22, False)]),
    (14.50, [("cuba", 13.82, False), ("ini", 14.20, False)]),
    (15.42, [("Harga", 14.54, False), ("pun", 14.90, False), ("sangat", 15.10, False)]),
    (16.14, [("sangat", 15.44, False), ("murah", 15.64, True)]),
    (17.12, [("Berminat?", 16.18, False), ("dapatkan", 16.62, False)]),
    (17.80, [("di", 17.08, False), ("beg kuning", 17.16, True), ("ni", 17.50, False)]),
]
HOOK = dict(end=3.32, y=100, kicker="ubat gigi paling", title="berbaloi",
            options=[("Colgate Total", "01"), ("Enamel Strength", "02")], select_at=[0.10, 1.46])
SECTIONS = [
    (3.32, 8.70, "kelebihan", "1 / 3", "dapat set lengkap"),
    (8.70, 13.82, "kelebihan", "2 / 3", "kuat & putih"),
    (13.82, 16.18, "kelebihan", "3 / 3", "harga murah"),
]
STICKERS = [  # (mula, tamat, teks, x, y, sudut)
    (3.86, 8.60, "+ berus gigi", 50, 250, 2.0),
    (5.02, 8.60, "bulu lembut", 80, 320, -1.5),
    (6.26, 8.60, "+ cooling towel", 110, 390, 1.5),
    (8.10, 8.60, "satu harga", 50, 460, -2.0),
    (9.32, 13.72, "berkualiti", 50, 250, 2.0),
    (10.76, 13.72, "kuatkan gigi", 80, 320, -1.5),
    (12.56, 13.72, "putihkan gigi", 110, 390, 1.5),
    (15.64, 16.10, "sangat murah", 50, 250, -2.0),
]
CIRCLES = []
CTA = dict(title="berbaloi", title_at=16.18, title_y=230, card_at=16.40, card_y=1180,
           card_label="Colgate Total", name="Colgate Total Enamel Strength",
           tags="berus gigi · cooling towel · satu harga",
           button="Tekan bakul kuning ↓", button_color=(255, 200, 40, 255), button_text_color=(22, 22, 26, 255))
