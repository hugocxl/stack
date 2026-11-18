from geometry import DETAIL, EDGE
from scenes.redraws._w1 import rain_barrel

DESCRIPTION = "An elbowed downspout turns into the lid of a rain barrel."


def draw(s):
    rain_barrel(s, capped=True)
    s.ellipse(-9, -3, 55, 7.5, 7.5, EDGE)
    s.tube([(-9, -3, 56), (-9, -3, 64), (-9, -4, 68), (-9, -8, 71),
            (-9, -22, 71), (-9, -30, 74), (-9, -32, 80), (-9, -32, 99)], 5.5)
    s.ellipse(-9, -32, 99, 6.1, 6.1, EDGE)
    s.ellipse(-9, -32, 99, 3.9, 3.9, DETAIL)
    s.line([(-14, -3, 60), (-8, 3, 60), (-4, 1, 60)], DETAIL)
