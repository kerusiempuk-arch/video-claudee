# Trash bag / beg sampah (Drive 12DKri6uo2h9fNST3btw0fP8F-6AWJwOp)
# --- potongan (build.py), masa ikut video ASAL
REMOVE = [
    (2.68, 3.64),    # "okay, aaa"
    (5.30, 6.60),    # "okay, aa"
    (6.86, 12.21),   # bunyi + "okay, ya spesialnya" (ambilan pertama, diulang lepas tu)
    (16.38, 17.08),  # "okay"
    (24.50, 24.96),  # "aa"
    (26.02, 28.16),  # "okay, dengan 100 pcs" (diulang lepas tu)
]
SRC_END = 35.7
TAIL = 1.0
# NOTA: "okay" sebelum "harga" (~31.3) bercantum dengan "harga" — tak dipotong supaya "harga" tak hilang.

# --- overlay (build.py), masa ikut video SELEPAS dipotong (transkripsi cut.wav)
END = 23.73
CAPTION_Y = 545

CAPTIONS = [
    (1.69, [("Trash", 0.07, ""), ("bag", 0.58, "box"), ("ataupun", 0.90, "")]),
    (2.91, [("beg sampah.", 1.69, "serif")]),
    (4.41, [("100 pcs", 2.91, "box"), ("semua.", 3.99, "")]),
    (5.04, [("Tengok", 4.41, ""), ("yang", 4.59, ""), ("spesial", 4.74, "serif")]),
    (6.00, [("beg", 5.04, ""), ("sampah", 5.25, ""), ("ni.", 5.68, "")]),
    (6.99, [("Dia", 6.00, ""), ("tebal.", 6.33, "box")]),
    (8.69, [("Ada", 6.99, ""), ("pelbagai", 7.26, ""), ("saiz.", 8.08, "serif")]),
    (9.99, [("Susah", 8.69, ""), ("nak", 9.25, ""), ("koyak.", 9.61, "box")]),
    (11.11, [("Biasa,", 9.99, ""), ("beg", 10.48, ""), ("sampah", 10.66, "")]),
    (11.80, [("kalau", 11.11, ""), ("kita", 11.32, ""), ("beli", 11.52, "")]),
    (13.11, [("kat", 11.80, ""), ("kedai", 12.04, ""), ("biasa,", 12.61, "")]),
    (13.99, [("dia", 13.11, ""), ("senang", 13.27, ""), ("bocor,", 13.59, "box")]),
    (15.00, [("senang", 13.99, ""), ("koyak.", 14.62, "serif")]),
    (16.38, [("Ya", 15.00, ""), ("ini", 15.19, ""), ("dia", 15.49, ""), ("spesial.", 15.75, "box")]),
    (17.69, [("Dengan", 16.38, ""), ("banyak", 16.69, ""), ("macam", 17.08, ""), ("ni,", 17.38, "")]),
    (19.24, [("100 pcs", 17.69, "box"), ("macam", 18.69, ""), ("ni,", 19.00, "")]),
    (21.00, [("harga", 19.24, ""), ("sangat", 19.88, ""), ("berbaloi.", 20.18, "serif")]),
    (22.41, [("Berminat?", 21.00, ""), ("Dapatkan", 21.58, ""), ("di", 22.22, "")]),
    (23.73, [("beg kuning", 22.41, "serif")]),
]

HOOK = dict(start=0.15, end=2.85, text="review **beg sampah**", x=350, y=690)

CARDS = [
    dict(kind="icon", start=2.91, end=4.41, kicker="01 · ISI", title="*100 pcs* semua", icon="tag"),
    dict(kind="check", start=4.41, end=9.99, kicker="02 · SPESIAL", title="Kenapa *spesial*",
         items=[("Tebal", 6.33), ("Pelbagai saiz", 8.08), ("Susah nak koyak", 9.61)]),
    dict(kind="vs", start=9.99, end=16.38, kicker="KEDAI BIASA", old="Nipis", new="Tebal", new_at=15.75),
    dict(kind="icon", start=16.38, end=19.24, kicker="03 · BANYAK", title="*100 pcs* satu pek", icon="star"),
    dict(kind="icon", start=19.24, end=21.0, kicker="04 · HARGA", title="Harga *berbaloi*", icon="bolt"),
]
RAIL = dict(start=2.91, end=21.0, steps=[(2.91, "100 pcs"), (4.41, "Spesial"), (9.99, "Banding"),
                                         (16.38, "Banyak"), (19.24, "Harga")])
CTA = dict(start=21.0, button_at=21.58, button="Tekan *beg kuning*",
           items=["100 pcs satu pek", "Tebal, susah koyak", "Pelbagai saiz", "Harga berbaloi"])
