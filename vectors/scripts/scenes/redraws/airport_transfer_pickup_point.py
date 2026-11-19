from geometry import DETAIL, EDGE
from scenes.redraws._w5 import location_pin
from scenes.redraws.bus_shelter_directory import bus_pictogram

DESCRIPTION = "A curbside location pin displays an airport shuttle pictogram in its face."


def draw(s):
    s.box(-27, -14, 0, 57, 29, 5, 2.3)
    s.face([(-27, -2, 5), (30, -2, 5), (30, 15, 5), (-27, 15, 5)], DETAIL)
    s.line([(-19, 8, 5), (20, 8, 5)], DETAIL, dashed=True)
    location_pin(s, lambda x, z: (x, -3, z), 0, 50.5, 25, hole=False)
    bus_pictogram(s, 0, -3, 51, 1.47, EDGE)
