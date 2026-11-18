from geometry import BOLD, DETAIL
from scenes.redraws._kit import badge
from scenes.redraws._w4 import bezier_path
from scenes.redraws.platform_footprint import folded_map

DESCRIPTION = "An upright folded local map carries a prominent location pin and a check badge."


def draw(s):
    west, center, east = folded_map(s)
    west.line([(0, 49), (14, 46), (22, 32), (31, 31)], DETAIL)
    west.line([(6, 12), (19, 17), (22, 32)], DETAIL)
    center.line([(31, 31), (41, 27), (54, 17), (61, 18)], DETAIL)
    east.line([(61, 18), (74, 23), (93, 21)], DETAIL)
    east.line([(72, 12), (74, 23), (68, 40), (93, 48)], DETAIL)
    location = bezier_path((46, 23), ((39, 32), (32, 39), (32, 48)),
                           ((32, 67), (60, 67), (60, 48)),
                           ((60, 39), (53, 32), (46, 23)))
    center.line(location, BOLD)
    center.oval(46, 48, 5, 5, BOLD)
    badge(s, "check", *east.at(90, 40), 14)
