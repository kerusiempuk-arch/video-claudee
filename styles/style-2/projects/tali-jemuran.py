# Tali jemuran windproof (Drive 1C3Gw_d04iKBURoxG8sE_sS-w3LF8hLm0)
# --- potongan (build.py), masa ikut video ASAL
REMOVE = [
    (9.44, 10.10),   # "okay, aa" sebelum "hanger"
    (13.80, 14.06),  # "aa" sebelum "dia melendut"
    (21.30, 21.46),  # "aa" sebelum "jarak"
    (23.38, 30.52),  # "okay" + "bahan dia sangat berkualiti..." pertama (diulang) + cakap sampingan
]
SRC_END = 37.30
TAIL = 1.0

END = 27.34
CAPTION_Y = 1255  # bawah butang CTA (CTA tamat ~1250), atas kad (1390); orang jauh – muka ~y 800-1000
# CARD_TOP = 1360

CAPTIONS = [
    (1.31, [("Tali", 0.20, ""), ("jemuran", 0.37, "serif")]),
    (3.05, [("ini", 1.31, ""), ("tali", 1.59, ""), ("yang", 1.96, ""), ("biasa,", 2.34, "")]),
    (4.39, [("ini", 3.05, ""), ("dia", 3.40, ""), ("ada", 3.57, ""), ("lubang", 3.83, "box")]),
    (5.00, [("windproof", 4.39, "serif")]),
    (5.97, [("Tali", 5.00, ""), ("ini", 5.26, ""), ("walaupun", 5.46, "")]),
    (7.15, [("dia", 5.97, ""), ("melendut", 6.31, "")]),
    (8.73, [("ataupun", 7.15, ""), ("angin", 7.69, ""), ("bertiup,", 8.07, "")]),
    (10.50, [("hanger", 8.73, ""), ("dia", 9.41, ""), ("takkan", 9.61, ""), ("merapat", 10.05, "box")]),
    (12.22, [("Berbanding", 10.50, ""), ("kalau", 11.49, ""), ("ia", 11.91, ""), ("ni", 12.07, "")]),
    (13.45, [("dia", 12.22, ""), ("melendut,", 12.48, "")]),
    (14.89, [("ataupun", 13.45, ""), ("kalau", 13.90, ""), ("ia", 14.05, ""), ("berangin,", 14.17, "")]),
    (15.70, [("dia", 14.89, ""), ("akan", 14.96, ""), ("merapat", 15.21, "serif")]),
    (16.56, [("Bila", 15.70, ""), ("macam", 15.96, ""), ("ni,", 16.30, "")]),
    (17.84, [("ia", 16.56, ""), ("susah", 16.72, ""), ("nak", 17.02, ""), ("kering", 17.22, "box")]),
    (18.70, [("Kalau", 17.84, ""), ("macam", 18.30, ""), ("ni,", 18.55, "")]),
    (20.60, [("jarak", 18.70, ""), ("dia", 19.74, ""), ("tetap", 20.09, ""), ("sama", 20.30, "box")]),
    (22.58, [("Bahan", 20.60, ""), ("dia", 20.95, ""), ("sangat", 21.21, ""), ("berkualiti,", 21.66, "serif")]),
    (23.55, [("sangat", 22.58, ""), ("kuat", 23.04, "box")]),
    (25.13, [("Berminat", 23.55, ""), ("dengan", 24.01, ""), ("tali", 24.39, ""), ("jemuran", 24.64, "")]),
    (26.00, [("ni,", 25.13, ""), ("dapatkan", 25.41, ""), ("di", 25.88, "")]),
    (27.34, [("beg kuning", 26.00, "serif"), ("ni", 26.40, "")]),
]

HOOK = dict(start=0.15, end=2.9, text="review **tali jemuran**", x=350, y=1150)

CARDS = [
    dict(kind="vs", start=1.5, end=5.0, kicker="TALI JEMURAN", old="Tali biasa", new="Windproof", new_at=4.39),
    dict(kind="icon", start=5.0, end=15.7, kicker="01 · TAHAN ANGIN", title="Hanger *tak merapat*", icon="wind"),
    dict(kind="check", start=15.7, end=20.6, kicker="02 · MUDAH KERING", title="Jarak *tetap sama*",
         items=[("Tak susah kering", 17.22), ("Jarak hanger sama", 20.30)]),
    dict(kind="icon", start=20.6, end=23.55, kicker="03 · KUALITI", title="Sangat *kuat*", icon="shield"),
]
RAIL = dict(start=5.0, end=23.55, steps=[(5.0, "Tahan angin"), (15.7, "Mudah kering"), (20.6, "Kuat")])
CTA = dict(start=23.55, button_at=24.9, button="Tekan *beg kuning*",
           items=["Ada lubang, windproof", "Hanger tak merapat", "Jarak tetap sama", "Bahan berkualiti & kuat"])
