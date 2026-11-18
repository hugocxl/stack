from geometry import DETAIL, EDGE, oval
from scenes.redraws._w1 import upright_profile

DESCRIPTION = "A work boot has a raised pull strap, laces, and a thick tread sole."


def draw(s):
    sole = [(-41, 5), (-38, 1), (37, 1), (42, 4), (42, 9), (37, 12), (-41, 12)]
    upper = [(-38, 11), (-37, 51), (-34, 57), (-12, 57), (-8, 53),
             (-5, 36), (0, 29), (25, 25), (34, 21), (39, 14), (39, 11)]
    s.tube([(-34, 5, 54), (-39, 5, 63), (-44, 5, 63), (-45, 5, 58), (-37, 5, 47)], 2.2)
    upright_profile(s, sole[::-1], 14, 31)
    upright_profile(s, upper, 13, 28)
    s.line([(-35, 8, 57), (-15, 8, 57), (-13, -10, 57), (-34, -10, 57)], DETAIL)
    s.line([(-35, 13, 29), (-22, 13, 28), (-16, 13, 23), (-15, 13, 12)], DETAIL)
    for x, z in ((-14, 47), (-10, 39), (-5, 32)):
        s.line([(a, 13, b) for a, b in oval(x, z, 2, 2, count=20)], EDGE)
        s.line([(x, 13, z), (x + 5, 8, z + 2)], EDGE)
    for x in (-30, -17, -4, 9, 22, 35):
        s.line([(x, 14, 2), (x, 14, 6)], DETAIL)
