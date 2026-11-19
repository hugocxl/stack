from geometry import BOLD, EDGE, rounded
from scenes.redraws._w4 import paper

DESCRIPTION = "A phone displays a vertical video with four bold crop corners around the central image."


def draw(s):
    phone = paper(s, 110, pitch=.87, run=.35, angle=-11, depth=10)
    phone.slab(rounded(0, 0, 60, 110, 9), 10)
    phone.frame(5, 12, 50, 91, 4, EDGE)
    phone.rows(24, 6, (12,), ink=EDGE)
    phone.oval(40, 38, 4, 4)
    phone.line([(9, 65), (22, 47), (31, 59), (39, 54), (51, 68)], EDGE)
    for u, du in ((8, 1), (52, -1)):
        for v, dv in ((24, 1), (79, -1)):
            phone.line([(u, v + dv*9), (u, v), (u + du*9, v)], BOLD)
    phone.line([(12, 91), (47, 91)], EDGE)
    phone.oval(34, 91, 2.5, 2.5, EDGE)
