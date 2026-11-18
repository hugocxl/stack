from geometry import DETAIL, EDGE
from scenes.redraws._w5 import agreement, panel

DESCRIPTION = "A pen nib touches the end of a cursive signature on a ruled agreement sheet."


def draw(s):
    face, (x, z) = agreement(s)

    def pen(u, v):
        return face(x + u * .66 - v * .75, z + u * .75 + v * .66)

    panel(s, [(0, 0), (13, -4.1), (51, -4.1), (53, -2.7), (53, 2.7),
              (51, 4.1), (13, 4.1)], pen, 2.7, EDGE)
    for u in (13, 42):
        s.line([pen(u, -4), pen(u, 4)], DETAIL)
    s.line([pen(44, 1.8), pen(50, 1.8)], EDGE)
