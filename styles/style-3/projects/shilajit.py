# Shilajit + Tongkat Ali (liquid, sachet) (Drive 1f00CU2jEB34Xm95_C1P4ovMAbUm5derk) — Style 3
# Bina: python3 -I styles/style-3/build.py work/v1/raw.mp4 styles/style-3/projects/shilajit.py work/v1/hf

REMOVE = [
    (4.40, 5.07),    # "aa, okay"
    (7.10, 7.86),    # "okay, aa"
    (9.97, 10.94),   # "okay, aa"
    (20.64, 21.93),  # "okay, aa"
    (23.92, 24.68),  # "okay, aa"
    (27.12, 27.47),  # "okay"
    (34.47, 38.08),  # "okay, cara, cara nak, cara dia" (simpan "cara dia" terakhir)
    (38.74, 40.88),  # "cara dia" kedua & ketiga (ulangan)
    (44.42, 47.36),  # ulangan "berminat dengan Shilajit Tongkat" (simpan yang lengkap)
]
SRC_END = 51.9
TAIL = 1.9

# Kepala di bahagian atas frame (y ~5–25 %) → tajuk, CTA & gradien di BAWAH.
POSITION = "bottom"

END = 34.85
HEADS = [
    dict(start=0.0, end=3.2, kicker="Shilajit campur", title="Tongkat Ali.", pills=[(2.26, "Liquid")]),
    dict(start=3.2, end=4.8, kicker="Bentuk", title="Sachet."),
    dict(start=4.8, end=6.5, kicker="Setiap kotak", big=[(5.77, "10")], sub="pieces"),
    dict(start=6.5, end=13.36, kicker="Membantu", title="Bertenaga.",
         pills=[(10.11, "Tenaga harian"), (11.76, "Atasi kelesuan")]),
    dict(start=13.36, end=17.44, kicker="Khas untuk", title="Tenaga lelaki.", pills=[(16.0, "Bila diamalkan")]),
    dict(start=17.44, end=23.46, kicker="Kaum lelaki", title="Lebih sihat.",
         pills=[(20.01, "Badan terasa sihat"), (22.2, "Lebih bersemangat")]),
    dict(start=23.46, end=26.44, kicker="Lagi satu", title="Imun naik.", pills=[(24.69, "Tingkatkan imun")]),
    dict(start=26.44, end=29.04, kicker="Cara dia", title="1 sachet.", pills=[(27.6, "Untuk satu hari")]),
    dict(start=29.04, end=30.6, kicker="Rasa dia", title="Sedap."),
]
IMAGES = []   # tiada gambar produk diberi
CTA = dict(start=30.6, text="Beli di beg kuning")
