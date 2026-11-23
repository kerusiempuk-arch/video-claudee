# Boxer lelaki (video 1gI1bGT7A2_I4DFTn-jw5PHQ8X-NKUNGH)
END = 22.0
CAPTION_Y = 880
CARD_Y = 1180
ZOOM = 0.04
CAPTION_ACCENT = (255, 212, 59, 255)  # kuning: baju biru muda buat biru-ungu tak nampak

# (group_end, [(word, start, highlight)]) – masa dari transkripsi Whisper
CAPTIONS = [
    (1.08, [("Zaman", 0.00, False), ("sekarang", 0.64, False)]),
    (1.90, [("jarang", 1.10, False), ("dah", 1.60, False), ("orang", 1.78, False)]),
    (2.70, [("pakai", 1.92, False), ("spender", 2.28, True)]),
    (3.60, [("biasa", 2.72, False)]),
    (4.68, [("kebanyakan", 3.68, False)]),
    (5.50, [("pakai", 4.36, False), ("boxer", 4.70, True)]),
    (6.18, [("Sebab", 5.58, False), ("apa?", 5.94, False)]),
    (7.42, [("Pakai", 6.20, False), ("boxer", 6.54, False), ("ni", 6.96, False)]),
    (8.50, [("lebih", 7.44, False), ("selesa", 7.72, True)]),
    (9.32, [("pengudaraan", 8.56, True)]),
    (10.80, [("lebih", 9.34, False), ("lancar", 9.92, True)]),
    (11.50, [("Lagi", 10.86, False), ("satu", 11.02, False)]),
    (12.12, [("kain", 11.52, False), ("dia", 11.74, False), ("pun", 11.96, False)]),
    (13.40, [("sangat", 12.14, False), ("lembut", 12.48, True)]),
    (14.18, [("getah", 13.42, True), ("dia", 13.68, False), ("pun", 13.92, False)]),
    (16.40, [("lembut", 14.20, True)]),
    (18.15, [("Ada", 16.88, False), ("pelbagai", 16.98, False), ("saiz", 17.42, True)]),
    (19.80, [("ada", 18.22, False), ("pelbagai", 18.36, True)]),
    (20.76, [("Berminat?", 19.88, False), ("dapatkan", 20.36, False)]),
    (22.00, [("di", 20.78, False), ("bakul", 20.86, True), ("kuning", 21.10, True), ("ni", 21.20, False)]),
]
HOOK = dict(end=5.5, y=100, kicker="seluar dalam lelaki paling", title="selesa",
            options=[("Spender biasa", "01"), ("Boxer", "02")], select_at=[2.28, 4.70])
SECTIONS = [
    (5.5, 10.8, "kelebihan", "1 / 3", "selesa & sejuk"),
    (10.8, 16.6, "kelebihan", "2 / 3", "kain & getah"),
    (16.6, 19.8, "kelebihan", "3 / 3", "pilihan"),
]
STICKERS = [  # (start, end, text, x, y, angle)
    (7.7, 10.7, "lebih selesa", 50, 250, 2.0),
    (9.3, 10.7, "udara lancar", 80, 320, -1.5),
    (12.4, 16.5, "kain lembut", 50, 250, 2.0),
    (13.6, 16.5, "getah lembut", 80, 320, -1.5),
    (17.4, 19.7, "pelbagai saiz", 50, 250, -2.0),
    (18.6, 19.7, "pelbagai warna", 80, 320, 1.5),
]
CIRCLES = []
YELLOW = (255, 200, 40, 255)
CTA = dict(title="selesa", title_at=19.8, title_y=230, card_at=20.4, card_y=1180,
           card_label="Boxer Lelaki", name="Boxer Lelaki",
           tags="selesa · kain lembut · pelbagai saiz",
           button="Tekan bakul kuning ↓", button_color=YELLOW, button_text_color=(22, 22, 26, 255))
