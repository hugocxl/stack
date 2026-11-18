from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w2 import closed_outline, rule

DESCRIPTION = "A lock badge marks access to a vented storage locker with an inset door label."


def draw(s):
    s.box(-24, -15, 0, 48, 32, 78, 2)

    def door(x, z):
        return x, 17.1, z

    closed_outline(s, door, rounded(-19, 5, 38, 68, 2), EDGE)
    closed_outline(s, door, rounded(-8, 50, 16, 10, 1), DETAIL)
    rule(s, door, -4, 55, 8, DETAIL)
    for z in (11, 17, 63, 68):
        rule(s, door, -10, z, 20, EDGE)
    s.tube([(13, 17.3, 31), (13, 19.2, 31), (13, 19.2, 45), (13, 17.3, 45)], 1)
    badge(s, "lock", 28, 17, 61, 13)
