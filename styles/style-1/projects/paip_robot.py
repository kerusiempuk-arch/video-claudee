# Paip tangan robot / paip mekanikal (Drive 1WfT1JZHO3yhyuK3X5n8vZ18jj7NGoHOi) — Style 1
# Bina: python3 -I styles/style-1/build.py work/vid1127/raw.mp4 styles/style-1/projects/paip_robot.py work/vid1127/hf
REMOVE = [
    (6.24, 6.72),    # "okey"
    (12.88, 13.45),  # "okey"
    (18.42, 20.90),  # "Aku pusing ni" (cubaan pertama – ulang)
    (23.25, 24.12),  # "Okay"
    (26.22, 27.66),  # "Oke, nah,"
    (30.85, 31.45),  # "Kita," (mula semula)
    (32.70, 33.88),  # "kita boleh nak laras," (ulang – simpan "kita boleh nak adjust")
    (34.84, 37.26),  # "okey, nak basuh," (cubaan pertama)
    (39.75, 40.34),  # "okay"
]
SRC_END = 53.1
TAIL = 1.2
PUNCH_Y = 0.25

# ---------- overlay – masa ikut video SELEPAS dipotong
END = 35.57
CAPTION_Y = 1060      # tiada muka; produk (paip) di y 240–960 → kapsyen di bawah paip, atas sinki
CARD_Y = 1420
ZOOM = 0.04
SFX_WHOOSH = "drop"   # produk air / dapur

C_ = lambda end, *ws: (end, [(w, t, h) for w, t, h in ws])
CAPTIONS = [
    C_(0.94, ("Sekarang", 0.00, False), ("aku", 0.60, False)),
    C_(1.76, ("dah", 0.78, False), ("pasang", 0.94, True)),
    C_(2.26, ("paip", 1.76, True), ("ni", 2.00, False)),
    C_(3.10, ("Aku", 2.26, False), ("panggil", 2.48, False), ("paip", 2.80, False)),
    C_(3.84, ("tangan", 3.10, True), ("robot", 3.44, True)),
    C_(4.66, ("ataupun", 3.84, False), ("paip", 4.32, False)),
    C_(5.50, ("mekanikal", 4.66, True)),
    C_(6.50, ("Nak", 5.58, False), ("dongak", 5.82, True), ("ke", 6.16, False)),
    C_(6.88, ("atas", 6.50, False)),
    C_(7.90, ("nak", 6.88, False), ("turun", 7.00, True), ("ke", 7.20, False)),
    C_(8.06, ("bawah", 7.42, False)),
    C_(8.92, ("nak", 7.90, False), ("pusing", 8.06, True)),
    C_(10.30, ("360", 8.92, True), ("darjah", 9.48, False)),
    C_(11.34, ("Bagi", 10.40, False), ("air", 10.74, False), ("keluar", 10.98, True)),
    C_(13.10, ("ni", 11.34, False), ("tengok", 11.94, False), ("sekarang", 12.24, False)),
    C_(14.34, ("keseluruhan", 13.10, True), ("lubang", 13.66, False)),
    C_(15.06, ("air", 14.34, False), ("keluar", 14.48, True)),
    C_(16.86, ("Aku", 15.06, False), ("pusing", 15.34, True), ("ni", 15.72, False)),
    C_(17.62, ("Air", 16.86, False), ("mengalir", 17.00, True)),
    C_(18.46, ("ikut", 17.62, False), ("lubang", 17.78, False), ("tengah", 18.10, True)),
    C_(19.32, ("saja", 18.46, False), ("ni", 18.80, False)),
    C_(20.42, ("Jangkauan", 19.32, True), ("air", 19.88, False), ("dia", 20.10, False)),
    C_(20.80, ("kita", 20.42, False), ("boleh", 20.58, False)),
    C_(21.44, ("nak", 20.80, False), ("adjust", 21.02, True)),
    C_(23.06, ("Nak", 21.44, False), ("basuh", 21.64, False), ("sekitar", 22.00, False)),
    C_(23.86, ("singki", 23.06, True), ("ni", 23.56, False)),
    C_(24.80, ("kita", 23.86, False), ("boleh", 24.16, False), ("dongak", 24.42, True)),
    C_(25.52, ("macam", 24.80, False), ("ni", 25.06, False)),
    C_(26.28, ("Air", 25.52, False), ("akan", 25.70, False), ("pergi", 25.94, False)),
    C_(27.46, ("lebih", 26.28, False), ("jauh", 26.68, True)),
    C_(28.58, ("Nak", 27.46, False), ("cuci", 27.64, False), ("pinggan", 27.98, True)),
    C_(29.50, ("nak", 28.58, False), ("cuci", 28.76, False), ("singki", 29.02, True)),
    C_(30.38, ("sangat", 29.50, False), ("mudah", 29.88, True)),
    C_(31.94, ("walaupun", 30.38, False), ("nampak", 31.06, False), ("kecil", 31.38, True)),
    C_(32.46, ("Berminat", 31.94, False)),
    C_(33.26, ("dengan", 32.46, False), ("paip", 33.02, False)),
    C_(34.14, ("tangan", 33.26, True), ("robot", 33.56, True), ("ni", 33.84, False)),
    C_(34.56, ("dapatkan", 34.14, False)),
    C_(35.57, ("di", 34.56, False), ("beg", 34.66, True), ("kuning", 34.86, True)),
]
HOOK = dict(end=5.5, y=100,
            kicker="paip dapur paling", title="fleksibel",
            options=[("Paip tangan robot", "01"), ("Paip mekanikal", "02")], select_at=[3.10, 4.32])
SECTIONS = [
    (5.5, 10.3, "kelebihan", "1 / 3", "gerak ikut suka"),
    (10.3, 19.3, "kelebihan", "2 / 3", "2 cara air keluar"),
    (19.3, 31.9, "kelebihan", "3 / 3", "air pergi lebih jauh"),
]
STICKERS = [
    (5.9, 10.2, "dongak ke atas", 50, 250, 2.0),
    (7.0, 10.2, "turun ke bawah", 80, 320, -1.5),
    (8.9, 10.2, "pusing 360°", 110, 390, 1.5),
    (13.1, 19.2, "semua lubang", 50, 250, -2.0),
    (17.6, 19.2, "lubang tengah saja", 80, 320, 1.5),
    (21.0, 27.3, "boleh adjust", 50, 250, 2.0),
    (22.0, 27.3, "basuh sekitar singki", 80, 320, -1.5),
    (25.9, 27.3, "air pergi lebih jauh", 110, 390, 1.5),
    (27.6, 29.4, "cuci pinggan ✓", 50, 250, -2.0),
    (28.8, 29.4, "cuci singki ✓", 80, 320, 1.5),
]
CIRCLES = []
BIG_WORDS = [(29.6, 31.8, "mudah", True)]
CTA = dict(title="fleksibel", title_at=31.94, title_y=230, card_at=32.4, card_y=1180,
           card_label="Paip Tangan Robot", name="Paip Tangan Robot", tags="dongak · pusing 360° · 2 mod air",
           button="Tekan beg kuning ↓", button_color=(255, 200, 40, 255), button_text_color=(22, 22, 26, 255))
COVERS = []
