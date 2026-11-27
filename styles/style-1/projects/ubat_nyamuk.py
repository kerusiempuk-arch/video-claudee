# Ubat nyamuk lingkar / Mosquito Coils (Drive 1fUypndqjY9jzFl0ppzh1xcY3DY-_LJzJ) — salin fail ni, isi ikut video. Contoh lengkap: styles/style-1/projects/boxer.py. Bina: python3 -I styles/style-1/build.py <raw.mp4> <fail ini> <work_dir>
# ---------- potongan (build.py) – masa ikut video ASAL
REMOVE = [
    (0.00, 0.58),    # "Ha,"
    (5.08, 5.36),    # "Ha,"
    (7.12, 8.20),    # "Okay. Ha,"
    (12.54, 13.36),  # "Ha,"
    (16.46, 17.56),  # "Ha, okay."
    (19.04, 20.14),  # "Okay. Ha,"
    (23.60, 24.72),  # "Ha,"
    (27.08, 27.24),  # "Ha,"
    (27.80, 28.92),  # "Ah / okay"
    (30.06, 31.58),  # "aa.. oke"
    (34.00, 36.56),  # senyap + bunyi pendek
    (38.71, 38.94),  # "Okey,"
]
SRC_END = 41.6        # potong selepas ni (orang keluar frame / kamera jatuh)
TAIL = 1.2            # hujung tak dipotong senyap — masa baca CTA (1.2s supaya kad CTA sempat dibaca)
PUNCH_Y = 0.25        # punch-in fokus ke atas (muka)

# ---------- overlay (build.py) – masa ikut video SELEPAS dipotong
END = 27.03            # tempoh selepas potongan (build.py --plan)
CAPTION_Y = 760       # atas, paras dada (pilihan user); kena muka -> 700–760
CARD_Y = 1420       # kad hook rendah supaya produk tak tertutup
ZOOM = 0.04
# CAPTION_ACCENT = (255, 212, 59, 255)   # paksa warna; default auto: baju/latar biru → kuning
# BRIGHTEN = "auto"   # video gelap (YAVG < 105) dicerahkan auto; atau {"exposure": 0.4, "shadows": 0.25, "blacks": 0.08}; None = matikan
# SFX_WHOOSH = "drop"  # ganti whoosh dengan titisan air (produk air / dapur / mesin basuh)
# DENOISE = True      # buang bunyi latar, kekalkan suara utama sahaja

C_ = lambda end, *ws: (end, [(w, t, h) for w, t, h in ws])
CAPTIONS = [
    C_(0.72, ("Yang", 0.00, False), ("mana", 0.20, False), ("suka", 0.50, False)),
    C_(1.48, ("lepak-lepak", 0.74, True)),
    C_(2.58, ("sama", 1.50, False), ("kawan-kawan", 1.78, False)),
    C_(3.50, ("terutama", 2.62, False), ("sekali", 2.98, False)),
    C_(4.50, ("waktu", 3.52, False), ("malam", 3.74, True), ("tu", 4.16, False)),
    C_(5.84, ("Ini", 4.52, False), ("mosquito", 5.08, True), ("coil", 5.40, True)),
    C_(7.28, ("Tengok", 5.88, False), ("dia", 6.16, False), ("punya", 6.28, False), ("lingkaran", 6.56, True)),
    C_(8.48, ("Dia", 7.32, False), ("pun", 7.32, False), ("lain", 7.58, False), ("pada", 7.80, False), ("lain", 8.08, False)),
    C_(9.68, ("Dia", 8.54, False), ("melengkung", 8.70, True), ("ke", 9.12, False), ("bawah", 9.30, False)),
    C_(10.90, ("Dia", 9.72, False), ("punya", 9.84, False), ("stand", 10.10, True)),
    C_(12.44, ("ada", 11.10, False), ("empat", 11.30, True), ("kaki", 11.56, True), ("macam", 12.00, False), ("ni", 12.26, False)),
    C_(13.90, ("Jadinya", 12.48, False), ("lebih", 13.14, False), ("stabil", 13.36, True)),
    C_(14.88, ("Kalau", 13.94, False), ("yang", 14.06, False), ("biasa", 14.28, False)),
    C_(16.10, ("dia", 15.02, False), ("tegang", 15.18, True), ("ke", 15.58, False), ("atas", 15.80, False)),
    C_(17.08, ("Macam", 16.12, False), ("tu", 16.44, False), ("saja", 16.66, False)),
    C_(18.90, ("Beli", 17.14, False), ("ni", 17.40, False), ("siap", 17.76, False), ("bagi", 17.94, True), ("lagi", 18.46, False)),
    C_(19.74, ("Sangat", 19.00, False), ("banyak", 19.32, True)),
    C_(21.88, ("Selain", 20.84, False), ("pada", 21.20, False), ("nyamuk", 21.40, True)),
    C_(23.06, ("dia", 21.90, False), ("dapat", 22.02, False), ("mencegah", 22.32, True)),
    C_(24.98, ("serangga", 23.08, True), ("terbang", 23.92, False), ("lain-lain", 24.26, False)),
]
HOOK = dict(end=5.84, y=100,
            kicker="ubat nyamuk paling,", title="stabil",
            options=[("Lepak sama kawan", "01"), ("Waktu malam", "02"), ("Mosquito coil", "03")],
            select_at=[0.74, 3.52, 5.08])
SECTIONS = [
    (5.88, 9.72, "kelebihan", "1 / 3", "lingkaran lain"),
    (9.72, 17.10, "kelebihan", "2 / 3", "stand 4 kaki"),
    (17.10, 25.20, "kelebihan", "3 / 3", "sangat banyak"),
]
STICKERS = [
    (6.56, 9.66, "lingkaran lain", 70, 300, 2.0),
    (8.70, 9.66, "melengkung ke bawah", 110, 370, -1.5),
    (12.46, 13.90, "stand 4 kaki", 70, 300, 2.0),
    (13.36, 13.90, "lebih stabil ✓", 110, 370, -1.5),
    (14.28, 17.06, "yang biasa: tegang ke atas", 70, 300, -2.0),
    (17.94, 19.74, "beli siap bagi", 70, 300, 2.0),
    (19.32, 19.74, "sangat banyak", 110, 370, -1.5),
    (21.40, 24.96, "halau nyamuk", 70, 300, 2.0),
    (22.32, 24.96, "+ serangga terbang", 110, 370, -1.5),
]
CIRCLES = []
BIG_WORDS = [
    (11.30, 12.46, "4 kaki", True),
    (19.78, 20.82, "20 koil", True),
]
COVERS = [
    dict(at=6.6, kicker="ubat nyamuk lingkaran,", title="stabil",
         stickers=["stand 4 kaki", "20 koil ✓"], pill="kelebihan 1-3 · mosquito coil"),
    dict(at=15.5, kicker="lingkaran melengkung,", title="stabil",
         stickers=["halau nyamuk", "+ serangga terbang ✓"], pill="kelebihan 1-3 · mosquito coil"),
]
CTA = dict(title="stabil", title_at=25.20, title_y=230, card_at=25.40, card_y=1180,
           card_label="Mosquito Coils", name="Mosquito Coils", tags="melengkung · 4 kaki · 20 koil",
           button="Tekan beg kuning ↓", button_color=(255, 200, 40, 255), button_text_color=(22, 22, 26, 255))
