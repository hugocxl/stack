from geometry import BOLD, DETAIL, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w4 import front_surface

DESCRIPTION = "A tabletop announcement sign bears a megaphone and a clock badge."


def draw(s):
    sign = front_surface(s, angle=-14, y=14, z=4, lean=.48)
    heel = front_surface(s, angle=-14, y=-45)
    s.face([sign.at(82, 0), heel.at(82, 0), sign.at(82, 65)])
    sign.slab(rounded(0, 0, 82, 65, 4), 4)
    sign.outline([(39, 29), (55, 20), (55, 47), (39, 38), (24, 38), (24, 29)], BOLD)
    sign.line([(29, 29), (32, 18), (38, 18), (35, 29)])
    for a, b in (((60, 39), (65, 42)), ((61, 33), (67, 33)), ((60, 27), (65, 24))):
        sign.line([a, b], DETAIL)
    badge(s, "clock", *sign.at(80, 61), 15)
