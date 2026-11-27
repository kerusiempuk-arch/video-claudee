# Kasut Sneakers (sarung / slip-on) (Drive 1fkk9NGAqalfUfC9e6ljhbvyXnGCqjDNw)
# ---------- potongan (build.py) – masa ikut video ASAL
REMOVE = [
    (0.00, 2.25),    # "Ah, dek." (awal)
    (6.36, 7.28),    # "okey. Ha,"
    (11.04, 11.46),  # "Ha,"
    (12.38, 20.96),  # "okey. Hmm… Tepi saja. Kenapa nak buat video ni? Okey, ha,"
    (23.36, 23.88),  # "Ha,"
    (27.80, 28.74),  # "okey. Ah,"
    (30.22, 31.74),  # "susah nak licin" (owner minta buang)
    (32.76, 32.98),  # "okay"
    (34.40, 34.88),  # "Okay,"
]
SRC_END = 39.2
TAIL = 1.2
PUNCH_Y = 0.25

# ---------- overlay – masa ikut video SELEPAS dipotong
END = 21.83
CAPTION_Y = 680
CARD_Y = 1420
ZOOM = 0.04

C_ = lambda end, *ws: (end, [(w, t, h) for w, t, h in ws])
CAPTIONS = [
    C_(1.04, ("Tengok", 0.00, False), ("kasut", 0.46, False)),
    C_(2.10, ("simple", 1.04, True), ("sahaja", 1.60, False)),
    C_(3.06, ("sarung", 2.32, True), ("macam", 2.56, False), ("tu", 2.86, False)),
    C_(3.95, ("sahaja", 3.06, False), ("nak", 3.32, False), ("pakai", 3.48, False)),
    C_(5.00, ("nak", 4.02, False), ("pergi", 4.14, False), ("jalan-jalan", 4.30, True)),
    C_(6.35, ("nak", 5.20, False), ("pergi", 5.24, False), ("kedai", 5.40, True)),
    C_(7.18, ("naik", 6.46, False), ("motor", 6.54, True)),
    C_(8.05, ("sangat", 7.20, False), ("sesuai", 7.46, True)),
    C_(8.95, ("pakai", 8.14, False), ("naik", 8.34, False), ("motor", 8.46, False)),
    C_(10.35, ("ada", 9.20, False), ("pelbagai", 9.34, False), ("saiz", 9.78, True)),
    C_(11.40, ("warna", 10.48, False), ("aku", 10.80, False), ("punya", 11.02, False)),
    C_(12.90, ("warna", 11.82, False), ("hitam", 12.42, True)),
    C_(14.00, ("ada", 12.98, False), ("warna", 13.28, False), ("biru", 13.54, True)),
    C_(15.12, ("tapak", 14.16, False), ("anti-slip", 14.50, True)),
    C_(16.14, ("dia", 15.20, False), ("tak", 15.34, True), ("licin", 15.50, True)),
    C_(17.58, ("nak", 16.30, False), ("pakai", 16.38, False), ("sarung", 16.74, True), ("sahaja", 17.28, False)),
]
HOOK = dict(end=8.05, y=100, kicker="kasut sneakers,", title="simple",
            options=[("Jalan-jalan", "01"), ("Pergi kedai", "02"), ("Naik motor", "03")],
            select_at=[4.30, 5.40, 6.54])
SECTIONS = [
    (8.05, 10.45, "kelebihan", "1 / 3", "pelbagai saiz"),
    (10.45, 14.10, "kelebihan", "2 / 3", "hitam & biru"),
    (14.10, 17.58, "kelebihan", "3 / 3", "tapak anti-slip"),
]
STICKERS = [
    (9.34, 10.40, "pelbagai saiz", 80, 260, 2.0),
    (12.42, 14.05, "hitam ✓", 80, 260, 2.0),
    (13.54, 14.05, "biru ✓", 130, 340, -1.5),
    (14.50, 16.12, "tapak anti-slip", 80, 260, 2.0),
    (15.34, 16.12, "tak licin ✓", 130, 340, -1.5),
]
CIRCLES = []
BIG_WORDS = [  # (mula, tamat, perkataan, titik_merah)
    (16.74, 17.54, "sarung", True),
]
CTA = dict(title="simple", title_at=17.58, title_y=470, card_at=17.72, card_y=1180,
           card_label="Kasut Sneakers", name="Kasut Sneakers", tags="sarung · anti-slip · pelbagai saiz",
           button="Tekan beg kuning ↓", button_color=(255, 200, 40, 255), button_text_color=(22, 22, 26, 255))

# ---------- cover photo (tools/cover.py) – `at` ikut masa video ASAL
COVERS = [
    dict(at=36.0, kicker="kasut sneakers,", title="simple", shift=250,
         stickers=["sarung saja", "tapak anti-slip ✓"], pill="kelebihan 1-3 · kasut sneakers"),
    dict(at=30.0, kicker="tapak anti-slip,", title="tak licin",
         stickers=["hitam & biru", "pelbagai saiz ✓"], pill="kelebihan 1-3 · kasut sneakers"),
]
