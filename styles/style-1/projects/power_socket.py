# Power socket / extension (Drive 1oyUg6xdXh6cJuSmpmF_ZocH9v6hoI4NB) — salin fail ni, isi ikut video. Contoh lengkap: styles/style-1/projects/boxer.py. Bina: python3 -I styles/style-1/build.py <raw.mp4> <fail ini> <work_dir>
# ---------- potongan (build.py) – masa ikut video ASAL
REMOVE = [
    (0.00, 0.29),    # "Ha,"
    (4.80, 5.60),    # "okay"
    (6.00, 7.30),    # bunyi + "Extension." – mula tak habis
    (16.30, 17.25),  # "okay"
    (20.42, 20.92),  # "okay"
    (21.47, 22.80),  # bunyi kotak/plastik antara "ada dua" & "yang hitam"
    (24.45, 30.60),  # belek wayar senyap + "Harga." gagap
]
SRC_END = 36.1        # potong selepas ni (orang keluar frame / kamera jatuh)
TAIL = 1.2            # hujung tak dipotong senyap — masa baca CTA (1.2s supaya kad CTA sempat dibaca)
PUNCH_Y = 0.25        # punch-in fokus ke atas (muka)

# ---------- overlay (build.py) – masa ikut video SELEPAS dipotong
END = 21.93
CAPTION_Y = 760         # muka rendah dalam video ni – 680 kena dagu
CARD_Y = 1420
ZOOM = 0.04

def g(*ws):  # ((perkataan, mula, highlight)...) , end
    *words, end = ws
    return (end, list(words))

CAPTIONS = [
    g(("Cepat", 0.00, False), ("grab", 0.26, True), 0.50),
    g(("sekarang", 0.52, False), 1.30),
    g(("Sementara", 1.32, False), ("TikTok", 1.90, True), 2.32),
    g(("tengah", 2.34, False), ("bagi", 2.58, False), 3.08),
    g(("harga", 3.10, False), ("promo", 3.46, True), 3.86),
    g(("sekarang", 3.88, False), ("ni", 4.32, False), 4.78),
    g(("Ini", 4.80, False), ("power", 5.06, False), ("socket", 5.38, True), 6.22),
    g(("extension", 6.24, False), ("wire", 6.74, False), 7.24),
    g(("ataupun", 7.26, False), 7.64),
    g(("extension", 7.66, False), ("socket", 8.12, True), 9.24),
    g(("Tiga", 9.26, False), ("untuk", 9.48, False), ("plug", 9.78, True), 9.92),
    g(("tiga", 9.94, False), ("pin", 10.24, True), 10.90),
    g(("Enam", 10.92, False), ("untuk", 11.16, False), ("USB", 11.62, True), 12.70),
    g(("Tekan", 12.72, False), ("sekali", 12.86, False), ("on", 13.14, True), 13.60),
    g(("tekan", 13.62, False), ("sekali", 13.96, False), ("lagi", 14.24, False), 14.60),
    g(("off", 14.62, True), 15.34),
    g(("Ada", 15.36, False), ("dua", 15.44, True), 15.80),
    g(("yang", 15.82, False), ("hitam", 15.86, True), 16.40),
    g(("dan", 16.42, False), ("yang", 16.60, False), ("putih", 16.80, True), 17.76),
    g(("Harga", 17.78, False), ("memang", 18.14, False), 18.38),
    g(("tengah", 18.40, False), ("murah", 18.66, True), 18.96),
    g(("sekarang", 18.98, False), ("ni", 19.30, False), 19.64),
    g(("Berminat?", 19.66, False), ("klik", 20.12, False), 20.32),
    g(("beg", 20.34, True), ("kuning", 20.50, True), 21.93),
]
HOOK = dict(end=8.66, y=100, kicker="power socket,", title="promo",
            options=[("Cepat grab", "01"), ("Harga promo", "02"), ("Extension socket", "03")],
            select_at=[0.00, 3.10, 7.66])
SECTIONS = [  # (mula, tamat, "kelebihan", "1 / 3", subtajuk)
    (8.66, 12.70, "kelebihan", "1 / 3", "3 plug + 6 USB"),
    (12.70, 15.34, "kelebihan", "2 / 3", "suis on / off"),
    (15.34, 17.76, "kelebihan", "3 / 3", "2 warna"),
]
STICKERS = [  # (mula, tamat, teks, x, y, sudut)
    (9.78, 12.60, "3 plug, 3 pin", 50, 250, 2.0),
    (11.62, 12.60, "6 port USB", 80, 320, -1.5),
    (13.14, 15.30, "tekan sekali = on", 50, 250, 2.0),
    (14.62, 15.30, "tekan lagi = off", 80, 320, -1.5),
    (15.86, 17.70, "hitam", 50, 250, -2.0),
    (16.80, 17.70, "putih", 80, 320, 1.5),
]
CIRCLES = []
BIG_WORDS = []  # "murah" di tengah tutup muka (18.4s) – tajuk CTA "murah" dah cukup
CTA = dict(title="murah", title_at=19.66, title_y=230, card_at=19.86, card_y=1180,
           card_label="Extension Socket", name="Power Socket",
           tags="3 plug · 6 USB · on/off",
           button="Tekan beg kuning ↓", button_color=(255, 200, 40, 255), button_text_color=(22, 22, 26, 255))
COVERS = []
