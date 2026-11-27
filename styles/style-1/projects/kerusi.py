# Kerusi lipat camping (Drive 1s_PeI3lSdHu_1EtsfdJNkW-AWv-C9J0U)
# ---------- potongan (build.py) – masa ikut video ASAL
REMOVE = [
    (0.00, 0.96),    # "Nah, ah"
    (5.62, 7.42),    # "haa, healing-healing, haa" (sambungan terus ke "tepi ni ada beg")
    (11.55, 11.97),  # "haa okay"
    (13.92, 14.45),  # "okay"
    (19.60, 20.20),  # "okay"
    (30.14, 30.86),  # "okay, haa"
]
SRC_END = 49.6
TAIL = 1.2
PUNCH_Y = 0.25

END = 40.22
CAPTION_Y = 760       # atas, paras dada (680 kena mulut masa 6–9s)
CARD_Y = 1420
ZOOM = 0.04
SFX_WHOOSH = "whoosh"

def C_(end, *w):
    return (end, list(w))

CAPTIONS = [
    C_(0.70, ("Petang-petang", 0.00, False)),
    C_(1.64, ("duduk", 0.72, False), ("depan", 1.12, False), ("rumah", 1.34, True)),
    C_(2.30, ("macam", 1.64, False), ("ni", 1.96, False)),
    C_(3.34, ("sangat", 2.30, False), ("selesa", 2.64, True)),
    C_(4.56, ("guna", 3.34, False), ("kerusi", 4.02, False), ("ni", 4.38, False)),
    C_(5.40, ("Tepi", 4.56, False), ("ni", 4.82, False), ("ada", 5.10, False)),
    C_(5.92, ("beg", 5.40, True), ("dia", 5.64, False)),
    C_(6.36, ("nak", 5.92, False), ("letak", 6.06, False)),
    C_(7.16, ("botol", 6.36, False), ("air", 6.74, True), ("ke", 6.96, False)),
    C_(8.20, ("letak", 7.16, False), ("telefon", 7.48, True), ("ke", 7.94, False)),
    C_(8.96, ("sambil", 8.20, False), ("berehat", 8.60, True)),
    C_(10.16, ("sandar", 8.96, False), ("macam", 9.46, False), ("ni", 9.74, False)),
    C_(12.30, ("menenangkan", 11.28, True)),
    C_(13.60, ("Ini", 12.30, False), ("kerusi", 12.68, False), ("lipat", 13.04, True)),
    C_(14.60, ("serba", 13.60, False), ("guna", 14.06, True)),
    C_(15.44, ("Bagi", 14.60, False), ("kepala", 14.84, False), ("ada", 15.20, False)),
    C_(15.96, ("span", 15.44, True)),
    C_(16.72, ("bagi", 15.96, False), ("belakang", 16.02, False), ("ada", 16.50, False)),
    C_(17.00, ("span", 16.72, True)),
    C_(17.94, ("bagi", 17.00, False), ("tempat", 17.30, False), ("duduk", 17.56, False)),
    C_(18.50, ("span", 17.94, True)),
    C_(19.22, ("kiri", 18.50, False), ("kanan", 18.66, False), ("pun", 19.00, False)),
    C_(19.76, ("span", 19.22, True)),
    C_(20.86, ("Tak", 19.76, False), ("nak", 20.16, False), ("guna", 20.30, False)),
    C_(22.06, ("nak", 20.86, False), ("simpan", 21.28, True)),
    C_(23.12, ("lipat", 22.46, True), ("macam", 22.82, False)),
    C_(23.70, ("tu", 23.12, False), ("saja", 23.38, False)),
    C_(24.86, ("Bawah", 23.70, False), ("ni", 24.28, False), ("bahagian", 24.52, False)),
    C_(25.60, ("kaki", 24.86, True), ("ni", 25.26, False)),
    C_(27.58, ("Kita", 26.58, False), ("boleh", 26.96, False), ("nak", 27.26, False)),
    C_(28.30, ("tinggikan", 27.58, True)),
    C_(29.00, ("ataupun", 28.30, False), ("nak", 28.78, False)),
    C_(29.72, ("rendahkan", 29.00, True)),
    C_(31.34, ("level", 29.72, False), ("kerusi", 30.18, False), ("ni", 30.60, False)),
    C_(32.56, ("Nak", 31.34, False), ("pergi", 31.54, False), ("camping", 31.80, True)),
    C_(33.18, ("nak", 32.56, False), ("pergi", 32.58, False), ("healing", 32.80, True)),
    C_(34.08, ("tepi", 33.18, False), ("pantai", 33.40, True)),
    C_(35.54, ("Senang", 34.08, True), ("nak", 34.72, False), ("bawa", 34.88, False)),
    C_(36.56, ("nak", 35.54, False), ("kemas", 35.74, True)),
    C_(37.00, ("nak", 36.56, False), ("letak", 36.64, False), ("dalam", 36.82, False)),
    C_(37.92, ("kereta", 37.00, True), ("pun", 37.44, False)),
    C_(38.28, ("senang", 37.92, True)),
    C_(39.38, ("Berminat", 38.28, False), ("dapatkan", 38.92, True)),
    C_(40.22, ("di", 39.38, False), ("beg", 39.48, True), ("kuning", 39.64, True)),
]
HOOK = dict(end=4.56, y=100, kicker="kerusi lipat paling", title="selesa",
            options=[("Duduk depan rumah", "01"), ("Sangat selesa", "02")], select_at=[0.72, 2.30])
SECTIONS = [
    (4.56, 12.30, "kelebihan", "1 / 3", "ada beg tepi"),
    (12.30, 23.70, "kelebihan", "2 / 3", "span penuh"),
    (23.70, 34.08, "kelebihan", "3 / 3", "tinggi rendah boleh laras"),
]
STICKERS = [
    (5.40, 10.10, "beg tepi", 80, 260, 2.0),
    (6.36, 10.10, "botol air", 130, 340, -1.5),
    (7.48, 10.10, "telefon ✓", 180, 420, 1.5),
    (14.84, 19.70, "span kepala", 80, 260, 2.0),
    (16.02, 19.70, "span belakang", 130, 340, -1.5),
    (17.30, 19.70, "span tempat duduk", 180, 420, 1.5),
    (20.30, 23.60, "lipat & simpan", 80, 260, 2.0),
    (24.86, 30.50, "kaki boleh laras", 80, 260, 2.0),
    (27.58, 30.50, "tinggi / rendah", 130, 340, -1.5),
    (31.80, 34.00, "camping", 80, 260, 2.0),
    (33.18, 34.00, "tepi pantai", 130, 340, -1.5),
]
CIRCLES = []
BIG_WORDS = [  # (mula, tamat, perkataan, titik_merah)
    (10.16, 11.28, "selesa", True),
]
CTA = dict(title="selesa", title_at=34.08, title_y=230, card_at=38.28, card_y=1180,
           card_label="Kerusi Lipat", name="Kerusi Lipat Serba Guna", tags="span penuh · mudah lipat · kaki laras",
           button="Tekan beg kuning ↓", button_color=(255, 200, 40, 255), button_text_color=(22, 22, 26, 255))

# ---------- cover photo (tools/cover.py) – `at` ikut masa video ASAL
COVERS = [
    dict(at=3.0, kicker="kerusi lipat paling,", title="selesa",
         stickers=["span penuh", "senang lipat ✓"], pill="kelebihan 1-3 · kerusi lipat serba guna"),
    dict(at=46.0, kicker="kerusi lipat serba guna,", title="selesa",
         stickers=["camping & pantai", "senang bawa ✓"], pill="kelebihan 1-3 · kerusi lipat"),
]
