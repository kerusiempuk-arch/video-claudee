# Lampu / mentol LED UFO (Drive 1jBlWz_v0LNl3TN71ZZWLojeIATx7R6aQ)
REMOVE = [
    (0.00, 1.00),    # "Ba–" permulaan tersangkut
    (4.40, 9.03),    # "okey, aa, dia eye protection" pertama + perkataan tak jelas – diulang
    (10.40, 11.22),  # "okey, haa"
    (13.03, 14.31),  # "okey, aa"
]
SRC_END = 29.75
TAIL = 0.7

# --- overlay, masa ikut video SELEPAS dipotong
END = 19.26
CAPTION_Y = 655

CAPTIONS = [
    (1.14, [("Lampu", 0.08, ""), ("UFO", 0.70, "box")]),
    (3.12, [("ataupun", 1.14, ""), ("mentol", 1.92, ""), ("UFO,", 2.69, "serif")]),
    (4.50, [("dia", 3.12, ""), ("eye", 3.72, "box"), ("protection.", 3.85, "box")]),
    (5.97, [("Bahagian", 4.50, ""), ("penyambungnya", 5.00, "serif")]),
    (6.44, [("macam", 5.97, ""), ("ni,", 6.23, "")]),
    (7.85, [("sangat", 6.44, ""), ("terang", 6.76, "box"), ("lampu", 6.94, ""), ("ni,", 7.52, "")]),
    (8.49, [("gantung.", 7.85, "serif")]),
    (9.94, [("Pasang", 8.49, ""), ("pada", 8.93, ""), ("depan", 9.15, ""), ("rumah,", 9.48, "box")]),
    (11.37, [("belakang", 9.94, ""), ("rumah", 10.31, "box"), ("ataupun", 10.73, "")]),
    (12.63, [("kat", 11.37, ""), ("dalam", 11.51, ""), ("bilik", 11.83, "box"), ("ataupun", 12.24, "")]),
    (13.25, [("bilik", 12.63, ""), ("air,", 12.96, "box")]),
    (14.21, [("sangat", 13.25, ""), ("sesuai.", 13.77, "serif")]),
    (15.13, [("Berminat", 14.21, ""), ("dengan", 14.70, "")]),
    (16.76, [("mentol", 15.13, ""), ("LED", 15.72, "box"), ("UFO", 16.39, ""), ("ni,", 16.48, "")]),
    (17.30, [("dapatkan", 16.76, "")]),
    (19.26, [("di", 17.30, ""), ("beg kuning", 17.45, "serif"), ("ni.", 18.00, "")]),   # "dibuat pun" – SAHKAN beg kuning
]

HOOK = dict(start=0.15, end=3.0, text="review **lampu UFO**", x=350, y=860)

CARDS = [
    dict(kind="icon", start=3.12, end=4.50, kicker="01 · MATA", title="Eye *protection*", icon="shield"),
    dict(kind="icon", start=4.50, end=6.44, kicker="02 · PENYAMBUNG", title="Bahagian *penyambung*", icon="bolt"),
    dict(kind="check", start=6.44, end=8.49, kicker="03 · TERANG", title="Sangat *terang*",
         items=[("Sangat terang", 6.76), ("Boleh gantung", 7.85)]),
    dict(kind="check", start=8.49, end=14.21, kicker="04 · SESUAI", title="Pasang *di mana-mana*",
         items=[("Depan rumah", 9.48), ("Belakang rumah", 10.31), ("Dalam bilik", 11.83), ("Bilik air", 12.96)]),
]
RAIL = dict(start=3.12, end=14.21, steps=[(3.12, "Mata"), (4.50, "Penyambung"), (6.44, "Terang"), (8.49, "Sesuai")])
CTA = dict(start=14.21, button_at=16.76, button="Tekan *beg kuning*",
           items=["Eye protection", "Terang & boleh gantung", "Rumah, bilik & bilik air"])
