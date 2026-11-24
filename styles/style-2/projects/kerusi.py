# Kerusi lipat Super Tribe (Drive 1ZXlmSqhLTFF8HPFFLbhEOKCcsBf9-JK0)
# --- potongan (build.py), masa ikut video ASAL
REMOVE = [
    (0.00, 0.30),    # senyap di permulaan
    (3.78, 4.52),    # "haa"
    (8.00, 9.70),    # "okay"
    (10.88, 11.28),  # "haa"
    (12.36, 13.25),  # "dia ada lubang" pertama – diulang
    (14.38, 17.18),  # "haa, dia ada empat level, haa" – ulang "empat tahap"
    (19.95, 20.31),  # "haa"
    (21.13, 22.31),  # "nak lagi baring" pertama – diulang
    (26.95, 27.35),  # "haa"
    (28.88, 29.13),  # "haa"
    (33.10, 33.50),  # "haa"
    (35.92, 58.42),  # "hmm dah agak", senyap, "berminat dengan kerusi..." (ambil take terakhir)
]
SRC_END = 63.95
TAIL = 0.7

# --- overlay (build.py), masa ikut video SELEPAS dipotong (transkripsi cut.wav)
END = 27.33
CAPTION_Y = 640   # dada, bawah dagu (duduk)

CAPTIONS = [
    (0.78, [("Buka", 0.08, ""), ("saja,", 0.40, "box")]),
    (2.35, [("terus", 0.78, ""), ("boleh", 1.18, ""), ("duduk", 1.62, "serif")]),
    (4.21, [("Sangat", 2.35, ""), ("selesa", 2.78, "box"), ("kerusi", 3.32, ""), ("ni", 3.86, "")]),
    (5.52, [("dia", 4.21, ""), ("ada", 4.42, ""), ("empat", 4.75, "box"), ("tahap", 5.08, "")]),
    (6.31, [("di", 5.52, ""), ("belakang", 5.65, ""), ("ni,", 6.07, "")]),
    (7.39, [("punya", 6.31, ""), ("level", 6.40, "serif"), ("dia,", 6.94, "")]),
    (8.03, [("dia", 7.39, ""), ("ada", 7.55, ""), ("lubang", 7.71, "box")]),
    (9.22, [("macam", 8.03, ""), ("ni.", 8.30, ""), ("Jadinya", 8.52, "")]),
    (10.54, [("kita", 9.22, ""), ("boleh", 9.57, ""), ("adjust", 10.01, "serif")]),
    (11.07, [("sampai", 10.54, ""), ("empat,", 10.80, "box")]),
    (12.45, [("nak", 11.07, ""), ("lagi", 11.33, ""), ("bongkok,", 11.73, "box")]),
    (13.60, [("nak", 12.45, ""), ("lagi", 12.71, ""), ("rendah", 13.05, "box")]),
    (15.56, [("ataupun", 13.60, ""), ("nak", 14.19, ""), ("lagi", 14.45, ""), ("tinggi", 14.83, "box")]),
    (16.31, [("Ada", 15.56, ""), ("poket", 15.73, "serif"), ("lagi", 16.08, "")]),
    (16.95, [("kat", 16.31, ""), ("sini,", 16.51, "")]),
    (18.39, [("nak", 16.95, ""), ("letak", 17.18, ""), ("telefon,", 17.61, "box")]),
    (19.72, [("nak", 18.39, ""), ("letak", 18.65, ""), ("botol,", 19.08, "box")]),
    (20.64, [("sangat", 19.72, ""), ("sesuai", 20.07, "serif")]),
    (21.48, [("Ada", 20.64, ""), ("span,", 20.89, "box")]),
    (22.92, [("sangat", 21.48, ""), ("selesa", 22.04, "serif")]),
    (24.46, [("Berminat", 22.92, ""), ("dengan", 23.61, ""), ("kerusi", 24.00, "")]),
    (25.82, [("lipat", 24.46, ""), ("serba", 24.85, ""), ("guna", 25.27, ""), ("ni,", 25.56, "")]),
    (27.33, [("klik", 25.82, ""), ("beg kuning", 26.13, "serif")]),
]

HOOK = dict(start=0.15, end=2.3, text="review **kerusi lipat**", x=350, y=760)

CARDS = [
    dict(kind="icon", start=2.35, end=4.2, kicker="01 · SELESA", title="Sangat *selesa*", icon="heart"),
    dict(kind="check", start=4.2, end=10.8, kicker="02 · LARAS", title="*4 tahap* boleh laras",
         items=[("Lubang di belakang", 7.71), ("Boleh adjust", 10.01)]),
    dict(kind="check", start=10.8, end=15.5, kicker="03 · POSISI", title="Ikut *selesa* anda",
         items=[("Lagi bongkok", 11.73), ("Lagi rendah", 13.05), ("Lagi tinggi", 14.83)]),
    dict(kind="check", start=15.55, end=20.6, kicker="04 · POKET", title="Ada *poket* tepi",
         items=[("Letak telefon", 17.61), ("Letak botol", 19.08)]),
    dict(kind="icon", start=20.65, end=22.9, kicker="05 · SPAN", title="Ada *span*\nlebih selesa", icon="shield"),
]
RAIL = dict(start=2.35, end=22.9, steps=[(2.35, "Selesa"), (4.2, "Laras"), (10.8, "Posisi"), (15.55, "Poket"), (20.65, "Span")])
CTA = dict(start=22.92, button_at=25.1, button="Klik *beg kuning*",
           items=["Buka & terus duduk", "4 tahap boleh laras", "Poket telefon & botol", "Ada span, sangat selesa"])
