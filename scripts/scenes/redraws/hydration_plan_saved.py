from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w4 import desk_calendar

DESCRIPTION = "A water drop heads a wire-bound hydration calendar with a check badge on its upper corner."


def draw(s):
    calendar = desk_calendar(s)
    calendar.outline([(47, 77), (42, 71), (40, 67), (41, 63), (44, 61),
                      (50, 61), (53, 63), (54, 67), (52, 71)], EDGE)
    badge(s, "check", *calendar.at(92, 64), 14)
