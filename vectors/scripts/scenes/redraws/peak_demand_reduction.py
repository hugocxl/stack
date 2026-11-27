from scenes.redraws._kit import badge

DESCRIPTION = "Five demand columns rise and fall, and the tallest carries a down-arrow badge."


def draw(s):
    for i, h in enumerate((22, 38, 64, 44, 28)):
        s.box(-60 + i*24, -10, 0, 18, 18, h, 2)
    badge(s, "down", -2, -1, 76, 12)
