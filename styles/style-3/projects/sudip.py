# Set 5 sudip stainless (Drive 1iuNUyGuD9oarNN58nXCz7DibkwdXzEWE) — Style 3
# Bina: python3 -I styles/style-3/build.py work/v1/raw.mp4 styles/style-3/projects/sudip.py work/v1/hf

REMOVE = [
    (0.0, 19.08),    # bual dengan jurukamera sebelum mula ("dari mana?", "ya saya ada", "okay", "boleh", "ah")
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

END = 21.34
HEADS = [
    dict(start=0.0, end=4.0, kicker="Satu set", title="5 pieces.", pills=[(1.86, "Setiap satu lain jenis")]),
    dict(start=4.0, end=10.95, kicker="Lengkap", title="Semua ada.",
         pills=[(4.23, "Sudip nasi"), (5.88, "Sudip goreng sayur"), (9.0, "Kacau gulai · kuah")]),
    dict(start=10.95, end=14.6, kicker="Nak jimat", title="Satu harga.", pills=[(11.48, "5 pieces berlainan")]),
    dict(start=14.6, end=18.8, kicker="Kualiti", title="Tak berkarat.",
         pills=[(16.12, "Pemegang selesa"), (17.3, "Tak tercabut")]),
]
IMAGES = []   # tiada gambar produk diberi
CTA = dict(start=18.8, text="Beli di beg kuning")
