from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w1 import file_card

DESCRIPTION = "A folded-corner terms sheet carries a check badge at its signature line."


def draw(s):
    file_card(s, -31, 0, w=62, h=67, depth=5)
    s.line([(-23, 0, 55), (-1, 0, 55)], EDGE)
    for z, end in ((44, 18), (37, 13), (30, 19)):
        s.line([(-23, 0, z), (end, 0, z)], DETAIL)
    s.line([(-23, 0, 10), (22, 0, 10)], EDGE)
    stroke = [(-18, 13), (-15, 20), (-12, 22), (-11, 19), (-13, 14),
              (-9, 16), (-5, 18), (-3, 15), (1, 17), (7, 17)]
    s.line([(x, 0, z) for x, z in stroke], EDGE)
    badge(s, "check", 28, 0, 12, 12)
