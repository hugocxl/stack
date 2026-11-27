from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w4 import front_surface, upright
from scenes.redraws._w5 import pin_outline

DESCRIPTION = "A standing map pin contains a water bottle beneath a dispensing spout and droplet."


def draw(s):
    upright(s, pin_outline(0, 54, 30), 0, 7, angle=-33)
    pin = front_surface(s, angle=-33)
    pin.outline([(-7, 27), (-10, 30), (-10, 46), (-8, 50), (-4, 53), (-4, 57),
                 (4, 57), (4, 53), (8, 50), (10, 46), (10, 30), (7, 27)], EDGE)
    pin.rows(-9, 37, (18,), ink=DETAIL)
    pin.line([(-17, 69), (-5, 69), (-3, 67), (-3, 65), (3, 65),
              (3, 70), (0, 74), (-17, 74)], EDGE)
    pin.line([(-9, 74), (-9, 78), (-15, 78), (-4, 78)], EDGE)
    pin.outline([(0, 63), (-1.3, 61), (-.8, 59.5), (.8, 59.5), (1.3, 61)], BOLD)
