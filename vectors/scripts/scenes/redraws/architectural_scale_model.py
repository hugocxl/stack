from geometry import DETAIL, EDGE

DESCRIPTION = "A cutaway architectural model on a thin display base contains a miniature sofa and table."


def draw(s):
    s.box(-41, -32, 0, 82, 64, 5, 1.5)
    s.box(-38, -29, 5, 76, 58, 3, 1)
    s.box(-38, -29, 8, 4, 58, 40, .75)
    window = [(1, -25, 25), (31, -25, 25), (31, -25, 41), (1, -25, 41)]
    s.face([(-34, -25, 8), (38, -25, 8), (38, -25, 48), (-34, -25, 48)],
           openings=(window,))
    s.line([(-34, -29, 48), (38, -29, 48), (38, -25, 48)], EDGE)
    s.line([(16, -25, 25), (16, -25, 41)], DETAIL)

    s.box(-27, -13, 8, 17, 37, 8, 3)
    s.box(-29, -14, 12, 6, 39, 12, 2)
    for y in (-15, 19):
        s.box(-24, y, 12, 15, 6, 7, 2)
    s.line([(-22, 4, 16), (-11, 4, 16)], DETAIL)

    for x, y in ((10, -3), (27, -3), (10, 12), (27, 12)):
        s.tube([(x, y, 8), (x, y, 15)], 1, EDGE)
    s.box(7, -6, 15, 23, 21, 3, 4)
