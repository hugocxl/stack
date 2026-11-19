from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w1 import upright_profile

DESCRIPTION = "A standing accession card shows a museum vase above two lines of catalog information."


def draw(s):
    outline = [(-31, 0), (-31, 52), (-15, 52), (-12, 61), (9, 61),
               (12, 52), (31, 52), (31, 0)]
    upright_profile(s, outline, 0, 10)
    half = [(0, 47), (8, 47), (8, 44), (5, 44), (5, 41), (9, 37),
            (13, 34), (15, 29), (14, 24), (11, 20), (7, 17), (0, 17)]
    vase = half + [(-x, z) for x, z in reversed(half[1:-1])]
    s.line([(x, 0, z) for x, z in vase + vase[:1]], BOLD)
    s.line([(-8, 0, 44), (8, 0, 44)], DETAIL)
    for z, width in ((10, 33), (5, 24)):
        s.line([(-16, 0, z), (-16 + width, 0, z)], EDGE)
