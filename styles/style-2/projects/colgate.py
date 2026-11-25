# Ubat gigi + berus gigi Colgate Harry Potter (Drive 1rUKbeKcNmn6NIQfs_HjOQS9c7xXZjynp)
REMOVE = [
    (5.88, 6.30),    # "okay"
    (9.58, 13.85),   # "Beli ini bagi sekali dengan ubat gigi. Beli ini," – owner minta buang
    (16.28, 16.63),  # "okay"
]
SRC_END = 23.40
TAIL = 0.7

# --- overlay, masa ikut video SELEPAS dipotong
END = 17.30
CAPTION_Y = 655   # bawah dagu; produk dipegang paras dada
CARD_TOP = 1360   # nilai asal sebelum default jadi 1500

CAPTIONS = [
    (1.66, [("Kalau", 0.03, ""), ("tak", 0.37, ""), ("nak", 0.72, "")]),
    (2.22, [("memutihkan", 0.94, "serif"), ("gigi,", 1.66, "")]),    # disahkan owner
    (3.42, [("kita", 2.22, ""), ("gosok", 2.52, ""), ("gigi", 2.88, ""), ("pun", 3.18, "")]),
    (4.82, [("rasa", 3.42, ""), ("sangat", 3.70, ""), ("selesa,", 4.15, "box")]),
    (5.90, [("lembut", 4.82, "serif"), ("sahaja.", 5.36, "")]),
    (7.08, [("Dia", 5.90, ""), ("peppermint.", 6.12, "box")]),           # disahkan owner
    (9.33, [("Ini", 7.08, ""), ("Colgate", 7.30, "box"), ("Harry Potter.", 7.81, "serif")]),
    (10.61, [("Dia", 9.33, ""), ("bagi", 9.50, ""), ("sekali", 9.83, ""), ("dengan", 10.18, "")]),
    (11.58, [("berus gigi", 10.61, "box"), ("lagi.", 11.28, "")]),
    (12.50, [("Edisi", 11.58, ""), ("terhad,", 11.95, "serif")]),
    (13.54, [("berminat", 12.50, ""), ("dengan", 13.10, "")]),
    (15.11, [("Colgate", 13.54, "box"), ("Harry Potter", 14.06, ""), ("ni,", 14.89, "")]),
    (17.30, [("dapatkan", 15.11, ""), ("di", 15.64, ""), ("beg kuning.", 15.92, "serif")]),
]

HOOK = dict(start=0.15, end=3.0, text="review **Colgate Harry Potter**", x=350, y=860)

CARDS = [
    dict(kind="check", start=2.22, end=7.08, kicker="01 · SELESA", title="Gosok *lembut*",
         items=[("Sangat selesa", 4.15), ("Lembut sahaja", 4.82), ("Rasa peppermint", 6.12)]),
    dict(kind="check", start=9.33, end=11.53, kicker="02 · DAPAT SEKALI", title="Bonus *berus gigi*",
         items=[("Ubat gigi Colgate", 9.50), ("Berus gigi", 10.61)]),
    dict(kind="icon", start=11.53, end=12.50, kicker="03 · EDISI", title="Edisi *terhad*", icon="star"),
]
RAIL = dict(start=2.22, end=12.50, steps=[(2.22, "Selesa"), (9.33, "Set"), (11.53, "Terhad")])
CTA = dict(start=12.50, button_at=15.11, button="Tekan *beg kuning*",
           items=["Selesa & lembut", "Rasa peppermint", "Ubat gigi + berus gigi", "Edisi terhad"])
