from geometry import EDGE
from scenes.redraws._w1 import upright_profile

DESCRIPTION = "A curved streetlight carries a wrench-shaped service tag on its pole."


def draw(s):
    s.disk(-13, 0, 0, 8, 7, 4)
    s.tube([(-13, 0, 4), (-13, 0, 67), (-12, 0, 75), (-8, 0, 81),
            (0, 0, 84), (14, 0, 84)], 2.4, EDGE)
    s.box(9, -5, 80, 23, 10, 6, 3.1)
    s.line([(15, 5, 81), (26, 5, 81)], EDGE)
    wrench = [(-7, 32), (-9, 35), (-8, 39), (3, 50), (2, 55), (5, 61),
              (10, 63), (8, 57), (11, 54), (15, 55), (18, 60), (19, 55),
              (16, 50), (11, 48), (8, 48), (-3, 34)]
    upright_profile(s, wrench, 4, 3)
    s.line([(-14, 3, 40), (-6, 4, 40)], EDGE)
