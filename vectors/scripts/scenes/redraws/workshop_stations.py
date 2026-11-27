from geometry import EDGE

DESCRIPTION = "Three workbenches stand in a row on the workshop floor, each with a vise clamped to its top."


def bench(s, x, y):
    for dx, dy in ((3, 3), (39, 3), (3, 21), (39, 21)):
        s.tube([(x + dx, y + dy, 0), (x + dx, y + dy, 26)], 1.4, EDGE)
    s.box(x + 2, y + 2, 8, 38, 20, 2, 1)
    s.box(x, y, 26, 42, 24, 4, 1.5)
    s.box(x + 28, y + 4, 30, 10, 14, 7, 1.5)
    s.tube([(x + 33, y + 18, 33.5), (x + 33, y + 24, 33.5)], .9, EDGE)


def draw(s):
    for i in range(3):
        bench(s, -84 + i*54, -12)
