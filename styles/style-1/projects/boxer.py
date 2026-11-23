# Boxer lelaki (Drive 1gI1bGT7A2_I4DFTn-jw5PHQ8X-NKUNGH) — CONTOH STYLE 1 YANG DILULUSKAN
# --- langkah potong (cut.py), masa ikut video ASAL
REMOVE = [
    (3.30, 3.62),    # "aaa" sebelum "kebanyakan"
    (13.20, 15.00),  # "getah dia pun lembut" pertama – diulang lepas tu
    (17.95, 19.70),  # "ada pelbagai… okay" – ulangan tak habis + "okay"
]
SRC_END = 22.0              # selepas "...bakul kuning ni" + masa baca CTA
TAIL = 0.7                  # hujung tak dipotong senyap
PUNCH_Y = 0.25

END = 16.97                 # panjang selepas cut.py
CAPTION_Y = 1780            # bawah (permintaan user)
CARD_Y = 1180
ZOOM = 0.04
CAPTION_ACCENT = (255, 212, 59, 255)  # kuning: baju biru muda buat biru-ungu tak nampak

# (group_end, [(word, start, highlight)]) – masa ikut video SELEPAS dipotong (Whisper atas cut.mp4)
CAPTIONS = [
    (1.36, [("Zaman", 0.00, False), ("sekarang", 0.64, False)]),
    (1.90, [("jarang", 1.38, False), ("dah", 1.60, False), ("orang", 1.78, False)]),
    (2.72, [("pakai", 1.92, False), ("spender", 2.28, True)]),
    (3.42, [("biasa", 2.74, False)]),
    (4.02, [("Kebanyakan", 3.44, False)]),
    (5.30, [("pakai", 4.04, False), ("boxer", 4.42, True)]),
    (5.94, [("Sebab", 5.34, False), ("apa?", 5.64, False)]),
    (6.96, [("Pakai", 5.96, False), ("boxer", 6.24, False), ("ni", 6.76, False)]),
    (8.24, [("lebih", 6.98, False), ("selesa", 7.22, True)]),
    (8.84, [("Pengudaraan", 8.26, True)]),
    (10.06, [("lebih", 8.86, False), ("lancar", 9.18, True)]),
    (10.82, [("Lagi", 10.10, False), ("satu", 10.28, False)]),
    (11.34, [("kain", 10.84, False), ("dia", 11.00, False), ("pun", 11.24, False)]),
    (12.26, [("sangat", 11.36, False), ("lembut", 11.76, True)]),
    (13.04, [("getah", 12.28, True), ("dia", 12.52, False), ("pun", 12.76, False)]),
    (13.56, [("lembut", 13.06, True)]),
    (14.90, [("Ada", 13.58, False), ("pelbagai", 13.80, False), ("saiz", 14.22, True)]),
    (15.82, [("Berminat?", 14.92, False), ("dapatkan", 15.34, False), ("di", 15.74, False)]),
    (16.97, [("bakul", 15.84, True), ("kuning", 16.14, True), ("ni", 16.32, False)]),
]
HOOK = dict(end=5.3, y=100, kicker="seluar dalam lelaki paling", title="selesa",
            options=[("Spender biasa", "01"), ("Boxer", "02")], select_at=[2.28, 4.42])
SECTIONS = [
    (5.3, 10.06, "kelebihan", "1 / 3", "selesa & sejuk"),
    (10.06, 13.56, "kelebihan", "2 / 3", "kain & getah"),
    (13.56, 14.9, "kelebihan", "3 / 3", "pilihan"),
]
STICKERS = [  # (start, end, text, x, y, angle)
    (7.22, 10.0, "lebih selesa", 50, 250, 2.0),
    (8.86, 10.0, "udara lancar", 80, 320, -1.5),
    (11.76, 13.5, "kain lembut", 50, 250, 2.0),
    (13.06, 13.5, "getah lembut", 80, 320, -1.5),
    (14.22, 14.88, "pelbagai saiz", 50, 250, -2.0),
    (14.45, 14.88, "pelbagai warna", 80, 320, 1.5),
]
CIRCLES = []
YELLOW = (255, 200, 40, 255)
CTA = dict(title="selesa", title_at=14.9, title_y=230, card_at=15.2, card_y=1180,
           card_label="Boxer Lelaki", name="Boxer Lelaki",
           tags="selesa · kain lembut · pelbagai saiz",
           button="Tekan bakul kuning ↓", button_color=YELLOW, button_text_color=(22, 22, 26, 255))
