from geometry import EDGE
from scenes.redraws._w3 import Surface, wheelchair
from scenes.redraws._w5 import folded_point, map_stroke, standing_map

DESCRIPTION = "An upright folded venue map marks its destination with a wheelchair symbol inside a location pin."


def draw(s):
    standing_map(s)
    map_stroke(s, [(4, 10), (19, 16), (23, 32), (30, 36)])
    map_stroke(s, [(4, 30), (11, 25), (20, 26)])
    map_stroke(s, [(55, 13), (62, 12), (71, 24)])
    map_stroke(s, [(57, 34), (63, 29), (71, 31)])
    map_stroke(s, [(8, 7), (24, 5), (38, 7), (39, 13)], EDGE, dashed=True)
    pin = Surface(s, folded_point(38, 26))
    pin.plate([(-14, 2), (-13, 10), (-8, 15), (0, 17), (8, 15), (13, 10),
               (14, 2), (10, -5), (0, -14), (-10, -5)], 2)
    wheelchair(pin, 0, 3, 17)
