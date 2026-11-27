# Tai Chi Wellness Patch (Drive 19tm-KI274ncwD4P7ZxyWwdT2WS0s0YnX)
REMOVE = [
    (0.0, 0.68),     # "Aa" pembuka
    (4.62, 5.26),    # "Lagi. Ha,"
    (8.50, 9.62),    # "Okey"
    (11.58, 12.50),  # "Okey"
    (14.80, 15.22),  # "Okey"
    (19.6, 23.46),   # "Okey, mana yang dah lemah tu, rasa," – ulangan, simpan ambilan kedua
    (26.62, 27.76),  # "Okay"
    (29.64, 30.74),  # "Tak payah nak makan" – owner minta potong
    (31.66, 32.30),  # "Okay" sebelum "berminat"
]
SRC_END = 37.2
TAIL = 1.2
PUNCH_Y = 0.25

END = 25.52
CAPTION_Y = 680
CARD_Y = 1420
ZOOM = 0.04

CAPTIONS = [
    (0.44, [('Untuk', 0.00, False), ('nak', 0.20, False)]),
    (1.56, [('kepuasan', 0.44, True), ('dalam', 1.26, False)]),
    (2.28, [('hidup,', 1.56, False)]),
    (3.02, [('tahan', 1.98, False), ('lama', 2.28, True), ('sekali,', 2.52, False)]),
    (4.02, [('kaum', 3.02, False), ('lelaki.', 3.16, True)]),
    (5.16, [('Aku', 4.02, False), ('perkenalkan', 4.12, False)]),
    (5.92, [('Tai', 5.16, True), ('Chi', 5.48, True)]),
    (6.78, [('Wellness', 5.92, True), ('Patch,', 6.34, True)]),
    (7.60, [('untuk', 6.78, False), ('meningkatkan', 6.88, False)]),
    (8.70, [('tenaga', 7.60, True), ('lelaki.', 8.00, False)]),
    (9.56, [('Cara', 8.70, False), ('nak', 8.86, False), ('pakai,', 9.08, False)]),
    (10.26, [('kita', 9.56, False), ('tampal', 9.70, True)]),
    (11.00, [('kat', 10.08, False), ('pinggang', 10.26, True), ('ni.', 10.70, False)]),
    (11.58, [('Waktu', 11.00, False), ('dia', 11.30, False)]),
    (12.62, [('sebelum', 11.58, False), ('tidur,', 12.04, True)]),
    (13.50, [('tampal', 12.62, False), ('saja.', 13.02, False)]),
    (14.22, [('Bangun', 13.50, False), ('tidur,', 13.78, False)]),
    (14.98, [('baru', 14.06, False), ('buka.', 14.22, True)]),
    (15.76, [('Mana', 14.98, False), ('yang', 15.26, False), ('rasa', 15.46, False)]),
    (16.68, [('dah', 15.76, False), ('lemah', 15.96, True), ('tu,', 16.28, False)]),
    (17.54, [('nak', 16.68, False), ('pulihkan', 16.80, True)]),
    (18.22, [('balik', 17.30, False), ('tenaga,', 17.54, True)]),
    (18.96, [('jawapan', 18.22, False), ('dia', 18.62, False)]),
    (20.16, [('sangat', 18.96, False), ('senang.', 19.42, True)]),
    (20.96, [('Tampal', 20.16, True), ('saja.', 20.48, False)]),
    (21.82, [('Berminat', 20.96, False), ('dengan', 21.38, False)]),
    (22.62, [('Tai', 21.82, True), ('Chi', 22.24, True)]),
    (23.80, [('Wellness', 22.62, True), ('Patch', 23.18, True), ('ni.', 23.46, False)]),
    (24.22, [('Dapatkan', 23.80, False), ('di', 24.12, False)]),
    (25.52, [('beg', 24.22, True), ('kuning.', 24.40, True)]),
]
HOOK = dict(end=8.7, y=100, kicker="patch lelaki untuk", title="tenaga",
            options=[("Kepuasan", "01"), ("Tahan lama", "02"), ("Tenaga lelaki", "03")], select_at=[0.44, 2.28, 7.60])
SECTIONS = [
    (8.7, 14.98, "kelebihan", "1 / 3", "cara pakai"),
    (14.98, 18.22, "kelebihan", "2 / 3", "pulih tenaga"),
    (18.22, 20.96, "kelebihan", "3 / 3", "senang"),
]
STICKERS = [  # (mula, tamat, teks, x, y, sudut)
    (10.26, 14.9, "tampal di pinggang", 50, 250, 2.0),
    (12.04, 14.9, "sebelum tidur", 80, 320, -1.5),
    (14.22, 14.9, "buka bila bangun", 110, 390, 1.5),
    (16.80, 18.15, "pulihkan tenaga", 50, 250, -2.0),
    (20.16, 20.92, "tampal saja ✓", 50, 250, -1.5),
]
CIRCLES = []
BIG_WORDS = []  # "senang." tutup muka di sini – dibuang
COVERS = [
    dict(at=35.0, kicker="Tai Chi Wellness Patch,", title="tenaga", stickers=["tampal di pinggang", "tampal saja ✓"], pill="kelebihan 1-3 · patch lelaki"),
    dict(at=35.6, kicker="Tai Chi Wellness Patch,", title="senang", stickers=["tampal sebelum tidur", "pulihkan tenaga ✓"], pill="kelebihan 1-3 · cara pakai"),
]
YELLOW = (255, 200, 40, 255)
# tajuk CTA disorok (title_y=-500): punch-in dekat, tajuk tutup muka
CTA = dict(title="tenaga", title_at=20.96, title_y=-500, card_at=21.3, card_y=1500,
           card_label="Tai Chi Wellness Patch", name="Tai Chi Wellness Patch",
           tags="tampal saja · tenaga lelaki",
           button="Tekan beg kuning ↓", button_color=YELLOW, button_text_color=(22, 22, 26, 255))
