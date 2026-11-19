from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.systems_shapes import slider

DESCRIPTION = "Three sliders sit at the marked defaults on a control console with a reset badge."


def draw(s):
    s.box(-33, -26, 0, 66, 52, 10, 5)
    for y, position in ((-18, .31), (-3, .57), (12, .74)):
        slider(s, -24, y, 10, length=46, at=position)
        x = -24 + 46 * position
        s.line([(x, y + 9, 10), (x, y + 13, 10)], EDGE)
    s.line([(-19, 26, 5), (-5, 26, 5)], DETAIL)
    badge(s, "refresh", 29, -25, 14, 12)
