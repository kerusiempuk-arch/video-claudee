# Ninjago Block Series (Drive 1XcPyNJ2C_CfS5qmBhMM5ElLbqvizbI-I)
# Bina: python3 -I styles/style-2/build.py work/v1/raw.mp4 styles/style-2/projects/ninjago.py work/v1/hf

# --- potongan (build.py), masa ikut video ASAL
REMOVE = [
    (4.78, 6.18),    # "aa, okay, aa" sebelum "menggunakan"
    (8.97, 9.37),    # "aa" sebelum "sebelum ni"
    (17.56, 19.07),  # "aa" sebelum "dia dapat memupuk"
    (27.14, 32.27),  # arahan kepada perakam ("depan belakang... biar nampak muka") + kamera beralih
]
SRC_END = 37.5
TAIL = 0.7

# --- overlay (build.py), masa ikut video SELEPAS dipotong (transkripsi cut.wav)
END = 27.68
CAPTION_Y = 1290  # tiada muka di awal – produk di atas, jadi kapsyen di bawah produk; elak butang CTA (760–1260)
CARD_TOP = 1450   # kad turun sikit supaya tak bertindih kapsyen

CAPTIONS = [
    (2.09, [("Tengok", 0.19, ""), ("anak", 1.09, ""), ("aku", 1.33, ""), ("buat", 1.66, "")]),
    (3.32, [("rumah", 2.09, "box"), ("ke", 2.63, ""), ("kapal,", 2.67, "serif")]),
    (4.01, [("entah", 3.32, ""), ("aku", 3.63, ""), ("pun", 3.86, "")]),
    (4.60, [("tak", 4.01, ""), ("pasti.", 4.20, "")]),
    (6.32, [("menggunakan", 4.60, ""), ("Ninjago", 5.76, "serif")]),
    (7.66, [("Block Series", 6.32, "box"), ("ni,", 7.20, "")]),
    (8.42, [("sebelum", 7.66, ""), ("ni", 7.84, ""), ("dia", 7.99, ""), ("dah", 8.16, "")]),
    (9.13, [("buat", 8.42, ""), ("rumah,", 8.72, "box")]),
    (10.19, [("dah", 9.13, ""), ("buat", 9.33, ""), ("kapal,", 9.69, "box")]),
    (10.95, [("dah", 10.19, ""), ("buat", 10.28, ""), ("robot.", 10.54, "box")]),
    (12.26, [("Dengan", 10.95, ""), ("menggunakan", 11.60, "")]),
    (13.58, [("Ninjago", 12.26, "serif"), ("Block Series", 12.68, ""), ("ni,", 13.46, "")]),
    (14.80, [("macam-macam", 13.58, "box"), ("boleh", 14.23, ""), ("buat.", 14.61, "")]),
    (15.92, [("Dia", 14.80, ""), ("dapat", 15.05, ""), ("memupuk", 15.25, ""), ("minat", 15.81, "serif")]),
    (17.14, [("anak-anak", 15.92, ""), ("untuk", 16.46, ""), ("berfikir", 16.69, "")]),
    (18.00, [("lebih", 17.14, ""), ("kreatif,", 17.42, "box")]),
    (18.90, [("lebih", 18.00, ""), ("fokus.", 18.32, "serif")]),
    (20.16, [("Berbanding", 18.90, ""), ("asyik", 19.80, ""), ("dia", 19.98, "")]),
    (21.12, [("bagi", 20.16, ""), ("telefon", 20.50, "box"), ("tu,", 20.93, "")]),
    (22.27, [("baik", 21.12, ""), ("bagi", 21.46, ""), ("mainan", 21.94, "serif")]),
    (22.84, [("macam", 22.27, ""), ("ni.", 22.61, "")]),
    (24.06, [("Berminat", 22.84, ""), ("dengan", 23.28, ""), ("mainan", 23.93, "")]),
    (25.47, [("Ninjago", 24.06, "serif"), ("Block Series", 24.50, ""), ("ni,", 25.21, "")]),
    (26.11, [("dapatkan", 25.47, ""), ("di", 25.98, "")]),
    (27.68, [("beg kuning", 26.11, "serif")]),
]

HOOK = dict(start=0.15, end=4.55, text="anak buat **rumah ke kapal?**", x=350, y=690)

CARDS = [
    dict(kind="icon", start=4.6, end=7.66, kicker="NINJAGO BLOCK SERIES", title="Mainan *blok binaan*", icon="star"),
    dict(kind="check", start=7.66, end=14.8, kicker="01 · BOLEH BUAT", title="Macam-macam *boleh buat*",
         items=[("Rumah", 8.72), ("Kapal", 9.69), ("Robot", 10.54)]),
    dict(kind="check", start=14.8, end=18.9, kicker="02 · MINDA ANAK", title="Pupuk *minat* anak",
         items=[("Lebih kreatif", 17.42), ("Lebih fokus", 18.32)]),
    dict(kind="vs", start=18.9, end=22.84, kicker="BERBANDING", old="Telefon", new="Mainan", new_at=21.94),
]
RAIL = dict(start=7.66, end=22.84, steps=[(7.66, "Bina"), (14.8, "Kreatif"), (18.9, "vs Telefon")])
CTA = dict(start=22.84, button_at=25.47, button="Tekan *beg kuning*",
           items=["Bina rumah, kapal, robot", "Pupuk kreativiti anak", "Lebih fokus", "Ganti masa telefon"])
