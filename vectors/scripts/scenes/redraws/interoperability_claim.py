from geometry import DETAIL, EDGE, oval, rounded

DESCRIPTION = "One adapter body joins a round socket to a projecting rectangular plug."


def draw(s):
    s.box(0, 0, 0, 59, 40, 33, 4)
    s.line([(x, 40, z) for x, z in oval(27, 16, 12, 12)], EDGE)
    for x, z in ((23, 19), (31, 19), (27, 12)):
        s.line([(a, 40, b) for a, b in oval(x, z, 1.65, 1.65, count=20)], EDGE)
    s.box(57, 7, 12, 29, 27, 10, 1.5)
    for y in (12, 24):
        s.face([(x, v, 22) for x, v in rounded(72, y, 7, 5, .8)], DETAIL)
    s.line([(86, 12, 17), (86, 29, 17)], DETAIL)
