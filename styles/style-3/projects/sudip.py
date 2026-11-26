# Set 5 sudip stainless (Drive 1iuNUyGuD9oarNN58nXCz7DibkwdXzEWE) — Style 3
# Bina: python3 -I styles/style-3/build.py work/v1/raw.mp4 styles/style-3/projects/sudip.py work/v1/hf

REMOVE = [
    (0.0, 19.08),    # bual dengan jurukamera sebelum mula ("dari mana?", "ya saya ada", "okay", "boleh", "ah")
    (24.22, 25.10),  # "sudip gawit" (owner: buang)
    (29.25, 32.30),  # "untuk nak kacau, apa ni?" (cubaan pertama)
    (35.05, 35.70),  # "ah"
    (39.25, 40.75),  # "okay, ah"
    (44.20, 44.75),  # "okay"
    (45.70, 47.25),  # "berminat" pertama (ulang)
]
SRC_END = 51.1
TAIL = 1.9

# Kepala di bahagian atas frame (y ~5–30 %) → tajuk, CTA & gradien di BAWAH.
POSITION = "bottom"

END = 20.50
HEADS = [
    dict(start=0.0, end=4.0, kicker="Satu set", title="5 pieces.", pills=[(1.86, "Setiap satu lain jenis")]),
    dict(start=4.0, end=10.11, kicker="Lengkap", title="Semua ada.",
         pills=[(4.23, "Sudip nasi"), (5.04, "Sudip goreng sayur"), (8.16, "Kacau gulai · kuah")]),
    dict(start=10.11, end=13.76, kicker="Nak jimat", title="Satu harga.", pills=[(10.64, "5 pieces berlainan")]),
    dict(start=13.76, end=17.96, kicker="Kualiti", title="Tak berkarat.",
         pills=[(15.28, "Pemegang selesa"), (16.46, "Tak tercabut")]),
]
IMAGES = []   # tiada gambar produk diberi
CTA = dict(start=17.96, text="Beli di beg kuning")
# Cover: python3 -I tools/cover/make_cover.py work/v1/raw.mp4 21.1 work/v1/cover.png --style 3 --title "Set 5 Sudip." \
#   --kicker "5 jenis · Satu harga" --pills "Tak berkarat,Pemegang selesa,Tak tercabut" --pos bottom
