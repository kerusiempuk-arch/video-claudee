# Kuali + penutup kaca (Drive 1fiJ1i53uxGKGFQfE6oczyhqg79Dku9d8) — Style 3
# Bina: python3 -I styles/style-3/build.py work/v1/raw.mp4 styles/style-3/projects/kuali.py work/v1/hf

REMOVE = [
    (8.50, 9.50),    # "okay" (selepas "dicuci")
    (15.45, 16.44),  # "okay"
    (21.86, 22.54),  # "okay"
    (28.80, 29.82),  # "okay"
]
SRC_END = 35.6
TAIL = 1.9

# Kepala di bahagian atas frame (y ~5–25 %) → tajuk, CTA & gradien di BAWAH.
POSITION = "bottom"

END = 26.57
HEADS = [
    dict(start=0.0, end=4.55, kicker="Satu kuali", title="Masak semua.",
         pills=[(1.12, "Sayur"), (1.98, "Goreng ikan"), (3.35, "Goreng ayam")]),
    dict(start=4.55, end=7.0, kicker="Kuali ni", title="Tak berkarat.", pills=[(5.8, "Senang dicuci")]),
    dict(start=7.0, end=11.75, kicker="Sesuai untuk", title="Semua orang.",
         pills=[(7.43, "Keluarga"), (8.53, "Bujang"), (10.17, "Masak maggi · senang")]),
    dict(start=11.75, end=16.65, kicker="Pemegang", title="Panjang.", pills=[(15.12, "Penutup pun sama")]),
    dict(start=16.65, end=22.7, kicker="Penutup", title="Jernih.",
         pills=[(18.99, "Nampak dah masak ke tak"), (20.84, "Tak payah asyik pakai sudip")]),
    dict(start=22.7, end=24.3, kicker="Ada", title="Pelbagai saiz."),
]
IMAGES = []   # tiada gambar produk diberi
CTA = dict(start=24.3, text="Beli di beg kuning")
# Cover: python3 -I tools/cover/make_cover.py work/v1/raw.mp4 1.0 work/v1/cover.png --style 3 --title "Kuali Non-Stick." \
#   --kicker "Tak berkarat · Senang dicuci" --pills "Pemegang panjang,Penutup jernih,Pelbagai saiz" --pos bottom --y 1490
