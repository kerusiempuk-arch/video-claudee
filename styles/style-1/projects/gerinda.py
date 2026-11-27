# Grinder bawang (Drive 1LsVWTxrxpJLlrqFAvJdunaeziviWV667)
REMOVE = [
    (7.84, 8.70),    # "Okay."
    (14.45, 15.25),  # "Okay."
    (18.40, 20.15),  # bunyi gerinda panjang (simpan ~2s demo)
    (21.10, 22.45),  # "Okay."
    (24.82, 25.48),  # "Okay."
    (26.45, 27.40),  # "Okay. Nah"
]
SRC_END = 35.0
TAIL = 1.2
PUNCH_Y = 0.25
END = 25.48
CAPTION_Y = 680
CARD_Y = 1420
ZOOM = 0.04
SFX_WHOOSH = "drop"   # produk dapur

C_ = lambda end, *ws: (end, [(w, t, h) for w, t, h in ws])
CAPTIONS = [
    C_(1.14, ("Sebelum", 0.00, False), ("ini", 0.58, False)),
    C_(1.80, ("pakai", 1.16, False), ("tumbuk", 1.34, True)),
    C_(2.80, ("ataupun", 1.82, False), ("hiris", 2.44, True)),
    C_(3.36, ("dengan", 2.82, False), ("pisau", 3.06, True)),
    C_(4.40, ("kecil-kecil", 3.38, False)),
    C_(5.36, ("Sekarang", 4.52, False)),
    C_(5.90, ("lagi", 5.38, False), ("senang", 5.40, True)),
    C_(7.00, ("lagi", 5.92, False), ("memudahkan", 6.02, True)),
    C_(7.92, ("Letak", 7.14, False), ("saja", 7.36, False), ("dalam", 7.68, False)),
    C_(9.04, ("ini", 7.94, False), ("bawang", 8.42, True)),
    C_(9.70, ("ke", 9.04, False), ("apa", 9.12, False), ("semua", 9.24, False)),
    C_(10.90, ("Untuk", 9.72, False), ("nak", 9.92, False), ("menumis", 10.14, True)),
    C_(11.86, ("kita", 10.96, False), ("tutup", 11.06, True)),
    C_(12.95, ("tekan", 12.00, True), ("ini", 12.34, False), ("saja", 12.58, False)),
    C_(16.14, ("Tegak", 14.82, False), ("saja", 15.44, False), ("akan", 15.78, False)),
    C_(17.10, ("menjadi", 16.16, False), ("potongan", 16.56, False)),
    C_(18.10, ("hirisan", 17.12, True), ("kecil", 17.52, True)),
    C_(19.00, ("Ini", 18.14, False), ("grinder", 18.36, True)),
    C_(19.90, ("Nak", 19.04, False), ("menumis", 19.18, True)),
    C_(20.64, ("nak", 19.92, False), ("potong", 20.00, False), ("bawang", 20.20, True)),
    C_(21.50, ("ke", 20.66, False), ("apa", 20.78, False), ("semua", 20.90, False)),
    C_(22.50, ("sangat", 21.58, False), ("senang", 21.76, True)),
    C_(24.40, ("Berminat", 22.60, False), ("dengan", 23.10, False), ("grinder", 23.48, True)),
    C_(25.48, ("dapatkan", 24.44, False), ("di", 24.72, False), ("beg", 24.80, True), ("kuning", 25.00, True)),
]
HOOK = dict(end=4.45, y=100, kicker="nak potong bawang,", title="senang",
            options=[("Tumbuk", "01"), ("Hiris pisau", "02"), ("Grinder", "03")], select_at=[1.34, 2.44, 3.38])
SECTIONS = [
    (4.45, 9.70, "tip", "1 / 3", "letak bawang"),
    (9.70, 14.80, "tip", "2 / 3", "tutup & tekan"),
    (14.80, 22.50, "tip", "3 / 3", "hirisan kecil"),
]
STICKERS = [
    (5.40, 7.00, "lagi senang", 80, 260, 2.0),
    (8.42, 9.65, "letak bawang ↓", 80, 260, 2.0),
    (11.06, 12.90, "tutup", 80, 260, 2.0),
    (12.00, 12.90, "tekan saja ✓", 130, 340, -1.5),
    (16.56, 18.10, "hirisan kecil", 80, 260, 2.0),
    (19.18, 21.50, "nak menumis", 80, 260, 2.0),
    (20.20, 21.50, "potong bawang ✓", 130, 340, -1.5),
]
CIRCLES = []
BIG_WORDS = [(13.00, 14.60, "tekan", True)]
CTA = dict(title="senang", title_at=22.50, title_y=230, card_at=22.60, card_y=1180,
           card_label="Grinder", name="Grinder", tags="tumis · hiris · senang",
           button="Tekan beg kuning ↓", button_color=(255, 200, 40, 255), button_text_color=(22, 22, 26, 255))
COVERS = [
    dict(at=28.6, kicker="nak potong bawang,", title="senang",
         stickers=["letak, tutup, tekan", "hirisan kecil ✓"], pill="tip 1-3 · grinder bawang"),
    dict(at=23.27, kicker="akan menjadi potongan,", title="hirisan",
         stickers=["tekan saja", "potongan kecil ✓"], pill="tip 1-3 · grinder bawang"),
]
