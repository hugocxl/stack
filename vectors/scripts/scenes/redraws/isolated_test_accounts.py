from geometry import EDGE, rounded
from scenes.redraws._w5 import avatar_mark, identity_card

DESCRIPTION = "An ID card bearing a laboratory flask sits inside a dashed isolation boundary."


def draw(s):
    boundary = rounded(-10, -8, 91, 65, 6)
    s.line([(x, -.15 * z, z) for x, z in boundary + boundary[:1]], EDGE, dashed=True)
    face = identity_card(s)
    avatar_mark(s, face, 21, 23, 1.52)
    s.line([face(x, z) for x, z in ((48, 34), (57, 34), (55, 34), (55, 27),
                                   (62, 15), (60, 12), (45, 12), (43, 15),
                                   (50, 27), (50, 34))], EDGE)
    s.line([face(46, 20), face(59, 20)], EDGE)
