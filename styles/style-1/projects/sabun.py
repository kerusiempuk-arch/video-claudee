# Sabun pencuci pinggan (Drive 14LKjRE18e9Vm8gIgnqxN_5_GU2wAtOAZ) – gaya ikut video rujukan rak besi (TikTok @ashrafaamin)
REMOVE = [
    (0.00, 0.78),    # senyap awal
    (1.88, 3.64),    # "Menggunakan sabun pe-" (cubaan pertama tak habis)
    (5.76, 6.74),    # "Okay. Ha,"
    (9.66, 10.06),   # "Ha,"
    (11.03, 11.30),  # "Okay"
    (17.20, 17.58),  # "Nah,"
    (18.00, 18.74),  # "Ah,"
    (20.60, 21.74),  # "Oke, nah,"
    (27.30, 30.48),  # bilas panjang tanpa suara + "Nah,"
    (32.50, 32.78),  # "Okay,"
    (36.42, 37.75),  # "okay. Nah,"
]
SRC_END = 40.3
TAIL = 1.2
PUNCH_Y = 0.25

# ---------- overlay – masa ikut video SELEPAS dipotong
END = 25.47
CAPTION_Y = 680
CARD_Y = 1420
ZOOM = 0.04
SFX_WHOOSH = "drop"   # produk dapur / air

C_ = lambda end, *ws: (end, [(w, t, h) for w, t, h in ws])
CAPTIONS = [
    C_(0.64, ("Nak", 0.05, False), ("cuci", 0.32, False)),
    C_(1.10, ("pinggan", 0.66, True)),
    C_(1.90, ("menggunakan", 1.14, False)),
    C_(2.90, ("sabun", 1.92, True), ("pencuci", 2.34, False)),
    C_(3.20, ("ni", 2.92, False)),
    C_(3.84, ("Sangat", 3.24, False), ("senang", 3.46, True)),
    C_(4.60, ("nak", 3.86, False), ("guna", 4.04, False), ("kita", 4.38, False)),
    C_(5.30, ("tekan", 4.64, True), ("saja", 5.08, False)),
    C_(5.78, ("kat", 5.34, False), ("sini", 5.54, False)),
    C_(6.58, ("terkeluar", 5.80, True)),
    C_(7.34, ("Kemudian", 6.62, False), ("aku", 7.10, False)),
    C_(8.12, ("menggunakan", 7.36, False)),
    C_(8.86, ("span", 8.14, True), ("ni", 8.60, False)),
    C_(9.40, ("Kita", 8.88, False), ("tengok", 9.12, False)),
    C_(10.60, ("keberkesanannya", 9.42, True)),
    C_(11.12, ("Tengok", 10.68, False), ("dia", 10.90, False), ("dah", 11.04, False)),
    C_(12.20, ("berbuih", 11.14, True), ("dah", 11.70, False)),
    C_(13.02, ("Kotoran", 12.44, False), ("minyak", 12.80, True)),
    C_(13.78, ("memang", 13.04, False), ("sangat", 13.42, False)),
    C_(14.80, ("senang", 13.80, True), ("nak", 14.14, False), ("cuci", 14.30, False)),
    C_(15.36, ("Sekarang", 14.92, False), ("aku", 15.12, False)),
    C_(16.08, ("bilas", 15.38, True), ("dengan", 15.64, False), ("air", 15.84, True)),
    C_(16.90, ("kita", 16.10, False), ("tengok", 16.28, False)),
    C_(18.50, ("Sekejap", 17.62, False), ("saja", 18.14, True)),
    C_(20.00, ("Tengok", 19.40, False)),
    C_(20.78, ("dah", 20.04, False), ("bersih", 20.32, True)),
    C_(21.68, ("Kotoran", 20.80, False), ("minyak", 21.16, True)),
    C_(22.80, ("memang", 21.70, False), ("hilang", 21.96, True), ("terus", 22.36, False)),
    C_(23.90, ("Berminat", 22.96, False), ("dapatkan", 23.46, False)),
    C_(25.47, ("di", 23.92, False), ("beg", 24.02, True), ("kuning", 24.24, True)),
]
HOOK = dict(end=3.95, y=100,
            kicker="sabun pencuci pinggan,", title="senang",
            options=[("Cuci pinggan", "01"), ("Sabun pencuci", "02"), ("Sangat senang", "03")],
            select_at=[0.32, 1.92, 3.24])
SECTIONS = [  # label "tip" ikut video rujukan
    (3.95, 6.62, "tip", "1 / 3", "tekan je"),
    (6.62, 14.86, "tip", "2 / 3", "cepat berbuih"),
    (14.86, 22.90, "tip", "3 / 3", "bilas sekejap"),
]
STICKERS = [
    (4.64, 6.55, "tekan pam ↓", 80, 260, 2.0),
    (5.80, 6.55, "terus keluar", 130, 340, -1.5),
    (7.36, 10.60, "span + sabun", 80, 260, 2.0),
    (9.42, 10.60, "tengok hasil", 130, 340, -1.5),
    (12.44, 14.80, "kotoran minyak", 80, 260, 2.0),
    (13.80, 14.80, "senang cuci", 130, 340, -1.5),
    (15.38, 19.30, "bilas dengan air", 80, 260, 2.0),
    (17.62, 19.30, "sekejap saja", 130, 340, -1.5),
    (21.70, 22.85, "minyak hilang terus", 80, 260, 2.0),
]
CIRCLES = []
# perkataan besar sekejap di tengah video (macam "store", "4 layer", "ngam." dalam rujukan) – ditambah oleh sabun_extra.py
BIG_WORDS = [  # (mula, tamat, perkataan, titik_merah)
    (11.14, 12.40, "berbuih", True),
    (20.32, 21.66, "bersih", True),
]
EXTRA_SFX = [(t, "drop", 0.45) for t, *_ in BIG_WORDS]
CTA = dict(title="senang", title_at=22.80, title_y=230, card_at=23.00, card_y=1180,
           card_label="Sabun Pencuci", name="Sabun Pencuci Pinggan", tags="senang · berbuih · bersih",
           button="Tekan beg kuning ↓", button_color=(255, 200, 40, 255), button_text_color=(22, 22, 26, 255))
