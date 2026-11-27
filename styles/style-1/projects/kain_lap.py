# Kain Lap Dapur (gulung, serat buluh) (Drive 154vaB4qt49LcoP3EsC8IuMvq9pyLuAip)
REMOVE = [
    (9.84, 10.45),   # "okay" perlahan
    (12.95, 13.70),  # "okay"
    (17.75, 18.50),  # "okay"
    (23.95, 24.40),  # "okay"
    (29.60, 43.70),  # cubaan pertama "Kotor, kita boleh basuh…" + bual luar skrip ("boleh… jangan … adiklah") – simpan ulangan lengkap
]
SRC_END = 49.3
TAIL = 1.2
PUNCH_Y = 0.25
END = 29.33
CAPTION_Y = 900   # muka rendah dalam video ni → kapsyen di dada
CARD_Y = 1420
ZOOM = 0.04
SFX_WHOOSH = "drop"   # produk dapur
CAPTIONS = [
    (0.60, [("Kain", 0.00, False), ("lap", 0.42, True)]),
    (1.52, [("kat", 0.60, False), ("dapur", 0.82, True)]),
    (3.12, [("Setiap", 1.96, False), ("dapur", 2.20, True), ("rumah", 2.52, False)]),
    (3.68, [("wajib", 3.12, True), ("ada", 3.48, False)]),
    (4.32, [("benda", 3.68, False), ("ni", 3.96, False)]),
    (4.90, [("Kalau", 4.32, False), ("tak", 4.54, False), ("ada", 4.74, False)]),
    (5.80, [("benda", 4.90, False), ("ni", 5.12, False)]),
    (7.00, [("nampak", 5.80, False), ("berselera", 6.30, True)]),
    (8.36, [("nampak", 7.06, False), ("kotor", 7.28, True), ("dapur", 7.66, True)]),
    (9.80, [("Ini", 8.70, False), ("macam", 8.86, False), ("tisu", 9.22, True)]),
    (10.84, [("tapi", 9.80, False), ("dia", 10.10, False), ("kain", 10.36, True)]),
    (11.58, [("Dibuat", 10.84, False), ("daripada", 11.08, False)]),
    (12.66, [("serat", 11.58, True), ("buluh", 11.96, True)]),
    (13.62, [("Sangat", 12.66, False), ("tahan", 13.00, True)]),
    (14.84, [("Susah", 13.62, False), ("nak", 14.00, False), ("koyak", 14.14, True)]),
    (15.70, [("Gulungan", 14.88, True), ("dia", 15.36, False), ("ni", 15.52, False)]),
    (16.06, [("kita", 15.70, False), ("boleh", 15.86, False)]),
    (16.78, [("tarik", 16.06, True), ("saja", 16.48, False)]),
    (17.68, [("dan", 16.78, False), ("dia", 17.08, False), ("putus", 17.30, True)]),
    (18.42, [("macam", 17.68, False), ("ni", 17.98, False)]),
    (19.80, [("Macam", 18.42, False), ("gulungan", 18.70, False), ("tisu", 19.10, True)]),
    (20.66, [("Lap", 19.86, True), ("meja", 19.96, True)]),
    (22.08, [("lap", 20.84, True), ("cawan", 21.04, True), ("basah", 21.38, False)]),
    (23.14, [("lap", 22.08, True), ("pinggan", 22.28, True), ("basah", 22.62, False)]),
    (24.10, [("Sangat", 23.14, False), ("sesuai", 23.44, True)]),
    (24.94, [("Kotor", 24.10, True), ("kita", 24.40, False), ("boleh", 24.66, False)]),
    (25.48, [("basuh", 24.94, True), ("dan", 25.30, False)]),
    (25.90, [("kita", 25.48, False), ("boleh", 25.68, False)]),
    (27.42, [("guna", 25.90, False), ("berulang", 26.36, True), ("kali", 26.84, False)]),
    (28.10, [("Berminat", 27.42, False)]),
    (28.48, [("dapatkan", 28.10, False), ("di", 28.40, False)]),
    (29.33, [("beg", 28.48, True), ("kuning", 28.62, True)]),
]
HOOK = dict(end=5.6, y=100, kicker="kain lap dapur,", title="wajib",
            options=[("Kain lap", "01"), ("Setiap dapur", "02"), ("Wajib ada", "03")],
            select_at=[0.00, 1.96, 3.12])
SECTIONS = [
    (8.70, 14.80, "kelebihan", "1 / 3", "macam tisu, tapi kain"),
    (14.88, 24.00, "kelebihan", "2 / 3", "tarik & putus"),
    (24.10, 27.35, "kelebihan", "3 / 3", "boleh basuh"),
]
STICKERS = [
    (8.86, 10.80, "macam tisu", 80, 250, 2.0),
    (10.36, 10.80, "tapi kain ✓", 130, 320, -1.5),
    (11.58, 12.62, "serat buluh", 80, 250, 2.0),
    (16.06, 18.36, "tarik saja", 80, 250, 2.0),
    (17.30, 18.36, "putus sendiri ✓", 130, 320, -1.5),
    (19.86, 23.05, "lap meja", 80, 250, 2.0),
    (20.84, 23.05, "cawan basah", 130, 320, -1.5),
    (22.08, 23.05, "pinggan basah", 80, 390, 1.5),
    (24.94, 27.30, "boleh basuh", 80, 250, 2.0),
    (25.90, 27.30, "guna berulang kali ✓", 130, 320, -1.5),
]
CIRCLES = []
BIG_WORDS = [
    (12.66, 14.70, "tahan", True),
    (23.14, 24.05, "sesuai", True),
]
CTA = dict(title="wajib", title_at=27.30, title_y=230, card_at=27.42, card_y=1180,
           card_label="Kain Lap Dapur", name="Kain Lap Dapur", tags="tahan · boleh basuh · guna semula",
           button="Tekan beg kuning ↓", button_color=(255, 200, 40, 255), button_text_color=(22, 22, 26, 255))

COVERS = []
