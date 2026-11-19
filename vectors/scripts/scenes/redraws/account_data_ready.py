from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import arrow, coin
from scenes.redraws._w1 import fingerprint

DESCRIPTION = "A folded-corner profile data file carries a downward download arrow in a corner badge."


def draw(s):
    outline = [(-31, 0), (31, 0), (31, 50), (13, 68), (-31, 68)]
    for (x1, z1), (x2, z2) in zip(outline[1:], outline[2:]):
        s.face([(x1, -3, z1), (x2, -3, z2), (x2, 0, z2), (x1, 0, z1)], EDGE)
    s.face([(x, 0, z) for x, z in outline], EDGE)
    s.line([(13, 0, 68), (13, 0, 50), (31, 0, 50)], EDGE)

    fingerprint(s, -11, .01, 46, 11.5)
    for z, width in ((27, 38), (19, 32), (11, 24)):
        s.line([(-20, .01, z), (-20 + width, .01, z)], DETAIL)

    y = coin(s, 30, 5, 13, 13) + .01
    arrow(s, [(30, y, 21), (30, y, 6)], ink=BOLD, head=6)
