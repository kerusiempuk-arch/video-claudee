# Umpan tikus (Drive 1a0YVguFMLG6xZl4nsFoIrHX_Lx1otPJq)
REMOVE = [
    (4.30, 4.78),    # "aa"
    (6.45, 7.80),    # "okay, aa"
    (8.80, 9.47),    # "okay"
    (12.60, 15.90),  # "okay, aa, jangan risau" pertama (diulang) + "tikus ber-" gagap
    (22.03, 23.45),  # "okay, aa, dia tak" – ayat tak habis
]
SRC_END = 29.05
TAIL = 0.7

# --- overlay, masa ikut video SELEPAS dipotong
END = 20.31
CAPTION_Y = 655

CAPTIONS = [
    (1.26, [("Bosan", 0.10, ""), ("dengan", 0.35, ""), ("tikus,", 0.77, "box")]),
    (2.80, [("asyik", 1.26, ""), ("mengganggu", 1.61, "serif"), ("sekitar", 2.31, "")]),
    (3.64, [("rumah", 2.80, ""), ("kita,", 3.20, "")]),
    (4.94, [("ini", 3.64, ""), ("penyelesaian", 3.83, "box"), ("dia,", 4.58, "")]),
    (5.68, [("umpan", 4.94, "serif"), ("tikus.", 5.29, "")]),
    (6.81, [("Tikus", 5.68, ""), ("dia", 5.99, ""), ("akan", 6.18, ""), ("makan", 6.43, "")]),
    (7.62, [("benda", 6.81, ""), ("ni,", 7.06, ""), ("akan", 7.38, "")]),
    (8.92, [("berpindah", 7.62, "box"), ("alam", 8.21, ""), ("lah", 8.42, ""), ("dia.", 8.61, "")]),
    (9.83, [("Jangan", 8.92, ""), ("risau", 9.46, "")]),
    (11.35, [("dengan", 9.83, ""), ("berbau", 10.50, ""), ("busuk,", 10.90, "serif")]),
    (12.36, [("tikus", 11.35, ""), ("dia", 11.94, ""), ("makan", 12.12, "")]),
    (12.88, [("benda", 12.36, ""), ("ni,", 12.62, "")]),
    (13.78, [("dia", 12.88, ""), ("akan", 13.00, ""), ("keluar", 13.16, ""), ("rumah,", 13.41, "box")]),
    (14.76, [("dia", 13.78, ""), ("akan", 13.97, ""), ("cari", 14.36, ""), ("air,", 14.52, "serif")]),
    (15.95, [("jadinya", 14.76, ""), ("dalam", 15.25, ""), ("rumah", 15.68, "")]),
    (16.93, [("kita", 15.95, ""), ("tak", 16.34, ""), ("akan", 16.44, ""), ("ada", 16.72, "")]),
    (17.68, [("bau", 16.93, ""), ("busuk.", 17.14, "box")]),
    (18.92, [("Berminat", 17.68, ""), ("dapatkan", 18.23, "")]),
    (20.31, [("di", 18.92, ""), ("beg kuning", 19.02, "serif")]),
]

HOOK = dict(start=0.15, end=3.0, text="review **umpan tikus**", x=350, y=860)

CARDS = [
    dict(kind="vs", start=3.00, end=5.68, kicker="MASALAH TIKUS", old="Tikus", new="Umpan", new_at=4.94),
    dict(kind="icon", start=5.68, end=8.92, kicker="01 · BERKESAN", title="Berpindah *alam*", icon="bolt"),
    dict(kind="check", start=8.92, end=17.68, kicker="02 · TAK BERBAU", title="Tiada *bau busuk*",
         items=[("Tikus keluar rumah", 13.16), ("Cari air di luar", 14.52), ("Rumah tak bau busuk", 17.14)]),
]
RAIL = dict(start=5.68, end=17.68, steps=[(5.68, "Berkesan"), (8.92, "Tak berbau")])
CTA = dict(start=17.68, button_at=18.23, button="Tekan *beg kuning*",
           items=["Umpan tikus", "Tikus makan – berpindah alam", "Tikus keluar cari air", "Rumah tak bau busuk"])
