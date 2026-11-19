from math import cos, radians, sin

from geometry import DETAIL, EDGE
from scenes.redraws._w5 import rect

DESCRIPTION = "A snowflake-marked chest freezer sits in an outlined kitchen appliance bay beside the sink counter."


def draw(s):
    s.box(0, 0, 0, 83, 55, 3, 1)
    s.box(0, 0, 3, 83, 3, 39, 1)
    s.box(0, 3, 3, 3, 51, 39, 1)
    top = lambda x, y: (x, y, 3.1)
    for points in ([(35, 13), (35, 49), (78, 49), (78, 13)],
                   [(40, 13), (75, 13)]):
        s.line([top(x, y) for x, y in points], EDGE, dashed=True)
    s.box(4, 4, 3, 27, 39, 28, 1)
    s.box(3, 3, 30, 30, 42, 4, 1.6)
    rect(s, lambda x, y: (x, y, 34), 8, 16, 18, 20, 4, EDGE)
    s.tube([(17, 11, 34), (17, 11, 43), (17, 14, 46),
            (17, 20, 46), (17, 22, 43)], 1.25)
    s.face([(7, 43, 7), (7, 43, 27), (28, 43, 27), (28, 43, 7)], DETAIL)
    s.line([(12, 43, 22), (20, 43, 22)], DETAIL)
    s.box(39, 16, 3, 34, 27, 28, 2.6)
    s.box(38, 15, 29, 36, 29, 5, 3)
    s.tube([(48, 44, 27), (48, 47, 27), (63, 47, 27), (63, 44, 27)], 1.3)
    # Engrave the freezer symbol directly into the closed lid.
    for angle in range(0, 360, 60):
        theta = radians(angle)
        x, y = cos(theta), sin(theta)
        s.line([(56, 29, 34), (56+6.5*x, 29+6.5*y, 34)], EDGE)
        for direction in (-1, 1):
            s.line([(56+4*x, 29+4*y, 34),
                    (56+6*x-direction*2*y, 29+6*y+direction*2*x, 34)], DETAIL)
    for z in (8, 11, 14):
        s.line([(73, 24, z), (73, 35, z)], DETAIL)
