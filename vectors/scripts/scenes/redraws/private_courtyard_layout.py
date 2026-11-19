from geometry import DETAIL, EDGE, oval

DESCRIPTION = "Low perimeter walls enclose a courtyard with a paved walk around its central garden."


def draw(s):
    s.box(0, 0, 0, 86, 72, 5, 1)
    s.box(0, 0, 5, 86, 4, 24, 1)
    s.box(0, 4, 5, 4, 68, 24, 1)
    s.line([(34, 67, 5), (34, 57, 5), (15, 57, 5), (15, 14, 5),
            (71, 14, 5), (71, 57, 5), (52, 57, 5), (52, 67, 5)], EDGE)
    s.box(29, 23, 5, 27, 22, 3, 1)
    s.tube([(42, 33, 8), (42, 33, 25)], 1.4)
    crown = oval(42, 33, 12, 10)[:-1]
    tip = oval(42, 33, 5, 4)[:-1]
    s.solid(tip, 17, 8, top=crown, crease=False)
    s.solid(crown, 25, 10, top=tip, crease=False)
    s.line([(33, 39, 24), (41, 42, 22), (51, 40, 27)], DETAIL)
    for x, y in ((23, 20), (63, 18), (62, 47), (28, 49)):
        s.line([(x, y, 5), (x + 6, y, 5), (x + 6, y + 5, 5)], DETAIL)
    s.box(82, 4, 5, 4, 64, 8, 1)
    s.box(0, 68, 5, 34, 4, 8, 1)
    s.box(52, 68, 5, 34, 4, 8, 1)
