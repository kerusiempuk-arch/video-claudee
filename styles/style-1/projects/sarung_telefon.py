# Sarung telefon kalis air (Drive 19abmcEMpGkjFkFmxbjrKhqx-Yf7B8StS)
REMOVE = [
    (9.88, 10.07),   # "Okay,"
    (13.04, 13.26),  # "Okay,"
    (15.28, 16.72),  # "Okay. Dengan ini," (permulaan tak jadi)
    (22.28, 22.64),  # "Okay,"
    (25.80, 27.88),  # "selagi plastik ini tak akan..." (cubaan pertama)
    (32.40, 33.05),  # "Okey,"
]
SRC_END = 45.0
TAIL = 1.2
PUNCH_Y = 0.25

END = 35.62
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
    C_(14.60, ("dengan", 12.64, False), ("naik", 13.78, False), ("telefon", 13.96, True)),
    C_(15.76, ("Naik", 14.98, False), ("motor", 15.20, True)),
    C_(16.95, ("ada", 15.76, False), ("sarung", 16.12, True), ("macam ni", 16.42, False)),
    C_(18.40, ("Bawa", 17.54, False), ("motor", 17.78, True)),
    C_(19.80, ("letak", 18.72, False), ("telefon", 18.94, True), ("dalam ni", 19.32, False)),
    C_(20.40, ("selamat", 19.80, True)),
    C_(21.62, ("Selagi", 20.42, False), ("plastik", 21.06, True), ("ni", 21.46, False)),
    C_(22.20, ("tak", 21.62, False), ("koyak", 21.80, True)),
    C_(22.86, ("tak", 22.22, False), ("bocor", 22.38, True)),
    C_(24.30, ("telefon", 22.92, False), ("takkan", 23.26, False), ("basah", 23.70, True)),
    C_(25.40, ("Nak", 24.40, False), ("cas", 24.60, True), ("pun", 24.92, False)),
    C_(26.36, ("bahagian", 25.48, False), ("bawah", 25.64, True), ("ni", 26.06, False)),
    C_(27.34, ("dia", 26.34, False), ("ada", 26.62, False), ("lubang", 26.76, True)),
    C_(29.16, ("ada", 27.62, False), ("tempat", 27.86, True), ("untuk", 28.20, False)),
    C_(30.55, ("nak", 29.16, False), ("masuk", 29.42, False), ("wire cable", 29.68, True)),
    C_(31.74, ("Harga", 30.50, False), ("sangat-sangat", 31.10, False)),
    C_(32.22, ("murah", 31.74, True)),
    C_(33.42, ("Barang", 32.20, False), ("simple", 32.50, True), ("saja", 32.88, False)),
    C_(34.36, ("Berminat", 33.40, False), ("dapatkan", 33.98, False)),
    C_(35.62, ("di", 34.34, False), ("beg", 34.44, True), ("kuning", 34.56, True)),
]
HOOK = dict(end=6.80, y=100,
            kicker="sarung telefon,", title="waterproof",
            options=[("Simple sahaja", "01"), ("Waterproof", "02"), ("Transparent", "03")],
            select_at=[2.14, 4.02, 5.84])
SECTIONS = [
    (6.80, 14.90, "kelebihan", "1 / 3", "senang guna"),
    (14.90, 24.30, "kelebihan", "2 / 3", "selamat naik motor"),
    (24.30, 30.50, "kelebihan", "3 / 3", "boleh cas"),
]
STICKERS = [
    (6.88, 8.60, "masuk telefon ↓", 80, 260, 2.0),
    (10.00, 12.64, "2 button", 80, 260, 2.0),
    (11.60, 12.64, "tutup rapat ✓", 130, 340, -1.5),
    (14.98, 17.40, "naik motor", 80, 260, 2.0),
    (16.12, 17.40, "sarung macam ni", 130, 340, -1.5),
    (20.42, 24.24, "tak koyak", 80, 260, 2.0),
    (22.22, 24.24, "tak bocor", 130, 340, -1.5),
    (23.70, 24.24, "tak basah ✓", 110, 420, 1.5),
    (24.40, 27.30, "boleh cas", 80, 260, 2.0),
    (27.62, 30.45, "lubang wire ✓", 130, 340, -1.5),
]
CIRCLES = []
BIG_WORDS = [  # (mula, tamat, perkataan, titik_merah)
    (18.72, 20.38, "selamat", True),
]
CTA = dict(title="murah", title_at=30.50, title_y=230, card_at=31.10, card_y=1180,
           card_label="Sarung Telefon", name="Sarung Telefon Waterproof", tags="waterproof · boleh cas · murah",
           button="Tekan beg kuning ↓", button_color=(255, 200, 40, 255), button_text_color=(22, 22, 26, 255))

# ---------- cover photo (tools/cover.py) – `at` ikut masa video ASAL
COVERS = [
    dict(at=1.2, kicker="sarung telefon,", title="waterproof",
         stickers=["simple sahaja", "tak bocor ✓"], pill="kelebihan 1-3 · selamat naik motor"),
    dict(at=24.0, kicker="naik motor, telefon", title="selamat",
         stickers=["tak koyak, tak bocor", "telefon tak basah ✓"], pill="kelebihan 1-3 · boleh cas"),
]
