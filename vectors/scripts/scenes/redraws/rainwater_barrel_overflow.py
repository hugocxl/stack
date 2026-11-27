from math import sqrt

from geometry import DETAIL, EDGE
from scenes.redraws._sf import lip, turned

DESCRIPTION = "A ribbon of water spills over the rim and down the side of a hooped rain barrel into a puddle."


def radius(z):
    return 26 + 4*(1 - ((z - 30)/30)**2)


def draw(s):
    s.ellipse(22, 22, 0, 26, 18, DETAIL)
    turned(s, [(26, 0), (29, 14), (30, 30), (29, 46), (26, 60)], steps=4)
    for z in (14, 46):
        lip(s, 0, 0, z, 29.2, DETAIL, -40, 130)
    lip(s, 0, 0, 60, 22, DETAIL, -40, 130)
    n = (1/sqrt(2), 1/sqrt(2))
    t = (1/sqrt(2), -1/sqrt(2))
    def at(z, w, out=1.2):
        r = radius(z) + out
        return (n[0]*r + t[0]*w, n[1]*r + t[1]*w, z)
    left = [at(z, -(6 + (60 - z)*.08)) for z in range(60, 1, -4)]
    right = [at(z, 6 + (60 - z)*.08) for z in range(2, 61, 4)]
    top = [(n[0]*20 + t[0]*w, n[1]*20 + t[1]*w, 61) for w in (6, -6)]
    s.face([top[1]] + left + right + [top[0]], EDGE)
