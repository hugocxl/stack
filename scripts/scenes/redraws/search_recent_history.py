from geometry import EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w4 import front_surface, search_mark

DESCRIPTION = "A search field with a magnifying glass carries a clock badge on its right end."


def draw(s):
    field = front_surface(s, angle=-11, lean=.48, z=8)
    field.slab(rounded(0, 0, 105, 39, 18), 8)
    search_mark(field, 23, 22, 8.8)
    field.rows(42, 19, (30,), ink=EDGE)
    badge(s, "clock", *field.at(97, 35), 21)
