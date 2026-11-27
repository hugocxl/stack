from math import cos, radians, sin

from geometry import DETAIL, EDGE
from scenes.redraws._sf import lip, turned

DESCRIPTION = "A still desk bell rests on its round base with the plunger raised."


def draw(s):
    turned(s, [(31, 0), (31.4, 1.2), (31.4, 11), (30.2, 12.4)], steps=3)
    lip(s, 0, 0, 1.2, 30.8, DETAIL, -40, 130)
    dome = [(27*cos(radians(a)), 12.4 + 27*sin(radians(a))) for a in range(0, 91, 10)]
    turned(s, dome, steps=4)
    s.tube([(0, 0, 38), (0, 0, 46)], 1.5, EDGE)
    turned(s, [(4.4, 45.6), (5.4, 47.2), (5, 49.4), (2.8, 50.8), (.4, 51)])
