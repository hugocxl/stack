from geometry import BOLD, DETAIL, oval


DESCRIPTION = "A made bed with a tall headboard has a magnifying glass resting against the headboard corner."


def magnifier(s, x, y, z, r):
    outer = oval(x, z, r, r, count=48)
    inner = oval(x, z, r * .76, r * .76, count=48)
    s.tube([(x + r * .58, y, z - r * .58), (x + r * 1.61, y, z - r * 1.58)], r * .15)
    s.face([(a, y, b) for a, b in outer[:-1]], BOLD,
           openings=[[(a, y, b) for a, b in inner[:-1]]])


def draw(s):
    for x, y in ((4, 4), (46, 4), (4, 65), (46, 65)):
        s.box(x, y, 0, 5, 5, 8, 1.5)
    s.box(0, 0, 8, 54, 74, 6, 4)
    s.box(1, 1, 14, 52, 71, 6, 4)
    s.box(0, 0, 9, 54, 5, 29, 2)
    for x in (5, 28):
        s.box(x, 8, 20, 20, 15, 4, 4)
    s.line([(2, 29, 20), (52, 29, 20)], DETAIL)
    s.line([(52, 29, 20), (52, 29, 16)], DETAIL)
    magnifier(s, 56, 8, 31, 12)
