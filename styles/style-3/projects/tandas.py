# Portable toilet / tandas mudah alih (Drive 1Cq_8s6M6k0UJ9VDG93xPcVr9l9LowUeE) — Style 3
# Bina: python3 -I styles/style-3/build.py work/v3new/raw.mp4 styles/style-3/projects/tandas.py work/v3new/hf

REMOVE = [
    (1.10, 2.02),    # "okay, ah" (simpan "tengok")
    (4.50, 8.58),    # "Dia sangat kuat sampai, okay, sangat..." (ayat tak habis — ambil take kedua)
    (9.76, 10.84),   # "okay"
    (14.62, 15.32),  # "okay. Aa,"
    (17.13, 18.31),  # "baldi dia, okay" (ulangan — simpan "baldi ini")
    (19.02, 19.40),  # "aa"
]
SRC_END = 39.0
TAIL = 1.9

# Kepala di bahagian atas frame, produk di bawah → tajuk, CTA & gradien di BAWAH.
POSITION = "bottom"

END = 28.80
HEADS = [
    dict(start=0.0, end=2.5, kicker="Tengok cara guna", title="Portable Toilet."),
    dict(start=2.5, end=4.8, kicker="Duduk je", title="Sangat kuat."),
    dict(start=4.8, end=9.4, kicker="Ada tempat", title="Serba lengkap.",
         pills=[(5.1, "Letak tangan"), (6.72, "Sandar"), (7.91, "Tisu")]),
    dict(start=9.4, end=13.4, kicker="Dalamnya", title="Ada baldi.",
         pills=[(11.1, "Untuk yang susah bergerak")]),
    dict(start=13.4, end=15.6, kicker="Jadi boleh", title="Guna baldi."),
    dict(start=15.6, end=19.6, kicker="Tips", title="Sarung plastik.",
         pills=[(18.16, "Senang buang kotoran")]),
    dict(start=19.6, end=25.2, kicker="Tak guna baldi", title="Atas jamban.",
         pills=[(22.2, "Lubang jamban rumah"), (23.75, "Terus boleh guna")]),
]
IMAGES = []   # tiada gambar produk diberi
CTA = dict(start=25.2, text="Beli di beg kuning")
