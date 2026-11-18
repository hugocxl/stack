from geometry import BOLD, DETAIL
from scenes.redraws._kit import arrow
from scenes.redraws._w1 import flatbed_truck

DESCRIPTION = "A directional arrow runs from a raised loading dock into the level bed of a freight truck."


def draw(s):
    flatbed_truck(s, -8, 0, 1)
    s.box(-49, -24, 0, 41, 48, 20, 1.7)
    for y in (-18, 14):
        s.box(-8, y, 8, 3, 4, 8, .7)
    for y in (-12, 12):
        s.line([(-44, y, 20), (-15, y, 20)], DETAIL)
    arrow(s, [(-41, 5, 20), (9, 5, 20)], BOLD, head=9)
