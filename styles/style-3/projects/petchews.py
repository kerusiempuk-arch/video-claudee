# Pet Chews (ubat cacing/kutu kucing) — Drive 1LDsrqV5a47l5DEkTxMxzjzwoIxet5uYh
# Bina: python3 -I styles/style-3/build.py work/v1/raw.mp4 styles/style-3/projects/petchews.py work/v1/hf

REMOVE = [
    (5.20, 5.62),    # aa
    (6.80, 7.58),    # aa. Ya
    (10.15, 10.62),  # aa
    (12.66, 13.30),  # Okey aa
    (14.60, 16.28),  # aa akan nak, kucing aa
    (18.20, 20.70),  # harga pun sangat murah (owner minta buang)
    (23.56, 25.30),  # kalau kita pergi ke, aa (ayat tak habis)
    (27.98, 31.45),  # jumpa doktor, lagi mahal (owner minta buang) + okey. aa
    (32.30, 34.10),  # dia punya salam aa
    (35.78, 40.84),  # okey. Bagi kak kucing, kucing bagi kak kucing, dekatlah
    (42.95, 44.86),  # okey. Berminat, nih,
]
SRC_END = 47.4
TAIL = 1.9

POSITION = "bottom"  # muka di 10–28 % atas hampir sepanjang video
HEAD_Y = 1400        # botol dipegang paras dada (~50–65 %) → tajuk lebih bawah sikit

# --- overlay, masa SELEPAS potong
END = 24.88
HEADS = [
    dict(start=0.0, end=4.2, kicker="Kucing ada", title="Masalah.",
         pills=[(1.5, "Cacing"), (2.65, "Kutu"), (3.65, "Parasit")]),
    dict(start=4.2, end=5.25, kicker="Ini jawapan", title="Pet Chews."),
    dict(start=5.25, end=9.75, kicker="Kucing selalu", title="Garu-garu.",
         pills=[(7.1, "Gatal-gatal"), (8.3, "Jadi tak sihat")]),
    dict(start=9.75, end=13.05, kicker="Bagi ini", title="Lagi ceria.", pills=[(12.3, "Lagi sihat")]),
    dict(start=13.05, end=14.8, kicker="Harga", title="Berbaloi."),
    dict(start=14.8, end=17.9, kicker="Berbanding", title="Beli ubat.", pills=[(16.3, "Pergi kedai")]),
    dict(start=17.9, end=20.3, kicker="Tengok", title="Bentuk dia."),
    dict(start=20.3, end=21.75, kicker="Bagi kucing", title="Kunyah je."),
]
IMAGES = []
CTA = dict(start=21.75, text="Beli di beg kuning", y=1450)
