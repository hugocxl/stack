from math import cos, radians, sin

from geometry import DETAIL
from scenes.redraws._sf import BACK, person, plate, screen

DESCRIPTION = "Two thick rings overlap, and a member figure stands in the space they share."


def ring(r, w):
    return ([((r + w/2)*cos(radians(a)), (r + w/2)*sin(radians(a))) for a in range(0, 361, 4)] +
            [((r - w/2)*cos(radians(a)), (r - w/2)*sin(radians(a))) for a in range(360, -1, -4)])


def draw(s):
    at = screen()
    for u in (-26, 26):
        plate(s, lambda a, b, u=u: at(u + a, b), ring(40, 7), 5, BACK)
    person(s, at, 0, -1, 17)
