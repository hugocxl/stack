from geometry import DETAIL, EDGE
from scenes.redraws._w4 import Surface

DESCRIPTION = "A stack of three books has a bookplate with a fountain pen nib on the top volume."


def draw(s):
    for x, y, z, w, d in ((0, 0, 0, 96, 68), (5, 4, 18, 89, 63), (5, 9, 36, 83, 58)):
        s.box(x, y, z, w, d, 18, 3)
        for h in (4, 14):
            s.line([(x + 4, y + d, z + h), (x + w - 4, y + d, z + h)], DETAIL)
        s.line([(x + 7, y + 3, z + 18), (x + 7, y + d - 2, z + 18)], EDGE)
    cover = Surface(s, lambda u, v: (u, v, 54))
    cover.frame(29, 17, 46, 43, 4, EDGE)
    cover.outline([(50, 23), (39, 38), (46, 51), (56, 51), (63, 38)], EDGE)
    cover.line([(50, 23), (51, 38)], EDGE)
    cover.oval(51, 40, 2.3, 2.3, EDGE)
