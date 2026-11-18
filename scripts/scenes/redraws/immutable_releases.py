from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w1 import software_package

DESCRIPTION = "A tagged code package carries a closed padlock badge."


def draw(s):
    software_package(s, 0, 0, 0)
    tag = [(21, -14, 36), (25, -10, 36), (25, 7, 36),
           (12, 7, 36), (12, -10, 36), (16, -14, 36)]
    s.face(tag, EDGE)
    s.ellipse(18.5, -9, 36, 2, 2, DETAIL)
    s.line([(18.5, -9, 36), (15, -15, 40), (5, -11, 36)], DETAIL)
    badge(s, "lock", 34, 5, 29, 13)
