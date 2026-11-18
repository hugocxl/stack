from geometry import DETAIL, rounded
from scenes.redraws._w5 import clamshell

DESCRIPTION = "A folded paper takeout carton stands beside a reusable molded clamshell."


def draw(s):
    base = rounded(5, 5, 25, 23, 2.5)
    top = rounded(0, 0, 35, 32, 2)
    s.solid(base, 0, 32, top=top, crease=False)
    s.face([(0, 16, 32), (0, 32, 32), (35, 32, 32), (35, 16, 32),
            (26, 13, 35), (9, 13, 35)])
    s.face([(0, 0, 32), (35, 0, 32), (35, 16, 32), (26, 19, 36),
            (9, 19, 36), (0, 16, 32)])
    s.line([(35, 7, 32), (30, 16, 8), (35, 25, 32)], DETAIL)
    s.line([(4, 32, 29), (11, 31, 22), (24, 31, 22), (31, 32, 29)], DETAIL)
    clamshell(s, 39, 10, scale=.91)
