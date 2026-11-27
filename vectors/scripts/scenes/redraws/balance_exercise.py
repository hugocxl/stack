from math import cos, radians, sin

from geometry import DETAIL
from scenes.redraws._sf import lip, turned

DESCRIPTION = "A balance trainer: a soft half-dome sits on a round platform base."


def draw(s):
    turned(s, [(42, 0), (42, 7)], steps=1)
    dome = [(38*cos(radians(a)), 7 + 30*sin(radians(a))) for a in range(0, 91, 10)]
    turned(s, dome, steps=4)
    for a in (30, 55):
        r, z = 38*cos(radians(a)), 7 + 30*sin(radians(a))
        lip(s, 0, 0, z, r, DETAIL, -40, 130)
