# Bekas air batu / acuan ais silikon berpenutup (Drive 1Z54_Gs9gQO2MJ3J21aCTZGCfstGPIEHb) — Style 3
# Bina: python3 -I styles/style-3/build.py work/v1/raw.mp4 styles/style-3/projects/aisbatu.py work/v1/hf

REMOVE = [
    (0.0, 2.36),     # "isi sahaja" pertama (ulangan)
    (19.46, 22.31),  # "untuk nak buat air batu" ulangan + "okay?" + "haa"
    (26.0, 27.02),   # "okay?" + "haa"
    (29.72, 30.62),  # "rasa nak air," (gagap)
    (33.6, 36.42),   # "haa, setakat nak minum," pertama (ulangan)
    (40.36, 41.16),  # "okay"
    (46.53, 47.24),  # "okay"
]
SRC_END = 54.05
TAIL = 1.9

# Kepala di bahagian atas frame (y ~5–25 %) → tajuk, CTA & gradien di BAWAH.
POSITION = "bottom"

END = 34.16
HEADS = [
    dict(start=0.0, end=5.84, kicker="Senang je", title="Isi air.",
         pills=[(2.3, "Penuh setiap ruang"), (5.1, "Terus tutup")]),
    dict(start=5.84, end=9.92, kicker="Lepas tu", title="Masuk peti sejuk."),
    dict(start=9.92, end=12.2, kicker="Ini adalah", title="Bekas air batu."),
    dict(start=12.2, end=15.17, kicker="Design", title="Cantik.", pills=[(14.1, "Sangat menarik")]),
    dict(start=15.17, end=20.28, kicker="Kat rumah", title="Buat sendiri.",
         pills=[(16.0, "Nak minum air batu"), (17.5, "Nak air sejuk")]),
    dict(start=20.28, end=25.68, kicker="Minum sikit-sikit", title="Memang boleh.",
         pills=[(24.0, "Design menarik")]),
    dict(start=25.68, end=28.08, kicker="Ketulan air batu", title="Lebih menarik."),
    dict(start=28.08, end=29.48, kicker="Harga", title="Sangat murah."),
]
IMAGES = []   # tiada gambar produk diberi
CTA = dict(start=29.48, text="Beli di beg kuning")
# Cover: python3 -I tools/cover/make_cover.py work/v1/raw.mp4 52.5 work/v1/cover.png --style 3 --title "Bekas Air Batu." \
#   --kicker "Buat sendiri · Sangat murah" --pills "Design cantik,Penuh setiap ruang,Masuk peti sejuk" --pos bottom --y 760   # teks di tengah (owner)
