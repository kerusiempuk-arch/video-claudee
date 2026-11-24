# Vakum kereta tanpa wayar (Drive 10P-8Qfyc6WqY3en5g6d48BQd0SH9ctWq)
REMOVE = [
    (0.00, 0.80),    # "aaa" pembuka
    (6.94, 7.14),    # "ha"
    (8.46, 9.56),    # "haaa" + "abu" ketiga (gagap)
    (12.86, 13.42),  # "haaa"
    (14.76, 15.04),  # "haa"
    (17.30, 18.68),  # "haa, ni, haa"
    (19.76, 20.52),  # "haa"
    (22.86, 23.68),  # "okay"
    (26.12, 26.80),  # "okay"
    (28.24, 29.40),  # "ok" + "haa"
]
SRC_END = 40.4
TAIL = 1.2
PUNCH_Y = 0.25

END = 30.56
CAPTION_Y = 1780
CARD_Y = 1180
ZOOM = 0.04
CAPTION_ACCENT = (255, 212, 59, 255)   # baju biru muda

CAPTIONS = [  # (group_end, [(word, start, highlight)]) — masa SELEPAS dipotong
    (0.50, [("Nak", 0.00, False), ("vacuum", 0.18, True)]),
    (1.48, [("tempat-tempat", 0.52, False), ("sempit", 1.12, True)]),
    (1.92, [("macam", 1.50, False), ("ni", 1.80, False)]),
    (2.76, [("Kalau", 1.94, False), ("kita", 2.18, False), ("nak", 2.46, False)]),
    (3.70, [("guna", 2.60, False), ("penyapu", 2.78, True), ("biasa", 3.26, False)]),
    (4.38, [("nak", 3.80, False), ("guna", 3.84, False), ("tangan", 4.06, False)]),
    (4.88, [("susah", 4.40, True)]),
    (5.90, [("Aku", 4.90, False), ("pakai", 5.08, False), ("ini", 5.40, True)]),
    (7.10, [("Tengok", 6.50, False)]),
    (8.00, [("Habuk", 7.12, True), ("apa", 7.54, False)]),
    (8.62, [("pasir-pasir", 8.06, True)]),
    (10.36, [("celah-celah", 8.64, False), ("sempit", 9.26, True), ("ni", 9.86, False)]),
    (10.86, [("Menggunakan", 10.38, False)]),
    (11.76, [("vacuum", 10.88, True), ("ni", 11.40, False)]),
    (12.66, [("senang", 11.78, True), ("lagi", 12.48, False)]),
    (13.94, [("lebih", 12.68, False), ("berkesan", 13.20, True)]),
    (15.06, [("Tengok", 13.96, False), ("aku", 14.38, False), ("buat", 14.64, False)]),
    (16.54, [("sekejap", 15.08, True), ("sahaja", 15.62, False)]),
    (17.40, [("Terus", 16.56, False), ("cuci", 16.98, True)]),
    (18.44, [("Ini", 17.42, False), ("tak", 17.84, False), ("payah", 18.16, False)]),
    (19.50, [("nak", 18.46, False), ("tarik", 18.66, False), ("wire", 19.10, True)]),
    (20.40, [("Pakai", 19.52, False), ("bateri", 19.76, True), ("sahaja", 20.12, False)]),
    (20.98, [("kita", 20.42, False), ("cas", 20.70, True)]),
    (22.04, [("Depan", 21.02, False), ("dia", 21.54, False), ("ada", 21.62, False), ("brus", 21.78, True)]),
    (22.88, [("dia", 22.06, False), ("macam", 22.30, False), ("ni", 22.60, False)]),
    (23.50, [("Jadinya", 22.90, False)]),
    (24.48, [("dia", 23.52, False), ("melekat", 23.66, True), ("apa", 24.08, False), ("semua", 24.26, False)]),
    (25.18, [("kita", 24.50, False), ("tenyeh", 24.80, True)]),
    (25.96, [("dengan", 25.20, False), ("brus", 25.40, True), ("tu", 25.74, False)]),
    (27.06, [("dia", 25.98, False), ("akan", 26.34, False)]),
    (27.94, [("cepat", 27.08, False), ("disedut", 27.50, True)]),
    (28.86, [("Berminat", 27.96, False), ("dapatkan", 28.48, False)]),
    (29.95, [("di", 28.88, False), ("beg", 28.98, False), ("kuning", 29.12, True)]),
]
HOOK = dict(end=6.3, y=100, kicker="vacuum celah sempit paling", title="senang",
            options=[("Penyapu / tangan", "01"), ("Vacuum tanpa wayar", "02")], select_at=[2.78, 5.08])
SECTIONS = [  # (mula, tamat, "kelebihan", "1 / 3", subtajuk)
    (6.3, 13.96, "kelebihan", "1 / 3", "masuk celah sempit"),
    (13.96, 21.0, "kelebihan", "2 / 3", "tanpa wayar"),
    (21.0, 27.96, "kelebihan", "3 / 3", "ada brus depan"),
]
STICKERS = [  # (mula, tamat, teks, x, y, sudut)
    (7.12, 13.8, "habuk & pasir", 70, 300, 2.0),
    (8.64, 13.8, "celah-celah sempit", 110, 370, -1.5),
    (11.78, 13.8, "senang & berkesan", 150, 440, 1.5),
    (15.08, 20.9, "siap sekejap je", 70, 300, -2.0),
    (17.42, 20.9, "tak payah tarik wire", 110, 370, 1.5),
    (19.52, 20.9, "bateri, boleh cas", 150, 440, -1.5),
    (21.78, 27.9, "brus kat muncung", 70, 300, 2.0),
    (24.80, 27.9, "tenyeh kotoran melekat", 110, 370, -1.5),
    (27.08, 27.9, "cepat disedut", 150, 440, 1.5),
]
CIRCLES = []  # (mula, tamat, cx, cy, r, label, label_x, label_y)
CTA = dict(title="senang", title_at=27.96, title_y=230, card_at=28.6, card_y=1180,
           card_label="Vacuum Kereta", name="Vacuum Tanpa Wayar", tags="tanpa wayar · bateri cas · ada brus",
           button="Tekan bakul kuning ↓", button_color=(255, 200, 40, 255), button_text_color=(22, 22, 26, 255))
