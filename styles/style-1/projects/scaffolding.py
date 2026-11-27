# Scaffolding (Drive 1rXVfGA7Q95m9lIxuU5kqzt03BtVFN5dX) — salin fail ni, isi ikut video. Contoh lengkap: styles/style-1/projects/boxer.py. Bina: python3 -I styles/style-1/build.py <raw.mp4> <fail ini> <work_dir>
# ---------- potongan (build.py) – masa ikut video ASAL
REMOVE = [
    (13.62, 14.24),   # "okey"
    (16.74, 17.34),   # "okey"
    (24.40, 29.60),   # "okey. dia punya kaki dia, tunjuk bawah lah tu" (cakap dgn jurukamera)
    (31.00, 33.55),   # "dia ada lock" (cubaan pertama)
    (38.80, 39.98),   # "oke" sebelum "dia sangat stabil"
    (42.34, 46.58),   # "okay. berminat dengan scaffolding ni, apa-apa lah" (CTA cubaan pertama)
]
SRC_END = 50.4        # potong selepas ni (orang keluar frame / kamera jatuh)
TAIL = 1.2            # hujung tak dipotong senyap — masa baca CTA (1.2s supaya kad CTA sempat dibaca)
PUNCH_Y = 0.25        # punch-in fokus ke atas (muka)

# ---------- overlay (build.py) – masa ikut video SELEPAS dipotong
END = 32.79            # tempoh selepas potongan (build.py --plan)
CAPTION_Y = 680       # atas, paras dada (pilihan user); kena muka -> 700–760
CARD_Y = 1420       # kad hook rendah supaya produk tak tertutup
ZOOM = 0.04
# CAPTION_ACCENT = (255, 212, 59, 255)   # paksa warna; default auto: baju/latar biru → kuning
# BRIGHTEN = "auto"   # video gelap (YAVG < 105) dicerahkan auto; atau {"exposure": 0.4, "shadows": 0.25, "blacks": 0.08}; None = matikan
# SFX_WHOOSH = "drop"  # ganti whoosh dengan titisan air (produk air / dapur / mesin basuh)
# DENOISE = True      # buang bunyi latar, kekalkan suara utama sahaja

def _g(*ws):  # ("perkataan", mula, highlight) ...
    return list(ws)
CAPTIONS = [  # (group_end, [(perkataan, mula, highlight)])
    (1.44, _g(("Nak", 0.00, False), ("mengecat", 0.62, False), ("rumah", 1.02, False))),
    (2.22, _g(("kat", 1.44, False), ("tempat", 1.60, False), ("tinggi", 1.84, True))),
    (2.90, _g(("macam", 2.22, False), ("ni,", 2.52, False))),
    (3.80, _g(("lagi", 3.08, False), ("senang,", 3.18, True))),
    (5.20, _g(("lagi", 3.84, False), ("memudahkan.", 4.04, True))),
    (6.76, _g(("Aku", 5.48, False), ("menggunakan", 5.92, False))),
    (8.12, _g(("ni,", 6.76, False), ("scaffolding", 7.34, True))),
    (9.70, _g(("sebagai", 8.12, False), ("stand", 8.64, True), ("aku.", 9.20, False))),
    (11.10, _g(("Dia", 9.78, False), ("sangat", 10.04, False), ("stabil.", 10.38, True))),
    (12.90, _g(("Tengok,", 11.26, False), ("heavy", 11.96, True), ("duty.", 12.22, True))),
    (13.68, _g(("Barang", 13.04, False), ("ni,", 13.20, False), ("dia", 13.38, False))),
    (15.00, _g(("tak", 13.54, False), ("berkarat,", 13.68, True), ("anti-rust.", 14.16, True))),
    (16.32, _g(("Dan", 15.32, False), ("lagi", 15.58, False), ("satu,", 15.82, False))),
    (17.50, _g(("dia", 16.32, False), ("spesialnya,", 16.52, True))),
    (19.10, _g(("kita", 17.96, False), ("nak", 18.40, False), ("kemas,", 18.60, True))),
    (20.00, _g(("kita", 19.16, False), ("nak", 19.34, False), ("buka,", 19.48, True))),
    (20.98, _g(("dia", 20.04, False), ("senang", 20.20, True), ("saja.", 20.62, False))),
    (22.30, _g(("Dia", 21.04, False), ("punya", 21.34, False), ("kaki", 21.64, True))),
    (23.30, _g(("dia", 22.42, False), ("ada", 22.56, False), ("lock,", 22.78, True))),
    (24.90, _g(("ada", 23.36, False), ("lubang-lubang", 23.86, True), ("dia.", 24.52, False))),
    (25.92, _g(("Kita", 24.94, False), ("boleh", 25.36, False), ("adjust", 25.58, True))),
    (26.76, _g(("nak", 25.92, False), ("tinggi,", 26.16, True))),
    (27.38, _g(("nak", 26.76, False), ("rendah.", 26.88, True))),
    (28.60, _g(("Dia", 27.38, False), ("sangat", 27.54, False), ("stabil,", 27.88, True))),
    (29.44, _g(("sangat", 28.74, False), ("ringan.", 28.98, True))),
]
HOOK = dict(end=5.40, y=100,
            kicker="nak cat tempat tinggi,", title="senang",
            options=[("Lagi senang", "01"), ("Lagi memudahkan", "02")], select_at=[3.18, 4.04])
SECTIONS = [  # (mula, tamat, "kelebihan", "1 / 3", subtajuk)
    (5.40, 15.20, "kelebihan", "1 / 3", "stabil & heavy duty"),
    (15.20, 20.98, "kelebihan", "2 / 3", "senang kemas & buka"),
    (20.98, 27.38, "kelebihan", "3 / 3", "kaki boleh adjust"),
]
STICKERS = [  # (mula, tamat, teks, x, y, sudut)
    (7.40, 9.90, "jadi stand cat siling", 70, 300, 2.0),
    (11.30, 15.10, "sangat stabil ✓", 70, 300, 2.0),
    (12.00, 15.10, "heavy duty", 110, 370, -1.5),
    (13.70, 15.10, "tak berkarat", 150, 440, 1.5),
    (16.50, 20.90, "senang nak kemas", 70, 300, 2.0),
    (19.20, 20.90, "senang nak buka ✓", 110, 370, -1.5),
    (22.50, 27.30, "ada lock", 70, 300, 2.0),
    (23.90, 27.30, "lubang adjust", 110, 370, -1.5),
    (26.16, 27.30, "tinggi / rendah ✓", 150, 440, 1.5),
]
CIRCLES = []
COVERS = [  # cover photo (tools/cover.py) – at = masa video ASAL
    dict(at=44.0, kicker="nak cat tempat tinggi,", title="senang",
         stickers=["sangat stabil", "heavy duty ✓"], pill="kelebihan 1-3 · scaffolding"),
    dict(at=4.0, kicker="scaffolding untuk cat siling,", title="stabil",
         stickers=["tak berkarat", "boleh adjust tinggi ✓"], pill="kelebihan 1-3 · scaffolding"),
]
BIG_WORDS = [(10.04, 11.20, "stabil", True)]
CTA = dict(title="stabil", title_at=27.38, title_y=1580, card_at=29.44, card_y=1180,
           card_label="Scaffolding", name="Scaffolding", tags="stabil · ringan · adjustable",
           button="Tekan beg kuning ↓", button_color=(255, 200, 40, 255), button_text_color=(22, 22, 26, 255))
