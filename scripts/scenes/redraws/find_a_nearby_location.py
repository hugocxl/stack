from geometry import DETAIL, EDGE, oval
from scenes.redraws._w5 import folded_point, location_pin, map_stroke, standing_map

DESCRIPTION = "A folded neighborhood map shows a large location pin beside a marked current-position dot."


def draw(s):
    standing_map(s)
    for road in ([(4, 28), (26, 28), (40, 32), (69, 32)],
                 [(5, 11), (18, 11), (26, 16), (50, 16), (70, 11)],
                 [(13, 4), (13, 18), (19, 29), (19, 39)],
                 [(37, 4), (37, 17), (31, 28), (31, 39)],
                 [(61, 5), (58, 17), (58, 37)]):
        map_stroke(s, road, DETAIL)
    s.line([folded_point(x, z) for x, z in oval(28.7, 23, 3.3, 3.3, count=24)], EDGE)
    s.line([folded_point(x, z) for x, z in oval(28.7, 23, .9, .9, count=14)], EDGE)
    location_pin(s, lambda x, z: (x, 6, z), 64, 39, 11)
