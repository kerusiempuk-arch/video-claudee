# Paip sinki boleh laras (Drive 1WsnB4Ym1wN1RPo5H_S8TjNiAeNfK0Atq)
# ---------- potongan (build.py) – masa ikut video ASAL
REMOVE = [
    (0.0, 8.64),      # pembuka tak jelas ("macam mana nak tengok…", "sinki dah ber–")
    (12.88, 13.46),   # "okey?"
    (13.46, 15.00),   # "ikut kesesuaian" kali pertama
    (17.36, 18.16),   # "ha"
    (20.48, 21.02),   # "okay" (simpan "lutsinar")
    (27.46, 28.06),   # "wah dia" (tergagap sebelum "one way")
    (28.78, 29.44),   # bunyi pendek
    (34.56, 35.42),   # "okay"
]
SRC_END = 39.6        # potong selepas ni (orang keluar frame / kamera jatuh)
TAIL = 1.2            # hujung tak dipotong senyap — masa baca CTA (1.2s supaya kad CTA sempat dibaca)
PUNCH_Y = 0.25        # punch-in fokus ke atas (muka)

# ---------- overlay (build.py) – masa ikut video SELEPAS dipotong
END = 24.76
CAPTION_Y = 680
CARD_Y = 1420
ZOOM = 0.04
SFX_WHOOSH = "drop"   # produk sinki / air

C_ = lambda end, *ws: (end, [(w, t, h) for w, t, h in ws])
CAPTIONS = [
    C_(1.02, ("Boleh", 0.00, False), ("nak", 0.36, False), ("laras", 0.62, True)),
    C_(2.10, ("kat", 1.02, False), ("sini", 1.20, False)),
    C_(3.20, ("nak", 2.26, False), ("tarik", 2.32, False), ("pendek", 2.80, True)),
    C_(4.40, ("nak", 3.28, False), ("tarik", 3.36, False), ("panjang", 3.68, True)),
    C_(5.32, ("Ikut", 4.58, False), ("kesesuaian", 4.70, True)),
    C_(6.70, ("lubang", 5.32, False), ("sinki", 5.68, True), ("rumah", 5.96, False)),
    C_(7.54, ("Dia", 6.80, False), ("ada", 6.90, False), ("filter", 7.10, True)),
    C_(8.56, ("di", 7.54, False), ("dalam", 7.92, False), ("ni", 8.22, False)),
    C_(9.30, ("lutsinar", 8.58, True)),
    C_(10.08, ("Jadinya", 9.32, False), ("kita", 9.62, False), ("boleh", 9.90, False)),
    C_(11.02, ("nampak", 10.08, True), ("ada", 10.80, False)),
    C_(12.40, ("mendapan", 11.04, True), ("ataupun", 11.72, False)),
    C_(13.14, ("saluran", 12.42, False), ("ni", 12.92, False)),
    C_(13.92, ("tersumbat", 13.14, True)),
    C_(14.86, ("Lagi", 13.96, False), ("satu", 14.12, False), ("dia", 14.38, False), ("ada", 14.54, False)),
    C_(16.52, ("Anti", 15.48, False), ("odor", 15.82, True)),
    C_(17.22, ("anti", 16.54, False), ("bau", 16.70, True)),
    C_(18.42, ("Serangga", 17.26, True), ("tak", 17.54, False), ("dapat", 17.70, False), ("masuk", 17.88, False)),
    C_(19.32, ("bau", 18.50, False), ("daripada", 18.68, False), ("luar", 19.00, True)),
    C_(20.57, ("pun", 19.32, False), ("tak", 19.52, False), ("dapat", 19.72, False), ("masuk", 19.92, True)),
    C_(21.97, ("Bahan", 20.62, False), ("sangat", 21.02, False), ("padu", 21.42, True)),
    C_(23.17, ("sangat", 22.02, False), ("berkualiti", 22.26, True)),
]
HOOK = dict(end=4.45, y=100,
            kicker="paip sinki paling", title="senang",
            options=[("Boleh laras", "01"), ("Tarik pendek", "02"), ("Tarik panjang", "03")],
            select_at=[0.62, 2.80, 3.68])
SECTIONS = [
    (4.45, 6.75, "kelebihan", "1 / 3", "ikut saiz sinki"),
    (6.75, 13.92, "kelebihan", "2 / 3", "ada filter"),
    (13.92, 20.57, "kelebihan", "3 / 3", "one way, anti bau"),
]
STICKERS = [
    (4.70, 6.70, "laras ikut sinki", 80, 260, 2.0),
    (5.68, 6.70, "muat sinki rumah ✓", 130, 340, -1.5),
    (7.10, 10.92, "filter dalam", 80, 260, 2.0),
    (8.58, 10.92, "lutsinar ✓", 130, 340, -1.5),
    (11.04, 13.87, "nampak mendapan", 80, 260, -1.5),
    (13.14, 13.87, "tahu bila tersumbat", 130, 340, 2.0),
    (15.82, 20.52, "anti odor", 80, 260, 2.0),
    (17.26, 20.52, "serangga tak masuk", 130, 340, -1.5),
    (18.68, 20.52, "bau luar tak masuk ✓", 180, 420, 1.5),
]
CIRCLES = []
BIG_WORDS = [  # (mula, tamat, perkataan, titik_merah)
    (14.88, 15.77, "one way", True),
]
CTA = dict(title="padu", title_at=20.62, title_y=230, card_at=21.32, card_y=1180,
           card_label="Paip Sinki", name="Paip Sinki Boleh Laras", tags="boleh laras · filter · anti bau",
           button="Tekan beg kuning ↓", button_color=(255, 200, 40, 255), button_text_color=(22, 22, 26, 255))

# ---------- cover photo (tools/cover.py) – `at` ikut masa video ASAL
COVERS = [
    dict(at=37.0, kicker="paip sinki,", title="laras",
         stickers=["tarik pendek / panjang", "ikut saiz sinki ✓"], pill="kelebihan 1-3 · paip sinki"),
    dict(at=11.5, kicker="paip sinki,", title="anti bau",
         stickers=["filter lutsinar", "serangga tak masuk ✓"], pill="kelebihan 1-3 · one way, anti odor"),
]
