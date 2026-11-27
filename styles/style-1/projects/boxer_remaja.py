# Boxer anak remaja (Drive 19Ul7aFTUp6kYMQdsLkuiPaOUopbhcLfC) — salin fail ni, isi ikut video. Contoh lengkap: styles/style-1/projects/boxer.py. Bina: python3 -I styles/style-1/build.py <raw.mp4> <fail ini> <work_dir>
# ---------- potongan (build.py) – masa ikut video ASAL
REMOVE = [
    (3.95, 4.45),    # "ah" lepas "anak remaja aku"
    (5.00, 5.34),    # "aa" sebelum "dah banyak dah"
    (7.12, 7.44),    # gagap "anak-anak-anak" -> "anak-anak"
    (8.97, 9.40),    # "aa" sebelum "pakai boxer"
    (10.88, 12.20),  # "okay" + "ah"
    (18.29, 18.55),  # "okay" lepas "selesa dipakai"
    (21.69, 21.92),  # "okay" sebelum "tak panas"
    (22.85, 25.95),  # "Pengudaraan pun… dengan" – cubaan pertama tak habis
    (28.45, 29.75),  # "lebih" pertama (ulang)
    (31.05, 32.60),  # "okay" + "ha"
]
SRC_END = 40.2        # potong selepas ni (orang keluar frame / kamera jatuh)
TAIL = 0.7            # hujung tak dipotong senyap — masa baca CTA (1.2s supaya kad CTA sempat dibaca)
PUNCH_Y = 0.25        # punch-in fokus ke atas (muka)

# ---------- overlay (build.py) – masa ikut video SELEPAS dipotong
END = 25.67            # tempoh selepas potongan (build.py --plan)
CAPTION_Y = 680       # atas, paras dada (pilihan user); kena muka -> 700–760
CARD_Y = 1420       # kad hook rendah supaya produk tak tertutup
ZOOM = 0.04
# CAPTION_ACCENT = (255, 212, 59, 255)   # paksa warna; default auto: baju/latar biru → kuning
# BRIGHTEN = "auto"   # video gelap (YAVG < 105) dicerahkan auto; atau {"exposure": 0.4, "shadows": 0.25, "blacks": 0.08}; None = matikan
# SFX_WHOOSH = "drop"  # ganti whoosh dengan titisan air (produk air / dapur / mesin basuh)
# DENOISE = True      # buang bunyi latar, kekalkan suara utama sahaja

CAPTIONS = [  # (group_end, [(perkataan, mula, highlight)]) – masa SELEPAS potong
    (1.64, [("Aku", 0.00, False), ("beli", 0.50, False), ("boxer", 0.84, True), ("ni", 1.16, False)]),
    (2.38, [("aku", 1.66, False), ("nak", 1.78, False), ("bagi", 1.90, False)]),
    (3.50, [("anak", 2.26, False), ("remaja", 2.62, True), ("aku", 3.12, False)]),
    (4.32, [("Dah", 3.52, False), ("banyak", 3.72, False), ("dah", 4.06, False)]),
    (5.32, [("daripada", 4.32, False), ("anak-anak", 4.68, True)]),
    (6.46, [("ke", 5.32, False), ("remaja", 5.56, True)]),
    (7.32, [("pakai", 6.48, False), ("boxer", 6.60, True)]),
    (8.60, [("Kain", 7.34, False), ("dia", 7.64, False), ("lembut", 8.00, True)]),
    (9.64, [("getah", 8.62, True), ("pinggang", 8.92, False), ("pun", 9.32, False)]),
    (10.36, [("lembut", 9.66, True)]),
    (11.80, [("selesa", 10.38, True), ("dipakai", 10.68, False)]),
    (12.54, [("Material", 11.82, False), ("dia", 12.08, False)]),
    (13.40, [("dipakai", 12.56, False)]),
    (14.60, [("sejuk", 13.42, True), ("sahaja", 13.88, False)]),
    (15.50, [("tak", 14.62, False), ("panas", 14.74, True)]),
    (16.76, [("Dengan", 15.52, False), ("pakai", 15.78, False), ("boxer", 16.04, False)]),
    (17.56, [("pengudaraan", 16.78, True)]),
    (18.90, [("lebih", 17.58, False), ("nyaman", 18.30, True)]),
    (20.12, [("selesa", 18.92, True), ("dipakai", 19.30, False)]),
    (21.18, [("Ada", 20.14, False), ("pelbagai", 20.28, False), ("saiz", 20.66, True)]),
    (22.22, [("ada", 21.20, False), ("pelbagai", 21.30, False), ("warna", 21.70, True)]),
    (23.80, [("Harga", 22.24, False), ("sangat-sangat", 22.78, False), ("murah", 23.30, True)]),
    (24.68, [("Berminat?", 23.82, False), ("dapatkan", 24.22, False)]),
    (25.67, [("di", 24.62, False), ("beg", 24.70, True), ("kuning", 24.86, True)]),
]
HOOK = dict(end=7.2, y=100, kicker="dari anak-anak ke remaja, semua pakai", title="boxer",
            options=[("Anak-anak", "01"), ("Remaja", "02")], select_at=[4.68, 5.56])
SECTIONS = [  # (mula, tamat, label, "1 / 3", subtajuk)
    (7.2, 11.7, "kelebihan", "1 / 3", "kain & getah lembut"),
    (11.7, 20.0, "kelebihan", "2 / 3", "sejuk & nyaman"),
    (20.0, 23.75, "kelebihan", "3 / 3", "saiz, warna & harga"),
]
STICKERS = [  # (mula, tamat, teks, x, y, sudut)
    (8.00, 11.6, "kain lembut", 50, 250, 2.0),
    (9.66, 11.6, "getah lembut", 80, 320, -1.5),
    (10.68, 11.6, "selesa ✓", 110, 390, 1.5),
    (13.42, 16.6, "sejuk", 50, 250, 2.0),
    (14.74, 16.6, "tak panas ✓", 80, 320, -1.5),
    (20.66, 23.7, "pelbagai saiz", 50, 250, -2.0),
    (21.70, 23.7, "pelbagai warna", 80, 320, 1.5),
    (23.30, 23.7, "harga murah ✓", 110, 390, -1.5),
]
CIRCLES = []
COVERS = []
BIG_WORDS = [(17.58, 19.9, "nyaman", True)]
CTA = dict(title="selesa", title_at=23.75, title_y=230, card_at=24.0, card_y=1180,
           card_label="Boxer Lelaki", name="Boxer Lelaki", tags="kain lembut · sejuk · murah",
           button="Tekan beg kuning ↓", button_color=(255, 200, 40, 255), button_text_color=(22, 22, 26, 255))
