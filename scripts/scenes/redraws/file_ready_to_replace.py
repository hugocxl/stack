from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w3 import sheet

DESCRIPTION = "A foreground file with a clock badge overlaps an offset file behind it."


def draw(s):
    sheet(s, 60, 73, origin=(0, -2, 5), depth=4)
    front = sheet(s, 60, 73, origin=(22, 5, 0), depth=4)
    front.rules(10, 49, [24], ink=EDGE)
    front.rules(10, 37, [37, 32, 21], gap=8, ink=DETAIL)
    badge(s, "clock", *front.point(58, 14, -4), 14)
