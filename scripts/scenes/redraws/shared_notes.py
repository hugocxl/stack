from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w2 import closed_outline, open_volume, profile_mark, rule, upright_face

DESCRIPTION = "A nameplate bearing two profile seals clips onto the upper corner of an open lined notebook."


def draw(s):
    left, right = open_volume(s)
    for leaf in (left, right):
        for z, length in ((53, 31), (42, 34), (31, 34), (20, 26), (9, 28)):
            rule(s, leaf, 10, z, length, EDGE if z == 53 else DETAIL)

    a, b, c = right(49, 58)

    def plate(x, z):
        return a + .57*x, b - .43*x + 2, c + .93*z

    upright_face(s, plate, rounded(-19, -9, 45, 30, 4), 4)
    closed_outline(s, plate, rounded(-3, 14, 13, 3, 1.5), EDGE)
    for x in (-7, 14):
        profile_mark(s, plate, x, 3, 11)
