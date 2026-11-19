from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w2 import desk_calendar, rule

DESCRIPTION = "A circular sync badge overlaps a ring-bound shift calendar with availability blocks."


def draw(s):
    point = desk_calendar(s, active=None)
    for x, z in ((23, 49), (49, 21), (75, 49)):
        rule(s, point, x - 5, z, 10, EDGE)
    badge(s, "refresh", *point(96, 66), 15)
