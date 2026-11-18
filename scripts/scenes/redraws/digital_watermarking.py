from geometry import DETAIL, EDGE, oval
from scenes.redraws._w5 import lens_outline, photo_print

DESCRIPTION = "Three circular drop seals run diagonally across a mountain photo print."


def draw(s):
    face = photo_print(s, width=72, height=53)
    s.line([face(8, 14), face(20, 26), face(29, 17), face(35, 21), face(46, 10)], EDGE)
    s.line([face(48, 10), face(58, 15), face(64, 11)], DETAIL)
    lens_outline(s, face, 58, 37, 4, EDGE)
    for x, z in ((18, 38), (35, 32), (51, 25)):
        lens_outline(s, face, x, z, 6.5, DETAIL)
        drop = [(0, 4), *oval(0, -.8, 2.55, 2.3, 155, 385, 24), (0, 4)]
        s.line([face(x + u, z + v) for u, v in drop], EDGE)
