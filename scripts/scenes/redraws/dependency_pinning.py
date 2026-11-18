from geometry import EDGE
from scenes.redraws._w1 import software_package
from scenes.systems_shapes import rectangle

DESCRIPTION = "A raised pushpin holds the version label of a code package."


def draw(s):
    software_package(s, 0, 0, 0)
    rectangle(s, 8, -14, 36, 15, 22, EDGE, 1.5)
    s.tube([(17, -2, 36), (19, -4, 46)], 1.2, EDGE)
    s.disk(19, -4, 45, 6, 6, 3)
    s.disk(19, -4, 48, 3.5, 3.5, 7)
    s.disk(19, -4, 55, 7, 7, 3)
