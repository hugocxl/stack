from geometry import DETAIL, EDGE
from scenes.redraws._w1 import upright_profile
from scenes.systems_shapes import bezel

DESCRIPTION = "A pencil touches the personalization field under a T-shirt thumbnail on a standing product order card."


def draw(s):
    s.face([(-28, -6, 28), (28, -6, 28), (28, -23, 0), (-28, -23, 0)], EDGE)
    s.box(-33, -6, 0, 66, 6, 69, 2.8)
    bezel(s, -25, 0, 31, 50, 30, DETAIL, 2)
    shirt = [(-6, 56), (-15, 51), (-11, 44), (-7, 46), (-7, 35),
             (7, 35), (7, 46), (11, 44), (15, 51), (6, 56), (3, 53), (-3, 53)]
    s.line([(x, 0, z) for x, z in shirt + shirt[:1]], EDGE)
    bezel(s, -25, 0, 9, 50, 14, EDGE, 2)
    s.line([(-19, 0, 15), (-5, 0, 15)], DETAIL)

    upright_profile(s, [(3, 15), (7, 25), (30, 54), (36, 49), (13, 20)], 3, 2.3)
    for a, b in (((7, 25), (13, 20)), ((26, 49), (32, 44)), ((11, 22.5), (29, 46))):
        s.line([(x, 3, z) for x, z in (a, b)], DETAIL)
