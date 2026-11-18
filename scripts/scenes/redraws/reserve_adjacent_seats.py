from geometry import BOLD, DETAIL, rounded

DESCRIPTION = "One pair of high-backed rail seats shares a pedestal and a continuous reservation outline."


def draw(s):
    boundary = rounded(-5, -7, 77, 56, 8)
    s.line([(x, y, 0) for x, y in boundary + boundary[:1]], BOLD)

    # One frame supports a matched double seat.
    s.box(22, 15, 0, 25, 16, 4, 2)
    s.box(26, 18, 4, 17, 10, 16, 2)
    s.box(2, 3, 19, 62, 37, 5, 3)
    for x in (4, 35):
        s.box(x, 1, 23, 29, 9, 46, 4)
        s.box(x + 3, 9, 53, 23, 2.5, 12, 3, DETAIL)
        s.box(x, 8, 24, 29, 30, 7, 4)
    for x in (3, 33.5, 64):
        s.tube([(x, 34, 24), (x, 34, 40), (x, 12, 40)], 1.55)
