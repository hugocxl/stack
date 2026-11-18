from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._w5 import folded_point, map_stroke, standing_map

DESCRIPTION = "An upright folded street map carries a route through three marked stops."


def draw(s):
    standing_map(s)
    for road in ([(18, 4), (18, 36)], [(2, 18), (18, 18), (29, 24), (49, 24)],
                 [(38, 5), (38, 24), (49, 35)], [(57, 3), (57, 15), (70, 15)]):
        map_stroke(s, road, DETAIL)
    route = [(9, 10), (24, 10), (28, 32), (37, 32), (49, 32), (57, 25), (66, 25)]
    map_stroke(s, route, BOLD)
    for x, z in ((9, 10), (37, 32), (66, 25)):
        s.face([folded_point(u, v) for u, v in oval(x, z, 2.8, 2.8, count=24)], EDGE)
