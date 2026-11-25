# Bekas makanan stainless steel (Drive 11-lh2hqX1QBGoJCqq5fx3lgNou82FwwO) — salin fail ni, isi ikut video. Contoh lengkap: styles/style-1/projects/boxer.py. Bina: python3 -I styles/style-1/build.py <raw.mp4> <fail ini> <work_dir>
# ---------- potongan (build.py) – masa ikut video ASAL
REMOVE = [
    (0.0, 0.88),    # "Nah,"
    (9.53, 10.02),  # "okay"
    (29.35, 36.88), # 2x "berminat dengan bekas makanan stainless steel ni" + "dapatkan" (simpan take akhir)
]
SRC_END = 41.45        # potong selepas ni (orang keluar frame / kamera jatuh)
TAIL = 1.2            # hujung tak dipotong senyap — masa baca CTA (1.2s supaya kad CTA sempat dibaca)
PUNCH_Y = 0.25        # punch-in fokus ke atas (muka)

# ---------- overlay (build.py) – masa ikut video SELEPAS dipotong
END = 29.80            # tempoh selepas potongan (build.py --plan)
CAPTION_Y = 680       # atas, paras dada (pilihan user); kena muka -> 700–760
CARD_Y = 1180
ZOOM = 0.04
CAPTION_ACCENT = (255, 212, 59, 255)   # kuning: baju biru
# BRIGHTEN = "auto"   # video gelap (YAVG < 105) dicerahkan auto; atau {"exposure": 0.4, "shadows": 0.25, "blacks": 0.08}; None = matikan
# DENOISE = True      # buang bunyi latar, kekalkan suara utama sahaja

CAPTIONS = [  # (group_end, [(perkataan, mula, highlight)])
    (1.18, [("Tengok", 0.00, False), ("depan", 0.40, False), ("aku", 0.72, False)]),
    (1.90, [("sangat", 1.20, False), ("banyak", 1.52, True)]),
    (3.20, [("bekas", 1.92, False), ("makanan", 2.50, False)]),
    (4.10, [("stainless", 3.22, True), ("steel", 3.80, True)]),
    (4.70, [("Untuk", 4.12, False), ("nak", 4.20, False), ("simpan", 4.42, False)]),
    (5.42, [("makanan", 4.70, False), ("dalam", 5.16, False)]),
    (6.08, [("peti", 5.44, True), ("sejuk", 5.66, True)]),
    (6.98, [("ataupun", 6.10, False), ("untuk", 6.68, False)]),
    (8.30, [("hidangan", 7.00, True), ("boleh", 7.70, False)]),
    (8.88, [("Nak", 8.36, False), ("simpan", 8.54, False)]),
    (10.28, [("sayur", 8.90, True), ("ke", 9.34, False), ("apa", 9.50, False), ("semua", 9.62, False)]),
    (11.18, [("Nak", 10.32, False), ("buat", 10.56, False)]),
    (11.92, [("hidangan", 11.20, True)]),
    (13.16, [("bekas", 11.94, False), ("lauk", 12.38, True), ("ke", 12.74, False)]),
    (13.98, [("semua", 13.18, False), ("boleh", 13.40, False)]),
    (14.88, [("Penutup", 14.00, False), ("dia", 14.48, False), ("pun", 14.72, False)]),
    (15.60, [("kuat", 14.90, True)]),
    (16.64, [("Dia", 15.62, False), ("stainless", 15.92, False), ("steel", 16.40, False)]),
    (17.44, [("tak", 16.66, True), ("berkarat", 16.80, True)]),
    (18.56, [("Jadinya", 17.46, False), ("makanan", 17.90, False)]),
    (19.38, [("lebih", 18.58, False), ("bersih", 18.90, True)]),
    (20.70, [("lebih", 19.40, False), ("selamat", 19.72, True)]),
    (21.82, [("Dengan", 20.82, False), ("harga", 21.42, False)]),
    (22.92, [("yang", 21.84, False), ("sangat", 22.18, False), ("murah", 22.56, True)]),
    (23.62, [("macam", 22.94, False), ("ni", 23.22, False)]),
    (24.54, [("sangat", 23.64, False), ("berbaloi", 23.88, True)]),
    (25.54, [("memiliki", 24.56, False), ("benda", 25.14, False), ("ni", 25.38, False)]),
    (26.78, [("Berminat", 25.56, False), ("dengan", 26.38, False)]),
    (27.70, [("bekas", 26.80, False), ("makanan", 27.24, False)]),
    (28.80, [("stainless", 27.72, False), ("steel", 28.18, False), ("ni", 28.64, False)]),
    (29.28, [("dapatkan", 28.82, False), ("di", 29.16, False)]),
    (29.80, [("beg", 29.28, True), ("kuning", 29.42, True)]),
]
HOOK = dict(end=8.1, y=100,
            kicker="bekas makanan paling", title="serba guna",
            options=[("Simpan dalam peti sejuk", "01"), ("Untuk hidangan", "02")], select_at=[5.44, 7.0])
SECTIONS = [  # (mula, tamat, "kelebihan", "1 / 3", subtajuk)
    (8.1, 13.98, "kelebihan", "1 / 3", "simpan apa saja"),
    (13.98, 17.44, "kelebihan", "2 / 3", "kuat & tak berkarat"),
    (17.44, 25.56, "kelebihan", "3 / 3", "bersih & berbaloi"),
]
STICKERS = [  # (mula, tamat, teks, x, y, sudut)
    (8.9, 13.9, "sayur", 70, 300, 2.0),
    (11.2, 13.9, "lauk & hidangan", 110, 370, -1.5),
    (14.0, 17.4, "penutup kuat", 70, 300, 2.0),
    (16.7, 17.4, "tak berkarat", 110, 370, -1.5),
    (18.9, 20.7, "lebih bersih", 70, 300, 2.0),
    (19.7, 20.7, "lebih selamat", 110, 370, -1.5),
    (22.5, 25.5, "harga murah", 70, 300, 2.0),
    (23.9, 25.5, "sangat berbaloi", 110, 370, -1.5),
]
CIRCLES = []
CTA = dict(title="serba guna", title_at=25.56, title_y=230, card_at=26.0, card_y=1180,
           card_label="Bekas Makanan", name="Bekas Makanan Stainless Steel", tags="stainless steel · tak berkarat · serba guna",
           button="Tekan bakul kuning ↓", button_color=(255, 200, 40, 255), button_text_color=(22, 22, 26, 255))
