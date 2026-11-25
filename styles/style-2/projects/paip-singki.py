# Paip salur singki stainless (Drive 19hds0B9UfgxRNpQGHP861GNFzkEgstbM)
REMOVE = [
    (5.40, 5.73),    # "Okay,"
    (10.24, 10.43),  # "okay" selepas "tak berkarat"
    (18.58, 19.05),  # "okay" selepas "rumah kita"
    (22.40, 23.55),  # "kepala," pertama – diulang
]
SRC_END = 36.8
TAIL = 0.7

# --- overlay, masa ikut video SELEPAS dipotong (cut.wav)
END = 31.37
CAPTION_Y = 600   # muka di atas kanan, kepala paip di tengah kiri

CAPTIONS = [
    (1.05, [("Ini", 0.11, ""), ("paip", 0.26, ""), ("salur", 0.53, "")]),
    (2.43, [("singki", 1.05, "box"), ("rumah", 1.46, ""), ("aku", 1.82, ""), ("yang", 2.08, "")]),
    (3.54, [("biasa", 2.43, "serif"), ("sahaja,", 2.96, "")]),
    (5.00, [("aku", 3.54, ""), ("custom", 3.71, "box"), ("sendiri", 4.17, ""), ("sahaja.", 4.60, "")]),
    (6.21, [("Sekarang", 5.00, ""), ("aku", 5.69, ""), ("dah", 6.05, "")]),
    (7.21, [("ada", 6.21, ""), ("yang", 6.47, ""), ("ni,", 6.82, "serif")]),
    (8.47, [("ini", 7.21, ""), ("dia", 7.39, ""), ("stainless steel", 7.58, "box")]),
    (9.36, [("tak", 8.47, ""), ("berkarat.", 8.68, "serif")]),
    (10.41, [("Dia", 9.36, ""), ("flexible,", 9.58, "box")]),
    (11.79, [("kita", 10.41, ""), ("boleh", 10.63, ""), ("adjust", 11.05, "serif")]),
    (13.88, [("ikut", 11.79, ""), ("kesesuaian", 12.20, ""), ("lubang,", 13.33, "")]),
    (14.80, [("salur", 13.88, ""), ("buang", 14.20, ""), ("ni", 14.60, "")]),
    (16.24, [("dengan", 14.80, ""), ("singki", 15.20, "box"), ("rumah", 15.70, ""), ("kita.", 15.95, "")]),
    (18.08, [("Ini", 16.24, ""), ("single", 16.60, "box"), ("saja.", 17.32, "")]),   # disahkan owner
    (19.13, [("Specialnya", 18.08, "serif"), ("dia", 18.95, "")]),
    (20.17, [("kepala", 19.13, "box"), ("dia", 19.61, ""), ("ni,", 19.85, "")]),
    (21.49, [("dia", 20.17, ""), ("ada", 20.41, ""), ("filter,", 20.65, "box")]),
    (22.38, [("dia", 21.49, ""), ("anti-odour,", 21.62, "serif")]),
    (23.32, [("anti", 22.38, ""), ("serangga.", 22.62, "box")]),
    (24.78, [("Jadinya", 23.32, ""), ("bau,", 23.85, "box"), ("serangga", 24.19, "")]),
    (25.75, [("daripada", 24.78, ""), ("luar,", 25.28, "")]),
    (26.76, [("dia", 25.75, ""), ("takkan", 26.03, "serif"), ("masuk", 26.33, ""), ("ke", 26.72, "")]),
    (27.91, [("ruangan", 26.76, ""), ("dapur", 27.25, "box"), ("kita.", 27.49, "")]),
    (28.87, [("Nak", 27.91, ""), ("pasang", 27.99, ""), ("pun", 28.37, ""), ("senang.", 28.49, "serif")]),
    (30.01, [("Berminat?", 28.87, ""), ("Dapatkan", 29.36, ""), ("di", 29.86, "")]),
    (31.37, [("beg kuning", 30.01, "serif")]),
]

HOOK = dict(start=0.15, end=2.9, text="review **paip singki**", x=350, y=760)

CARDS = [
    dict(kind="vs", start=2.9, end=7.5, kicker="PAIP SALUR SINGKI", old="Biasa", new="Stainless", new_at=6.82),
    dict(kind="check", start=7.5, end=10.4, kicker="01 · BAHAN", title="Stainless *steel*",
         items=[("Tak berkarat", 8.68), ("Flexible", 9.58)]),
    dict(kind="icon", start=10.4, end=18.0, kicker="02 · FLEXIBLE", title="Boleh *adjust*\nikut lubang singki", icon="star"),
    dict(kind="check", start=18.0, end=23.3, kicker="03 · KEPALA", title="Kepala *berfilter*",
         items=[("Ada filter", 20.65), ("Anti bau", 21.62), ("Anti serangga", 22.38)]),
    dict(kind="icon", start=23.3, end=27.9, kicker="04 · DAPUR BERSIH", title="Bau & serangga\n*tak masuk*", icon="shield"),
]
RAIL = dict(start=7.5, end=27.9, steps=[(7.5, "Bahan"), (10.4, "Flexible"), (18.0, "Filter"), (23.3, "Bersih")])
CTA = dict(start=27.9, button_at=29.1, button="Tekan *beg kuning*",
           items=["Stainless tak berkarat", "Flexible, boleh adjust", "Ada filter", "Anti bau & serangga", "Senang pasang"])
