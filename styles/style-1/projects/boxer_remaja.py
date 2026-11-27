# Boxer anak remaja (Drive 19Ul7aFTUp6kYMQdsLkuiPaOUopbhcLfC) — salin fail ni, isi ikut video. Contoh lengkap: styles/style-1/projects/boxer.py. Bina: python3 -I styles/style-1/build.py <raw.mp4> <fail ini> <work_dir>
# ---------- potongan (build.py) – masa ikut video ASAL
REMOVE = [
    (3.95, 4.45),    # "ah" lepas "anak remaja aku"
    (4.95, 6.60),    # "aa" + "dah banyak dah" (owner minta potong)
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
END = 24.95            # tempoh selepas potongan (build.py --plan)
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
    (3.60, [("anak", 2.26, False), ("remaja", 2.62, True), ("aku", 3.12, False)]),
    (4.60, [("Dari", 3.68, False), ("anak-anak", 3.96, True)]),
    (5.74, [("ke", 4.60, False), ("remaja", 4.84, True)]),
    (6.60, [("pakai", 5.76, False), ("boxer", 5.88, True)]),
    (7.88, [("Kain", 6.62, False), ("dia", 6.92, False), ("lembut", 7.28, True)]),
    (8.92, [("getah", 7.90, True), ("pinggang", 8.20, False), ("pun", 8.60, False)]),
    (9.64, [("lembut", 8.94, True)]),
    (11.08, [("selesa", 9.66, True), ("dipakai", 9.96, False)]),
    (11.82, [("Material", 11.10, False), ("dia", 11.36, False)]),
    (12.68, [("dipakai", 11.84, False)]),
    (13.88, [("sejuk", 12.70, True), ("sahaja", 13.16, False)]),
    (14.78, [("tak", 13.90, False), ("panas", 14.02, True)]),
    (16.04, [("Dengan", 14.80, False), ("pakai", 15.06, False), ("boxer", 15.32, False)]),
    (16.84, [("pengudaraan", 16.06, True)]),
    (18.18, [("lebih", 16.86, False), ("nyaman", 17.58, True)]),
    (19.40, [("selesa", 18.20, True), ("dipakai", 18.58, False)]),
    (20.46, [("Ada", 19.42, False), ("pelbagai", 19.56, False), ("saiz", 19.94, True)]),
    (21.50, [("ada", 20.48, False), ("pelbagai", 20.58, False), ("warna", 20.98, True)]),
    (23.08, [("Harga", 21.52, False), ("sangat-sangat", 22.06, False), ("murah", 22.58, True)]),
    (23.96, [("Berminat?", 23.10, False), ("dapatkan", 23.50, False)]),
    (24.95, [("di", 23.90, False), ("beg", 23.98, True), ("kuning", 24.14, True)]),
]
HOOK = dict(end=6.48, y=100, kicker="dari anak-anak ke remaja, semua pakai", title="boxer",
            options=[("Anak-anak", "01"), ("Remaja", "02")], select_at=[3.96, 4.84])
SECTIONS = [  # (mula, tamat, label, "1 / 3", subtajuk)
    (6.48, 10.98, "kelebihan", "1 / 3", "kain & getah lembut"),
    (10.98, 19.28, "kelebihan", "2 / 3", "sejuk & nyaman"),
    (19.28, 23.03, "kelebihan", "3 / 3", "saiz, warna & harga"),
]
STICKERS = [  # (mula, tamat, teks, x, y, sudut)
    (7.28, 10.88, "kain lembut", 50, 250, 2.0),
    (8.94, 10.88, "getah lembut", 80, 320, -1.5),
    (9.96, 10.88, "selesa ✓", 110, 390, 1.5),
    (12.70, 15.88, "sejuk", 50, 250, 2.0),
    (14.02, 15.88, "tak panas ✓", 80, 320, -1.5),
    (19.94, 22.98, "pelbagai saiz", 50, 250, -2.0),
    (20.98, 22.98, "pelbagai warna", 80, 320, 1.5),
    (22.58, 22.98, "harga murah ✓", 110, 390, -1.5),
]
CIRCLES = []
COVERS = []
BIG_WORDS = [(16.86, 19.18, "nyaman", True)]
CTA = dict(title="selesa", title_at=23.03, title_y=230, card_at=23.28, card_y=1180,
           card_label="Boxer Lelaki", name="Boxer Lelaki", tags="kain lembut · sejuk · murah",
           button="Tekan beg kuning ↓", button_color=(255, 200, 40, 255), button_text_color=(22, 22, 26, 255))
