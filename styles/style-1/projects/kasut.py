# Kasut hitam (Drive 1_XhbVNVhXZDvXYCVnvAVr6_DkSsxzyUH) — salin fail ni, isi ikut video. Contoh lengkap: styles/style-1/projects/boxer.py. Bina: python3 -I styles/style-1/build.py <raw.mp4> <fail ini> <work_dir>
# ---------- potongan (build.py) – masa ikut video ASAL
REMOVE = [
    (0.0, 0.68),     # "Ha,"
    (7.55, 7.80),    # "okay"
    (8.75, 9.14),    # "ha"
    (16.05, 17.14),  # "okay, kasut ni." – ulangan tak habis
    (20.50, 20.90),  # "okay"
    (22.58, 23.86),  # "okay, tapak dia pun." – ulangan tak habis
    (29.42, 36.95),  # "okay, yang penting harga murah. Berminat." – take pertama
]
SRC_END = 41.6        # hujung video
TAIL = 1.2            # hujung tak dipotong senyap — masa baca CTA (1.2s supaya kad CTA sempat dibaca)
PUNCH_Y = 0.25        # punch-in fokus ke atas (muka)

# ---------- overlay (build.py) – masa ikut video SELEPAS dipotong
END = 24.79           # panjang selepas potongan (build.py --plan)
CAPTION_Y = 680       # atas, paras dada (pilihan user); kena muka -> 700–760
CARD_Y = 1180
ZOOM = 0.04

G = [  # (perkataan, mula, highlight) – masa selepas dipotong (Whisper atas cut.wav)
    [("Tengok", 0.00, False), ("kasut", 0.34, False), ("ni", 0.66, False)],
    [("aku", 0.82, False), ("pakai", 1.00, False)],
    [("sangat", 1.54, False), ("selesa", 2.02, True)],
    [("Kasut", 2.76, False), ("ni", 2.94, False)],
    [("warna", 3.34, False), ("hitam", 3.64, True)],
    [("Ada", 4.40, False), ("pelbagai", 4.58, False), ("saiz", 5.00, True)],
    [("Ada", 5.58, False), ("warna", 5.74, False), ("biru", 5.98, True)],
    [("Kasut", 6.50, False), ("ni", 6.82, False)],
    [("pergi", 7.44, False), ("jalan-jalan", 7.74, True)],
    [("santai-santai", 8.68, True)],
    [("ataupun", 9.46, False), ("jumpa", 9.72, False)],
    [("lepak", 10.24, True), ("sama", 10.62, False)],
    [("kawan-kawan", 10.94, False)],
    [("Sangat", 11.72, False), ("sesuai", 11.98, True)],
    [("Kasut", 12.72, False), ("ni", 13.04, False)],
    [("waterproof", 13.32, True)],
    [("Hujan", 14.38, False)],
    [("dia", 14.88, False), ("tak", 15.06, False), ("basah", 15.20, True)],
    [("Design", 16.04, False), ("tapak", 16.32, True), ("dia", 16.68, False)],
    [("pun", 16.92, False), ("sangat", 17.26, False), ("cantik", 17.54, True)],
    [("Sangat", 17.94, False), ("bagus", 18.28, True)],
    [("Dia", 18.88, False), ("tak", 19.02, False), ("licin", 19.16, True)],
    [("anti-slip", 19.76, True)],
    [("Yang", 20.56, False), ("penting", 20.70, False)],
    [("harga", 21.32, False), ("murah", 21.84, True)],
    [("Berminat?", 22.26, False)],
    [("dapatkan", 22.72, False), ("di", 23.10, False)],
    [("beg", 23.20, True), ("kuning", 23.34, True)],
]
_ENDS = [g[0][1] for g in G[1:]] + [END]
CAPTIONS = [(round(min(e, g[-1][1] + 0.9), 2), g) for g, e in zip(G, _ENDS)]

HOOK = dict(end=6.42, y=100,  # 2 pilihan warna disebut pada 3.64 & 5.98
            kicker="kasut paling", title="selesa",
            options=[("Warna hitam", "01"), ("Warna biru", "02")], select_at=[3.64, 5.98])
SECTIONS = [  # (mula, tamat, "kelebihan", "1 / 3", subtajuk)
    (6.42, 12.62, "kelebihan", "1 / 3", "jalan & lepak"),
    (12.62, 15.9, "kelebihan", "2 / 3", "kalis air"),
    (15.9, 22.22, "kelebihan", "3 / 3", "tapak anti-slip"),
]
STICKERS = [  # (mula, tamat, teks, x, y, sudut)
    (7.74, 12.5, "jalan-jalan", 50, 250, 2.0),
    (8.68, 12.5, "santai", 80, 320, -1.5),
    (10.24, 12.5, "lepak", 110, 390, 1.5),
    (13.32, 15.8, "waterproof", 50, 250, 2.0),
    (15.20, 15.8, "hujan tak basah", 80, 320, -1.5),
    (17.54, 20.45, "tapak cantik", 50, 250, 2.0),
    (19.16, 20.45, "tak licin", 80, 320, -1.5),
    (19.76, 20.45, "anti-slip", 110, 390, 1.5),
    (21.32, 22.2, "harga murah", 50, 250, -2.0),
]
CIRCLES = []  # (mula, tamat, cx, cy, r, label, label_x, label_y)
CTA = dict(title="selesa", title_at=22.22, title_y=230, card_at=22.5, card_y=1180,
           card_label="Kasut Lelaki", name="Kasut Lelaki", tags="selesa · kalis air · anti-slip",
           button="Tekan beg kuning ↓", button_color=(255, 200, 40, 255), button_text_color=(22, 22, 26, 255))
