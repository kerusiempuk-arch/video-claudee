# Perangkap tikus / pelekat tikus (Drive 1bsnwtcVPV-fZCMcflWjUK9bCKvgFKAaR). Bina: python3 -I styles/style-1/build.py <raw.mp4> <fail ini> <work_dir>
# ---------- potongan (build.py) – masa ikut video ASAL
REMOVE = [
    (1.34, 1.86),    # "aa"
    (7.48, 7.82),    # "aa"
    (9.04, 9.40),    # "aa"
    (12.70, 13.76),  # "aa, okey, aa"
    (16.24, 16.58),  # "aa"
    (19.02, 19.28),  # "okey"
    (21.30, 22.74),  # "dia pijak kat sini. aa" (ulangan – simpan yang lengkap)
    (25.90, 26.94),  # "okey. ha"
    (29.41, 29.61),  # "okay"
]
SRC_END = 35.4
TAIL = 1.2
PUNCH_Y = 0.25

# ---------- overlay (build.py) – masa ikut video SELEPAS dipotong
END = 27.50
CAPTION_Y = 680
CARD_Y = 1420
ZOOM = 0.04
W_ = lambda *ws: [(w, t, h) for w, t, h in ws]
CAPTIONS = [  # (group_end, [(perkataan, mula, highlight)])
    (1.28, W_(("Perangkap", 0.00, False), ("tikus", 0.68, True))),
    (2.42, W_(("cara", 1.28, False), ("nak", 1.62, False), ("guna", 1.82, False))),
    (3.30, W_(("sangat", 2.42, False), ("senang", 2.74, True))),
    (4.26, W_(("Tanpa", 3.34, False), ("menggunakan", 3.66, False))),
    (5.20, W_(("bahan", 4.26, False), ("kimia", 4.48, True))),
    (6.60, W_(("tanpa", 5.22, False), ("racun", 5.86, True))),
    (7.70, W_(("Kita", 6.68, False), ("buka", 6.86, False), ("sahaja", 7.22, True))),
    (8.30, W_(("getah", 7.76, False), ("dia", 8.02, False))),
    (8.90, W_(("sangat", 8.30, False), ("kuat", 8.62, True))),
    (9.40, W_(("melekat", 9.04, True))),
    (10.50, W_(("Nah", 9.42, False), ("kita", 9.58, False), ("letak", 9.78, True))),
    (11.16, W_(("di", 10.52, False), ("tempat-tempat", 10.68, False))),
    (12.08, W_(("yang", 11.16, False), ("kita", 11.32, False), ("jangka", 11.62, False))),
    (13.10, W_(("laluan", 12.08, False), ("tikus", 12.30, True))),
    (13.70, W_(("Contohnya", 13.26, False))),
    (14.60, W_(("kat", 13.74, False), ("belakang", 13.98, False), ("rumah", 14.30, True))),
    (15.50, W_(("ni", 14.60, False), ("kita", 14.76, False), ("letak", 15.00, False))),
    (16.30, W_(("Nanti", 15.58, False), ("tikus", 15.76, True))),
    (17.08, W_(("dia", 16.32, False), ("akan", 16.56, False), ("datang", 16.74, False))),
    (17.56, W_(("Dia", 17.10, False), ("pijak", 17.26, True))),
    (18.14, W_(("kat", 17.56, False), ("bahagian", 17.74, False))),
    (18.95, W_(("yang", 18.14, False), ("bergetah", 18.28, True))),
    (19.80, W_(("dia", 19.00, False), ("akan", 19.16, False), ("melekat", 19.36, True))),
    (20.06, W_(("Tengok", 19.84, False))),
    (21.00, W_(("sekali", 20.06, False), ("beli", 20.44, True))),
    (21.58, W_(("banyak", 21.08, False), ("pieces", 21.14, True))),
    (22.26, W_(("dia", 21.58, False), ("bagi", 21.78, False))),
    (22.76, W_(("Harga", 22.30, False), ("pun", 22.66, False))),
    (23.44, W_(("sangat", 22.76, False), ("murah", 23.04, True))),
    (24.36, W_(("Berminat", 23.48, False), ("dengan", 23.84, False))),
    (25.48, W_(("pelekat", 24.36, False), ("tikus", 24.70, True), ("ni", 25.16, False))),
    (25.96, W_(("dapatkan", 25.52, False), ("di", 25.84, False))),
    (27.50, W_(("beg", 25.96, True), ("kuning", 26.08, True))),
]
HOOK = dict(end=6.6, y=100, kicker="perangkap tikus,", title="senang",
            options=[("Tanpa bahan kimia", "01"), ("Tanpa racun", "02")], select_at=[4.48, 5.86])
SECTIONS = [  # (mula, tamat, label, "n / 3", subtajuk)
    (6.68, 9.40, "kelebihan", "1 / 3", "getah sangat kuat"),
    (9.42, 19.80, "kelebihan", "2 / 3", "letak di laluan tikus"),
    (19.84, 23.44, "kelebihan", "3 / 3", "banyak pieces, murah"),
]
STICKERS = [  # (mula, tamat, teks, x, y, sudut)
    (7.22, 9.30, "buka sahaja", 50, 250, 2.0),
    (8.62, 9.30, "getah kuat ✓", 80, 320, -1.5),
    (12.30, 17.00, "laluan tikus", 50, 250, 2.0),
    (13.98, 17.00, "belakang rumah", 80, 320, -1.5),
    (17.26, 18.95, "tikus pijak", 50, 250, 2.0),
    (20.44, 23.40, "sekali beli", 50, 250, 2.0),
    (21.14, 23.40, "banyak pieces", 80, 320, -1.5),
]
CIRCLES = []
BIG_WORDS = []  # "melekat" besar tutup muka – dibuang
COVERS = []
CTA = dict(title="murah", title_at=23.48, title_y=230, card_at=23.6, card_y=1180,
           card_label="Pelekat Tikus", name="Pelekat Tikus", tags="tanpa racun · getah kuat · murah",
           button="Tekan beg kuning ↓", button_color=(255, 200, 40, 255), button_text_color=(22, 22, 26, 255))
