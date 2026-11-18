from math import cos, pi

from geometry import BOLD, DETAIL, EDGE, oval, rounded
from scenes.redraws._kit import arrow

DESCRIPTION = "A clockwise renewal arrow curves around the ribbon seal of a certificate."


def draw(s):
    s.box(-43, -3, 0, 86, 4, 57, 1)
    border = rounded(-38, 5, 76, 47, 2)
    s.line([(x, 1.01, z) for x, z in border + border[:1]], DETAIL)
    s.line([(-29, 1.01, 41), (1, 1.01, 41)], EDGE)
    for z, width in ((31, 26), (24, 22), (17, 19)):
        s.line([(-29, 1.01, z), (-29 + width, 1.01, z)], DETAIL)

    x, y, z = 17, 1.02, 25
    s.face([(x + u, y, z + v) for u, v in
            ((-5, -4), (-7, -11), (-4, -10), (-2, -12),
             (0, -7), (2, -12), (4, -10), (7, -11), (5, -4))], EDGE)
    seal = oval(0, 0, 7.5, 7.5, count=64)[:-1]
    scallops = [1 + .07 * cos(i * pi / 4) for i in range(len(seal))]
    s.face([(x + u * scale, y + .01, z + v * scale)
            for (u, v), scale in zip(seal, scallops)], EDGE)

    arc = oval(x, z, 15, 16, -61, -361, 48)
    arrow(s, [(a, y + .02, b) for a, b in arc], ink=BOLD, head=7)
