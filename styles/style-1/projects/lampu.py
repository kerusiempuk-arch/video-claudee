# Lampu kelip-kelip LED + remote (Drive 1gLT0QAAq6L5Jk_MAPPObade_HcE4CrXP)
REMOVE = [
    (0.00, 3.70),    # "Korang ingat waktu raya saja ke?" pertama (ulang)
    (7.25, 8.98),    # "Ha, ni lampu kelip-kelip." (ulang)
    (13.35, 14.36),  # "Ha, okey"
    (30.84, 32.85),  # "Nak pakai remote pun boleh." (berulang dgn ayat seterusnya)
    (36.70, 37.12),  # "okay" sebelum "Kalau tak ada bateri"
]
SRC_END = 54.5
TAIL = 1.2
PUNCH_Y = 0.25

END = 37.93
CAPTION_Y = 1780
CARD_Y = 1180
ZOOM = 0.04

CAPTIONS = [  # (group_end, [(perkataan, mula, highlight)])
    (0.70, [("Korang", 0.00, False), ("ingat", 0.34, False)]),
    (1.44, [("waktu", 0.70, False), ("raya", 1.04, True)]),
    (2.18, [("saja", 1.44, False), ("ke", 1.78, False)]),
    (2.76, [("ada", 2.18, False), ("lampu", 2.36, False)]),
    (3.24, [("kelip-kelip?", 2.76, True)]),
    (4.10, [("Lampu", 3.24, False), ("kelip-kelip", 3.64, True)]),
    (4.66, [("ni,", 4.10, False), ("yang", 4.40, False)]),
    (5.26, [("spesialnya,", 4.66, False)]),
    (6.20, [("dia", 5.26, False), ("boleh", 5.40, False), ("kontrol", 5.62, False)]),
    (7.06, [("pakai", 6.20, False), ("remote", 6.50, True)]),
    (7.88, [("Tengok", 7.06, False), ("aku", 7.14, False), ("tekan", 7.38, False)]),
    (8.96, [("lampu", 7.88, False), ("kelip-kelip", 8.50, True)]),
    (10.58, [("ni", 8.96, False), ("sesuai", 9.42, False), ("diletak", 10.02, False)]),
    (11.78, [("pada", 10.58, False), ("motor,", 10.86, True)]),
    (12.88, [("pada", 11.78, False), ("basikal,", 11.94, True)]),
    (13.40, [("kat", 12.88, False), ("rumah", 13.08, True)]),
    (14.66, [("pun", 13.40, False), ("boleh.", 13.80, False)]),
    (15.06, [("Kita", 14.66, False), ("boleh", 14.84, False)]),
    (15.68, [("kontrol", 15.06, False), ("pakai", 15.44, False)]),
    (16.96, [("remote", 15.68, True), ("ni", 16.10, False), ("saja.", 16.32, False)]),
    (17.40, [("Tak", 16.96, False), ("payah", 17.10, False)]),
    (18.08, [("nak", 17.40, False), ("tekan.", 17.56, True)]),
    (18.62, [("Ataupun", 18.08, False), ("kita", 18.36, False)]),
    (19.04, [("nak", 18.62, False), ("tekan", 18.78, False)]),
    (20.04, [("kat", 19.04, False), ("sini", 19.24, True), ("pun", 19.50, False), ("boleh.", 19.70, False)]),
    (20.80, [("Tapi", 20.04, False), ("nak", 20.36, False)]),
    (21.36, [("lagi", 20.80, False), ("mudah,", 21.08, True)]),
    (22.70, [("pakai", 21.36, False), ("remote", 21.52, True), ("saja.", 21.90, False)]),
    (23.30, [("Kalau", 22.70, False), ("tak", 22.96, False), ("ada", 23.14, False)]),
    (23.88, [("bateri,", 23.30, True)]),
    (25.18, [("kita", 23.88, False), ("boleh", 24.04, False), ("cas.", 24.30, True)]),
    (25.84, [("Pakai", 25.18, False), ("kabel", 25.54, False)]),
    (26.76, [("pengecas", 25.84, True)]),
    (27.46, [("yang", 26.76, False), ("telah", 26.92, False), ("diberi", 27.14, False)]),
    (28.64, [("Ini", 27.46, False), ("pelekat", 27.88, True), ("dia.", 28.34, False)]),
    (29.40, [("Lekat", 28.64, False), ("pada", 29.12, False)]),
    (30.04, [("motor", 29.40, True), ("ke,", 29.84, False)]),
    (31.74, [("pada", 30.04, False), ("basikal", 30.30, True), ("ke.", 30.90, False)]),
    (33.08, [("Lagi", 31.74, False), ("memudahkan,", 31.96, True)]),
    (33.84, [("lagi", 33.08, False), ("cantik,", 33.20, True)]),
    (34.66, [("lagi", 33.84, False), ("menarik.", 34.00, True)]),
    (35.46, [("Berminat", 34.66, False), ("dengan", 35.02, False)]),
    (36.84, [("lampu", 35.46, False), ("kelip-kelip", 35.88, True), ("ni.", 36.32, False)]),
    (37.32, [("Dapatkan", 36.84, False), ("di", 37.18, False)]),
    (37.93, [("bakul", 37.32, True), ("ni.", 37.64, False)]),
]
HOOK = dict(end=6.9, y=100,  # select_at = bila "raya" / "remote" disebut
            kicker="lampu kelip-kelip ni", title="remote",
            options=[("Untuk raya je?", "01"), ("Kontrol pakai remote", "02")], select_at=[1.04, 6.50])
SECTIONS = [  # (mula, tamat, "kelebihan", "1 / 3", subtajuk)
    (6.9, 14.6, "kelebihan", "1 / 3", "letak mana-mana"),
    (14.6, 22.6, "kelebihan", "2 / 3", "kontrol pakai remote"),
    (22.6, 34.6, "kelebihan", "3 / 3", "boleh cas & lekat"),
]
STICKERS = [  # (mula, tamat, teks, x, y, sudut)
    (8.0, 14.4, "macam-macam warna", 50, 250, 2.0),
    (10.86, 14.4, "motor", 80, 320, -1.5),
    (11.94, 14.4, "basikal", 110, 390, 1.5),
    (13.08, 14.4, "rumah", 140, 460, -2.0),
    (15.68, 22.5, "remote je", 50, 250, -2.0),
    (18.78, 22.5, "tekan butang pun boleh", 80, 320, 1.5),
    (21.08, 22.5, "lagi mudah", 110, 390, -1.5),
    (24.30, 27.7, "boleh cas", 50, 250, 2.0),
    (25.84, 27.7, "kabel pengecas disediakan", 80, 320, -1.5),
    (27.88, 34.5, "ada pelekat", 50, 250, -2.0),
    (29.40, 34.5, "motor · basikal", 80, 320, 1.5),
    (33.20, 34.5, "cantik & menarik", 110, 390, -1.5),
]
CIRCLES = []  # (mula, tamat, cx, cy, r, label, label_x, label_y)
CTA = dict(title="remote", title_at=34.66, title_y=230, card_at=35.46, card_y=1180,
           card_label="Lampu Kelip-Kelip", name="Lampu Kelip-Kelip LED", tags="remote · boleh cas · pelekat",
           button="Tekan bakul kuning ↓", button_color=(255, 200, 40, 255), button_text_color=(22, 22, 26, 255))
