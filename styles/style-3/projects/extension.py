# Extension wire 5 soket (Drive 1ObFq5nl5FwmKf4-Y3bOtqGrn3oOLhpBS) — Style 3
# Bina: python3 -I styles/style-3/build.py work/v2/raw.mp4 styles/style-3/projects/extension.py work/v2/hf

REMOVE = [
    (1.40, 2.66),    # gagap "ada lima su..." (ulang: "ada lima soket")
    (5.20, 6.34),    # "okay" + "haa"
    (12.78, 16.98),  # "okay" + "haa" + senyap panjang
    (18.58, 19.08),  # "haa, dia"
    (21.82, 22.44),  # "okay"
]
SRC_END = 26.6
TAIL = 1.9

END = 17.32
# Kepala di bahagian atas frame (y ~100–600) → tajuk, CTA & gradien di BAWAH.
POSITION = "bottom"
HEADS = [
    dict(start=0.0, end=4.05, kicker="Extension wire", title="5 soket.", pills=[(3.15, "Untuk 3 pin")]),
    dict(start=4.05, end=5.15, kicker="Ada sticker", title="SIRIM."),
    dict(start=5.15, end=9.7, kicker="Ada", title="Surge protector.",
         pills=[(6.95, "Lindungi elektrik"), (8.6, "Daripada kilat")]),
    dict(start=9.7, end=12.05, kicker="Boleh", title="Gantung dinding.", pills=[(11.15, "Ada slot")]),
    dict(start=12.05, end=14.8, kicker="Wire dia", title="Panjang.", pills=[(13.3, "Tebal"), (13.8, "Lebih selamat")]),
]
IMAGES = []   # tiada gambar produk diberi
CTA = dict(start=14.8, text="Beli di beg kuning")
