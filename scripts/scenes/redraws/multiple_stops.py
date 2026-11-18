from geometry import BOLD, DETAIL
from scenes.redraws._w5 import folded_point, location_pin, map_stroke, standing_map

DESCRIPTION = "A route winds across a standing folded map and connects three location pins."


def draw(s):
    standing_map(s)
    for road in ([(4, 31), (18, 34), (29, 29), (49, 34), (70, 32)],
                 [(33, 6), (47, 7), (59, 5), (70, 8)]):
        map_stroke(s, road, DETAIL)
    map_stroke(s, [(12, 12), (20, 8), (29, 9), (37, 17), (45, 11),
                   (54, 9), (64, 14)], BOLD)
    for x, z in ((12, 12), (37, 17), (64, 14)):
        location_pin(s, folded_point, x, z + 10.92, 6)
