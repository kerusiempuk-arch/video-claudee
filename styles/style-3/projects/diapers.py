# Diapers / Underpads Companylove saiz M (Drive 1Ng3G1PyHVMhvdw6did6FqWImXyeGflga) — Style 3
# Bina: python3 -I styles/style-3/build.py work/v1/raw.mp4 styles/style-3/projects/diapers.py work/v1/hf

REMOVE = [
    (0.0, 0.39),     # "aa"
    (4.84, 5.00),    # "aa"
    (8.71, 8.81),    # "aa"
    (12.00, 12.55),  # "okay"
    (13.64, 14.21),  # "okay"
    (17.42, 18.62),  # "aa bahag- pada" (gagap)
    (20.13, 22.90),  # "berminat dengan aa diapers" (ulangan pertama)
]
SRC_END = 28.18
TAIL = 1.9

# Kepala di bahagian atas frame (y ~8–25 %) → tajuk, CTA & gradien di BAWAH.
POSITION = "bottom"

END = 21.05
HEADS = [
    dict(start=0.0, end=5.0, kicker="Companylove", title="Diapers.", pills=[(3.53, "Size M")]),
    dict(start=5.0, end=10.5, kicker="Sesuai untuk", title="Bawa jalan.",
         pills=[(5.38, "Balik kampung"), (7.0, "Jalan-jalan"), (8.24, "Saiz pack padat")]),
    dict(start=10.5, end=12.0, kicker="Satu pack", big=[(10.67, "8+1")], sub="pieces."),
    dict(start=12.0, end=16.18, kicker="Ada", title="Pelbagai saiz.",
         pills=[(13.26, "Pelbagai pieces"), (14.52, "Pilih di menu")]),
]
IMAGES = []   # tiada gambar produk diberi
CTA = dict(start=16.18, text="Beli di beg kuning")
