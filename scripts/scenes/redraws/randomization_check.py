from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge

DESCRIPTION = "An assignment grid mixes round and triangular tokens, with a check badge on its near corner."


def draw(s):
    s.box(0, 0, 0, 92, 90, 11, 5)
    for i in range(1, 4):
        a = 6 + i*20
        s.line([(a, 5, 11), (a, 86, 11)], DETAIL)
        s.line([(5, a, 11), (86, a, 11)], DETAIL)
    for j, row in enumerate(("oott", "toto", "otto", "ttoo")):
        for i, kind in enumerate(row):
            x, y = 16 + i*20, 16 + j*20
            if kind == "o":
                s.disk(x, y, 11, 5.1, 5.1, 2, EDGE)
            else:
                s.solid([(x - 7, y + 6), (x + 1, y - 8), (x + 6, y + 6)],
                        11, 2, ink=EDGE, crease=False)
    badge(s, "check", 96, 69, 11, 15)
