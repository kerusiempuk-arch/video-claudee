# Ubat gigi + berus gigi Colgate Harry Potter (Drive 1rUKbeKcNmn6NIQfs_HjOQS9c7xXZjynp)
REMOVE = [
    (5.88, 6.30),    # "okay"
    (9.29, 13.85),   # "Beli ini bagi sekali dengan ubat gigi. Beli ini," – owner minta buang
    (16.28, 16.63),  # "okay"
]
SRC_END = 23.40
TAIL = 0.7

# --- overlay, masa ikut video SELEPAS dipotong
END = 17.01
CAPTION_Y = 655   # bawah dagu; produk dipegang paras dada

CAPTIONS = [
    (1.66, [("Kalau", 0.03, ""), ("tak", 0.37, ""), ("nak", 0.72, "")]),
    (2.22, [("sensitifkan", 0.94, "serif"), ("gigi,", 1.66, "")]),    # whisper "memotifkan" – SAHKAN
    (3.42, [("kita", 2.22, ""), ("gosok", 2.52, ""), ("gigi", 2.88, ""), ("pun", 3.18, "")]),
    (4.82, [("rasa", 3.42, ""), ("sangat", 3.70, ""), ("selesa,", 4.15, "box")]),
    (5.90, [("lembut", 4.82, "serif"), ("sahaja.", 5.36, "")]),
    (7.08, [("Dia", 5.90, ""), ("peppermint.", 6.12, "box")]),           # SAHKAN
    (9.04, [("Ini", 7.08, ""), ("Colgate", 7.30, "box"), ("Harry Potter.", 7.81, "serif")]),
    (10.32, [("Dia", 9.04, ""), ("bagi", 9.21, ""), ("sekali", 9.54, ""), ("dengan", 9.89, "")]),
    (11.29, [("berus gigi", 10.32, "box"), ("lagi.", 10.99, "")]),
    (12.21, [("Edisi", 11.29, ""), ("terhad,", 11.66, "serif")]),
    (13.25, [("berminat", 12.21, ""), ("dengan", 12.81, "")]),
    (14.82, [("Colgate", 13.25, "box"), ("Harry Potter", 13.77, ""), ("ni,", 14.60, "")]),
    (17.01, [("dapatkan", 14.82, ""), ("di", 15.35, ""), ("beg kuning.", 15.63, "serif")]),
]

HOOK = dict(start=0.15, end=3.0, text="review **Colgate Harry Potter**", x=350, y=860)

CARDS = [
    dict(kind="check", start=2.22, end=7.08, kicker="01 · SELESA", title="Gosok *lembut*",
         items=[("Sangat selesa", 4.15), ("Lembut sahaja", 4.82), ("Rasa peppermint", 6.12)]),
    dict(kind="check", start=9.04, end=11.24, kicker="02 · DAPAT SEKALI", title="Bonus *berus gigi*",
         items=[("Ubat gigi Colgate", 9.21), ("Berus gigi", 10.32)]),
    dict(kind="icon", start=11.24, end=12.21, kicker="03 · EDISI", title="Edisi *terhad*", icon="star"),
]
RAIL = dict(start=2.22, end=12.21, steps=[(2.22, "Selesa"), (9.04, "Set"), (11.24, "Terhad")])
CTA = dict(start=12.21, button_at=14.82, button="Tekan *beg kuning*",
           items=["Selesa & lembut", "Rasa peppermint", "Ubat gigi + berus gigi", "Edisi terhad"])
