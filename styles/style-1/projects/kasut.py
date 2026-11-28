# Kasut kain jaring tapak getah (Drive 12nYVeOH7TsBZ-3rZFqZtsTWmxqDIgoAj)
# ---------- potongan (build.py) – masa ikut video ASAL
REMOVE = [
    (0.00, 0.32),   # "aa"
    (2.00, 3.46),   # "okey. aa"
    (4.92, 5.36),   # gagap "dia,"
    (6.10, 6.48),   # "aa"
    (7.60, 8.70),   # "okey. aa" (8.74 = "ta"-pak)
    (22.30, 23.24), # "okey. aa"
]
SRC_END = 33.0
TAIL = 1.2
PUNCH_Y = 0.25

END = 22.56
CAPTION_Y = 680
CARD_Y = 1420
ZOOM = 0.04

W_ = lambda *ws: [(w, t, h) for w, t, h in ws]
CAPTIONS = [  # (group_end, [(perkataan, mula, highlight)])
    (0.82, W_(("Tengok", 0.00, False), ("kasut", 0.34, True))),
    (1.78, W_(("lain", 0.84, False), ("daripada", 1.08, False), ("lain", 1.36, True))),
    (2.74, W_(("Bahagian", 1.80, False), ("cover", 2.38, True))),
    (3.52, W_(("dia", 2.76, False), ("berlubang", 3.04, True))),
    (4.84, W_(("Tengok", 3.54, False), ("ini", 3.90, False), ("pun sama", 4.12, True))),
    (6.28, W_(("Tapak", 4.86, False), ("dia", 5.22, False), ("bergetah", 5.60, True))),
    (7.56, W_(("anti-slip", 6.30, True))),
    (8.44, W_(("Jalan", 7.02, False), ("kat tempat", 7.58, False), ("basah", 7.94, True))),
    (9.46, W_(("dia", 8.46, False), ("tak", 8.56, False), ("licin", 8.72, True))),
    (10.28, W_(("Bahagian", 9.48, False), ("dalam", 9.60, False))),
    (11.18, W_(("dia", 10.04, False), ("ada", 10.30, False), ("span", 10.48, True))),
    (12.40, W_(("Ini", 11.20, False), ("kita", 11.32, False), ("boleh buka", 11.68, True))),
    (13.04, W_(("pek", 12.40, False), ("dia", 12.62, False))),
    (13.86, W_(("Kalau", 13.06, False), ("kotor", 13.28, True))),
    (14.68, W_(("boleh", 13.88, False), ("basuh", 14.02, True))),
    (15.40, W_(("Kasut", 14.70, False), ("ini", 14.96, False))),
    (16.90, W_(("ada", 15.42, False), ("pelbagai", 15.82, False), ("warna", 16.20, True))),
    (18.26, W_(("ada", 16.92, False), ("pelbagai", 17.02, False), ("saiz", 17.40, True))),
    (19.52, W_(("Berminat", 18.28, False), ("dengan", 18.70, False))),
    (20.48, W_(("kasut", 19.54, False), ("yang", 20.06, False), ("sangat", 20.24, False))),
    (21.30, W_(("selesa", 20.50, True), ("ni", 20.86, False))),
    (22.56, W_(("Dapatkan", 21.32, False), ("di", 21.62, False), ("beg kuning", 21.76, True))),
]
HOOK = dict(end=1.78, y=100, kicker="kasut", title="lain",
            options=[("Kasut biasa", "01"), ("Lain daripada lain", "02")], select_at=[0.34, 1.36])
SECTIONS = [  # (mula, tamat, label, "n / 3", subtajuk)
    (1.80, 4.84, "kelebihan", "1 / 3", "cover berlubang"),
    (4.84, 9.46, "kelebihan", "2 / 3", "tapak getah, anti-slip"),
    (9.46, 14.68, "kelebihan", "3 / 3", "dalam ada span"),
]
STICKERS = [  # (mula, tamat, teks, x, y, sudut)
    (3.04, 4.76, "cover berlubang ✓", 50, 250, 2.0),
    (5.60, 9.38, "tapak bergetah", 50, 260, 2.0),
    (6.30, 9.38, "anti-slip ✓", 80, 340, -1.5),
    (8.56, 9.38, "tempat basah? tak licin", 110, 420, 1.5),
    (10.48, 14.60, "ada span", 50, 260, 2.0),
    (11.68, 14.60, "boleh buka", 80, 340, -1.5),
    (14.02, 14.60, "boleh basuh ✓", 110, 420, 1.5),
    (15.82, 18.20, "pelbagai warna", 50, 260, 2.0),
    (17.02, 18.20, "pelbagai saiz ✓", 80, 340, -1.5),
]
CIRCLES = []
BIG_WORDS = []  # perkataan besar kena muka (y tetap) → guna sticker di kiri
COVERS = [  # at = masa video ASAL
    dict(at=31.0, kicker="kasut lain daripada", title="lain",
         stickers=["cover berlubang", "anti-slip ✓"], pill="kelebihan 1-3 · Kasut Selesa"),
    dict(at=10.0, kicker="tapak bergetah,", title="anti-slip",
         stickers=["tempat basah", "tak licin ✓"], pill="kelebihan 1-3 · tapak getah"),
]
CTA = dict(title="selesa", title_at=18.28, title_y=150, card_at=18.50, card_y=1180,
           card_label="Kasut", name="Kasut Selesa", tags="berlubang · anti-slip · boleh basuh",
           button="Tekan beg kuning ↓", button_color=(255, 200, 40, 255), button_text_color=(22, 22, 26, 255))
