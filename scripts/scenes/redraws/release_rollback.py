from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import arrow
from scenes.redraws._w1 import software_package

DESCRIPTION = "A version tag sits on a sealed software package encircled by a looping rollback arrow."


def draw(s):
    software_package(s, 0, 0, 0)
    tag = [(8, -13, 36), (16, -18, 36), (24, -13, 36),
           (24, 11, 36), (8, 11, 36)]
    s.face(tag, EDGE)
    s.ellipse(16, -10, 36, 2.2, 2.2, DETAIL)
    s.line([(16, -10, 36), (17, -17, 41), (7, -17, 36)], DETAIL)
    for y in (1, 6):
        s.line([(12, y, 36), (20, y, 36)], DETAIL)

    arrow(s, [(33, -15, 9), (43, -10, 7), (49, 0, 5), (50, 11, 3),
              (47, 22, 2), (39, 31, 2), (27, 37, 2), (12, 40, 2),
              (-4, 40, 2), (-19, 37, 2), (-29, 32, 2)], BOLD, head=9)
