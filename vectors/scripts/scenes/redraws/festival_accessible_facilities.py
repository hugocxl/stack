from geometry import DETAIL, EDGE
from scenes.redraws._w3 import Surface, wheelchair
from scenes.redraws._w5 import folded_point, location_pin, map_stroke, standing_map

DESCRIPTION = "A folded festival map marks the facilities with a large wheelchair location pin beside a printed tent."


def draw(s):
    standing_map(s)
    map_stroke(s, [(2, 12), (23, 12), (35, 16), (52, 13), (71, 13)],
               EDGE, dashed=True)
    map_stroke(s, [(39, 16), (42, 25), (60, 34), (71, 34)])
    map_stroke(s, [(6, 25), (9, 30), (14, 30), (17, 40), (21, 30), (24, 30),
                   (27, 25), (6, 25)], EDGE)
    map_stroke(s, [(7, 25), (7, 19), (25, 19), (25, 25)])
    map_stroke(s, [(14, 19), (17, 25), (20, 19)])
    map_stroke(s, [(55, 37), (55, 24), (67, 24), (67, 37), (55, 37)], DETAIL)
    x, y, z = folded_point(57, 20)
    marker = Surface(s, (x, y + 8, z))
    location_pin(s, marker.point, 0, 24, 13, hole=False)
    wheelchair(marker, 0, 25, 16)
