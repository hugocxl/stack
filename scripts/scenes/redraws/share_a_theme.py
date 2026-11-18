from math import cos, radians, sin

from geometry import EDGE, rounded
from scenes.redraws._kit import arrow
from scenes.redraws._w3 import Surface

DESCRIPTION = "Three paint-swatch leaves fan out from a rivet, with a share arrow pointing away from the fan."


def draw(s):
    # The strips hide the share arrow until it clears the fan.
    x, y, z = 16, 2, 28
    arrow(s, [(x, y, z), (x + 26, y - 26, z)], EDGE, head=12)
    for angle, depth in ((-20, 8), (15, 4), (49, 0)):
        a = radians(angle)
        strip = Surface(s, (0, -depth, 19), rise=(-.48, .88),
                        across=(.98, -.18), back=(0, -1, 0))

        def turn(x, z):
            return (x * cos(a) - z * sin(a), x * sin(a) + z * cos(a))

        strip.plate([turn(x, z) for x, z in rounded(-12, -18, 24, 91, 5)], 4)
        for z in (20, 39, 57):
            strip.stroke([turn(x, v) for x, v in rounded(-7, z, 14, 11, 2)],
                         EDGE, closed=True)
    strip.oval(0, 0, 3.4, 3.4, EDGE)
