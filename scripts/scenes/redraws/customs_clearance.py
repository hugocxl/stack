from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w1 import software_package, web_globe
from scenes.systems_shapes import bezel

DESCRIPTION = "A check badge overlaps the globe-marked customs label on a taped shipping carton."


def draw(s):
    software_package(s, 0, 0, 0, 1.18, show_code=False)
    y = 24.78
    bezel(s, -28, y, 6, 51, 28, EDGE, 1.5)
    web_globe(s, -16, y, 20, 8)
    for z, width in ((25, 19), (19, 14), (13, 20)):
        s.line([(-3, y, z), (-3 + width, y, z)], DETAIL)
    badge(s, "check", 29, y + 2, 31, 13)
