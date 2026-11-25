# Mata bit magnetic / bit screwdriver (Drive 1PCJP0VYGxnsd3MqdqUbKJmyllstWDiOs)
REMOVE = [
    (3.40, 4.10),    # "aa"
    (5.45, 8.62),    # "okay, okay, aa"
    (9.66, 12.44),   # "sepuluh pisar dalam satu box" pertama – diulang
    (13.99, 14.99),  # "okay, aa"
    (20.25, 21.79),  # "aa, ni, aa"
    (23.29, 23.86),  # "okay, aa"
    (37.45, 45.30),  # "berminat" pertama + "aa" – diulang
]
SRC_END = 50.78
TAIL = 0.7

# --- overlay, masa ikut video SELEPAS dipotong
END = 29.05
CAPTION_Y = 655   # bawah dagu, tak bertindih senarai CTA (top 760)

CAPTIONS = [
    (2.30, [("Mata", 0.05, ""), ("bit", 0.85, "")]),
    (3.20, [("magnetic", 2.30, "serif")]),
    (4.88, [("dua", 3.20, ""), ("sekali", 3.54, ""), ("aku", 4.07, ""), ("dapat,", 4.33, "")]),
    (5.91, [("magnetic,", 4.88, "box")]),
    (6.86, [("sepuluh", 5.91, ""), ("pieces", 6.19, "box"), ("dalam", 6.51, "")]),
    (7.30, [("satu", 6.86, ""), ("box,", 7.09, "")]),
    (8.96, [("untuk", 7.30, ""), ("nak", 7.80, ""), ("tebuk", 8.04, ""), ("lubang,", 8.28, "")]),
    (10.31, [("drill", 8.96, "serif"), ("pada", 9.41, ""), ("kayu,", 9.77, "box")]),
    (11.66, [("pada", 10.31, ""), ("plat", 10.67, ""), ("besi,", 11.12, "box")]),   # "pelik besi" – SAHKAN
    (12.41, [("boleh.", 11.66, "")]),
    (13.84, [("Ini", 12.41, ""), ("semua", 12.59, ""), ("magnetic,", 13.05, "serif")]),
    (14.83, [("lebih", 13.84, ""), ("selamat,", 14.31, "box")]),
    (16.00, [("skru", 14.83, ""), ("tak", 15.23, ""), ("jatuh,", 15.43, "")]),
    (17.73, [("nak", 16.00, ""), ("skru", 16.25, ""), ("tempat", 16.76, ""), ("sempit,", 17.17, "box")]),
    (18.72, [("nak", 17.73, ""), ("tebuk", 17.93, ""), ("lubang,", 18.27, "")]),
    (19.84, [("sangat", 18.72, ""), ("sesuai.", 19.28, "serif")]),
    (20.68, [("Dengan", 19.84, ""), ("kes", 20.26, "box"), ("dia", 20.47, "")]),
    (21.34, [("macam", 20.68, ""), ("ni,", 21.13, "")]),
    (22.57, [("dia", 21.34, ""), ("lebih", 21.52, ""), ("tersusun,", 21.87, "box")]),
    (23.88, [("lebih", 22.57, ""), ("kemas.", 22.93, "serif")]),
    (24.61, [("Berminat", 23.88, ""), ("dengan", 24.56, "")]),
    (25.90, [("bit", 24.61, ""), ("screwdriver", 24.90, "box")]),
    (27.56, [("bermagnetic", 25.90, ""), ("ni,", 26.77, ""), ("dapatkan", 26.90, ""), ("di", 27.43, "")]),
    (29.05, [("beg kuning", 27.56, "serif")]),
]

HOOK = dict(start=0.15, end=3.0, text="review **mata bit magnetic**", x=350, y=860)

CARDS = [
    dict(kind="check", start=3.20, end=7.30, kicker="DAPAT 2 SET", title="10 pieces *satu box*",
         items=[("Bermagnetic", 4.88), ("10 pieces setiap box", 7.09)]),
    dict(kind="check", start=7.30, end=12.41, kicker="01 · DRILL", title="Tebuk *lubang*",
         items=[("Kayu", 9.77), ("Plat besi", 11.12)]),
    dict(kind="check", start=12.41, end=19.84, kicker="02 · MAGNETIC", title="Lebih *selamat*",
         items=[("Semua magnetic", 13.05), ("Skru tak jatuh", 15.43), ("Sesuai tempat sempit", 17.17)]),
    dict(kind="check", start=19.84, end=23.88, kicker="03 · KES", title="Lebih *kemas*",
         items=[("Lebih tersusun", 21.87), ("Lebih kemas", 22.93)]),
]
RAIL = dict(start=7.30, end=23.88, steps=[(7.30, "Drill"), (12.41, "Magnetic"), (19.84, "Kemas")])
CTA = dict(start=23.88, button_at=26.90, button="Tekan *beg kuning*",
           items=["10 pieces satu box", "Drill kayu & plat besi", "Magnetic – skru tak jatuh", "Kes tersusun & kemas"])
