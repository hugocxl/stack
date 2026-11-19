from geometry import DETAIL, EDGE
from scenes.redraws._w1 import upright_profile

DESCRIPTION = "An open public supply cabinet holds a tall milk carton and a handled detergent jug."


def draw(s):
    s.box(-29, -16, 0, 58, 38, 5, 1)
    s.box(-28, -16, 5, 56, 4, 75, 1, DETAIL)
    s.box(-29, -12, 5, 4, 34, 75, 1)
    jug = [(-15, 5), (-15, 21), (-12, 27), (-8, 29), (-8, 34), (0, 34),
           (0, 29), (12, 27), (16, 22), (16, 5)]
    handle = [(4, 20), (5, 25), (9, 24), (12, 22), (12, 19), (7, 19)]
    upright_profile(s, jug, 17, 19)
    s.line([(x, 17, z) for x, z in handle + handle[:1]], EDGE)
    s.line([(-9, 17, 12), (4, 17, 12)], DETAIL)
    s.box(-25, -12, 35, 50, 34, 4, 1)
    s.box(-13, -6, 39, 26, 23, 21, 1.2)
    s.face([(-13, 17, 60), (13, 17, 60), (13, 5, 67), (-13, 5, 67)], EDGE)
    s.face([(13, -6, 60), (13, 17, 60), (13, 5, 67)], EDGE)
    s.line([(-7, 17, 49), (6, 17, 49)], DETAIL)
    s.line([(-5, 17, 54), (4, 17, 54)], DETAIL)
    s.box(25, -12, 5, 4, 34, 75, 1)
    s.box(-30, -17, 80, 60, 40, 5, 1.5)
