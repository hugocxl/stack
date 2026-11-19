from geometry import BOLD, DETAIL, EDGE, oval

DESCRIPTION = "A single tally tag hangs against a stack of square building tiles."


def draw(s):
    for z in (0, 8, 16, 24, 32):
        s.box(0, 0, z, 72, 60, 7, 1.2)
    s.line([(8, 10, 39), (62, 10, 39), (62, 50, 39)], DETAIL)
    tag = [(37, 30), (48, 30), (55, 24), (55, 5), (27, 5), (27, 24)]
    s.face([(x, 66, z) for x, z in tag], EDGE)
    s.line([(x, 66, z) for x, z in oval(42, 25, 2.3, 2.3)], DETAIL)
    s.tube([(38, 51, 39), (40, 62, 39), (41, 66, 31), (42, 66, 25)], 1.05)
    for x in (32, 38, 44, 50):
        s.line([(x, 66, 10), (x, 66, 19)], EDGE)
    s.line([(29, 66, 11), (53, 66, 18)], BOLD)
