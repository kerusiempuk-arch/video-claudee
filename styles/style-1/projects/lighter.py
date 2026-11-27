# Lighter USB (Drive 1iTdm3rz80UD_pBfCmc48N6fUwwKUGBYz) — salin fail ni, isi ikut video. Contoh lengkap: styles/style-1/projects/boxer.py. Bina: python3 -I styles/style-1/build.py <raw.mp4> <fail ini> <work_dir>
# ---------- potongan (build.py) – masa ikut video ASAL
REMOVE = [
    (0.00, 2.70),  # bunyi klik lighter sebelum mula cakap
    (12.35, 12.95),  # jeda selepas "buang"
    (27.50, 28.10),  # "okey"
    (30.00, 31.05),  # jeda selepas "udara berangin"
    (31.08, 31.75),  # bunyi "aa" pendek sebelum "tiada"
]
SRC_END = 35.4        # potong selepas ni (orang keluar frame / kamera jatuh)
TAIL = 1.2            # hujung tak dipotong senyap — masa baca CTA (1.2s supaya kad CTA sempat dibaca)
PUNCH_Y = 0.25        # punch-in fokus ke atas (muka)

# ---------- overlay (build.py) – masa ikut video SELEPAS dipotong
END = 28.63
CAPTION_Y = 680       # atas, paras dada
CARD_Y = 1420
ZOOM = 0.04

W_ = lambda *ws: [(w, t, h) for w, t, h in ws]
CAPTIONS = [  # (group_end, [(perkataan, mula, highlight)])
    (1.48, W_(("Ini", 0.00, False), ("lighter", 0.82, False))),
    (2.40, W_(("yang", 1.22, False), ("biasa", 1.48, True))),
    (3.98, W_(("Ini", 2.60, False), ("yang", 2.76, False), ("terbaru", 3.02, True))),
    (4.64, W_(("Design", 4.22, False), ("pun", 4.32, False))),
    (6.20, W_(("sangat", 4.64, False), ("menarik", 5.10, True))),
    (7.90, W_(("Lighter", 6.38, False), ("ni", 6.52, False), ("pakai gas", 6.76, True))),
    (9.10, W_(("Habis", 8.26, False), ("gas", 8.52, True))),
    (9.80, W_(("buang", 9.22, True))),
    (10.90, W_(("Udara", 9.82, False), ("berangin", 10.16, True))),
    (12.20, W_(("tangan", 10.94, False), ("basah", 11.18, True))),
    (13.48, W_(("api", 12.24, False), ("tak", 12.42, False), ("hidup", 12.54, True))),
    (14.48, W_(("Kalau", 13.50, False), ("yang", 13.72, False), ("ni", 13.96, False))),
    (15.02, W_(("semua", 14.50, False), ("tu", 14.62, False))),
    (15.76, W_(("tak ada", 14.88, False), ("masalah", 15.22, True))),
    (17.00, W_(("Kita", 15.78, False), ("cas", 16.00, True), ("saja", 16.34, False))),
    (18.20, W_(("Ketahanan", 17.24, False), ("bateri", 17.70, True))),
    (19.30, W_(("sangat", 18.48, False), ("lama", 18.84, True))),
    (20.55, W_(("Cara", 19.38, False), ("guna", 19.60, True))),
    (21.22, W_(("kita", 20.60, False), ("tekan", 20.66, True))),
    (22.30, W_(("tolak", 21.34, False), ("ke", 21.54, False), ("belakang", 21.76, True))),
    (23.65, W_(("dia", 22.34, False), ("akan", 22.62, False), ("menyala", 22.88, True))),
    (24.60, W_(("Tangan", 23.70, False), ("basah", 23.98, True))),
    (25.60, W_(("udara", 24.66, False), ("berangin", 24.94, True))),
    (26.90, W_(("tiada", 25.64, False), ("masalah", 25.90, True))),
    (27.54, W_(("Berminat?", 26.94, False))),
    (28.63, W_(("klik", 27.56, False), ("beg", 27.70, True), ("kuning", 27.82, True))),
]
HOOK = dict(end=6.2, y=100, kicker="lighter yang", title="terbaru",
            options=[("Lighter biasa", "01"), ("Yang terbaru", "02")], select_at=[1.48, 3.02])
SECTIONS = [  # (mula, tamat, label, "n / 3", subtajuk)
    (13.50, 19.30, "kelebihan", "1 / 3", "tak pakai gas, cas saja"),
    (19.30, 23.65, "kelebihan", "2 / 3", "senang guna"),
    (23.65, 26.90, "kelebihan", "3 / 3", "tahan angin & tangan basah"),
]
STICKERS = [  # (mula, tamat, teks, x, y, sudut)
    (8.52, 13.4, "habis gas, buang", 50, 250, 2.0),
    (10.16, 13.4, "angin? tak hidup", 80, 320, -1.5),
    (11.18, 13.4, "tangan basah ✗", 110, 390, 1.5),
    (16.00, 19.2, "cas saja", 50, 250, 2.0),
    (17.70, 19.2, "bateri tahan lama", 80, 320, -1.5),
    (20.66, 23.5, "tekan", 50, 250, 2.0),
    (21.34, 23.5, "tolak ke belakang", 80, 320, -1.5),
    (24.94, 26.8, "tahan angin ✓", 50, 250, 2.0),
    (23.98, 26.8, "tangan basah ✓", 80, 320, -1.5),
]
CIRCLES = []
BIG_WORDS = [(6.76, 7.90, "pakai gas", True)]
COVERS = [  # at = masa video ASAL
    dict(at=8.2, kicker="lighter USB", title="terbaru",
         stickers=["cas saja", "tak pakai gas ✓"], pill="kelebihan 1-3 · bateri tahan lama"),
    dict(at=25.6, kicker="tangan basah, berangin,", title="menyala",
         stickers=["tekan & tolak", "tiada masalah ✓"], pill="kelebihan 1-3 · senang guna"),
]
CTA = dict(title="terbaru", title_at=26.94, title_y=230, card_at=27.1, card_y=1180,
           card_label="Lighter USB", name="Lighter USB", tags="cas saja · tahan angin · senang guna",
           button="Tekan beg kuning ↓", button_color=(255, 200, 40, 255), button_text_color=(22, 22, 26, 255))
