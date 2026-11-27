# Puzzle matematik (Drive 1X4fJgvvZoKB5RP4V_89KDUJCKxOHoXvG)
# ---------- potongan (build.py) – masa ikut video ASAL
REMOVE = [
    (0.00, 1.17),    # senyap awal + perkataan pendek "Ki…" (owner: buang terus)
    (3.78, 4.25),    # "okey"
    (10.15, 10.78),  # "nah"
    (12.55, 13.76),  # "okay"/"ha" pendek sebelum "Dalam ni"
    (21.84, 22.36),  # "okay"
    (22.98, 25.25),  # "ada, aa," (cubaan pertama) – kekal "Dan juga | ada lambang"
    (34.50, 37.40),  # "Okay. Beserta dengan warna." (cubaan pertama)
]
SRC_END = 42.03
TAIL = 0.83
PUNCH_Y = 0.00

# ---------- overlay – masa ikut video SELEPAS dipotong
END = 31.18
CAPTION_Y = 680
CARD_Y = 1420
ZOOM = 0.04

C_ = lambda end, *ws: (end, [(w, t, h) for w, t, h in ws])
CAPTIONS = [
    C_(0.71, ("Puzzle", 0.00, True)),
    C_(1.25, ("ataupun", 0.73, False)),
    C_(2.67, ("puzzle", 1.27, False), ("matematik", 1.79, True)),
    C_(3.57, ("Sesuai", 2.69, False), ("untuk", 3.23, False)),
    C_(4.55, ("anak-anak", 3.59, True), ("yang", 4.09, False), ("baru", 4.31, False)),
    C_(5.07, ("nak", 4.57, False), ("mengenal", 4.83, False)),
    C_(6.11, ("nombor", 5.09, True)),
    C_(7.51, ("Dia", 6.15, False), ("mainan", 6.79, True)),
    C_(8.57, ("sambil", 7.53, False), ("belajar", 7.87, True)),
    C_(9.43, ("Kita", 8.59, False), ("boleh", 8.79, False), ("pusing", 9.01, True)),
    C_(10.21, ("macam", 9.45, False), ("ni", 9.77, False)),
    C_(11.27, ("Dalam", 10.23, False), ("ni", 10.35, False), ("dia", 11.09, False)),
    C_(11.85, ("ada", 11.29, False), ("tulis", 11.43, False)),
    C_(12.61, ("nombor", 11.87, True)),
    C_(14.19, ("Nombor", 12.63, False), ("asas", 12.99, True), ("saja", 13.35, False)),
    C_(15.21, ("Satu,", 14.21, False), ("dua,", 14.85, False)),
    C_(16.75, ("tiga,", 15.23, False)),
    C_(17.59, ("sampai", 16.77, False), ("kosong", 16.89, True)),
    C_(18.19, ("Dan", 17.61, False), ("juga", 17.81, False)),
    C_(19.75, ("ada", 18.21, False), ("lambang", 18.95, True)),
    C_(20.63, ("Selain", 19.77, False), ("itu", 20.01, False), ("dia", 20.23, False)),
    C_(21.23, ("juga", 20.35, False), ("ada", 20.65, False)),
    C_(22.35, ("operasi", 21.25, True), ("asas", 21.71, True)),
    C_(23.41, ("Seperti", 22.37, False), ("tambah,", 22.69, True)),
    C_(24.03, ("tolak,", 23.43, True)),
    C_(24.93, ("sama", 24.05, False), ("dengan,", 24.33, False)),
    C_(26.05, ("darab", 24.95, True), ("dan", 25.55, False), ("juga", 25.81, False)),
    C_(26.71, ("bahagi", 26.07, True)),
    C_(27.97, ("Berserta", 26.73, False), ("dengan", 27.07, False)),
    C_(28.63, ("warna-warni", 27.61, True)),
    C_(29.37, ("Sangat", 28.65, False), ("menarik", 28.95, True)),
    C_(30.61, ("Berminat?", 29.39, False), ("dapatkan", 30.15, False)),
    C_(31.18, ("di", 30.63, False), ("beg", 30.73, True), ("kuning", 30.83, True)),
]
HOOK = dict(end=5.93, y=100, kicker="mainan sambil", title="belajar",
            options=[("Puzzle", "01"), ("Puzzle matematik", "02")], select_at=[0.09, 1.27])
SECTIONS = [
    (6.13, 10.13, "kelebihan", "1 / 3", "mainan sambil belajar"),
    (10.13, 19.73, "kelebihan", "2 / 3", "nombor & lambang"),
    (19.73, 26.63, "kelebihan", "3 / 3", "operasi asas"),
]
STICKERS = [  # (mula, tamat, teks, x, y, sudut)
    (7.87, 10.03, "sambil belajar", 50, 250, 2.0),
    (9.01, 10.03, "boleh pusing", 80, 320, -1.5),
    (11.87, 14.13, "ada nombor", 50, 250, 2.0),
    (12.99, 14.13, "nombor asas", 80, 320, -1.5),
    (18.95, 19.63, "ada lambang", 50, 250, -2.0),
    (22.69, 26.58, "tambah · tolak", 50, 250, 2.0),
    (24.95, 26.58, "darab · bahagi", 80, 320, -1.5),
    (27.61, 29.33, "warna-warni", 50, 250, -2.0),
    (28.95, 29.33, "sangat menarik", 80, 320, 1.5),
]
CIRCLES = []
BIG_WORDS = [  # perkataan besar sekejap – tiada sticker masa ni
    (14.21, 16.73, "1, 2, 3", True),
    (21.25, 22.58, "+ − × ÷", False),
]
COVERS = []
YELLOW = (255, 200, 40, 255)
CTA = dict(title="belajar", title_at=29.39, title_y=230, card_at=29.63, card_y=1180,
           card_label="Puzzle Matematik", name="Puzzle Matematik",
           tags="nombor · operasi asas · warna-warni",
           button="Tekan beg kuning ↓", button_color=YELLOW, button_text_color=(22, 22, 26, 255))
