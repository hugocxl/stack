from geometry import BOLD, DETAIL, EDGE
from scenes.systems_shapes import bezel

DESCRIPTION = "A weatherproof monitoring cabinet shows an upward measurement trend in its built-in instrument window."


def draw(s):
    for x in (-22, 15):
        s.box(x, -7, 0, 8, 15, 20, 1)
    s.box(-29, -17, 12, 58, 34, 58, 4)
    s.box(-31, -19, 68, 62, 38, 5, 2)
    bezel(s, -23, 17, 28, 46, 34, EDGE, 2)
    s.line([(-17, 17, 55), (-17, 17, 34), (17, 17, 34)], DETAIL)
    s.line([(-14, 17, 38), (-7, 17, 43), (-1, 17, 40), (8, 17, 50),
            (13, 17, 48), (18, 17, 55)], BOLD)
    s.line([(-13, 17, 21), (-5, 17, 21)], EDGE)
    s.line([(5, 17, 21), (13, 17, 21)], EDGE)
    for z in (57, 52, 47):
        s.line([(29, -8, z), (29, 7, z)], DETAIL)
