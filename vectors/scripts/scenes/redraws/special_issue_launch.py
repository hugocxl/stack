from geometry import DETAIL, EDGE
from scenes.redraws._kit import arrow
from scenes.redraws._w4 import landscape, paper

DESCRIPTION = "A magazine stands on an A-frame display beside a rising arrow."


def draw(s):
    cover = paper(s, 91, pitch=.94, run=.27, angle=-23, depth=15)
    for u in (16, 56):
        x, y, z = cover.at(u, 7)
        fx, fy, _ = cover.at(u, 91)
        bx, by = fx - 18, fy - 32
        s.tube([(fx, fy, 2), (x, y, z), (bx, by, 2)], 1.7, EDGE)
    s.tube([(*cover.at(16, 91)[:2], 11), (*cover.at(56, 91)[:2], 11)], 1.3, DETAIL)
    cover.slab([(0, 0), (70, 0), (70, 91), (0, 91)], 5)
    cover.line([(5, 2), (5, 88)], EDGE)
    cover.rows(12, 14, (47,), ink=EDGE)
    landscape(cover, 12, 28, 46, 45)
    cover.rows(12, 81, (29,))
    s.tube([cover.at(1, 91), cover.at(70, 91)], 2, EDGE)
    x, y, z = cover.at(76, 30)
    arrow(s, [(x, y, z), (x + 9, y - 3, z + 12), (x + 13, y - 6, z + 37)], EDGE, head=10)
