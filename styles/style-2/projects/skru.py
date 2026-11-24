# Skru aluminium (Drive 1qgmb6cAJejet7ayWudYiOU9KEnz_jtW8) — tangan sahaja, tiada muka
# --- potongan (build.py), masa ikut video ASAL
REMOVE = [
    (9.38, 10.27),   # "okay, aa"
    (12.43, 13.26),  # "aa"
    (16.53, 16.81),  # "aa"
    (18.68, 19.45),  # "okay"
]
SRC_END = 26.06
TAIL = 0.7

# --- overlay (build.py), masa ikut video SELEPAS dipotong
END = 21.98
CAPTION_Y = 570   # tiada muka – bawah jalur rail (318–504), atas skru di tapak tangan
CAPTIONS = [
    (1.56, [("Skru", 0.00, ""), ("aluminium", 0.32, "serif")]),
    (2.77, [("Yang", 1.56, ""), ("aku", 1.79, ""), ("pilih", 2.03, ""), ("ni", 2.41, "")]),
    (3.74, [("warna", 2.77, ""), ("oren", 3.17, "box")]),
    (4.23, [("ada", 3.74, ""), ("lagi", 3.95, "")]),
    (5.22, [("warna", 4.23, ""), ("lain-lain,", 4.58, "")]),
    (5.92, [("warna", 5.22, ""), ("biru,", 5.49, "box")]),
    (7.34, [("warna", 5.92, ""), ("merah", 6.33, "box"), ("ada,", 6.76, "")]),
    (8.20, [("ikut", 7.34, ""), ("kita", 7.64, ""), ("rasa", 7.91, "")]),
    (9.19, [("masing-masing.", 8.20, "")]),
    (10.82, [("Skru", 9.19, ""), ("ni", 9.53, ""), ("sangat", 9.69, ""), ("ringan,", 10.18, "box")]),
    (11.33, [("tak", 10.82, ""), ("berkarat", 11.06, "serif")]),
    (12.48, [("pasang", 11.33, ""), ("pada", 11.75, ""), ("motor", 12.08, "box")]),
    (14.20, [("ataupun", 12.48, ""), ("mana-mana", 12.79, ""), ("tempat,", 13.53, "")]),
    (15.10, [("ia", 14.20, ""), ("sesuai,", 14.37, "serif")]),
    (16.02, [("sangat", 15.10, ""), ("cantik.", 15.52, "box")]),
    (16.92, [("Satu", 16.02, ""), ("set", 16.32, ""), ("ni,", 16.60, "")]),
    (18.02, [("30", 16.92, "box"), ("pieces,", 17.36, "")]),
    (19.30, [("agak", 18.02, ""), ("sangat-sangat", 18.24, "")]),
    (20.00, [("murah.", 19.30, "serif")]),
    (21.28, [("Berminat?", 20.00, ""), ("Dapatkan", 20.59, ""), ("di", 21.10, "")]),
    (21.98, [("beg kuning", 21.28, "serif")]),
]

HOOK = dict(start=0.15, end=2.7, text="review **skru aluminium**", x=290, y=250)

CARDS = [
    dict(kind="chips", start=2.77, end=9.15, kicker="01 · WARNA", title="Pelbagai *warna*",
         chips=["Oren", "Biru", "Merah"], chips_at=3.17,
         colors=["#F28C28", "#2F6BFF", "#E0342B"], colors_at=6.33),
    dict(kind="check", start=9.15, end=11.30, kicker="02 · KUALITI", title="Sangat *ringan*",
         items=[("Sangat ringan", 10.18), ("Tak berkarat", 11.06)]),
    dict(kind="check", start=11.30, end=15.98, kicker="03 · SESUAI", title="Sesuai *di mana-mana*",
         items=[("Pasang pada motor", 12.08), ("Mana-mana tempat", 12.79), ("Sangat cantik", 15.52)]),
    dict(kind="icon", start=15.98, end=19.30, kicker="04 · HARGA", title="30 pcs satu set\n*sangat murah*", icon="tag"),
]
RAIL = dict(start=2.77, end=19.30, steps=[(2.77, "Warna"), (9.15, "Ringan"), (11.30, "Sesuai"), (15.98, "Murah")])
CTA = dict(start=19.30, button_at=19.75, button="Tekan *beg kuning*",
           items=["Pelbagai warna", "Ringan & tak berkarat", "Sesuai untuk motor", "30 pcs satu set, murah"])
