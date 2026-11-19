from geometry import EDGE
from scenes.redraws.availability_by_region import location_pin
from scenes.redraws.platform_footprint import folded_map

DESCRIPTION = "A pierced location pin is planted at a street intersection on an upright folded map."


def draw(s):
    west, center, east = folded_map(s)
    west.line([(0, 18), (9, 21), (22, 24), (31, 35)], EDGE)
    west.line([(11, 53), (14, 41), (22, 24), (25, 15), (27, 7)], EDGE)
    center.line([(31, 35), (47, 37), (61, 30)], EDGE)
    center.line([(39, 9), (48, 19), (47, 37), (43, 51), (46, 56)])
    east.line([(61, 30), (74, 22), (93, 23)], EDGE)
    east.line([(68, 11), (74, 22), (79, 36), (86, 50)])
    east.line([(64, 40), (79, 36), (93, 40)])
    x, y, z = west.at(22, 24)
    location_pin(s, (x, y + .3, z), size=.96)
