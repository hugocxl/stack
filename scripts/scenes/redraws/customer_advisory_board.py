from math import hypot

from geometry import DETAIL, EDGE, rounded

DESCRIPTION = "Three inward-facing seats attach to a shared round discussion table."


def seat(s, x, y):
    distance = hypot(x, y)
    dx, dy = x / distance, y / distance

    def place(u, v, z):
        return x - u*dy + v*dx, y + u*dx + v*dy, z

    s.tube([place(0, 0, 5), place(0, 0, 17)], 2.9)
    cushion = [place(u, v, 0)[:2] for u, v in rounded(-11, -9, 22, 19, 3)]
    s.solid(cushion, 16, 4)
    for u in (-8, 8):
        s.tube([place(u, 7, 19), place(u, 10, 32)], 1.55)
    s.face([place(u, 10, v) for u, v in rounded(-11, 27, 22, 13, 4)], EDGE)


def draw(s):
    seats = ((-29, -30), (-17, 40), (42, -6))
    for x, y in seats:
        s.tube([(0, 0, 6), (x, y, 6)], 2.4, DETAIL)
    seat(s, *seats[0])
    s.disk(0, 0, 0, 12, 12, 8, DETAIL)
    s.disk(0, 0, 8, 4.6, 4.6, 21)
    s.disk(0, 0, 29, 31, 31, 5)
    for location in seats[1:]:
        seat(s, *location)
