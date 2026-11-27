# Sarung telefon kalis air (Drive 19abmcEMpGkjFkFmxbjrKhqx-Yf7B8StS)
REMOVE = [
    (9.88, 10.07),   # "Okay,"
    (13.04, 13.26),  # "Okay,"
    (15.28, 19.70),  # "Okay. Dengan ini, dengan ada ni naik telefon" (sebutan kurang sesuai – owner)
    (22.28, 22.64),  # "Okay,"
    (25.80, 27.88),  # "selagi plastik ini tak akan..." (cubaan pertama)
    (32.40, 33.05),  # "Okey,"
]
SRC_END = 45.0
TAIL = 1.2
PUNCH_Y = 0.25

END = 33.38
CAPTION_Y = 760  # orang duduk rendah, 680 kena mulut
CARD_Y = 1420
ZOOM = 0.04
# SFX_WHOOSH = "drop"

C_ = lambda end, *ws: (end, [(w, t, h) for w, t, h in ws])
CAPTIONS = [
    C_(1.30, ("Sarung", 0.00, False), ("telefon", 0.60, True)),
    C_(2.10, ("Tengok", 1.34, False)),
    C_(3.20, ("simple", 2.14, True), ("sahaja", 2.60, False)),
    C_(5.40, ("tapi", 3.20, False), ("waterproof", 4.02, True)),
    C_(6.84, ("Dia", 5.48, False), ("transparent", 5.84, True)),
    C_(8.62, ("Masukkan", 6.88, False), ("telefon", 7.52, True), ("dalam", 7.94, False)),
    C_(9.95, ("Kemudian", 8.66, False), ("button", 9.48, True)),
    C_(11.20, ("Dia", 10.00, False), ("ada", 10.12, False), ("2 button", 10.24, True)),
    C_(12.66, ("Kita", 11.60, False), ("buttonkan", 11.60, True)),
    C_(13.52, ("Naik", 12.74, False), ("motor", 12.96, True)),
    C_(14.71, ("ada", 13.52, False), ("sarung", 13.88, True), ("macam ni", 14.18, False)),
    C_(16.16, ("Bawa", 15.30, False), ("motor", 15.54, True)),
    C_(17.56, ("letak", 16.48, False), ("telefon", 16.70, True), ("dalam ni", 17.08, False)),
    C_(18.16, ("selamat", 17.56, True)),
    C_(19.38, ("Selagi", 18.18, False), ("plastik", 18.82, True), ("ni", 19.22, False)),
    C_(19.96, ("tak", 19.38, False), ("koyak", 19.56, True)),
    C_(20.62, ("tak", 19.98, False), ("bocor", 20.14, True)),
    C_(22.06, ("telefon", 20.68, False), ("takkan", 21.02, False), ("basah", 21.46, True)),
    C_(23.16, ("Nak", 22.16, False), ("cas", 22.36, True), ("pun", 22.68, False)),
    C_(24.12, ("bahagian", 23.24, False), ("bawah", 23.40, True), ("ni", 23.82, False)),
    C_(25.10, ("dia", 24.10, False), ("ada", 24.38, False), ("lubang", 24.52, True)),
    C_(26.92, ("ada", 25.38, False), ("tempat", 25.62, True), ("untuk", 25.96, False)),
    C_(28.31, ("nak", 26.92, False), ("masuk", 27.18, False), ("wire cable", 27.44, True)),
    C_(29.50, ("Harga", 28.26, False), ("sangat-sangat", 28.86, False)),
    C_(29.98, ("murah", 29.50, True)),
    C_(31.18, ("Barang", 29.96, False), ("simple", 30.26, True), ("saja", 30.64, False)),
    C_(32.12, ("Berminat", 31.16, False), ("dapatkan", 31.74, False)),
    C_(33.38, ("di", 32.10, False), ("beg", 32.20, True), ("kuning", 32.32, True)),
]
HOOK = dict(end=6.80, y=100,
            kicker="sarung telefon,", title="waterproof",
            options=[("Simple sahaja", "01"), ("Waterproof", "02"), ("Transparent", "03")],
            select_at=[2.14, 4.02, 5.84])
SECTIONS = [
    (6.80, 12.66, "kelebihan", "1 / 3", "senang guna"),
    (12.66, 22.06, "kelebihan", "2 / 3", "selamat naik motor"),
    (22.06, 28.26, "kelebihan", "3 / 3", "boleh cas"),
]
STICKERS = [
    (6.88, 8.60, "masuk telefon ↓", 80, 260, 2.0),
    (10.00, 12.64, "2 button", 80, 260, 2.0),
    (11.60, 12.64, "tutup rapat ✓", 130, 340, -1.5),
    (12.74, 15.16, "naik motor", 80, 260, 2.0),
    (13.88, 15.16, "sarung macam ni", 130, 340, -1.5),
    (18.18, 22.00, "tak koyak", 80, 260, 2.0),
    (19.98, 22.00, "tak bocor", 130, 340, -1.5),
    (21.46, 22.00, "tak basah ✓", 110, 420, 1.5),
    (22.16, 25.06, "boleh cas", 80, 260, 2.0),
    (25.38, 28.21, "lubang wire ✓", 130, 340, -1.5),
]
CIRCLES = []
BIG_WORDS = [  # (mula, tamat, perkataan, titik_merah)
    (16.48, 18.14, "selamat", True),
]
CTA = dict(title="murah", title_at=28.26, title_y=230, card_at=28.86, card_y=1180,
           card_label="Sarung Telefon", name="Sarung Telefon Waterproof", tags="waterproof · boleh cas · murah",
           button="Tekan beg kuning ↓", button_color=(255, 200, 40, 255), button_text_color=(22, 22, 26, 255))

# ---------- cover photo (tools/cover.py) – `at` ikut masa video ASAL
COVERS = [
    dict(at=1.2, kicker="sarung telefon,", title="waterproof",
         stickers=["simple sahaja", "tak bocor ✓"], pill="kelebihan 1-3 · selamat naik motor"),
    dict(at=24.0, kicker="naik motor, telefon", title="selamat",
         stickers=["tak koyak, tak bocor", "telefon tak basah ✓"], pill="kelebihan 1-3 · boleh cas"),
]
