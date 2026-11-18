from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import badge

DESCRIPTION = "A ribboned gift box sits open with a plus badge at its opening."


def draw(s):
    # The tilted lid rests across the side walls, leaving the front of the box open.
    s.face([(-29, -22, 0), (29, -22, 0), (29, -22, 26), (-29, -22, 26)], DETAIL)
    s.face([(-29, -22, 0), (-29, 22, 0), (-29, 22, 26), (-29, -22, 26)], EDGE)

    def lid(x, y):
        return x, y, 30 + (-4 - y) * 24 / 34

    s.face([(-31, -4, 26), (31, -4, 26), lid(31, -4), lid(-31, -4)], EDGE)
    s.face([(31, -38, 50), (31, -4, 26), lid(31, -4), lid(31, -38)], EDGE)
    s.face([lid(x, y) for x, y in ((-31, -38), (31, -38), (31, -4), (-31, -4))], EDGE)
    for x in (-5, 5):
        s.line([lid(x, -38), lid(x, -25)], DETAIL)
        s.line([lid(x, -16), lid(x, -4), (x, -4, 26)], DETAIL)

    # Two ribbon loops meet at a small knot on the lid.
    for center, start, end in ((-8, 18, 342), (8, 198, 522)):
        loop = oval(center, -22, 8, 4, start, end, 28)
        s.line([lid(0, -22), *(lid(x, y) for x, y in loop), lid(0, -22)], EDGE)
    s.line([lid(-9, -14), lid(0, -22), lid(10, -15)], EDGE)
    knot = oval(0, -22, 2.1, 1.7, count=20)[:-1]
    s.face([lid(x, y) for x, y in knot], EDGE)

    s.face([(29, -22, 0), (29, 22, 0), (29, 22, 26), (29, -22, 26)], EDGE)
    s.face([(-29, 22, 0), (29, 22, 0), (29, 22, 26), (-29, 22, 26)], EDGE)
    for x in (-5, 5):
        s.line([(x, 22, 0), (x, 22, 26)], DETAIL)

    badge(s, "plus", 28, 9, 31, 11)
