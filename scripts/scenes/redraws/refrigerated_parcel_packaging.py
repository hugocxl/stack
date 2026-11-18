from math import cos, radians, sin

from geometry import DETAIL, EDGE, rounded
from scenes.systems_shapes import rectangle

DESCRIPTION = "A flat ice pack with a snowflake rests inside the fitted foam liner of an open shipping carton."


def draw(s):
    left, right, back, front, rim = -33, 33, -24, 24, 29
    s.face([(left, back, rim), (right, back, rim), (right, -31, 64), (left, -31, 64)], EDGE)
    s.line([(-28, -29, 59), (28, -29, 59), (28, -25, 34), (-28, -25, 34), (-28, -29, 59)], DETAIL)
    s.box(-29, -20, 0, 58, 40, 10, 3, DETAIL)
    s.face([(-25, -16, 10), (25, -16, 10), (25, -16, 27), (-25, -16, 27)], DETAIL)
    s.face([(-25, -16, 10), (-25, 16, 10), (-25, 16, 27), (-25, -16, 27)], DETAIL)

    s.box(-23, -14, 10, 46, 28, 12, 4)
    rectangle(s, -19, -11, 22, 38, 22, DETAIL, 3)
    for angle in (0, 60, 120, 180, 240, 300):
        a = radians(angle)
        for offset in (-1, 1):
            b = a + offset * .76
            s.line([(8 * cos(a), 8 * sin(a), 22),
                    (8 * cos(a) - 3 * cos(b), 8 * sin(a) - 3 * sin(b), 22)], EDGE)
        s.line([(0, 0, 22), (8 * cos(a), 8 * sin(a), 22)], EDGE)

    hole = [(*point, rim) for point in rounded(-25, -16, 50, 32, 3)]
    s.face([(left, back, rim), (right, back, rim), (right, front, rim), (left, front, rim)],
           EDGE, openings=(hole,))
    s.face([(right, back, 0), (right, front, 0), (right, front, rim), (right, back, rim)], EDGE)
    s.face([(left, front, 0), (right, front, 0), (right, front, rim), (left, front, rim)], EDGE)
    s.line([(-25, front, rim - 5), (25, front, rim - 5)], DETAIL)
