# Tai Chi Wellness Patch (Drive 1mhbqOpimAM3FUfH0iTdWyCqU0DKGjR2R)
# --- potongan (build.py), masa ikut video ASAL
REMOVE = [(0.0, 0.45), (4.87, 5.08), (8.70, 9.05), (11.12, 11.36), (17.06, 17.38)]  # "ah" awal, "ha", "okay" x3 antara ayat
SRC_END = 22.1
TAIL = 1.2
PUNCH_Y = 0.25
END = 19.13
CAPTION_Y = 1780
CARD_Y = 1180
ZOOM = 0.04
# (group_end, [(word, start, highlight)]) – masa ikut video SELEPAS dipotong
CAPTIONS = [
    (0.80, [("Kepada", 0.00, False), ("kaum", 0.62, False)]),
    (1.80, [("lelaki", 0.80, True), ("yang", 1.46, False)]),
    (2.36, [("ada", 1.80, False), ("rasa", 2.06, False)]),
    (3.16, [("lemah", 2.36, True), ("itu,", 2.88, False)]),
    (4.48, [("dah", 3.18, False), ("tak", 3.28, False), ("bermaya", 3.44, True)]),
    (5.60, [("cuba", 4.50, False), ("benda", 4.86, False), ("ni", 5.10, False)]),
    (6.36, [("Nah,", 5.68, False), ("ini", 5.74, False)]),
    (6.74, [("Tai", 6.02, True), ("Chi", 6.38, True)]),
    (7.60, [("Wellness", 6.74, True), ("Patch", 7.18, True)]),
    (8.66, [("Cara", 7.66, False), ("nak", 7.86, False), ("guna", 8.10, False)]),
    (9.74, [("sangat", 8.68, False), ("senang", 9.08, True)]),
    (10.48, [("Tampal", 9.76, True), ("saja", 10.18, False)]),
    (11.40, [("bahagian", 10.50, False), ("pinggang", 10.86, True)]),
    (12.06, [("kat", 11.24, False), ("belakang", 11.42, False), ("ni", 11.90, False)]),
    (13.50, [("sebelum", 12.08, False), ("tidur", 12.50, True), ("malam", 12.84, False)]),
    (14.28, [("Bangun", 13.62, False), ("tidur", 13.80, False)]),
    (15.00, [("baru", 14.12, False), ("buka", 14.30, True)]),
    (15.94, [("Hasil", 15.06, False), ("dia", 15.22, False), ("memang", 15.56, False)]),
    (17.14, [("sangat", 15.96, False), ("memuaskan", 16.24, True)]),
    (18.00, [("Berminat?", 17.18, False), ("dapatkan", 17.62, False)]),
    (19.13, [("di", 18.02, False), ("bakul", 18.12, True), ("ni", 18.36, False)]),
]
HOOK = dict(end=5.6, y=100, kicker="lelaki yang selalu rasa", title="lemah",
            options=[("Rasa lemah", "01"), ("Dah tak bermaya", "02")], select_at=[2.36, 3.44])
SECTIONS = [
    (5.6, 7.6, "kelebihan", "1 / 3", "kenali produk"),
    (7.6, 14.9, "kelebihan", "2 / 3", "cara guna"),
    (14.9, 17.14, "kelebihan", "3 / 3", "hasil"),
]
STICKERS = [  # (start, end, text, x, y, angle)
    (6.02, 7.55, "Tai Chi Wellness Patch", 50, 250, 2.0),
    (9.08, 11.9, "sangat senang", 50, 250, 2.0),
    (10.86, 11.9, "tampal di pinggang", 80, 320, -1.5),
    (12.5, 14.85, "sebelum tidur", 50, 250, -2.0),
    (14.12, 14.85, "buka bila bangun", 80, 320, 1.5),
    (16.24, 17.1, "sangat memuaskan", 50, 250, 2.0),
]
CIRCLES = []
YELLOW = (255, 200, 40, 255)
CTA = dict(title="memuaskan", title_at=17.14, title_y=230, card_at=17.4, card_y=1180,
           card_label="Tai Chi Wellness Patch", name="Tai Chi Wellness Patch",
           tags="mudah guna · sebelum tidur · memuaskan",
           button="Tekan bakul kuning ↓", button_color=YELLOW, button_text_color=(22, 22, 26, 255))
