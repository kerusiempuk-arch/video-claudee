# Beg aluminium foil peti sejuk (Drive 18BqI6BD_hhIhbOA_B-3bjVANo3qnTXH6)
REMOVE = [
    (0.00, 0.80),    # senyap awal
    (3.72, 4.40),    # "okey."
]
SRC_END = 11.6
TAIL = 1.2
PUNCH_Y = 0.25

END = 9.84
CAPTION_Y = 680
CARD_Y = 1420
ZOOM = 0.04
SFX_WHOOSH = "drop"   # produk dapur

C_ = lambda end, *ws: (end, [(w, t, h) for w, t, h in ws])
CAPTIONS = [
    C_(1.40, ("Aluminium", 0.00, True), ("foil", 0.80, False)),
    C_(2.08, ("beg", 1.58, True), ("dalam", 1.80, False)),
    C_(3.00, ("peti", 2.08, False), ("sejuk", 2.52, True)),
    C_(3.72, ("Nak", 3.14, False), ("letak", 3.42, False)),
    C_(4.24, ("ikan", 3.72, True)),
    C_(5.06, ("letak", 4.28, False), ("ayam", 4.54, True)),
    C_(5.56, ("dalam", 5.06, False), ("beg", 5.38, False)),
    C_(6.46, ("berlainan", 5.56, True)),
    C_(7.16, ("Makanan", 6.50, False)),
    C_(7.84, ("lebih", 7.16, False), ("bersih", 7.20, True)),
    C_(8.58, ("lebih", 7.88, False), ("selamat", 8.00, True)),
    C_(9.14, ("Berminat", 8.62, False)),
    C_(9.84, ("klik", 9.14, False), ("beg", 9.26, True), ("kuning", 9.42, True)),
]
HOOK = dict(end=6.30, y=100, kicker="beg aluminium foil,", title="asing",
            options=[("Ikan", "01"), ("Ayam", "02")], select_at=[3.72, 4.54])
SECTIONS = [
    (6.30, 7.86, "kelebihan", "1 / 2", "lebih bersih"),
    (7.86, 8.60, "kelebihan", "2 / 2", "lebih selamat"),
]
STICKERS = [
    (0.80, 2.94, "dalam peti sejuk", 600, 300, 2.0),
    (5.56, 6.30, "beg berlainan", 640, 300, -1.5),
    (7.16, 8.55, "lebih bersih", 640, 300, 2.0),
    (8.00, 8.55, "lebih selamat ✓", 660, 370, -1.5),
]
CIRCLES = []
BIG_WORDS = []
CTA = dict(title="selamat", title_at=8.55, title_y=230, card_at=8.62, card_y=1180,
           card_label="Aluminium Foil", name="Beg Aluminium Foil", tags="bersih · selamat",
           button="Tekan beg kuning ↓", button_color=(255, 200, 40, 255), button_text_color=(22, 22, 26, 255))
COVERS = [
    dict(at=10.4, kicker="beg aluminium foil,", title="selamat",
         stickers=["ikan, ayam asing", "lebih bersih ✓"], pill="kelebihan 1-2 · beg aluminium foil"),
    dict(at=2.0, kicker="dalam peti sejuk,", title="asing",
         stickers=["beg berlainan", "lebih selamat ✓"], pill="kelebihan 1-2 · beg aluminium foil"),
]
