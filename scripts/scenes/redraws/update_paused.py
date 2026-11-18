from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws.page_moved import Surface

DESCRIPTION = "A software package with a code mark on its lid and an install slot carries a pause badge."


def software_package(s):
    s.box(0, 0, 0, 84, 53, 34, 4)
    s.box(-1, -1, 33, 86, 55, 7, 4)
    # Print the code mark near the centre of the lid in its diagonal plane.
    for stroke in [[(-12, 6), (-22, 0), (-12, -6)],
                   [(5, 7), (-5, -7)], [(12, 6), (22, 0), (12, -6)]]:
        s.line([(42 + (u - 2 * v) / 1.73, 26 - (u + 2 * v) / 1.73, 40)
                for u, v in stroke], EDGE)
    front = Surface(s, (0, 53, 0))
    front.frame(25, 6, 35, 5, 2, EDGE)
    return front


def draw(s):
    software_package(s)
    badge(s, "pause", 84, 7, 39, 15)
