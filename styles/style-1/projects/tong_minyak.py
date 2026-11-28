# Tong minyak + corong (Drive 1eo7aKT664pedCJ3Zj8-2pQn0KADxkFE2) — salin fail ni, isi ikut video. Contoh lengkap: styles/style-1/projects/boxer.py. Bina: python3 -I styles/style-1/build.py <raw.mp4> <fail ini> <work_dir>
# ---------- potongan (build.py) – masa ikut video ASAL
REMOVE = [
    (7.15, 7.59),   # "okay"
    (8.92, 12.00),  # "dia siap ada" (tak habis, ulang)
    (16.15, 23.08), # okay + "dia ada lubang untuk udara" + okay + "yang spesial corong ni dekat tu" + okay (ulangan; simpan ayat lengkap 23.2)
    (14.20, 14.44), # "okay"
    (27.02, 27.28), # bunyi pendek selepas "keluar"
    (31.15, 31.39), # "okay"
    (35.30, 36.30), # jeda (bunyi pasang corong) selepas "corong ini"
    (40.08, 41.10), # "kita ha.." (mula tak jadi) – simpan "kita masukkan"
]
SRC_END = 52.4        # potong selepas ni (orang keluar frame / kamera jatuh)
TAIL = 1.2            # hujung tak dipotong senyap — masa baca CTA (1.2s supaya kad CTA sempat dibaca)
PUNCH_Y = 0.25        # punch-in fokus ke atas (muka)

# ---------- overlay (build.py) – masa ikut video SELEPAS dipotong
END = 36.96
CAPTION_Y = 740       # muka agak rendah – turun sikit dari dagu
CARD_Y = 1420
ZOOM = 0.04
SFX_WHOOSH = "drop"   # produk cecair (minyak) – titisan

W_ = lambda *ws: [(w, t, h) for w, t, h in ws]
CAPTIONS = [  # (group_end, [(perkataan, mula, highlight)])
    (1.68, W_(("Tong", 0.00, False), ("minyak", 0.30, True), ("ni", 1.34, False))),
    (3.10, W_(("saiz", 1.68, False), ("5 liter", 1.96, True))),
    (4.70, W_(("Ada yang", 3.22, False), ("10 liter", 3.72, True))),
    (6.55, W_(("ada yang", 4.84, False), ("20 liter", 5.52, True))),
    (7.90, W_(("Tengok", 6.60, False), ("kita buka", 6.86, False), ("dalam", 7.42, True))),
    (10.05, W_(("Dia ada", 8.46, False), ("corong", 8.88, True), ("lagi", 9.62, False))),
    (11.60, W_(("Spesial", 10.56, True), ("corong", 10.82, False), ("dia ni", 11.22, False))),
    (13.40, W_(("Ada lubang", 11.76, False), ("minyak", 12.68, True), ("masuk", 13.00, False))),
    (15.25, W_(("ada lubang", 13.48, False), ("udara", 14.46, True), ("keluar", 14.80, False))),
    (16.36, W_(("Jadinya", 15.64, False))),
    (17.20, W_(("kita tuang", 16.38, False), ("minyak", 16.72, True))),
    (18.45, W_(("lebih", 17.22, False), ("lancar", 17.74, True))),
    (19.42, W_(("Contoh", 18.54, False))),
    (20.12, W_(("nak tuang", 19.44, False), ("minyak", 19.76, True))),
    (21.72, W_(("daripada", 20.14, False), ("dalam tong", 20.62, False))),
    (22.86, W_(("Ini", 21.76, False))),
    (24.66, W_(("kita", 22.88, False), ("sambung", 23.12, True), ("ke bahagian tu", 23.76, False))),
    (25.70, W_(("Muncung", 24.92, True), ("ni", 25.54, False))),
    (26.80, W_(("kita", 25.70, False), ("masukkan", 26.18, True))),
    (28.00, W_(("ke dalam", 26.80, False), ("tangki motor", 27.14, True))),
    (29.46, W_(("ataupun", 28.00, False), ("tangki kereta", 28.42, True))),
    (30.94, W_(("Kita tuang", 29.46, False), ("saja", 29.94, False), ("macam tu", 30.18, False))),
    (32.10, W_(("Minyak", 30.94, False), ("tak tumpah", 31.32, True))),
    (32.96, W_(("tak membazir", 32.14, True))),
    (33.70, W_(("lebih selamat", 32.98, True))),
    (35.46, W_(("Berminat", 33.70, False), ("dengan", 34.22, False), ("minyak ni", 34.60, False))),
    (36.96, W_(("dapatkan", 35.46, False), ("di beg kuning", 35.92, True))),
]
HOOK = dict(end=6.55, y=100, kicker="tong minyak, tuang", title="lancar",
            options=[("5 liter", "01"), ("10 liter", "02"), ("20 liter", "03")], select_at=[1.96, 3.72, 5.52])
SECTIONS = [  # (mula, tamat, label, "n / 3", subtajuk)
    (6.60, 11.70, "kelebihan", "1 / 3", "siap ada corong"),
    (11.70, 18.45, "kelebihan", "2 / 3", "lubang udara, tuang lancar"),
    (18.54, 33.70, "kelebihan", "3 / 3", "tak tumpah, tak membazir"),
]
STICKERS = [  # (mula, tamat, teks, x, y, sudut)
    (8.88, 11.6, "siap ada corong", 50, 250, 2.0),
    (10.56, 11.6, "corong spesial ✓", 80, 320, -1.5),
    (12.68, 17.5, "lubang minyak masuk", 50, 250, 2.0),
    (14.46, 17.5, "lubang udara keluar", 80, 320, -1.5),
    (23.12, 25.6, "sambung corong", 50, 250, 2.0),
    (26.18, 30.8, "tangki motor", 50, 250, 2.0),
    (28.42, 30.8, "tangki kereta", 80, 320, -1.5),
    (31.32, 33.6, "tak tumpah ✓", 50, 260, 2.0),
    (32.14, 33.6, "tak membazir ✓", 80, 340, -1.5),
    (32.98, 33.6, "lebih selamat ✓", 110, 420, 1.5),
]
CIRCLES = []
BIG_WORDS = [(17.74, 18.45, "lancar", True)]
COVERS = [  # at = masa video ASAL
    dict(at=4.4, kicker="tong minyak,", title="lancar",
         stickers=["siap ada corong", "tak tumpah ✓"], pill="kelebihan 1-3 · Tong Minyak"),
    dict(at=45.5, kicker="minyak tak tumpah,", title="selamat",
         stickers=["lubang udara", "tuang lancar ✓"], pill="kelebihan 1-3 · Tong Minyak"),
]
CTA = dict(title="selamat", title_at=33.70, title_y=230, card_at=33.9, card_y=1180,
           card_label="Tong Minyak", name="Tong Minyak + Corong", tags="tuang lancar · tak tumpah · ada corong",
           button="Tekan beg kuning ↓", button_color=(255, 200, 40, 255), button_text_color=(22, 22, 26, 255))
