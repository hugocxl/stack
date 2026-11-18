from geometry import DETAIL, EDGE
from scenes.redraws._w1 import software_package
from scenes.systems_shapes import bezel

DESCRIPTION = "A clear adhesive document pouch holds a folded shipping form against the face of a carton."


def draw(s):
    software_package(s, 0, 0, 0, 1.22, show_code=False)
    y = 25.62
    bezel(s, -28, y, 4, 54, 35, EDGE, 2)
    s.line([(a, y, b) for a, b in ((-21, 9), (-21, 34), (9, 34),
                                   (18, 25), (18, 9), (-21, 9))], DETAIL)
    s.line([(9, y, 34), (9, y, 25), (18, y, 25)], EDGE)
    for z, width in ((25, 19), (18, 28), (13, 22)):
        s.line([(-16, y, z), (-16 + width, y, z)], DETAIL)
    s.line([(-28, y, 29), (-23, y, 29)], EDGE)
    s.line([(21, y, 29), (26, y, 29)], EDGE)
