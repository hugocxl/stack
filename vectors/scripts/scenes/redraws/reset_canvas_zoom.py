from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface

DESCRIPTION = "Four framing corners sit inside a magnifier with a circular reset arrow attached to its rim."


def draw(s):
    lens = Surface(s, (0, 0, 0), rise=(-.39, .92), back=(0, -.92, -.39),
                   across=(.98, -.2))
    s.tube([lens.point(18, 31, 4), lens.point(43, 6, 4)], 6, EDGE)
    lens.plate(oval(0, 49, 32, 32, count=64)[:-1], 4)
    lens.oval(0, 49, 27, 27, DETAIL)
    for x, v in ((-15, 62), (15, 62), (-15, 36), (15, 36)):
        dx = -1 if x < 0 else 1
        dv = -1 if v < 49 else 1
        lens.stroke([(x, v - 7 * dv), (x, v), (x - 7 * dx, v)], EDGE)
    badge(s, "refresh", *lens.point(31, 70, -3), 14)
