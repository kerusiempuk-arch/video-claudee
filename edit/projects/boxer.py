# Boxer lelaki (video 1gI1bGT7A2_I4DFTn-jw5PHQ8X-NKUNGH)
# --- langkah potong (cut.py), masa ikut video ASAL
REMOVE = [(13.20, 15.00)]   # "getah dia pun lembut" pertama – diulang lepas tu
SRC_END = 22.0              # selepas "...bakul kuning ni" + masa baca CTA
TAIL = 0.7                  # hujung tak dipotong senyap
PUNCH_Y = 0.25

END = 18.62                 # panjang selepas cut.py
CAPTION_Y = 880
CARD_Y = 1180
ZOOM = 0.04
CAPTION_ACCENT = (255, 212, 59, 255)  # kuning: baju biru muda buat biru-ungu tak nampak

# (group_end, [(word, start, highlight)]) – masa ikut video SELEPAS dipotong (Whisper atas cut.mp4)
CAPTIONS = [
    (1.06, [("Zaman", 0.00, False), ("sekarang", 0.58, False)]),
    (1.88, [("jarang", 1.08, False), ("orang", 1.60, False)]),
    (2.70, [("pakai", 1.90, False), ("spender", 2.26, True)]),
    (3.42, [("biasa", 2.72, False)]),
    (4.34, [("kebanyakan", 3.44, False)]),
    (5.28, [("pakai", 4.36, False), ("boxer", 4.72, True)]),
    (6.18, [("Sebab", 5.30, False), ("apa?", 5.94, False)]),
    (7.30, [("Pakai", 6.20, False), ("boxer", 6.50, False), ("ni", 6.96, False)]),
    (8.18, [("lebih", 7.32, False), ("selesa", 7.54, True)]),
    (9.16, [("pengudaraan", 8.20, True)]),
    (10.24, [("lebih", 9.18, False), ("lancar", 9.50, True)]),
    (11.10, [("Lagi", 10.26, False), ("satu", 10.56, False)]),
    (11.68, [("kain", 11.14, False), ("dia", 11.30, False), ("pun", 11.54, False)]),
    (12.42, [("sangat", 11.70, False), ("lembut", 12.06, True)]),
    (13.34, [("getah", 12.44, True), ("dia", 12.84, False), ("pun", 13.08, False)]),
    (13.92, [("lembut", 13.36, True)]),
    (14.95, [("Ada", 13.94, False), ("pelbagai", 14.06, False), ("saiz", 14.50, True)]),
    (16.30, [("ada", 15.20, False), ("pelbagai", 15.42, True)]),
    (17.00, [("Berminat?", 16.46, False)]),
    (17.50, [("dapatkan", 17.02, False), ("di", 17.40, False)]),
    (18.62, [("bakul", 17.52, True), ("kuning", 17.80, True), ("ni", 17.94, False)]),
]
HOOK = dict(end=5.3, y=100, kicker="seluar dalam lelaki paling", title="selesa",
            options=[("Spender biasa", "01"), ("Boxer", "02")], select_at=[2.26, 4.72])
SECTIONS = [
    (5.3, 10.26, "kelebihan", "1 / 3", "selesa & sejuk"),
    (10.26, 13.9, "kelebihan", "2 / 3", "kain & getah"),
    (13.9, 16.4, "kelebihan", "3 / 3", "pilihan"),
]
STICKERS = [  # (start, end, text, x, y, angle)
    (7.54, 10.2, "lebih selesa", 50, 250, 2.0),
    (9.18, 10.2, "udara lancar", 80, 320, -1.5),
    (12.06, 13.85, "kain lembut", 50, 250, 2.0),
    (13.36, 13.85, "getah lembut", 80, 320, -1.5),
    (14.50, 16.35, "pelbagai saiz", 50, 250, -2.0),
    (15.42, 16.35, "pelbagai warna", 80, 320, 1.5),
]
CIRCLES = []
YELLOW = (255, 200, 40, 255)
CTA = dict(title="selesa", title_at=16.4, title_y=230, card_at=16.7, card_y=1180,
           card_label="Boxer Lelaki", name="Boxer Lelaki",
           tags="selesa · kain lembut · pelbagai saiz",
           button="Tekan bakul kuning ↓", button_color=YELLOW, button_text_color=(22, 22, 26, 255))
