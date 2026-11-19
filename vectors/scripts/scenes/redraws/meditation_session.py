from geometry import DETAIL, EDGE
from scenes.redraws._w4 import Surface

DESCRIPTION = "A round pleated meditation cushion with a stitched lotus rests on a square mat."


def draw(s):
    s.box(-44, -38, 0, 88, 76, 5, 10)
    s.disk(0, 0, 5, 32, 29, 17)
    s.ellipse(0, 0, 22, 28, 25, DETAIL)
    for x, y in ((29, 12), (23, 20), (16, 25), (7, 28), (-4, 28)):
        s.line([(x, y, 9), (x*.99, y*.99, 15)], DETAIL)
    top = Surface(s, lambda u, v: ((u + v)*.707, (v - u)*.707, 22))
    top.outline([(0, -13), (5, -7), (7, -2), (6, 3), (0, 8),
                 (-6, 3), (-7, -2), (-5, -7)], EDGE)
    for sign in (-1, 1):
        top.line([(sign*6, -3), (sign*12, -6), (sign*17, -6),
                  (sign*14, 1), (sign*7, 7), (0, 8)], EDGE)
        top.line([(sign*14, 2), (sign*21, 3), (sign*16, 9),
                  (sign*7, 11), (0, 8)], EDGE)
