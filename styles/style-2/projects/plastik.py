# Plastik restore (Drive 1DFjxOwlEe6a_KsUo1izjeqLi9QkKxWbV)
REMOVE = [
    (0.00, 7.40),    # pembuka tak jelas ("sini, ni, ni...") + "aa"
    (19.95, 22.63),  # "ini plastik restore" kali kedua (ulangan) + "okey, aa"
    (31.08, 36.12),  # "aa, ini aku tunjuk sikit saja, okey sekarang untuk nak buat video, okey"
]
SRC_END = 39.95
TAIL = 0.7

END = 23.06
CAPTION_Y = 655

CAPTIONS = [
    (1.46, [("Tengok", 0.04, ""), ("dah", 0.46, ""), ("pudar", 0.70, "box"), ("dah,", 1.09, "")]),
    (2.88, [("aku", 1.46, ""), ("nak", 1.62, ""), ("suruh", 1.78, ""), ("nampak", 2.04, "")]),
    (3.95, [("baru", 2.35, ""), ("balik,", 2.56, ""), ("berkilat", 2.88, "serif"), ("balik,", 3.50, "")]),
    (5.08, [("aku", 3.95, ""), ("pakai", 4.34, ""), ("ini", 4.53, ""), ("saja.", 4.75, "")]),
    (7.34, [("Ini", 5.08, ""), ("plastik", 5.45, "box"), ("restore,", 6.31, "serif")]),
    (8.60, [("senang", 7.34, ""), ("saja", 7.76, ""), ("nak", 8.05, ""), ("buat.", 8.26, "")]),
    (9.76, [("Kita", 8.60, ""), ("gosok", 8.99, "box"), ("saja", 9.39, "")]),
    (10.89, [("pakai", 9.76, ""), ("span", 10.25, "serif")]),
    (11.68, [("yang", 10.89, ""), ("diberi", 11.05, ""), ("ni.", 11.30, "")]),
    (13.36, [("Bahagian", 11.68, ""), ("kereta", 12.30, "box"), ("ataupun", 12.64, "")]),
    (14.32, [("bahagian", 13.36, ""), ("dashboard", 13.80, "box")]),
    (15.72, [("sebelah", 14.32, ""), ("dalam", 14.74, ""), ("pun", 15.11, ""), ("boleh.", 15.22, "")]),
    (17.20, [("Selain", 15.72, ""), ("pada", 16.34, ""), ("kereta,", 16.63, "")]),
    (18.11, [("nak", 17.20, ""), ("buat", 17.45, ""), ("pada", 17.78, "")]),
    (19.56, [("motor", 18.11, "box"), ("ke", 18.53, ""), ("semua", 18.69, ""), ("boleh.", 19.15, "serif")]),
    (20.46, [("Berminat", 19.56, ""), ("dengan", 20.18, "")]),
    (21.43, [("plastik", 20.46, "box"), ("restore", 21.02, ""), ("ni", 21.30, "")]),
    (22.02, [("dapatkan", 21.43, ""), ("di", 21.90, "")]),
    (23.06, [("beg kuning", 22.02, "serif")]),
]
HOOK = dict(start=0.15, end=3.0, text="review **plastik restore**", x=350, y=860)
CARDS = [
    dict(kind="vs", start=0.40, end=5.08, kicker="PLASTIK KERETA", old="Pudar", new="Berkilat", new_at=2.88),
    dict(kind="check", start=5.08, end=11.68, kicker="01 · SENANG", title="Senang *nak buat*",
         items=[("Gosok saja", 9.39), ("Guna span yang diberi", 11.05)]),
    dict(kind="check", start=11.68, end=19.56, kicker="02 · SERBA BOLEH", title="Kereta & *motor*",
         items=[("Bahagian kereta", 12.30), ("Dashboard sebelah dalam", 14.32), ("Motor pun boleh", 18.11)]),
]
RAIL = dict(start=5.08, end=19.56, steps=[(5.08, "Senang"), (11.68, "Serba boleh")])
CTA = dict(start=19.56, button_at=21.43, button="Tekan *beg kuning*",
           items=["Pudar jadi berkilat balik", "Gosok guna span diberi", "Kereta, dashboard & motor"])
