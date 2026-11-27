# Paip sinki boleh laras (Drive 1WsnB4Ym1wN1RPo5H_S8TjNiAeNfK0Atq)
# ---------- potongan (build.py) – masa ikut video ASAL
REMOVE = [
    (0.0, 8.64),      # pembuka tak jelas ("macam mana nak tengok…", "sinki dah ber–")
    (12.88, 13.46),   # "okey?"
    (13.46, 15.00),   # "ikut kesesuaian" kali pertama
    (17.36, 18.16),   # "ha"
    (20.48, 21.74),   # "okay, …lah"
    (27.46, 28.06),   # "wah dia" (tergagap sebelum "one way")
    (28.78, 29.44),   # bunyi pendek
    (34.56, 35.42),   # "okay"
]
SRC_END = 39.6        # potong selepas ni (orang keluar frame / kamera jatuh)
TAIL = 1.2            # hujung tak dipotong senyap — masa baca CTA (1.2s supaya kad CTA sempat dibaca)
PUNCH_Y = 0.25        # punch-in fokus ke atas (muka)

# ---------- overlay (build.py) – masa ikut video SELEPAS dipotong
END = 24.04
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
    C_(8.58, ("di", 7.54, False), ("dalam", 7.92, False), ("ni", 8.22, False)),
    C_(9.36, ("Jadinya", 8.60, False), ("kita", 8.90, False), ("boleh", 9.18, False)),
    C_(10.30, ("nampak", 9.36, True), ("ada", 10.08, False)),
    C_(11.68, ("mendapan", 10.32, True), ("ataupun", 11.00, False)),
    C_(12.42, ("saluran", 11.70, False), ("ni", 12.20, False)),
    C_(13.20, ("tersumbat", 12.42, True)),
    C_(14.14, ("Lagi", 13.24, False), ("satu", 13.40, False), ("dia", 13.66, False), ("ada", 13.82, False)),
    C_(15.80, ("Anti", 14.76, False), ("odor", 15.10, True)),
    C_(16.50, ("anti", 15.82, False), ("bau", 15.98, True)),
    C_(17.70, ("Serangga", 16.54, True), ("tak", 16.82, False), ("dapat", 16.98, False), ("masuk", 17.16, False)),
    C_(18.60, ("bau", 17.78, False), ("daripada", 17.96, False), ("luar", 18.28, True)),
    C_(19.85, ("pun", 18.60, False), ("tak", 18.80, False), ("dapat", 19.00, False), ("masuk", 19.20, True)),
    C_(21.25, ("Bahan", 19.90, False), ("sangat", 20.30, False), ("padu", 20.70, True)),
    C_(22.45, ("sangat", 21.30, False), ("berkualiti", 21.54, True)),
]
HOOK = dict(end=4.45, y=100,
            kicker="paip sinki paling", title="senang",
            options=[("Boleh laras", "01"), ("Tarik pendek", "02"), ("Tarik panjang", "03")],
            select_at=[0.62, 2.80, 3.68])
SECTIONS = [
    (4.45, 6.75, "kelebihan", "1 / 3", "ikut saiz sinki"),
    (6.75, 13.20, "kelebihan", "2 / 3", "ada filter"),
    (13.20, 19.85, "kelebihan", "3 / 3", "one way, anti bau"),
]
STICKERS = [
    (4.70, 6.70, "laras ikut sinki", 80, 260, 2.0),
    (5.68, 6.70, "muat sinki rumah ✓", 130, 340, -1.5),
    (7.10, 10.20, "filter dalam", 80, 260, 2.0),
    (10.32, 13.15, "nampak mendapan", 80, 260, -1.5),
    (12.42, 13.15, "tahu bila tersumbat", 130, 340, 2.0),
    (15.10, 19.80, "anti odor", 80, 260, 2.0),
    (16.54, 19.80, "serangga tak masuk", 130, 340, -1.5),
    (17.96, 19.80, "bau luar tak masuk ✓", 180, 420, 1.5),
]
CIRCLES = []
BIG_WORDS = [  # (mula, tamat, perkataan, titik_merah)
    (14.16, 15.05, "one way", True),
]
CTA = dict(title="padu", title_at=19.90, title_y=230, card_at=20.60, card_y=1180,
           card_label="Paip Sinki", name="Paip Sinki Boleh Laras", tags="boleh laras · filter · anti bau",
           button="Tekan beg kuning ↓", button_color=(255, 200, 40, 255), button_text_color=(22, 22, 26, 255))

# ---------- cover photo (tools/cover.py) – `at` ikut masa video ASAL
COVERS = [
    dict(at=37.0, kicker="paip sinki,", title="laras",
         stickers=["tarik pendek / panjang", "ikut saiz sinki ✓"], pill="kelebihan 1-3 · paip sinki"),
    dict(at=11.5, kicker="paip sinki,", title="anti bau",
         stickers=["ada filter", "serangga tak masuk ✓"], pill="kelebihan 1-3 · one way, anti odor"),
]
