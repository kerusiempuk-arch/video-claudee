# Hos / getah buang air mesin basuh 3 meter (Drive 1CFBVSQjClOS7NgjrQylHtqGjw3hyLSL6)
REMOVE = [
    (0.00, 1.10),    # "ha" pembuka
    (4.40, 11.00),   # "okay. Siap bagi pengikat dia lagi, okay. Kita tengok ia asal. Ha, ni ia asal." (pengikat diulang di hujung)
    (13.00, 13.26),  # "ha"
    (16.40, 16.56),  # "ha"
    (22.10, 22.30),  # "ha"
    (23.10, 23.42),  # "okay"
    (24.82, 26.36),  # "kat bahagian, ha," -> "banjir kat sini"
    (26.78, 31.97),  # + "okay"
    (37.39, 37.59),  # "okay"  # "Jadi dengan air ini, air dia terus masuk ke lubang air buang" – diulang lengkap lepas ni
]
SRC_END = 43.3
TAIL = 1.2
PUNCH_Y = 0.25

END = 24.20
CAPTION_Y = 680
CARD_Y = 1180
ZOOM = 0.04

CAPTIONS = [  # masa ikut video SELEPAS dipotong (Whisper atas cut.wav)
    (0.92, [("Getah", 0.00, False), ("mesin", 0.60, False)]),
    (1.96, [("basuh", 0.92, True), ("rumah", 1.24, False), ("aku", 1.56, False)]),
    (2.64, [("yang", 1.98, False), ("aku", 2.28, False), ("baru", 2.46, False)]),
    (3.28, [("dapat", 2.64, False)]),
    (4.04, [("Yang", 3.30, False), ("asal", 3.58, False), ("dia", 3.86, False)]),
    (5.06, [("pendek", 4.04, True), ("saja", 4.48, False)]),
    (6.40, [("Yang", 5.08, False), ("baru", 5.22, False), ("ni", 5.64, False)]),
    (6.94, [("panjang", 6.42, True), ("dia", 6.62, False)]),
    (8.34, [("3", 6.94, True), ("meter", 7.26, True)]),
    (9.10, [("Sebabnya", 8.36, False)]),
    (9.74, [("yang", 9.12, False), ("asal", 9.42, False)]),
    (10.42, [("dia", 9.74, False), ("pendek", 9.96, True)]),
    (11.16, [("dia", 10.44, False), ("tak", 10.58, False), ("sampai", 10.74, True)]),
    (12.24, [("ke", 11.18, False), ("lubang", 11.36, False), ("air", 11.72, False)]),
    (13.08, [("Jadinya", 12.26, False)]),
    (13.84, [("buang", 13.10, False), ("air", 13.26, False)]),
    (14.24, [("dia", 13.86, False), ("akan", 14.02, False)]),
    (15.28, [("banjir", 14.26, True), ("kat", 14.66, False), ("sini", 14.82, False)]),
    (15.76, [("Air", 15.30, False), ("daripada", 15.42, False)]),
    (16.56, [("mesin", 15.78, False), ("basuh", 16.04, False)]),
    (17.18, [("dia", 16.58, False), ("akan", 16.78, False), ("terus", 17.02, True)]),
    (18.00, [("masuk", 17.20, False), ("ke", 17.60, False)]),
    (18.78, [("lubang", 18.02, False), ("salur", 18.44, True)]),
    (19.60, [("air", 18.80, False), ("buang", 19.00, False)]),
    (20.76, [("Sangat", 19.62, False), ("panjang", 19.86, True)]),
    (21.28, [("Siap", 20.78, False), ("bagi", 21.02, False)]),
    (22.28, [("pengikat", 21.30, True), ("dia", 21.78, False), ("lagi", 21.94, False)]),
    (22.90, [("Berminat?", 22.30, False)]),
    (23.32, [("dapatkan", 22.92, False), ("di", 23.24, False)]),
    (24.20, [("beg", 23.34, True), ("kuning", 23.48, True)]),
]
HOOK = dict(end=8.34, y=100, kicker="hos mesin basuh paling", title="panjang",
            options=[("Hos asal (pendek)", "01"), ("Hos baru 3 meter", "02")], select_at=[3.30, 6.42])
SECTIONS = [
    (8.34, 19.60, "kelebihan", "1 / 3", "sampai lubang air"),
    (19.60, 20.76, "kelebihan", "2 / 3", "sangat panjang"),
    (20.76, 22.28, "kelebihan", "3 / 3", "siap pengikat"),
]
STICKERS = [  # (mula, tamat, teks, x, y, sudut)
    (9.96, 15.28, "pendek = banjir", 50, 250, 2.0),
    (17.02, 19.58, "terus ke salur", 50, 250, -2.0),
    (18.44, 19.58, "tak banjir lagi", 80, 320, 1.5),
    (19.86, 20.74, "3 meter", 50, 250, 2.0),
    (21.30, 22.26, "siap pengikat", 50, 250, -2.0),
]
CIRCLES = []
YELLOW = (255, 200, 40, 255)
CTA = dict(title="panjang", title_at=22.28, title_y=230, card_at=22.50, card_y=1180,
           card_label="Hos Mesin Basuh", name="Hos Mesin Basuh 3m",
           tags="3 meter · siap pengikat",
           button="Tekan beg kuning ↓", button_color=YELLOW, button_text_color=(22, 22, 26, 255))
