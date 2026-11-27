# Seluar trek hitam (Drive 18-miBOVu7rQ80PnA1Pl-tKFQ9ilLJsPH) — Style 3
# Bina: python3 -I styles/style-3/build.py work/v1/raw.mp4 styles/style-3/projects/trek.py work/v1/hf

REMOVE = [
    (4.15, 8.44),    # "okay, aa" + "ada poket berzip, okay" (ulangan pertama)
    (10.40, 10.84),  # "okay"
    (13.85, 17.42),  # "okay" + "bahagian ping-" (ulangan pertama)
    (18.22, 18.76),  # "aa"
    (26.10, 26.31),  # "okay"
    (34.90, 37.70),  # "nak basuh memang senang kering" (ulangan pertama)
]
SRC_END = 45.2
TAIL = 1.9

# Kepala di bahagian atas frame → tajuk, CTA & gradien di BAWAH.
POSITION = "bottom"

END = 29.26
HEADS = [
    dict(start=0.0, end=3.50, kicker="Seluar trek", title="Warna hitam."),
    dict(start=3.50, end=7.80, kicker="Poket dia", title="Siap berzip.",
         pills=[(5.45, "Kanan · kiri")]),
    dict(start=7.80, end=12.80, kicker="Pinggang", title="Getah tebal.",
         pills=[(10.58, "Sangat selesa")]),
    dict(start=12.80, end=15.55, kicker="Siap ada", title="Tali.",
         pills=[(14.0, "Boleh ketatkan")]),
    dict(start=15.55, end=21.30, kicker="Material", title="Kain stretch.",
         pills=[(17.38, "Tengok dekat")]),
    dict(start=21.30, end=27.00, kicker="Lepas basuh", title="Cepat kering.",
         pills=[(22.21, "Senang basuh"), (25.03, "Senang dibersihkan")]),
]
IMAGES = []
CTA = dict(start=27.00, text="Beli di beg kuning")
# Cover: python3 -I tools/cover/make_cover.py work/v1/raw.mp4 42.8 work/v1/cover.png --style 3 --title "Seluar Trek." \
#   --kicker "Kain stretch · Cepat kering" --pills "Poket berzip,Getah tebal,Ada tali" --pos bottom --y 760
