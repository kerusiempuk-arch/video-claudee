# Ubat gigi + berus gigi Colgate Harry Potter (Drive 1rUKbeKcNmn6NIQfs_HjOQS9c7xXZjynp)
REMOVE = [
    (5.88, 6.30),    # "okay"
    (9.20, 13.85),   # "Beli ini bagi sekali dengan ubat gigi. Beli ini," – owner minta buang
    (16.28, 16.63),  # "okay"
]
SRC_END = 23.40
TAIL = 0.7

# --- overlay, masa ikut video SELEPAS dipotong
END = 16.92
CAPTION_Y = 655   # bawah dagu; produk dipegang paras dada

CAPTIONS = [
    (1.66, [("Kalau", 0.03, ""), ("tak", 0.37, ""), ("nak", 0.72, "")]),
    (2.22, [("sensitifkan", 0.94, "serif"), ("gigi,", 1.66, "")]),    # whisper "memotifkan" – SAHKAN
    (3.42, [("kita", 2.22, ""), ("gosok", 2.52, ""), ("gigi", 2.88, ""), ("pun", 3.18, "")]),
    (4.82, [("rasa", 3.42, ""), ("sangat", 3.70, ""), ("selesa,", 4.15, "box")]),
    (5.90, [("lembut", 4.82, "serif"), ("sahaja.", 5.36, "")]),
    (7.08, [("Dia", 5.90, ""), ("peppermint.", 6.12, "box")]),           # SAHKAN
    (8.95, [("Ini", 7.08, ""), ("Colgate", 7.30, "box"), ("Harry Potter.", 7.81, "serif")]),
    (10.23, [("Dia", 8.95, ""), ("bagi", 9.12, ""), ("sekali", 9.45, ""), ("dengan", 9.80, "")]),
    (11.20, [("berus gigi", 10.23, "box"), ("lagi.", 10.90, "")]),
    (12.12, [("Edisi", 11.20, ""), ("terhad,", 11.57, "serif")]),
    (13.16, [("berminat", 12.12, ""), ("dengan", 12.72, "")]),
    (14.73, [("Colgate", 13.16, "box"), ("Harry Potter", 13.68, ""), ("ni,", 14.51, "")]),
    (16.92, [("dapatkan", 14.73, ""), ("di", 15.26, ""), ("beg kuning.", 15.54, "serif")]),
]

HOOK = dict(start=0.15, end=3.0, text="review **Colgate Harry Potter**", x=350, y=860)

CARDS = [
    dict(kind="check", start=2.22, end=7.08, kicker="01 · SELESA", title="Gosok *lembut*",
         items=[("Sangat selesa", 4.15), ("Lembut sahaja", 4.82), ("Rasa peppermint", 6.12)]),
    dict(kind="check", start=8.95, end=11.15, kicker="02 · DAPAT SEKALI", title="Bonus *berus gigi*",
         items=[("Ubat gigi Colgate", 9.12), ("Berus gigi", 10.23)]),
    dict(kind="icon", start=11.15, end=12.12, kicker="03 · EDISI", title="Edisi *terhad*", icon="star"),
]
RAIL = dict(start=2.22, end=12.12, steps=[(2.22, "Selesa"), (8.95, "Set"), (11.15, "Terhad")])
CTA = dict(start=12.12, button_at=14.73, button="Tekan *beg kuning*",
           items=["Selesa & lembut", "Rasa peppermint", "Ubat gigi + berus gigi", "Edisi terhad"])
