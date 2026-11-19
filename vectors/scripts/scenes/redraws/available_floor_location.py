from geometry import EDGE

DESCRIPTION = "A cutaway building exposes one empty middle floor between occupied stories, with dashes tracing the vacant bay."


def draw(s):
    s.box(0, 0, 0, 76, 42, 35, 1)
    s.box(0, 0, 34, 76, 7, 32, 1)
    s.box(0, 7, 34, 6, 35, 32, 1)
    s.box(71, 34, 34, 5, 8, 32, 1)
    s.box(0, 0, 63, 76, 42, 33, 1)
    for z in (9, 71):
        for x in (10, 33, 56):
            s.box(x, 42, z, 11, 1.1, 15, 1, EDGE)
    s.line([(8, 43, 39), (68, 43, 39), (68, 43, 59), (8, 43, 59), (8, 43, 39)],
           EDGE, dashed=True)
    s.box(-2, -2, 95, 80, 46, 4, 1)
