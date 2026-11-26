# Boxer (rujukan Style 3, Drive 1hHKM5lkYPdj2YYQVw6qiHSPtgzrcHYP5) — dibina semula dari video rujukan, TANPA subtitle bawah.
# Gambar produk: screenshot dari listing TikTok Shop (owner beri) – letak dalam work/<nama>/img/ (tak masuk git).
# Bina: python3 -I styles/style-3/build.py work/vid1/raw.mp4 styles/style-3/projects/boxer.py work/vid1/hf

REMOVE = []
SRC_END = 29.3
TAIL = 1.9

END = 29.3  # dari --plan
HEADS = [  # masa SELEPAS potong. pills=[(bila disebut, "teks")]; big=[(bila, "nilai")] untuk nombor besar
    dict(start=0.0, end=4.75, kicker="Setiap hari", title="Lain warna.",
         pills=[(1.05, "Ahad · Hijau"), (2.79, "Isnin · Kelabu"), (4.0, "Rabu · Biru")]),
    dict(start=4.75, end=7.45, kicker="Sayang duit", title="Boxer baru."),
    dict(start=7.45, end=9.1, kicker="Boxer lama", title="Dah koyak.", pills=[(8.1, "Terkoyak-koyak")]),
    dict(start=9.1, end=11.3, kicker="Penyelesaian", title="Boxer TikTok."),
    dict(start=11.3, end=15.3, kicker="Jangan risau", title="Tiada brand.",
         pills=[(12.6, "Tak tulis brand"), (13.6, "Orang tak tahu")]),
    dict(start=15.3, end=16.7, kicker="Design", title="Nampak ok."),
    dict(start=16.7, end=19.0, kicker="Rasa dia", title="Lembut.",
         pills=[(17.1, "Depan lembut"), (17.9, "Dalam pun lembut")]),
    dict(start=19.0, end=21.8, kicker="Saiz · hingga", big=[(19.0, "3XL"), (19.9, "5XL")],
         sub="ikut saiz yang korang pakai"),
    dict(start=21.8, end=23.5, kicker="Kain dia", title="Selesa. Sejuk.", pills=[(22.0, "Selesa"), (22.8, "Sejuk")]),
    dict(start=23.5, end=25.3, kicker="Nak jimat", big=[(23.5, "2×"), (24.6, "3×")], sub="beli combo terus.", line=True),
]
IMAGES = [  # kad gambar produk (latar blur + gelap)
    dict(src="work/vid1/img/p1.png", start=9.6, end=11.3),
    dict(src="work/vid1/img/p2.png", start=15.4, end=16.7),
    dict(src="work/vid1/img/p3.png", start=22.2, end=23.5),
]
CTA = dict(start=25.3, text="Beli di beg kuning")
