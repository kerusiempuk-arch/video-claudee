# Buku "Solat" (Drive 1s1ONIE-gV2FhexDOwmj5VEyL57yFHp2E) — Style 3
# Bina: python3 -I styles/style-3/build.py work/v1/raw.mp4 styles/style-3/projects/solat.py work/v1/hf

REMOVE = [
    (9.93, 11.21),   # "okay, syarat." (ulangan — simpan "syarat dia")
    (15.02, 24.60),  # "okay, aa" + selak buku tanpa suara + "okay"
    (27.30, 28.33),  # "dengan, aa" (ulangan — simpan "dengan orang")
    (29.26, 29.86),  # "okay"
    (31.49, 32.32),  # "okay, aa"
    (36.87, 37.65),  # "okay"
]
SRC_END = 41.9
TAIL = 1.9

# Kepala di bahagian atas frame (y ~5–25 %), buku dipegang paras dada → tajuk, CTA & gradien di BAWAH.
POSITION = "bottom"

END = 25.20
HEADS = [
    dict(start=0.0, end=4.0, kicker="Sempurnakan", title="Solat anda.", pills=[(2.0, "Buku bertajuk Solat")]),
    dict(start=4.0, end=8.6, kicker="Perbaiki solat", title="3 hari saja.",
         pills=[(4.66, "Membantu perbaiki solat"), (6.9, "Dalam masa 3 hari")]),
    dict(start=8.6, end=12.2, kicker="Syarat dia", title="Baca & amal.",
         pills=[(9.46, "Baca buku ni"), (10.73, "Cuba amalkan")]),
    dict(start=12.2, end=17.22, kicker="Malu · segan", title="Belajar sendiri.",
         pills=[(13.27, "Segan belajar dengan orang"), (15.85, "Cuba dapatkan buku ni")]),
    dict(start=17.22, end=21.77, kicker="Kualiti", title="Berwarna.",
         pills=[(17.57, "Cetakan berwarna"), (19.84, "Kertas berkualiti")]),
    dict(start=21.77, end=23.02, kicker="Harga", title="Sangat murah."),
]
IMAGES = []   # tiada gambar produk diberi
CTA = dict(start=23.02, text="Beli di beg kuning")
# Cover: python3 -I tools/cover/make_cover.py work/v1/raw.mp4 7.0 work/v1/cover.png --style 3 --title "Buku Solat." \
#   --kicker "Perbaiki solat · 3 hari" --pills "Cetakan berwarna,Kertas berkualiti,Sangat murah" --pos bottom --y 760
