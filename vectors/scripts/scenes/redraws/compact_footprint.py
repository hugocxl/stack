from geometry import DETAIL, EDGE

DESCRIPTION = "A folded stepladder stands with a dimension bracket spanning its shallow footprint."


def draw(s):
    for x in (4, 46):
        s.tube([(x, -9, 2), (x, -3, 80)], 2.8)
    for x in (0, 50):
        s.tube([(x, 13, 3), (x, -1, 85)], 3.2)
    for z in (23, 44, 65, 84):
        y = 13 - (z - 3) * 14 / 82
        s.tube([(0, y + .5, z), (50, y + .5, z)], 2.45)
    for x in (0, 50):
        s.tube([(x, 13, 3), (x, 12.3, 7)], 3.4, DETAIL)

    s.line([(64, -11, 1), (64, 16, 1)], EDGE)
    for y in (-11, 16):
        s.line([(59, y, 1), (69, y, 1)], EDGE)
        s.line([(55, y, 1), (58, y, 1)], DETAIL)
