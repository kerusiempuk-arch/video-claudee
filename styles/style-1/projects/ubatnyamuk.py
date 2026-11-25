# Tapak lingkaran nyamuk (Drive 1I3FFA6XKHs3kLlPMqg3A2NPhazRqTi2s)
REMOVE = [
    (1.80, 2.85),    # "Okay"
    (7.74, 7.92),    # "haa" (nafas)
    (19.20, 19.58),  # "haa"
    (29.00, 31.75),  # "okay, haa, dengan nyamuk.. dia" – mula palsu
    (33.30, 33.64),  # "okey"
    (34.75, 35.35),  # "okey"
]
SRC_END = 37.2
TAIL = 1.2
PUNCH_Y = 0.25
END = 28.77           # build.py --plan
CAPTION_Y = 680
CARD_Y = 1180
ZOOM = 0.04

CAPTIONS = [  # masa ikut video SELEPAS dipotong
    (1.84, [('Ini', 0.02, False), ('lingkaran', 0.74, True), ('nyamuk.', 1.46, False)]),
    (2.62, [('Tengok', 1.84, False), ('lain', 2.12, False), ('daripada', 2.34, False)]),
    (3.20, [('lain.', 2.62, False)]),
    (4.14, [('Dia', 3.20, False), ('melendik', 3.50, True), ('ke', 3.96, False)]),
    (5.12, [('bawah', 4.14, False), ('macam', 4.48, False), ('ni.', 4.76, False)]),
    (6.38, [('Ini', 5.12, False), ('sangat', 5.32, False), ('berkesan.', 5.60, True)]),
    (7.24, [('Dia', 6.38, False), ('punya', 6.54, False), ('tapak', 6.72, False)]),
    (7.66, [('dia.', 7.24, False)]),
    (8.48, [('Kita', 7.66, False), ('nak', 7.84, False), ('pasang,', 8.04, False)]),
    (9.02, [('dia', 8.48, False), ('ada', 8.60, False), ('empat', 8.78, True)]),
    (9.92, [('kaki.', 9.02, False)]),
    (11.08, [('Dia', 9.92, False), ('punya', 10.36, False), ('bekas', 10.56, True)]),
    (11.40, [('dia.', 11.08, False)]),
    (12.30, [('Jadi,', 11.40, False)]),
    (13.50, [('letak', 12.38, False), ('macam', 12.88, False), ('ni,', 13.14, False)]),
    (14.50, [('dia', 13.50, False), ('lebih', 13.58, False), ('stabil.', 13.78, True)]),
    (15.20, [('Sebabnya', 14.50, False), ('dia', 14.90, False), ('ada', 15.02, False)]),
    (16.04, [('empat', 15.20, True), ('kaki.', 15.46, False)]),
    (17.08, [('Kalau', 16.04, False), ('yang', 16.28, False), ('tapak', 16.64, False)]),
    (18.16, [('lingkaran', 17.08, True), ('nyamuk', 17.60, False), ('yang', 17.90, False)]),
    (18.80, [('biasa,', 18.16, False)]),
    (19.54, [('dia', 18.80, False), ('ada', 18.94, False), ('satu', 19.10, True)]),
    (20.30, [('saja.', 19.54, False)]),
    (20.92, [('Lepas', 20.30, False), ('tu,', 20.46, False)]),
    (22.10, [('ini', 20.92, False), ('yang', 21.20, False), ('spesialnya.', 21.42, True)]),
    (23.10, [('Dia', 22.10, False), ('lebih', 22.26, False), ('panjang', 22.50, True)]),
    (24.62, [('berbanding', 23.10, False), ('yang', 23.64, False), ('biasa.', 23.82, False)]),
    (25.88, [('Dengan', 24.62, False), ('menggunakannya,', 25.00, False)]),
    (26.96, [('dia', 25.88, False), ('lebih', 26.00, False), ('stabil.', 26.28, True)]),
    (27.44, [('Berminat?', 26.96, False)]),
    (28.06, [('Dapatkan', 27.44, False), ('di', 27.86, False), ('beg', 27.98, False)]),
    (28.60, [('kuning.', 28.06, True)]),
]
HOOK = dict(end=3.0, y=100, kicker="tapak lingkaran nyamuk paling", title="stabil",
            options=[("Tapak biasa", "01"), ("Tapak 4 kaki", "02")], select_at=[1.0, 2.1])
SECTIONS = [
    (3.0, 9.8, "kelebihan", "1 / 3", "melendik ke bawah"),
    (9.8, 20.2, "kelebihan", "2 / 3", "4 kaki, lebih stabil"),
    (20.2, 24.5, "kelebihan", "3 / 3", "lebih panjang"),
]
STICKERS = [
    (3.5, 9.7, "melendik ke bawah", 70, 300, 2.0),
    (5.3, 9.7, "sangat berkesan", 110, 370, -1.5),
    (8.8, 9.7, "4 kaki", 150, 440, 1.5),
    (10.4, 20.1, "ada bekas", 70, 300, -2.0),
    (13.6, 20.1, "lebih stabil", 110, 370, 1.5),
    (18.9, 20.1, "biasa: 1 kaki je", 150, 440, -1.5),
    (22.3, 24.4, "lebih panjang", 70, 300, 2.0),
    (23.1, 24.4, "berbanding biasa", 110, 370, -1.5),
]
CIRCLES = []
YELLOW = (255, 200, 40, 255)
CTA = dict(title="stabil", title_at=24.5, title_y=230, card_at=26.9, card_y=1180,
           card_label="Tapak Lingkaran Nyamuk", name="Tapak Lingkaran Nyamuk",
           tags="4 kaki · stabil · ada bekas",
           button="Tekan beg kuning ↓", button_color=YELLOW, button_text_color=(22, 22, 26, 255))
