# Magnetic frame saiz F4 (Drive 1pXMAKfHB0mht6MoJmyw_KGtycI3yT97F) — Style 3
# Bina: python3 -I styles/style-3/build.py work/v1/raw.mp4 styles/style-3/projects/frame.py work/v1/hf

REMOVE = [
    (2.84, 4.14),    # "aa, nak letak" (ulangan pertama)
    (7.32, 8.20),    # "aa, ya kan ni"
    (11.95, 12.76),  # "okey"
]
SRC_END = 20.3
TAIL = 1.9

# Kepala di bahagian atas frame (y ~5–25 %) → tajuk, CTA & gradien di BAWAH.
POSITION = "bottom"

END = 15.89
HEADS = [
    dict(start=0.0, end=2.79, kicker="Frame gambar", title="Magnetic.", pills=[(1.69, "Saiz F4")]),
    dict(start=2.79, end=5.6, kicker="Nak letak", title="Gambar.", pills=[(4.71, "Sangat sesuai")]),
    dict(start=5.6, end=8.6, kicker="Frame warna", title="Gold.", pills=[(7.6, "Sangat menarik")]),
    dict(start=8.6, end=11.64, kicker="Ada", title="Pelbagai saiz."),
]
IMAGES = []   # tiada gambar produk diberi
CTA = dict(start=11.64, text="Beli di beg kuning")
