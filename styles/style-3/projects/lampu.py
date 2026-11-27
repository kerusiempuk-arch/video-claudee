# Lampu solar kelip-kelip bentuk bunga (Drive 1evFShvfLqYX0qS2hvkl5iLW2EAtjsWXq) — Style 3
# Bina: python3 -I styles/style-3/build.py work/v1/raw.mp4 styles/style-3/projects/lampu.py work/v1/hf

REMOVE = [
    (0.0, 3.47),     # "Haa, yang nampak muka apa kali ini?" — buka terus pada "Lampu kelip-kelip…"
    (5.85, 6.78),    # "haa"
    (8.62, 9.02),    # "aa"
    (14.75, 15.32),  # "okay, aa"
    (17.42, 18.95),  # "aa, kita just. Aa," (ayat tak habis)
]
SRC_END = 35.25
TAIL = 1.9

# Kepala di bahagian atas frame (y ~5–25 %) → tajuk, CTA & gradien di BAWAH.
POSITION = "bottom"

END = 26.44
HEADS = [
    dict(start=0.0, end=4.2, kicker="Lampu solar", title="Kelip-kelip.",
         pills=[(1.84, "Bentuk bunga"), (2.88, "Guna solar saja")]),
    dict(start=4.2, end=9.48, kicker="Siap ada", title="Pemacak.",
         pills=[(5.99, "Pacak kat tanah"), (8.01, "Sangkut kat pagar")]),
    dict(start=9.48, end=11.58, kicker="Tak payah", title="Tarik wire."),
    dict(start=11.58, end=15.12, kicker="Panel solar", title="Hadap matahari."),
    dict(start=15.12, end=17.2, kicker="Waktu malam", title="Berkelip."),
    dict(start=17.2, end=24.28, kicker="Ada", title="Banyak mod.",
         pills=[(20.37, "Video seterusnya"), (21.93, "Cara pasang · cahaya")]),
]
IMAGES = []   # tiada gambar produk diberi
CTA = dict(start=24.28, text="Beli di beg kuning")
# Cover: python3 -I tools/cover/make_cover.py work/v1/raw.mp4 28.3 work/v1/cover.png --style 3 --title "Lampu Solar." \
#   --kicker "Bentuk bunga · Kelip-kelip" --pills "Siap pemacak,Tak payah tarik wire,Banyak mod" --pos bottom --y 760
