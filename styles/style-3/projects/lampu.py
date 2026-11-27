# Lampu kepala LED (Drive 1ZsJlHeKWPaLHcVYeDUB2hyDdd5EVmpc9) — Style 3
# Bina: python3 -I styles/style-3/build.py work/v1/raw.mp4 styles/style-3/projects/lampu.py work/v1/hf

REMOVE = [
    (0.0, 2.38),     # "Putih," pertama (ulangan) — buka terus pada "putih, kuning, biru"
    (7.15, 9.38),    # "boleh zoom in" pertama (ulangan)
    (11.45, 18.62),  # "tengok… tengok sangat luas" take pertama + bual — ambil take kedua
    (23.20, 31.88),  # "apa tu? apa tu?" orang lain + "tepi, tepi, tepi" (kamera merayau)
    (38.35, 40.68),  # "okay, getah dia pun," — ambil take penuh
    (43.40, 44.88),  # "berminat," pertama (ulangan)
]
SRC_END = 47.2
TAIL = 1.9
BRIGHTEN = None      # demo lampu — jangan cerahkan, cahaya lampu mesti nampak kontras

END = 18.96
HEADS = [
    dict(start=0.0, end=3.1, kicker="3 cahaya", title="Tukar warna.",
         pills=[(0.05, "Putih"), (0.5, "Kuning"), (1.04, "Biru")]),
    dict(start=3.1, end=4.91, kicker="Fokus cahaya", title="Boleh zoom.",
         pills=[(3.14, "Zoom in"), (4.05, "Zoom out")]),
    dict(start=4.91, end=9.01, kicker="Jarak cahaya", title="Sangat luas.",
         pills=[(7.23, "Satu bilik terang")]),
    dict(start=9.01, end=11.97, kicker="Bateri", title="Ada indikator."),
    dict(start=11.97, end=13.94, kicker="Port cas", title="Type-C."),
    dict(start=13.94, end=16.64, kicker="Getah dia", title="Lembut.",
         pills=[(15.6, "Selesa dipakai")]),
]
IMAGES = []   # tiada gambar produk diberi
CTA = dict(start=16.64, text="Beli di beg kuning", y=780)   # kepala di atas frame hujung video → CTA di dada, atas lampu
