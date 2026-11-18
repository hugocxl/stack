from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import badge
from scenes.redraws._w1 import upright_profile

DESCRIPTION = "A sawtooth-roof factory with a leaf emblem carries a down-arrow badge beside its chimney."


def draw(s):
    s.solid(oval(-17, -7, 10, 10)[:-1], 16, 60,
            top=oval(-17, -7, 7, 7)[:-1], crease=False)
    s.disk(-17, -7, 75, 8.2, 8.2, 3)
    s.ellipse(-17, -7, 78, 5, 5, DETAIL)
    profile = [(-34, 0), (-34, 28), (-10, 42), (-10, 28), (14, 42),
               (14, 28), (35, 41), (35, 0)]
    upright_profile(s, profile, 15, 34)
    for x in (-26, -11):
        s.line([(x, 15, 9), (x + 8, 15, 9), (x + 8, 15, 21),
                (x, 15, 21), (x, 15, 9)], DETAIL)
    leaf = []
    for side in (1, -1):
        for i in range(25):
            t = i / 24 if side == 1 else 1 - i / 24
            bulge = side * 9 * t * (1 - t) * 4
            leaf.append((5 + 22*t - .48*bulge, 15, 7 + 21*t + .75*bulge))
    s.line(leaf, EDGE)
    s.line([(1, 15, 4), (19, 15, 20)], DETAIL)
    badge(s, "down", 3, -9, 76, 13)
