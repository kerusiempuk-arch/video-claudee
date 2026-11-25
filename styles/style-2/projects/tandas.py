# Tandas mudah alih / portable toilet (Drive 1bFiGdxGBkvI3jPsNznwPAgnXqVlu28HP)
# --- potongan (build.py), masa ikut video ASAL
REMOVE = [
    (1.42, 1.98),    # "okey"
    (11.78, 12.26),  # "okey"
    (12.68, 13.62),  # "okey"
    (20.46, 21.22),  # "okey"
    (22.66, 23.18),  # "okey"
    (23.18, 24.29),  # "dalam ni" pertama – diulang
    (27.29, 28.38),  # "okey, aa"
    (30.84, 31.48),  # "tak nak guna boleh" kedua – ulangan
    (36.30, 39.22),  # "Kalau tak nak guna, aa, ini kita terus" – mula semula
    (44.10, 44.64),  # "okey"
]
SRC_END = 49.3
TAIL = 1.4

# --- overlay, masa ikut video SELEPAS dipotong
END = 36.26
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
    (9.32, [("isteri", 8.30, ""), ("mengandung,", 8.54, "serif")]),
    (10.60, [("isteri", 9.32, ""), ("baru", 9.62, ""), ("lepas", 9.86, ""), ("bersalin", 10.21, "box")]),
    (11.27, [("Kita", 10.60, ""), ("tengok,", 10.87, "")]),
    (11.67, [("dia", 11.27, ""), ("ada", 11.47, "")]),
    (12.93, [("tempat", 11.67, ""), ("letak", 12.07, ""), ("tangan,", 12.40, "box")]),
    (13.86, [("tempat", 12.93, ""), ("sandar,", 13.55, "box")]),
    (14.65, [("tempat", 13.86, ""), ("tisu,", 14.26, "box")]),
    (16.08, [("bawah", 14.65, ""), ("dia", 14.98, ""), ("anti-slip", 15.18, "serif")]),
    (17.60, [("jadinya", 16.08, ""), ("dia", 16.47, ""), ("tak", 16.70, ""), ("menggelongsor", 16.84, "box")]),
    (19.34, [("Kita", 17.60, ""), ("tengok", 17.95, ""), ("kat", 18.47, ""), ("dalam,", 18.73, "")]),
    (19.95, [("dalam", 19.34, ""), ("ni,", 19.78, "")]),
    (21.24, [("dia", 19.95, ""), ("ada", 20.21, ""), ("baldi", 20.55, "box"), ("dia,", 20.81, "")]),
    (22.62, [("boleh", 21.24, ""), ("buka", 21.68, ""), ("nak", 22.02, ""), ("guna.", 22.27, "")]),
    (23.84, [("Tak", 22.62, ""), ("nak", 22.85, ""), ("guna", 23.06, ""), ("boleh.", 23.36, "")]),
    (25.38, [("Sebelum", 23.84, ""), ("guna,", 24.19, ""), ("pastikan", 24.72, "")]),
    (26.40, [("sarung", 25.38, ""), ("plastik", 25.90, "box"), ("dulu", 26.10, "")]),
    (27.61, [("supaya", 26.40, ""), ("senang", 26.92, ""), ("nak", 27.16, ""), ("cuci", 27.35, "box")]),
    (28.44, [("kotoran.", 27.61, "serif")]),
    (29.35, [("Kalau", 28.44, ""), ("tak", 28.62, ""), ("nak", 28.78, ""), ("guna,", 28.94, "")]),
    (30.14, [("ini", 29.35, ""), ("kita", 29.41, ""), ("terus", 29.62, ""), ("letak", 29.88, "")]),
    (31.31, [("kat", 30.14, ""), ("atas", 30.24, ""), ("lubang", 30.44, ""), ("jamban", 30.76, "box")]),
    (31.86, [("rumah", 31.31, ""), ("kita.", 31.49, "")]),
    (32.40, [("Berminat", 31.86, ""), ("dengan", 32.07, "")]),
    (33.50, [("portable toilet", 32.40, "serif"), ("ni,", 33.30, "")]),
    (34.13, [("dapatkan", 33.50, ""), ("di", 33.91, "")]),
    (36.26, [("beg kuning", 34.13, "serif")]),
]

HOOK = dict(start=0.15, end=2.9, text="review **portable toilet**", x=350, y=800)

CARDS = [
    dict(kind="check", start=2.95, end=10.6, kicker="01 · SESUAI UNTUK", title="Sesuai untuk *semua*",
         items=[("Orang uzur & warga emas", 5.77), ("Sakit lutut", 7.45), ("Isteri mengandung", 8.54),
                ("Baru lepas bersalin", 10.21)]),
    dict(kind="check", start=10.6, end=15.1, kicker="02 · CIRI-CIRI", title="Lengkap & *selesa*",
         items=[("Tempat letak tangan", 12.40), ("Tempat sandar", 13.55), ("Tempat tisu", 14.26)]),
    dict(kind="icon", start=15.1, end=17.6, kicker="03 · ANTI-SLIP", title="Tak *menggelongsor*", icon="shield"),
    dict(kind="icon", start=17.6, end=23.84, kicker="04 · DI DALAM", title="Ada *baldi*\nboleh buka", icon="star"),
    dict(kind="check", start=23.84, end=28.44, kicker="05 · TIPS", title="Sarung *plastik* dulu",
         items=[("Senang cuci kotoran", 27.35)]),
    dict(kind="icon", start=28.44, end=31.86, kicker="06 · 2 DALAM 1", title="Letak atas *jamban*", icon="bolt"),
]
RAIL = dict(start=2.95, end=31.86, steps=[(2.95, "Sesuai"), (10.6, "Ciri"), (15.1, "Anti-slip"),
                                          (17.6, "Baldi"), (23.84, "Tips"), (28.44, "Jamban")])
CTA = dict(start=31.86, button_at=33.5, button="Tekan *beg kuning*",
           items=["Mudah bawa ke mana-mana", "Tempat tangan, sandar & tisu", "Tapak anti-slip", "Boleh letak atas jamban"])
