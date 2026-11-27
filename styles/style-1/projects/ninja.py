# Mainan blok Ninja Ghost (Drive 1A7Tnn0lov6AtS9X7qIQ_BthT8p-y6y7F)
REMOVE = [
    (27.18, 27.66),  # "Okay"
]
SRC_END = 36.0
TAIL = 1.2
PUNCH_Y = 0.25
END = 30.38
CAPTION_Y = 680
CARD_Y = 1420
ZOOM = 0.04

CAPTIONS = [
    (1.72, [("Ini", 0.30, False), ("anak", 1.10, False), ("aku", 1.34, False)]),
    (2.54, [("buat", 1.56, False), ("kapal", 1.72, True)]),
    (3.60, [("Dengan", 2.80, False), ("model", 3.18, False)]),
    (4.74, [("superhero", 3.60, True)]),
    (5.72, [("dia", 4.74, False), ("gabungkan", 5.12, True)]),
    (6.68, [("dengan", 5.72, False), ("mainan", 5.98, False), ("lain", 6.36, True)]),
    (8.10, [("Sangat", 7.34, False), ("menarik", 7.64, True)]),
    (8.94, [("mainan", 8.10, False), ("ini", 8.56, False)]),
    (10.12, [("Macam-macam", 9.06, False), ("boleh", 9.54, False), ("buat", 9.78, False)]),
    (10.84, [("Anak-anak", 10.12, False), ("akan", 10.62, False)]),
    (11.56, [("lebih", 10.84, False), ("kreatif", 11.08, True)]),
    (12.46, [("lebih", 11.68, False), ("fokus", 11.86, True)]),
    (13.06, [("kalau", 12.46, False), ("kita", 12.76, False)]),
    (13.92, [("bagi", 13.06, False), ("benda", 13.30, False), ("ni", 13.52, False)]),
    (14.74, [("Berbanding", 14.08, False), ("asyik", 14.54, False)]),
    (15.62, [("dia", 14.74, False), ("bagi", 14.88, False), ("telefon", 15.18, True)]),
    (16.48, [("asyik", 15.76, False), ("dia", 16.02, False), ("mengadap", 16.18, False)]),
    (17.34, [("TV", 16.48, True), ("tu", 16.82, False)]),
    (18.12, [("baik", 17.42, False), ("bagi", 17.60, False), ("benda", 17.90, False)]),
    (18.64, [("macam", 18.12, False), ("ni", 18.40, False)]),
    (19.90, [("Boleh", 19.10, False), ("buat", 19.28, False), ("rumah", 19.46, True)]),
    (20.78, [("boleh", 20.18, False), ("buat", 20.38, False), ("kapal", 20.56, False)]),
    (21.28, [("terbang", 20.78, True)]),
    (22.34, [("boleh", 21.46, False), ("buat", 21.72, False), ("roket", 21.90, True)]),
    (23.60, [("boleh", 22.48, False), ("buat", 22.74, False), ("istana", 22.94, True)]),
    (24.50, [("Harga", 23.60, False), ("sangat", 24.18, False)]),
    (25.12, [("berbaloi", 24.50, True)]),
    (26.10, [("Berminat", 25.12, False), ("dengan", 25.72, False)]),
    (27.30, [("mainan", 26.10, False), ("Ninjago", 26.72, True)]),
    (28.52, [("Block", 27.30, False), ("Series", 27.70, False), ("ini", 28.08, False)]),
    (29.04, [("Dapatkan", 28.52, False), ("di", 28.96, False)]),
    (30.38, [("beg", 29.04, True), ("kuning", 29.26, True)]),
]
HOOK = dict(end=6.9, y=100, kicker="mainan blok paling", title="kreatif",
            options=[("Bina kapal", "01"), ("Model superhero", "02"), ("Gabung mainan lain", "03")],
            select_at=[1.72, 3.60, 5.72])
SECTIONS = [  # (mula, tamat, label, "n / 3", subtajuk)
    (7.0, 14.0, "kelebihan", "1 / 3", "kreatif & fokus"),
    (14.0, 18.9, "kelebihan", "2 / 3", "ganti skrin"),
    (18.9, 23.6, "kelebihan", "3 / 3", "macam-macam binaan"),
]
STICKERS = [
    (10.84, 13.9, "lebih kreatif", 50, 250, 2.0),
    (11.86, 13.9, "lebih fokus", 80, 320, -1.5),
    (15.18, 18.8, "kurang telefon", 50, 250, -2.0),
    (16.48, 18.8, "kurang TV", 80, 320, 1.5),
    (19.46, 23.5, "rumah", 50, 250, 2.0),
    (20.56, 23.5, "kapal terbang", 80, 320, -1.5),
    (21.90, 23.5, "roket", 110, 390, 1.5),
    (22.94, 23.5, "istana", 140, 460, -2.0),
]
CIRCLES = []
COVERS = [  # tiada muka dalam video – A = set penuh, B = binaan
    dict(at=6.0, kicker="mainan blok paling,", title="kreatif",
         stickers=["model superhero", "lebih fokus ✓"], pill="kelebihan 1-3 · Ninjago Block Series"),
    dict(at=9.0, kicker="ganti telefon & TV,", title="kreatif",
         stickers=["kapal · roket · istana", "harga berbaloi ✓"], pill="kelebihan 1-3 · Ninjago Block Series"),
]
BIG_WORDS = [(7.34, 8.94, "menarik", True)]
YELLOW = (255, 200, 40, 255)
CTA = dict(title="kreatif", title_at=23.6, title_y=230, card_at=25.12, card_y=1180,
           card_label="Ninjago Block Series", name="Ninjago Block Series",
           tags="kreatif · fokus · berbaloi",
           button="Tekan beg kuning ↓", button_color=YELLOW, button_text_color=(22, 22, 26, 255))
