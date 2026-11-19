from geometry import EDGE, oval
from scenes.redraws._w5 import folded_point, location_pin, mapped_route

DESCRIPTION = "A route crosses an accordion-fold map and ends at the point of a destination pin."


def draw(s):
    mapped_route(s)
    s.line([folded_point(x, z) for x, z in oval(9, 11, 2.8, 2.8, count=24)], EDGE)
    _, y, _ = folded_point(65, 29)
    location_pin(s, lambda x, z: (x, y, z), 65, 47.2, 10)
