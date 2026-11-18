from geometry import DETAIL, EDGE, oval, rounded
from scenes.redraws._w5 import printed_stroke

DESCRIPTION = "A buffet counter supports three chafing dishes with one, two, and three dots along its serving edge."


def chafing_dish(s, x, y, z):
    for dx in (2, 17):
        s.box(x + dx, y + 3, z, 2.5, 14, 4, .8)
    s.box(x, y, z + 4, 22, 20, 6, 2)
    s.solid(rounded(x, y, 22, 20, 2), z + 10, 7,
            rounded(x + 3, y + 3, 16, 14, 2), crease=False)
    s.tube([(x + 8, y + 10, z + 17), (x + 8, y + 10, z + 19.5),
            (x + 14, y + 10, z + 19.5), (x + 14, y + 10, z + 17)], .85)


def draw(s):
    s.box(2, 3, 0, 79, 26, 26, 2.5)
    s.box(0, 0, 25, 83, 33, 5, 2.1)
    for x in (3, 30.5, 58):
        chafing_dish(s, x, 3, 30)
    face = lambda x, z: (x, 33, z)
    for i, x in enumerate((14, 41.5, 69), 1):
        for j in range(i):
            center = x + 3.5 * (j - (i - 1) / 2)
            printed_stroke(s, face, oval(center, 27.5, 1.03, 1.03, count=15), EDGE)
    s.line([(7, 29, 5), (76, 29, 5)], DETAIL)
