from geometry import DETAIL, EDGE
from scenes.redraws._kit import coin
from scenes.redraws._w1 import web_globe

DESCRIPTION = "A container ship carries stacked freight containers and a globe emblem over its bow."


def draw(s):
    deck = [(-62, -13), (-55, -20), (43, -20), (68, 0), (43, 20),
            (-55, 20), (-62, 13)]
    keel = [(-57, -10), (-50, -16), (41, -16), (60, 0), (41, 16),
            (-50, 16), (-57, 10)]
    s.solid(keel, 0, 16, top=deck, crease=False)
    s.face([(x, y, 16) for x, y in deck], EDGE)
    s.line([(-57, 16, 5), (44, 17, 5), (61, 2, 5)], DETAIL)

    s.box(-53, -11, 16, 22, 22, 20, 2)
    s.box(-55, -13, 36, 26, 26, 10, 2)
    for x in (-49, -42, -35):
        s.line([(x, 13, 41), (x + 4, 13, 41)], EDGE)
    s.box(-48, -4, 46, 9, 8, 9, 1)

    for x, z in ((-26, 16), (7, 16), (-26, 29)):
        s.box(x, -15, z, 31, 30, 13, 1)
        for rib in range(x + 6, x + 30, 6):
            s.line([(rib, 15, z + 3), (rib, 15, z + 10)], DETAIL)

    x, z = 49, 44
    y = coin(s, x, 6, z, 19, depth=3)
    web_globe(s, x, y, z, 15)
