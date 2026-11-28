# Beg kanvas tebal / beg alat (Drive 1AyTak4sNN0HgMBL35TI2W-UzXsUPEft7)
REMOVE = [
    (5.9, 6.95),    # "Zip." – permulaan yang diulang ("Tengok. Zip pun lancar…")
    (11.45, 12.85), # "Kanvas." – diulang dalam ayat penuh
]
SRC_END = 28.88
TAIL = 1.2
PUNCH_Y = 0.25
END = 22.78
CAPTION_Y = 680
CARD_Y = 1420
ZOOM = 0.04
CAPTIONS = [
    (0.76, [("Tengok", 0.00, False)]),
    (1.52, [("tali", 0.76, True), ("dia", 1.10, False), ("pun", 1.26, False)]),
    (2.20, [("kuat", 1.52, True)]),
    (2.82, [("Memang", 2.20, False), ("takkan", 2.54, False)]),
    (3.72, [("putus", 2.82, True), ("punya", 3.26, False)]),
    (4.26, [("Susah", 3.72, False), ("nak", 4.10, False)]),
    (5.28, [("putus", 4.26, True)]),
    (5.90, [("Tengok", 5.28, False)]),
    (6.42, [("zip", 5.90, True), ("pun", 6.04, False)]),
    (7.50, [("lancar", 6.42, True), ("saja", 6.94, False)]),
    (8.02, [("Tengok", 7.50, False), ("bahagian", 7.74, False)]),
    (8.86, [("dalam", 8.02, True)]),
    (9.30, [("Dia", 8.86, False), ("kain", 9.06, False)]),
    (10.20, [("kanvas", 9.30, True), ("yang", 9.70, False)]),
    (11.22, [("tebal", 10.20, True)]),
    (11.60, [("Letak", 11.22, False)]),
    (12.70, [("spanar", 11.60, True)]),
    (13.40, [("alat-alat", 12.70, False)]),
    (14.36, [("membaiki", 13.40, True)]),
    (14.70, [("ataupun", 14.36, False)]),
    (15.86, [("alat", 14.70, False), ("pertukangan", 15.08, True)]),
    (17.36, [("sangat", 15.86, False), ("sesuai", 16.36, True)]),
    (18.30, [("Lasak", 17.36, True), ("beg", 17.80, False), ("ni", 17.90, False)]),
    (19.38, [("Dia", 18.30, False), ("heavy", 18.46, True), ("duty", 18.72, True)]),
    (20.12, [("Berminat", 19.38, False), ("dengan", 19.72, False)]),
    (21.08, [("beg", 20.12, False), ("kanvas", 20.36, True), ("yang", 20.82, False)]),
    (21.70, [("tebal", 21.08, True), ("ni", 21.42, False)]),
    (22.18, [("Dapatkan", 21.70, False), ("di", 22.06, False)]),
    (22.78, [("beg", 22.18, True), ("kuning", 22.30, True)]),
]
HOOK = dict(end=5.2, y=100, kicker="beg kanvas paling", title="lasak",
            options=[("Tali kuat", "01"), ("Takkan putus", "02")], select_at=[0.76, 2.82])
SECTIONS = [  # (mula, tamat, label, "n / 3", subtajuk)
    (5.2, 8.8, "kelebihan", "1 / 3", "zip lancar"),
    (8.8, 11.1, "kelebihan", "2 / 3", "kanvas tebal"),
    (11.1, 17.3, "kelebihan", "3 / 3", "sesuai alat pertukangan"),
]
STICKERS = [  # (mula, tamat, teks, x, y, sudut)
    (5.90, 8.7, "zip lancar ✓", 50, 250, 2.0),
    (7.74, 8.7, "ruang dalam", 80, 320, -1.5),
    (9.30, 11.0, "kain kanvas tebal ✓", 50, 250, 2.0),
    (11.60, 17.2, "spanar", 50, 260, 2.0),
    (13.40, 17.2, "alat membaiki", 80, 340, -1.5),
    (15.08, 17.2, "alat pertukangan ✓", 110, 420, 1.5),
    (17.36, 19.3, "lasak ✓", 50, 250, 2.0),
    (18.46, 19.3, "heavy duty ✓", 80, 320, -1.5),
]
CIRCLES = []
COVERS = [  # A = muka + produk, B = beg terbuka
    dict(at=26.0, kicker="beg kanvas paling,", title="lasak",
         stickers=["tali kuat", "kanvas tebal ✓"], pill="kelebihan 1-3 · Beg Kanvas"),
    dict(at=12.0, kicker="letak alat pertukangan,", title="lasak",
         stickers=["zip lancar", "heavy duty ✓"], pill="kelebihan 1-3 · Beg Kanvas"),
]
BIG_WORDS = []  # "lasak." besar tutup muka (muka di atas frame masa ni) → guna sticker
YELLOW = (255, 200, 40, 255)
CTA = dict(title="tebal", title_at=19.38, title_y=230, card_at=20.12, card_y=1180,
           card_label="Beg Kanvas", name="Beg Kanvas",
           tags="tali kuat · zip lancar · heavy duty",
           button="Tekan beg kuning ↓", button_color=YELLOW, button_text_color=(22, 22, 26, 255))
