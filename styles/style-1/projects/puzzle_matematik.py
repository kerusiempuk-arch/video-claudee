# Puzzle matematik (Drive 1X4fJgvvZoKB5RP4V_89KDUJCKxOHoXvG)
# ---------- potongan (build.py) – masa ikut video ASAL
REMOVE = [
    (0.00, 0.75),    # senyap awal
    (3.78, 4.25),    # "okey"
    (10.15, 10.78),  # "nah"
    (12.55, 13.76),  # "okay"/"ha" pendek sebelum "Dalam ni"
    (21.84, 22.36),  # "okay"
    (22.98, 25.25),  # "ada, aa," (cubaan pertama) – kekal "Dan juga | ada lambang"
    (34.50, 37.40),  # "Okay. Beserta dengan warna." (cubaan pertama)
]
SRC_END = 42.40
TAIL = 1.2
PUNCH_Y = 0.25

# ---------- overlay – masa ikut video SELEPAS dipotong
END = 31.55
CAPTION_Y = 680
CARD_Y = 1420
ZOOM = 0.04

C_ = lambda end, *ws: (end, [(w, t, h) for w, t, h in ws])
CAPTIONS = [
    C_(1.08, ("Puzzle", 0.46, True)),
    C_(1.62, ("ataupun", 1.10, False)),
    C_(3.04, ("puzzle", 1.64, False), ("matematik", 2.16, True)),
    C_(3.94, ("Sesuai", 3.06, False), ("untuk", 3.60, False)),
    C_(4.92, ("anak-anak", 3.96, True), ("yang", 4.46, False), ("baru", 4.68, False)),
    C_(5.44, ("nak", 4.94, False), ("mengenal", 5.20, False)),
    C_(6.48, ("nombor", 5.46, True)),
    C_(7.88, ("Dia", 6.52, False), ("mainan", 7.16, True)),
    C_(8.94, ("sambil", 7.90, False), ("belajar", 8.24, True)),
    C_(9.80, ("Kita", 8.96, False), ("boleh", 9.16, False), ("pusing", 9.38, True)),
    C_(10.58, ("macam", 9.82, False), ("ni", 10.14, False)),
    C_(11.64, ("Dalam", 10.60, False), ("ni", 10.72, False), ("dia", 11.46, False)),
    C_(12.22, ("ada", 11.66, False), ("tulis", 11.80, False)),
    C_(12.98, ("nombor", 12.24, True)),
    C_(14.56, ("Nombor", 13.00, False), ("asas", 13.36, True), ("saja", 13.72, False)),
    C_(15.58, ("Satu,", 14.58, False), ("dua,", 15.22, False)),
    C_(17.12, ("tiga,", 15.60, False)),
    C_(17.96, ("sampai", 17.14, False), ("kosong", 17.26, True)),
    C_(18.56, ("Dan", 17.98, False), ("juga", 18.18, False)),
    C_(20.12, ("ada", 18.58, False), ("lambang", 19.32, True)),
    C_(21.00, ("Selain", 20.14, False), ("itu", 20.38, False), ("dia", 20.60, False)),
    C_(21.60, ("juga", 20.72, False), ("ada", 21.02, False)),
    C_(22.72, ("operasi", 21.62, True), ("asas", 22.08, True)),
    C_(23.78, ("Seperti", 22.74, False), ("tambah,", 23.06, True)),
    C_(24.40, ("tolak,", 23.80, True)),
    C_(25.30, ("sama", 24.42, False), ("dengan,", 24.70, False)),
    C_(26.42, ("darab", 25.32, True), ("dan", 25.92, False), ("juga", 26.18, False)),
    C_(27.08, ("bahagi", 26.44, True)),
    C_(28.34, ("Berserta", 27.10, False), ("dengan", 27.44, False)),
    C_(29.00, ("warna-warni", 27.98, True)),
    C_(29.74, ("Sangat", 29.02, False), ("menarik", 29.32, True)),
    C_(30.98, ("Berminat?", 29.76, False), ("dapatkan", 30.52, False)),
    C_(31.55, ("di", 31.00, False), ("beg", 31.10, True), ("kuning", 31.20, True)),
]
HOOK = dict(end=6.3, y=100, kicker="mainan sambil", title="belajar",
            options=[("Puzzle", "01"), ("Puzzle matematik", "02")], select_at=[0.46, 1.64])
SECTIONS = [
    (6.5, 10.5, "kelebihan", "1 / 3", "mainan sambil belajar"),
    (10.5, 20.1, "kelebihan", "2 / 3", "nombor & lambang"),
    (20.1, 27.0, "kelebihan", "3 / 3", "operasi asas"),
]
STICKERS = [  # (mula, tamat, teks, x, y, sudut)
    (8.24, 10.4, "sambil belajar", 50, 250, 2.0),
    (9.38, 10.4, "boleh pusing", 80, 320, -1.5),
    (12.24, 14.5, "ada nombor", 50, 250, 2.0),
    (13.36, 14.5, "nombor asas", 80, 320, -1.5),
    (19.32, 20.0, "ada lambang", 50, 250, -2.0),
    (23.06, 26.95, "tambah · tolak", 50, 250, 2.0),
    (25.32, 26.95, "darab · bahagi", 80, 320, -1.5),
    (27.98, 29.7, "warna-warni", 50, 250, -2.0),
    (29.32, 29.7, "sangat menarik", 80, 320, 1.5),
]
CIRCLES = []
BIG_WORDS = [  # perkataan besar sekejap – tiada sticker masa ni
    (14.58, 17.10, "1, 2, 3", True),
    (21.62, 22.95, "+ − × ÷", False),
]
COVERS = []
YELLOW = (255, 200, 40, 255)
CTA = dict(title="belajar", title_at=29.76, title_y=230, card_at=30.0, card_y=1180,
           card_label="Puzzle Matematik", name="Puzzle Matematik",
           tags="nombor · operasi asas · warna-warni",
           button="Tekan beg kuning ↓", button_color=YELLOW, button_text_color=(22, 22, 26, 255))
