from scenes.redraws._kit import badge

DESCRIPTION = "Three rows of venue seats flank a center aisle, with a check badge on the selected seat."


def draw(s):
    s.box(0, 0, 0, 98, 79, 5, 2)
    for row in range(3):
        y = 4 + row * 23
        z = 17 - row * 6
        s.box(1, y, 3, 96, 23, z - 3, 1)
        for x in (7, 24, 57, 74):
            s.box(x, y + 3, z, 14, 6, 14, 2.5)
            s.box(x, y + 9, z, 14, 9, 4, 2)
    badge(s, "check", 91, 7, 33, 10)
