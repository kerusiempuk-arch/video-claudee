# Ubat gigi + berus gigi Colgate Harry Potter (Drive 1rUKbeKcNmn6NIQfs_HjOQS9c7xXZjynp)
REMOVE = [
    (5.88, 6.30),    # "okay"
    (16.28, 16.63),  # "okay"
]
SRC_END = 23.40
TAIL = 0.7

# --- overlay, masa ikut video SELEPAS dipotong
END = 21.37
CAPTION_Y = 655   # bawah dagu; produk dipegang paras dada

CAPTIONS = [
    (1.66, [("Kalau", 0.03, ""), ("tak", 0.37, ""), ("nak", 0.72, "")]),
    (2.22, [("sensitifkan", 0.94, "serif"), ("gigi,", 1.66, "")]),    # whisper "memotifkan" – SAHKAN
    (3.42, [("kita", 2.22, ""), ("gosok", 2.52, ""), ("gigi", 2.88, ""), ("pun", 3.18, "")]),
    (4.82, [("rasa", 3.42, ""), ("sangat", 3.70, ""), ("selesa,", 4.15, "box")]),
    (5.90, [("lembut", 4.82, "serif"), ("sahaja.", 5.36, "")]),
    (7.08, [("Dia", 5.90, ""), ("peppermint.", 6.12, "box")]),           # SAHKAN
    (9.32, [("Ini", 7.08, ""), ("Colgate", 7.35, "box"), ("Harry Potter.", 8.07, "serif")]),
    (10.94, [("Beli", 9.32, ""), ("ini", 9.58, ""), ("bagi", 9.77, ""), ("sekali", 10.07, "")]),
    (11.70, [("dengan", 10.49, ""), ("ubat gigi.", 10.94, "box")]),
    (13.14, [("Beli", 11.70, ""), ("ini,", 12.07, ""), ("dia", 12.51, ""), ("bagi", 12.81, "")]),
    (14.22, [("sekali", 13.14, ""), ("dengan", 13.87, "")]),
    (15.68, [("berus gigi", 14.22, "box"), ("lagi.", 15.12, "")]),
    (16.64, [("Edisi", 15.68, ""), ("terhad,", 16.05, "serif")]),
    (17.83, [("berminat", 16.64, ""), ("dengan", 17.24, "")]),
    (19.18, [("Colgate", 17.83, "box"), ("Harry Potter", 18.29, ""), ("ni,", 19.10, "")]),
    (21.37, [("dapatkan", 19.18, ""), ("di", 19.77, ""), ("beg kuning.", 19.92, "serif")]),
]

HOOK = dict(start=0.15, end=3.0, text="review **Colgate Harry Potter**", x=350, y=860)

CARDS = [
    dict(kind="check", start=2.22, end=7.08, kicker="01 · SELESA", title="Gosok *lembut*",
         items=[("Sangat selesa", 4.15), ("Lembut sahaja", 4.82), ("Rasa peppermint", 6.12)]),
    dict(kind="check", start=9.32, end=15.60, kicker="02 · DAPAT SET", title="Sekali *beli*",
         items=[("Ubat gigi", 10.94), ("Berus gigi", 14.22)]),
    dict(kind="icon", start=15.60, end=16.64, kicker="03 · EDISI", title="Edisi *terhad*", icon="star"),
]
RAIL = dict(start=2.22, end=16.64, steps=[(2.22, "Selesa"), (9.32, "Set"), (15.60, "Terhad")])
CTA = dict(start=16.64, button_at=19.18, button="Tekan *beg kuning*",
           items=["Selesa & lembut", "Rasa peppermint", "Ubat gigi + berus gigi", "Edisi terhad"])
