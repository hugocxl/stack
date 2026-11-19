from geometry import BOLD, DETAIL, oval
from scenes.redraws._w1 import upright_profile

DESCRIPTION = "A currency symbol is engraved in the round face of a location pin."


def draw(s):
    outline = [(0, 0), *oval(0, 51, 29, 29, 224, -44, 44)]
    upright_profile(s, outline, 3, 8)
    s.line([(a, 3, b) for a, b in oval(0, 51, 22, 22, count=56)], DETAIL)
    stroke = [(11, 61), (6, 64), (-2, 65), (-9, 62), (-11, 57), (-7, 53),
              (-1, 51), (6, 49), (10, 46), (10, 42), (7, 38), (0, 37),
              (-7, 39), (-11, 43)]
    s.line([(x, 3, z) for x, z in stroke], BOLD)
    s.line([(0, 3, 32), (0, 3, 70)], BOLD)
