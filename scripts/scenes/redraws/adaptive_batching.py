from geometry import BOLD, DETAIL, EDGE, oval, rounded
from scenes.redraws._kit import coin
from scenes.redraws._w1 import upright_profile

DESCRIPTION = "A conveyor with a rotary size dial carries a two-carton batch and a three-carton batch."


def draw(s):
    s.box(-20, -29, 0, 40, 27, 29, 3)
    s.box(-23, -32, 0, 46, 33, 5, 2)
    belt = list(reversed(rounded(-53, 23, 106, 14, 7)))
    upright_profile(s, belt, 0, 32)
    rim = [(x, 0, z) for x, z in rounded(-50, 26, 100, 8, 4)]
    s.line(rim + rim[:1], DETAIL)
    for x in (-45, 45):
        s.line([(a, 0, b) for a, b in oval(x, 30, 4, 4, count=22)], EDGE)

    for left, count in ((-42, 3), (12, 2)):
        right = left + 13 * count
        s.face([(right, -28, 37), (right, -4, 37),
                (right, -4, 55), (right, -28, 55)], EDGE)
        s.face([(left, -4, 37), (right, -4, 37),
                (right, -4, 55), (left, -4, 55)], EDGE)
        s.face([(left, -28, 55), (right, -28, 55),
                (right, -4, 55), (left, -4, 55)], EDGE)
        for divider in range(1, count):
            seam = left + 13 * divider
            s.line([(seam, -28, 55), (seam, -4, 55), (seam, -4, 37)], EDGE)
        s.line([(left, -16, 55), (right, -16, 55)], DETAIL)

    coin(s, 0, 2, 15, 10, depth=4)
    s.line([(0, 2, 15), (4.5, 2, 19.5)], BOLD)
    s.line([(x, -2, z) for x, z in oval(0, 15, 13, 12, 23, 158, 18)], DETAIL)
