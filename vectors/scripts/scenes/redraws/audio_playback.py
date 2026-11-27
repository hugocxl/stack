from math import cos, radians, sin

from geometry import DETAIL, EDGE
from scenes.redraws._sf import BACK, capsule, plate, screen

DESCRIPTION = "Over-ear headphones: a continuous padded headband joins two cushioned earcups."


def draw(s):
    at = screen()
    R = 46
    band = [at(R*cos(radians(a)), R*sin(radians(a))) for a in range(0, 181, 6)]
    s.tube([(x, y - 6, z) for x, y, z in band], 3.6, EDGE)
    s.tube(band, 4.4, EDGE)
    for side in (-1, 1):
        cup = lambda u, v, side=side: at(side*R + u, v)
        plate(s, lambda u, v: cup(u - 12, v - 40), capsule(24, 42), 12, BACK)
        plate(s, lambda u, v: cup(u - 8, v - 36), capsule(16, 34), 3, (0, 1, 0), rim=False)
        s.line([cup(-4 + a, -19 + b) for a, b in []] or [cup(0, -32), cup(0, -8)], DETAIL)
