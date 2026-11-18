from geometry import DETAIL, EDGE
from scenes.redraws._w1 import rain_barrel

DESCRIPTION = "A broad ribbon of water spills over the rim and down the side of a rain barrel."


def draw(s):
    rain_barrel(s, capped=False)
    s.line([(-12, 3, 54), (-3, 1, 54), (5, 3, 54), (13, 2, 54)], DETAIL)
    s.line([(-8, -6, 54), (0, -8, 54), (8, -6, 54)], DETAIL)
    s.face([(7, 16, 54), (16, 11, 54), (21, 16, 52), (24, 20, 46),
            (25, 22, 31), (29, 24, 16), (34, 25, 5), (25, 31, 5),
            (20, 28, 14), (18, 26, 32), (16, 24, 44), (13, 21, 50)], EDGE)
    s.line([(20, 23, 42), (22, 25, 27), (23, 28, 17)], DETAIL)
    s.ellipse(28, 27, 1, 13, 8, DETAIL, -15, 155)
    s.line([(33, 30, 5), (37, 31, 8)], DETAIL)
    s.line([(22, 32, 4), (20, 36, 6)], DETAIL)
