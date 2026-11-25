# Rod kimpalan (Drive 1bKW_CD-lVRjxruOR-4VN384RQmA9cGoL) — salin fail ni, isi ikut video. Contoh lengkap: styles/style-1/projects/boxer.py. Bina: python3 -I styles/style-1/build.py <raw.mp4> <fail ini> <work_dir>
# ---------- potongan (build.py) – masa ikut video ASAL
REMOVE = [
    (13.28, 14.16),  # "okey" + "aa" sebelum "kalau kat kedai"
    (16.45, 20.36),  # "beli ini saja" kali kedua – ulangan
    (24.50, 25.95),  # "okey" + "berminat" pertama – gagap
]
SRC_END = 29.87        # potong selepas ni (orang keluar frame / kamera jatuh)
TAIL = 1.2            # hujung tak dipotong senyap — masa baca CTA (1.2s supaya kad CTA sempat dibaca)
PUNCH_Y = 0.25        # punch-in fokus ke atas (muka)

# ---------- overlay (build.py) – masa ikut video SELEPAS dipotong
END = 22.54            # tempoh selepas potongan (build.py --plan)
CAPTION_Y = 680       # atas, paras dada (pilihan user); kena muka -> 700–760
CARD_Y = 1180
ZOOM = 0.04
# CAPTION_ACCENT = (255, 212, 59, 255)   # paksa warna; default auto: baju/latar biru → kuning
# BRIGHTEN = "auto"   # video gelap (YAVG < 105) dicerahkan auto; atau {"exposure": 0.4, "shadows": 0.25, "blacks": 0.08}; None = matikan
# DENOISE = True      # buang bunyi latar, kekalkan suara utama sahaja

CAPTIONS = [  # (group_end, [(perkataan, mula, highlight)]) — masa ikut cut.wav
    (0.96, [("Tengok,", 0.00, False)]),
    (1.98, [("rod", 0.98, False), ("kimpalan", 1.14, True)]),
    (3.40, [("100", 2.04, True), ("batang", 2.30, False), ("semua", 2.80, False)]),
    (4.48, [("siap", 3.56, False), ("bagi", 3.94, False)]),
    (5.08, [("dalam", 4.50, False), ("bekas", 4.70, True)]),
    (5.70, [("macam", 5.10, False), ("ni.", 5.38, False)]),
    (6.36, [("Lebih", 5.76, False), ("kemas,", 5.98, True)]),
    (7.45, [("lebih", 6.40, False), ("tersusun.", 6.58, True)]),
    (8.74, [("Nak", 7.52, False), ("buat", 7.72, False), ("DIY,", 8.06, True)]),
    (10.00, [("welding", 8.82, True), ("sendiri,", 9.14, False)]),
    (11.36, [("beli", 10.40, False), ("ini", 10.64, False), ("saja.", 10.84, False)]),
    (12.00, [("Sangat", 11.42, False), ("murah", 11.72, True)]),
    (12.62, [("harga", 12.00, False), ("dia.", 12.40, False)]),
    (13.40, [("Kalau", 12.66, False), ("kat", 12.84, False), ("kedai", 13.00, True)]),
    (13.88, [("tak", 13.40, False), ("dapat", 13.54, False)]),
    (14.90, [("harga", 13.88, True), ("macam", 14.20, False), ("ni.", 14.44, False)]),
    (15.46, [("Tambah", 15.02, False), ("pula", 15.26, False)]),
    (16.30, [("sekarang", 15.46, False), ("ni,", 15.88, False)]),
    (17.70, [("harga", 16.38, False), ("tengah", 16.50, False), ("promosi,", 16.80, True)]),
    (18.86, [("lagi-lagilah", 17.78, False), ("murah.", 18.28, True)]),
    (19.70, [("Berminat", 18.90, False), ("dengan", 19.32, False)]),
    (20.92, [("rod", 19.70, False), ("kimpalan", 20.02, True), ("ni,", 20.58, False)]),
    (21.38, [("dapatkan", 20.96, False), ("dia", 21.24, False)]),
    (22.54, [("beg", 21.38, True), ("kuning.", 21.54, True)]),
]
HOOK = dict(end=7.45, y=100,
            kicker="rod kimpalan paling", title="murah",
            options=[("Siap dalam bekas", "01"), ("Lebih tersusun", "02")], select_at=[3.56, 6.40])
SECTIONS = [  # (mula, tamat, "kelebihan", "1 / 3", subtajuk)
    (7.45, 11.36, "kelebihan", "1 / 3", "DIY sendiri"),
    (11.36, 14.90, "kelebihan", "2 / 3", "harga murah"),
    (14.90, 18.86, "kelebihan", "3 / 3", "harga promosi"),
]
STICKERS = [  # (mula, tamat, teks, x, y, sudut)
    (8.06, 11.3, "welding sendiri", 50, 250, 2.0),
    (10.40, 11.3, "beli ni je", 80, 320, -1.5),
    (11.72, 14.85, "sangat murah", 50, 250, 2.0),
    (13.88, 14.85, "kedai tak dapat harga ni", 80, 320, -1.5),
    (16.80, 18.80, "harga promosi", 50, 250, -2.0),
    (18.28, 18.80, "lagi murah", 80, 320, 1.5),
]
CIRCLES = []
CTA = dict(title="murah", title_at=18.86, title_y=230, card_at=19.2, card_y=1180,
           card_label="Rod Kimpalan", name="Rod Kimpalan", tags="kemas · DIY · harga promosi",
           button="Tekan beg kuning ↓", button_color=(255, 200, 40, 255), button_text_color=(22, 22, 26, 255))
