from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w1 import code_brackets

DESCRIPTION = "An open developer manual has text lines on one page and a large code bracket symbol on the other."


def draw(s):
    s.box(-49, -28, 0, 98, 56, 4, 2)
    for direction in (-1, 1):
        s.face([(0, 27, 4), (direction * 47, 27, 4), (direction * 47, 27, 16),
                (direction * 22, 27, 13), (0, 27, 5)], EDGE)
        s.face([(0, -27, 5), (direction * 22, -27, 13), (direction * 47, -27, 16),
                (direction * 47, 27, 16), (direction * 22, 27, 13), (0, 27, 5)], EDGE)
        s.line([(direction * 9, 27, 6), (direction * 23, 27, 10),
                (direction * 46, 27, 13)], DETAIL)
    for y, end in ((-15, -10), (-6, -13), (3, -10), (12, -18)):
        s.line([(-40, y, 15.2), (-22, y, 13), (end, y, 5 - end * 8 / 22)], DETAIL)
    code_brackets(s, lambda u, v: (26 + u, -v, 13 + u * .15), 18, BOLD)
