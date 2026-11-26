# Tagooli 8-in-1 Advanced Multivitamin Soft Chews – vitamin kucing (Drive 11YujZMT0ddOBeJxHrGlUf5NjaRrclbjB)
REMOVE = [
    (0.00, 0.95),    # senyap awal
    (7.70, 8.74),    # "Kucing dah," (mula tak habis)
    (17.65, 19.55),  # "Bentuk dia." (cubaan pertama)
    (24.16, 25.05),  # "Okay."
    (29.94, 31.86),  # "Dapatkan," (ulangan pertama)
    (35.45, 36.74),  # "berminat," (ulangan pertama)
]
SRC_END = 38.40       # buang "saya ni..." di hujung
TAIL = 1.2
PUNCH_Y = 0.25
END = 28.65
CAPTION_Y = 680
CARD_Y = 1420
ZOOM = 0.04

C_ = lambda end, *ws: (end, [(w, t, h) for w, t, h in ws])
CAPTIONS = [  # 0–3.8s tiada kapsyen: close-up produk (kapsyen tutup label), pilihan kad hook dah sebut
    C_(4.66, ("Ini", 3.82, False), ("untuk", 4.16, False)),
    C_(5.90, ("vitamin", 4.68, False), ("kucing.", 5.10, True)),
    C_(6.90, ("Kalau", 6.24, False), ("nampak", 6.48, False)),
    C_(7.60, ("kucing", 6.88, False), ("dah", 7.22, False), ("tak", 7.40, False)),
    C_(8.60, ("selera", 7.62, True), ("makan,", 7.94, False)),
    C_(9.50, ("dah", 8.74, False), ("lesu,", 8.98, True)),
    C_(11.00, ("kurang", 9.54, False), ("ceria", 9.74, True), ("tu.", 10.20, False)),
    C_(12.26, ("Maksudnya,", 11.42, False), ("dia", 11.88, False), ("ada", 12.08, False)),
    C_(13.26, ("kekurangan", 12.28, True), ("sesuatu", 12.82, False)),
    C_(14.40, ("dalam", 13.28, False), ("badan", 13.50, False), ("dia.", 13.98, False)),
    C_(15.24, ("Kita", 14.64, False), ("tengok", 14.94, False)),
    C_(16.00, ("bentuk", 15.26, True), ("dia", 15.74, False)),
    C_(16.95, ("macam", 16.12, False), ("ni.", 16.52, False)),
    C_(17.68, ("Bau", 17.02, True), ("pun,", 17.38, False)),
    C_(18.92, ("kucing", 17.72, False), ("dah", 18.06, False), ("berselera.", 18.22, True)),
    C_(19.80, ("Harga", 18.98, False)),
    C_(21.00, ("sangat-sangat", 19.44, False), ("berbaloi.", 20.08, True)),
    C_(22.10, ("Nak", 21.04, False), ("kucing", 21.22, False), ("ceria,", 21.58, True)),
    C_(23.40, ("kucing", 22.18, False), ("sihat.", 22.50, True)),
    C_(24.90, ("Dapatkan", 23.46, False), ("8-in-1", 24.10, True)),
    C_(26.10, ("multivitamin", 25.06, False)),
    C_(27.20, ("soft", 26.18, False), ("chews.", 26.42, True)),
    C_(27.90, ("Berminat,", 27.32, False)),
    C_(28.65, ("klik", 27.92, False), ("beg", 28.02, True), ("kuning.", 28.14, True)),
]
HOOK = dict(end=5.90, y=100,
            kicker="multivitamin kucing,", title="ceria",
            options=[("8-in-1", "01"), ("Soft chews", "02"), ("Vitamin kucing", "03")],
            select_at=[0.00, 3.00, 4.68])
SECTIONS = [
    (5.90, 14.40, "kelebihan", "1 / 3", "bila kucing lesu"),
    (14.40, 18.90, "kelebihan", "2 / 3", "kucing berselera"),
    (18.90, 23.30, "kelebihan", "3 / 3", "harga berbaloi"),
]
STICKERS = [
    (7.62, 11.00, "tak selera makan", 80, 260, 2.0),
    (8.98, 11.00, "lesu, kurang ceria", 130, 340, -1.5),
    (12.28, 14.35, "kekurangan sesuatu", 80, 260, 2.0),
    (15.26, 18.85, "bentuk soft chew", 80, 260, 2.0),
    (17.72, 18.85, "kucing berselera ✓", 130, 340, -1.5),
    (19.44, 20.95, "harga berbaloi ✓", 80, 260, 2.0),
    (21.22, 23.25, "kucing ceria", 80, 260, 2.0),
    (22.50, 23.25, "kucing sihat ✓", 130, 340, -1.5),
]
CIRCLES = []
BIG_WORDS = []  # "berbaloi." besar tutup muka (y tetap 230–450) -> guna sticker
CTA = dict(title="ceria", title_at=23.30, title_y=230, card_at=23.46, card_y=1180,
           card_label="Tagooli", name="Tagooli 8-in-1 Multivitamin", tags="8-in-1 · soft chews · kucing sihat",
           button="Tekan beg kuning ↓", button_color=(255, 200, 40, 255), button_text_color=(22, 22, 26, 255))

# ---------- cover photo (tools/cover.py) – `at` ikut masa video ASAL
COVERS = []
