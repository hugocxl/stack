from math import cos, radians, sin

from geometry import DETAIL, rounded

DESCRIPTION = "Three built-in chairs face a round team worktable with a shared plan at its center."


def chair(s, x, y, angle):
    c, q = cos(radians(angle)), sin(radians(angle))

    def place(u, v):
        return x + u*c - v*q, y + u*q + v*c

    s.box(x - 3.5, y - 3.5, 2, 7, 7, 12, 1.4)
    s.solid([place(u, v) for u, v in rounded(-12, -11, 24, 22, 3)], 14, 4)
    for u in (-9, 9):
        a, b = place(u, 8)
        s.box(a - 1.4, b - 1.4, 18, 2.8, 2.8, 15, .7, DETAIL)
    s.solid([place(u, v) for u, v in rounded(-12, 7, 24, 4, 1.2)], 29, 9)


def draw(s):
    seats = ((-30, -47, 180), (-24, 40, 0), (47, -4, -90))
    for x, y, _ in seats:
        s.tube([(0, 0, 2), (x, y, 2)], 2.4, DETAIL)
    chair(s, *seats[0])
    s.disk(0, 0, 0, 19, 19, 4, DETAIL)
    s.disk(0, 0, 4, 5, 5, 24)
    s.disk(0, 0, 28, 39, 35, 5)
    s.box(-11, -13, 33, 22, 26, 1, 1, DETAIL)
    for y, width in ((-6, 12), (0, 9), (6, 13)):
        s.line([(-6, y, 34), (-6 + width, y, 34)], DETAIL)
    for seat in seats[1:]:
        chair(s, *seat)
