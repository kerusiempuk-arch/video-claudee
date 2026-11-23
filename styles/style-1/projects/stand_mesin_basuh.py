# Stand mesin basuh beroda (Drive 1yQV7CIpsbShCcFj2KOGCVvcnO6DbvKfs)
# ---------- potongan (build.py) – masa ikut video ASAL
REMOVE = [
    (0.00, 0.85),    # "aa"
    (2.52, 3.08),    # okey
    (6.62, 7.26),    # okey
    (9.70, 10.03),   # aa
    (14.12, 14.43),  # okey
    (19.10, 20.56),  # okey
    (28.45, 28.92),  # okey
]
SRC_END = 39.75
TAIL = 0.7
PUNCH_Y = 0.25

END = 33.2
CAPTION_Y = 1780
CARD_Y = 1180
ZOOM = 0.04
CAPTIONS = [
    (0.92, [('Ini', 0.0, False), ('stand', 0.44, False), ('untuk', 0.66, False)]),
    (1.82, [('mesin', 0.92, False), ('basuh', 1.18, True)]),
    (2.62, [('Dia', 1.82, False), ('punya', 1.84, False), ('kapasiti', 2.06, True)]),
    (3.24, [('dia', 2.62, False), ('boleh', 2.78, False), ('tanggung', 2.92, False)]),
    (4.00, [('beban', 3.24, False), ('sampai', 3.6, False)]),
    (5.28, [('500', 4.0, False), ('kilogram', 4.46, True)]),
    (6.12, [('Boleh', 5.28, False), ('laras', 5.42, True)]),
    (6.70, [('Nak', 6.12, False), ('panjang', 6.12, False)]),
    (7.86, [('nak', 6.7, False), ('pendek', 6.88, True)]),
    (8.28, [('Bawah', 7.86, False), ('roda', 8.02, False)]),
    (9.16, [('dia', 8.28, False), ('hidup', 8.52, True)]),
    (9.86, [('Boleh', 9.16, False), ('pusing', 9.34, False)]),
    (11.50, [('360', 9.86, False), ('darjah', 10.72, True)]),
    (12.02, [('Keempat-empat', 11.5, False)]),
    (13.00, [('roda', 12.02, False), ('dia', 12.52, False)]),
    (13.86, [('Lagi', 13.0, False), ('satu', 13.08, False)]),
    (14.84, [('dia', 13.86, False), ('ada', 14.14, False), ('tapak', 14.34, True)]),
    (15.88, [('yang', 14.84, False), ('kekal', 15.32, False)]),
    (16.90, [('Sangat', 15.88, False), ('kuat', 16.24, True)]),
    (17.84, [('Boleh', 16.9, False), ('nak', 17.12, False), ('laras', 17.3, False)]),
    (18.34, [('nak', 17.84, False), ('besar', 17.88, True)]),
    (19.20, [('nak', 18.34, False), ('kecil', 18.44, True)]),
    (20.16, [('Ada', 19.2, False), ('bacaan', 19.36, False), ('air', 19.88, True)]),
    (21.58, [('untuk', 20.16, False), ('keseimbangan', 20.58, True)]),
    (22.32, [('Lagi', 21.82, False), ('satu', 22.02, False)]),
    (23.40, [('dia', 22.32, False), ('ada', 22.4, False), ('span', 22.54, False)]),
    (24.48, [('Letak', 23.4, False), ('mesin', 23.76, False), ('basuh', 24.12, False)]),
    (25.36, [('ke', 24.48, False), ('atas', 24.66, False), ('ni', 24.88, False)]),
    (25.78, [('jadinya', 25.36, False), ('kita', 25.52, False)]),
    (26.26, [('nak', 25.78, False), ('cuci', 25.92, True)]),
    (27.24, [('bahagian', 26.26, False), ('bawah', 26.58, False)]),
    (28.16, [('bahagian', 27.24, False), ('belakang', 27.44, True)]),
    (28.84, [('ataupun', 28.16, False), ('nak', 28.44, False), ('alih', 28.68, True)]),
    (29.54, [('ke', 28.84, False), ('tempat', 29.0, False), ('lain', 29.3, False)]),
    (30.56, [('Lagi', 29.54, False), ('senang', 30.0, True)]),
    (31.70, [('lagi', 30.56, False), ('memudahkan', 30.72, True)]),
    (32.52, [('Berminat', 31.7, False), ('dapatkan', 32.14, False)]),
    (33.20, [('di', 32.52, False), ('beg', 32.62, False), ('kuning', 32.72, True)]),
]
HOOK = dict(end=5.2, y=100, kicker="stand mesin basuh paling", title="kuat",
            options=[("Khas mesin basuh", "01"), ("Tahan sampai 500 kg", "02")], select_at=[0.9, 4.0])
SECTIONS = [
    (5.2, 13.0, "kelebihan", "1 / 3", "laras & roda 360°"),
    (13.0, 21.8, "kelebihan", "2 / 3", "tapak kukuh & seimbang"),
    (21.8, 31.6, "kelebihan", "3 / 3", "senang cuci & alih"),
]
STICKERS = [
    (5.4, 12.9, "panjang ↔ pendek", 50, 250, 2.0),
    (7.9, 12.9, "roda hidup", 80, 320, -1.5),
    (9.9, 12.9, "pusing 360°", 110, 390, 1.5),
    (14.3, 21.7, "tapak kekal", 50, 250, -2.0),
    (17.1, 21.7, "laras besar / kecil", 80, 320, 1.5),
    (19.4, 21.7, "ada bacaan air", 110, 390, -1.5),
    (23.4, 31.5, "cuci bawah & belakang", 50, 250, 2.0),
    (28.4, 31.5, "senang alih", 80, 320, -1.5),
]
CIRCLES = []
CTA = dict(title="kuat", title_at=31.6, title_y=230, card_at=32.1, card_y=1180,
           card_label="Stand Mesin Basuh", name="Stand Mesin Basuh", tags="500 kg · roda 360° · boleh laras",
           button="Tekan bakul kuning ↓", button_color=(255, 200, 40, 255), button_text_color=(22, 22, 26, 255))
