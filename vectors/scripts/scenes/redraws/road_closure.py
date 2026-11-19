from geometry import BOLD, DETAIL, EDGE

DESCRIPTION = "A striped roadwork barricade spans both lanes of a short road segment."


def draw(s):
    for y in (1, 47):
        s.line([(0, y, 0), (76, y, 0)], EDGE)
    for x in (1, 13, 25, 48, 61, 73):
        s.line([(x, 24, 0), (min(x + 7, 76), 24, 0)], DETAIL)
    for y in (6, 42):
        s.box(29, y - 2, 0, 16, 4, 2, .7)
        s.box(34, y - 1.5, 2, 4, 3, 25, 1)
    s.box(33, 1, 15, 7, 47, 11, 1.5, BOLD)
    for y in (3, 11, 19, 27, 35, 43):
        s.line([(40, y, 16), (40, y + 4, 24.5)], EDGE)
