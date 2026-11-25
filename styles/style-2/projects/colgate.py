# Ubat gigi + berus gigi Colgate Harry Potter (Drive 1rUKbeKcNmn6NIQfs_HjOQS9c7xXZjynp)
REMOVE = [
    (5.88, 6.30),    # "okay"
    (9.57, 12.12),   # "Beli ini bagi sekali dengan ubat gigi" – owner minta buang (preview 9–12 s)
    (16.28, 16.63),  # "okay"
]
SRC_END = 23.40
TAIL = 0.7

# --- overlay, masa ikut video SELEPAS dipotong
END = 18.82
CAPTION_Y = 655   # bawah dagu; produk dipegang paras dada

CAPTIONS = [
    (1.66, [("Kalau", 0.03, ""), ("tak", 0.37, ""), ("nak", 0.72, "")]),
    (2.22, [("sensitifkan", 0.94, "serif"), ("gigi,", 1.66, "")]),    # whisper "memotifkan" – SAHKAN
    (3.42, [("kita", 2.22, ""), ("gosok", 2.52, ""), ("gigi", 2.88, ""), ("pun", 3.18, "")]),
    (4.82, [("rasa", 3.42, ""), ("sangat", 3.70, ""), ("selesa,", 4.15, "box")]),
    (5.90, [("lembut", 4.82, "serif"), ("sahaja.", 5.36, "")]),
    (7.08, [("Dia", 5.90, ""), ("peppermint.", 6.12, "box")]),           # SAHKAN
    (9.15, [("Ini", 7.08, ""), ("Colgate", 7.35, "box"), ("Harry Potter.", 8.07, "serif")]),
    (10.59, [("Beli", 9.15, ""), ("ini,", 9.52, ""), ("dia", 9.96, ""), ("bagi", 10.26, "")]),
    (11.67, [("sekali", 10.59, ""), ("dengan", 11.32, "")]),
    (13.13, [("berus gigi", 11.67, "box"), ("lagi.", 12.57, "")]),
    (14.09, [("Edisi", 13.13, ""), ("terhad,", 13.50, "serif")]),
    (15.28, [("berminat", 14.09, ""), ("dengan", 14.69, "")]),
    (16.63, [("Colgate", 15.28, "box"), ("Harry Potter", 15.74, ""), ("ni,", 16.55, "")]),
    (18.82, [("dapatkan", 16.63, ""), ("di", 17.22, ""), ("beg kuning.", 17.37, "serif")]),
]

HOOK = dict(start=0.15, end=3.0, text="review **Colgate Harry Potter**", x=350, y=860)

CARDS = [
    dict(kind="check", start=2.22, end=7.08, kicker="01 · SELESA", title="Gosok *lembut*",
         items=[("Sangat selesa", 4.15), ("Lembut sahaja", 4.82), ("Rasa peppermint", 6.12)]),
    dict(kind="check", start=9.15, end=13.05, kicker="02 · DAPAT SEKALI", title="Sekali *beli*",
         items=[("Ubat gigi Colgate", 9.52), ("Berus gigi", 11.67)]),
    dict(kind="icon", start=13.05, end=14.09, kicker="03 · EDISI", title="Edisi *terhad*", icon="star"),
]
RAIL = dict(start=2.22, end=14.09, steps=[(2.22, "Selesa"), (9.15, "Set"), (13.05, "Terhad")])
CTA = dict(start=14.09, button_at=16.63, button="Tekan *beg kuning*",
           items=["Selesa & lembut", "Rasa peppermint", "Ubat gigi + berus gigi", "Edisi terhad"])
