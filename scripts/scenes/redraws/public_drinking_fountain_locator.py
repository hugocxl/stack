from geometry import EDGE, oval
from scenes.redraws._w1 import upright_profile

DESCRIPTION = "A pedestal drinking fountain sends a water arc into its basin beside a map pin."


def draw(s):
    s.box(-13, -12, 0, 26, 24, 33, 4)
    s.box(-27, -21, 33, 54, 42, 6, 8)
    s.ellipse(0, 0, 39, 23, 16, EDGE)
    s.ellipse(1, 2, 39, 3, 2.6, EDGE)
    s.tube([(-17, -6, 39), (-17, -6, 45), (-13, -5, 49)], 2.3)
    s.line([(-13 + 16 * t / 24, -5 + 7 * t / 24,
             49 - 10 * (t / 24) ** 2 + 17 * (t / 24) * (1 - t / 24))
            for t in range(25)], EDGE)
    pin = [(29, 25), *oval(29, 47, 12, 12, 220, -40, 36)]
    upright_profile(s, pin, -9, 3)
    s.line([(x, -9, z) for x, z in oval(29, 47, 5, 5, count=28)], EDGE)
