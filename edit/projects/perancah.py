# Perancah lipat (video 1hVBeYmqNrjeLxb_zo6JKLbaCDI0twYgL)
END = 21.3
CAPTION_Y = 1010
CARD_Y = 1110

CAPTIONS = [  # (group_end, [(word, start, highlight)])
    (1.00, [("Nanti-nanti", 0.00, False)]),
    (2.40, [("saya", 1.06, False), ("nak", 1.26, False), ("naik", 1.30, False), ("atas", 1.40, True)]),
    (9.40, [("Nanti", 8.30, False), ("dulu", 8.90, True)]),
]
HOOK = dict(end=3.0, kicker="perancah lipat paling", title="kukuh",
            options=[("Ringan nak angkat", "01"), ("Kukuh nak panjat", "02")], select_at=[1.0, 2.0])
SECTIONS = [
    (3.0, 9.2, "kelebihan", "1 / 3", "naik senang"),
    (9.2, 14.4, "kelebihan", "2 / 3", "kukuh & stabil"),
    (14.4, 18.4, "kelebihan", "3 / 3", "berdiri pun boleh"),
]
STICKERS = [
    (3.5, 9.0, "duduk pun selesa", 70, 300, 2.0),
    (5.4, 9.0, "sampai tingkap atas", 110, 370, -1.5),
    (9.6, 14.2, "besi tebal", 70, 300, 2.0),
    (10.8, 14.2, "tak goyang", 110, 370, -1.5),
    (12.2, 14.2, "tahan berat", 150, 440, 1.5),
    (14.8, 18.3, "platform lebar", 70, 300, -2.0),
    (16.0, 18.3, "selamat buat kerja cat", 110, 370, 1.5),
]
CIRCLES = [
    (6.0, 7.8, 650, 225, 85, "tinggi", 760, 250),
    (10.6, 12.4, 860, 735, 80, "besi kukuh", 560, 800),
]
CTA = dict(title="kukuh", title_at=18.4, card_at=19.3, card_label="Perancah Lipat",
           name="Perancah Lipat", tags="ringan · kukuh · boleh lipat", button="Link dekat bawah ↓")
