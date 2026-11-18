from geometry import DETAIL, EDGE

DESCRIPTION = "A divided sorting tray groups round, square, and triangular tokens into three compartments."


def draw(s):
    s.box(0, 0, 0, 96, 81, 8, 5)
    # The bins share a single rim, with one full-width compartment in front.
    s.box(0, 0, 8, 96, 4, 9, 1)
    s.box(0, 3, 8, 4, 75, 9, 1)
    s.box(46, 4, 8, 4, 42, 7, 1)
    s.box(4, 42, 8, 89, 4, 7, 1)
    for x, y in ((15, 15), (32, 15), (23, 31)):
        s.disk(x, y, 8, 6, 6, 3, EDGE)
    for x, y in ((59, 10), (75, 10), (68, 25)):
        s.box(x, y, 8, 11, 11, 3, .8)
    for x, y in ((20, 60), (45, 64), (69, 58)):
        s.solid([(x, y - 7), (x + 7, y + 5), (x - 7, y + 5)], 8, 3, ink=EDGE)
    s.box(92, 3, 8, 4, 75, 9, 1)
    s.box(1, 77, 8, 94, 4, 9, 2)
    s.line([(9, 81, 5), (86, 81, 5)], DETAIL)
