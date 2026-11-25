# Tandas mudah alih / portable toilet (Drive 1bFiGdxGBkvI3jPsNznwPAgnXqVlu28HP)
# --- potongan (build.py), masa ikut video ASAL
REMOVE = [
    (1.42, 1.98),    # "okey"
    (11.78, 12.26),  # "okey"
    (12.68, 13.62),  # "okey"
    (20.46, 21.22),  # "okey"
    (22.30, 23.18),  # "okey"
    (23.18, 24.29),  # "dalam ni" pertama – diulang
    (27.10, 28.38),  # "okey, haa"
    (36.30, 39.22),  # "Kalau tak nak guna, aa, ini kita terus" – mula semula
    (44.10, 44.64),  # "okey"
]
SRC_END = 49.3
TAIL = 1.4

# --- overlay, masa ikut video SELEPAS dipotong
END = 36.55
CAPTION_Y = 660   # muka agak rendah dalam video ni
CARD_TOP = 1400   # produk besar di tengah-bawah; kad rendah sedikit

CAPTIONS = [
    (1.05, [("Portable toilet", 0.08, "serif")]),
    (1.93, [("boleh", 1.05, ""), ("nak", 1.42, ""), ("bawa", 1.64, "")]),
    (2.95, [("ke", 1.93, ""), ("mana-mana", 2.08, "box")]),
    (5.07, [("sesuai", 2.95, ""), ("untuk", 3.50, ""), ("orang", 3.82, ""), ("keuzuran", 4.20, "box")]),
    (6.24, [("orang", 5.07, ""), ("tua,", 5.77, "")]),
    (6.92, [("orang", 6.24, ""), ("sakit,", 6.49, "")]),
    (8.30, [("orang", 6.92, ""), ("sakit", 7.10, ""), ("lutut,", 7.45, "box")]),
    (9.32, [("isteri", 8.30, ""), ("mengandung,", 8.61, "serif")]),
    (10.52, [("isteri", 9.32, ""), ("baru", 9.56, ""), ("lepas", 9.76, ""), ("bersalin", 10.01, "box")]),
    (11.32, [("Kita", 10.52, ""), ("tengok,", 10.79, "")]),
    (11.72, [("dia", 11.32, ""), ("ada", 11.51, "")]),
    (12.98, [("tempat", 11.72, ""), ("letak", 12.12, ""), ("tangan,", 12.45, "box")]),
    (14.02, [("tempat", 12.98, ""), ("sandar,", 13.47, "box")]),
    (14.71, [("tempat", 14.02, ""), ("tisu,", 14.31, "box")]),
    (16.23, [("bawah", 14.71, ""), ("dia,", 15.04, ""), ("anti-slip", 15.46, "serif")]),
    (17.60, [("jadinya", 16.23, ""), ("dia", 16.68, ""), ("tak", 16.76, ""), ("menggelongsor", 16.83, "box")]),
    (19.20, [("Kita", 17.60, ""), ("tengok", 17.92, ""), ("kat", 18.40, ""), ("dalam,", 18.64, "")]),
    (19.76, [("dalam", 19.20, ""), ("ni,", 19.65, "")]),
    (21.10, [("dia", 19.76, ""), ("ada", 20.00, ""), ("baldi", 20.24, "box"), ("dia,", 20.56, "")]),
    (22.24, [("boleh", 21.10, ""), ("buka,", 21.36, ""), ("nak", 21.68, ""), ("guna", 21.92, "")]),
    (22.86, [("boleh,", 22.24, "")]),
    (24.12, [("tak", 22.86, ""), ("nak", 23.04, ""), ("guna", 23.36, ""), ("boleh.", 23.84, "")]),
    (25.38, [("Sebelum", 24.12, ""), ("guna,", 24.64, ""), ("pastikan", 24.84, "")]),
    (26.52, [("sarung", 25.38, ""), ("plastik", 25.78, "box"), ("dulu", 26.25, "")]),
    (27.78, [("supaya", 26.52, ""), ("senang", 27.07, ""), ("nak", 27.32, ""), ("cuci", 27.61, "box")]),
    (28.68, [("kotoran.", 27.78, "serif")]),
    (29.62, [("Kalau", 28.68, ""), ("tak", 28.90, ""), ("nak", 29.12, ""), ("guna,", 29.26, "")]),
    (30.65, [("ini", 29.62, ""), ("kita", 29.80, ""), ("terus", 30.04, ""), ("letak", 30.34, "")]),
    (31.78, [("kat", 30.65, ""), ("atas", 30.76, ""), ("lubang", 31.00, ""), ("jamban", 31.42, "box")]),
    (32.36, [("rumah", 31.78, ""), ("kita.", 32.10, "")]),
    (32.97, [("Berminat", 32.36, ""), ("dengan", 32.68, "")]),
    (33.95, [("portable toilet", 32.97, "serif"), ("ni,", 33.86, "")]),
    (34.42, [("dapatkan", 33.95, ""), ("di", 34.33, "")]),
    (36.55, [("beg kuning", 34.42, "serif")]),
]

HOOK = dict(start=0.15, end=2.9, text="review **portable toilet**", x=350, y=800)

CARDS = [
    dict(kind="check", start=2.95, end=10.52, kicker="01 · SESUAI UNTUK", title="Sesuai untuk *semua*",
         items=[("Orang uzur & warga emas", 5.77), ("Sakit lutut", 7.45), ("Isteri mengandung", 8.61),
                ("Baru lepas bersalin", 10.01)]),
    dict(kind="check", start=10.52, end=15.3, kicker="02 · CIRI-CIRI", title="Lengkap & *selesa*",
         items=[("Tempat letak tangan", 12.45), ("Tempat sandar", 13.47), ("Tempat tisu", 14.31)]),
    dict(kind="icon", start=15.3, end=17.6, kicker="03 · ANTI-SLIP", title="Tak *menggelongsor*", icon="shield"),
    dict(kind="icon", start=17.6, end=24.12, kicker="04 · DI DALAM", title="Ada *baldi*\nboleh buka", icon="star"),
    dict(kind="check", start=24.12, end=28.68, kicker="05 · TIPS", title="Sarung *plastik* dulu",
         items=[("Senang cuci kotoran", 27.61)]),
    dict(kind="icon", start=28.68, end=32.36, kicker="06 · 2 DALAM 1", title="Letak atas *jamban*", icon="bolt"),
]
RAIL = dict(start=2.95, end=32.36, steps=[(2.95, "Sesuai"), (10.52, "Ciri"), (15.3, "Anti-slip"),
                                          (17.6, "Baldi"), (24.12, "Tips"), (28.68, "Jamban")])
CTA = dict(start=32.36, button_at=33.95, button="Tekan *beg kuning*",
           items=["Mudah bawa ke mana-mana", "Tempat tangan, sandar & tisu", "Tapak anti-slip", "Boleh letak atas jamban"])
