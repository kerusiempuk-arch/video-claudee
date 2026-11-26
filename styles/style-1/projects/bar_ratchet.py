# Bar ratchet trak (Drive 1QTj62wG1AmvRvk-OEwvOcUzhnycu0aQ_) — salin fail ni, isi ikut video. Contoh lengkap: styles/style-1/projects/boxer.py. Bina: python3 -I styles/style-1/build.py <raw.mp4> <fail ini> <work_dir>
# ---------- potongan (build.py) – masa ikut video ASAL
REMOVE = [
    (23.40, 26.15),  # ulangan "kita lock,"
    (28.48, 29.22),  # ulangan "barang dalam bak,"
    (34.76, 35.32),  # "ok,"
    (38.40, 39.60),  # "okay,"
    (44.38, 45.25),  # "nah,"
]
SRC_END = 50.3        # potong selepas ni (orang keluar frame / kamera jatuh)
TAIL = 1.2            # hujung tak dipotong senyap — masa baca CTA (1.2s supaya kad CTA sempat dibaca)
PUNCH_Y = 0.25        # punch-in fokus ke atas (muka)

# ---------- overlay (build.py) – masa ikut video SELEPAS dipotong
END = 37.76
CAPTION_Y = 680       # atas, paras dada
CARD_Y = 1420
ZOOM = 0.04

W_ = lambda *ws: [(w, t, h) for w, t, h in ws]
CAPTIONS = [  # (group_end, [(perkataan, mula, highlight)])
    (1.76, W_(("Bar", 0.60, False), ("ratchet", 1.28, True))),
    (2.50, W_(("trak", 1.78, True))),
    (3.58, W_(("Fungsi", 2.54, False), ("benda", 2.86, False), ("ni", 3.06, False))),
    (4.30, W_(("kawal", 3.60, True), ("barang", 3.84, False))),
    (5.26, W_(("dalam", 4.14, False), ("baket", 4.34, False), ("supaya", 4.78, False))),
    (6.12, W_(("tak", 5.28, False), ("menggelongsor", 5.52, True))),
    (7.60, W_(("ke", 6.14, False), ("depan", 6.40, False), ("belakang", 6.82, False))),
    (9.40, W_(("Ini", 7.82, False), ("dia", 8.16, False), ("universal", 8.54, True))),
    (11.06, W_(("Boleh", 9.48, False), ("semua", 9.80, False), ("kenderaan", 10.24, True))),
    (12.06, W_(("untuk", 11.08, False), ("pikap", 11.34, True))),
    (13.40, W_(("Sebab", 12.08, False), ("boleh", 12.36, False), ("laras", 12.50, True))),
    (14.50, W_(("Nak", 13.56, False), ("pendekkan", 13.70, True))),
    (15.08, W_(("nak", 14.52, False), ("panjang", 14.60, True))),
    (16.70, W_(("Cara", 15.10, False), ("nak", 15.30, False), ("pasang", 15.52, True))),
    (19.30, W_(("kita", 16.76, False), ("letak", 17.10, False), ("macam ni", 17.72, False))),
    (20.98, W_(("Lepas", 19.38, False), ("tu", 19.60, False), ("lock", 20.10, True))),
    (21.80, W_(("dia", 21.02, False), ("akan", 21.14, False), ("ketat", 21.30, True))),
    (22.50, W_(("sendiri", 21.82, True))),
    (24.60, W_(("Barang", 22.90, False), ("dalam", 23.38, False), ("baket", 23.60, False))),
    (25.58, W_(("tak", 24.64, False), ("menggelongsor", 24.96, True))),
    (27.18, W_(("ke", 25.60, False), ("depan", 25.76, False), ("belakang", 26.62, False))),
    (28.24, W_(("Dah", 27.44, False), ("terhalang", 27.64, True))),
    (29.08, W_(("Nak", 28.26, False), ("buka", 28.56, True))),
    (30.80, W_(("buka", 29.24, False), ("lock", 30.06, True), ("ni", 30.28, False))),
    (32.50, W_(("akan", 31.28, False), ("terbuka", 31.48, True), ("sendiri", 32.12, False))),
    (34.80, W_(("Kita", 32.96, False), ("boleh", 33.92, False), ("kemas", 34.50, True))),
    (35.82, W_(("barang", 34.82, False), ("tak", 35.16, False), ("berkarat", 35.34, False))),
    (36.86, W_(("Berminat?", 35.84, False), ("dapatkan", 36.36, False))),
    (37.80, W_(("di", 36.74, False), ("beg", 36.88, True), ("ni", 37.18, False))),
]
HOOK = dict(end=7.6, y=100, kicker="barang dalam baket", title="terkawal",
            options=[("Kawal barang", "01"), ("Tak menggelongsor", "02")], select_at=[3.60, 5.52])
SECTIONS = [  # (mula, tamat, label, "n / 3", subtajuk)
    (7.6, 15.08, "kelebihan", "1 / 3", "universal & boleh laras"),
    (15.08, 28.24, "kelebihan", "2 / 3", "senang pasang"),
    (28.24, 35.84, "kelebihan", "3 / 3", "senang buka"),
]
STICKERS = [  # (mula, tamat, teks, x, y, sudut)
    (8.54, 15.0, "universal", 50, 250, 2.0),
    (11.34, 15.0, "semua pikap", 80, 320, -1.5),
    (12.50, 15.0, "boleh laras", 110, 390, 1.5),
    (20.10, 27.3, "lock je", 50, 250, 2.0),
    (21.30, 27.3, "ketat sendiri", 80, 320, -1.5),
    (24.96, 27.3, "tak menggelongsor", 110, 390, 1.5),
    (31.48, 35.8, "terbuka sendiri", 50, 250, 2.0),
    (34.50, 35.8, "senang kemas", 80, 320, -1.5),
]
CIRCLES = []
BIG_WORDS = [(27.5, 28.8, "terhalang", True)]
COVERS = []
CTA = dict(title="terkawal", title_at=35.84, title_y=230, card_at=36.2, card_y=1180,
           card_label="Bar Ratchet Trak", name="Bar Ratchet Trak", tags="universal · boleh laras · ketat sendiri",
           button="Tekan beg kuning ↓", button_color=(255, 200, 40, 255), button_text_color=(22, 22, 26, 255))
