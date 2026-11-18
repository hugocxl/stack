from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w5 import car_mark, location_pin

DESCRIPTION = "A curbside location pin contains a car pictogram that marks the rideshare meeting point."


def draw(s):
    s.face([(-30, -14, 4), (25, -14, 4), (25, 9, 4),
            (-11, 9, 4), (-11, 20, 4), (-30, 20, 4)], EDGE)
    s.line([(-30, 20, 0), (-11, 20, 0), (-11, 9, 0),
            (25, 9, 0), (25, -14, 0)], DETAIL)
    for x, y in ((-30, 20), (-11, 20), (-11, 9), (25, 9)):
        s.line([(x, y, 0), (x, y, 4)], DETAIL)
    face = lambda x, z: (x, 3, z)
    location_pin(s, face, 0, 36, 18, hole=False)
    car_mark(s, face, 0, 35, .86, BOLD)
