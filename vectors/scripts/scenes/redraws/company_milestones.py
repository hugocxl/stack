from geometry import DETAIL, EDGE

DESCRIPTION = "A timeline rail has three evenly spaced event ticks and a flag on the last milestone."


def draw(s):
    s.box(0, 0, 0, 106, 24, 13, 5)
    s.line([(15, 12, 13), (91, 12, 13)], EDGE)
    for x in (15, 53, 91):
        s.disk(x, 12, 13, 6.5, 6.5, 3, EDGE)
        s.line([(x, 24, 1), (x, 24, 10)], DETAIL)
    s.tube([(91, 12, 15), (91, 12, 64)], 1.7)
    s.face([(91, 12, 62), (118, 12, 56), (110, 12, 49), (118, 12, 42),
            (91, 12, 47)], EDGE)
