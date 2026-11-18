from geometry import DETAIL, rounded
from scenes.redraws._w5 import panel, rect

DESCRIPTION = "An open rigid catering case has a hinged lid, a molded carry handle, and three fitted food compartments."


def draw(s):
    lid = lambda x, z: (x, 2 - .42 * (z - 17), z)
    panel(s, rounded(0, 16, 67, 35, 4), lid, 4)
    rect(s, lid, 5, 21, 57, 25, 3, DETAIL)
    s.box(0, 2, 0, 67, 44, 5, 3)
    s.box(0, 2, 4, 3, 44, 13, 1)
    floor = lambda x, y: (x, y, 6)
    for x, y, w, d in ((5, 7, 27, 34), (37, 7, 25, 14), (37, 26, 25, 15)):
        rect(s, floor, x, y, w, d, 3)
    s.box(33, 4, 5, 3, 40, 8, 1)
    s.box(35, 22, 5, 30, 3, 8, 1)
    s.box(64, 2, 4, 3, 44, 13, 1)
    s.box(0, 43, 4, 67, 4, 13, 1.5)
    for x in (13, 51):
        s.box(x, 46, 10, 5, 2, 6, .7)
    s.tube([(24, 46, 9), (24, 52, 9), (27, 55, 9),
            (41, 55, 9), (44, 52, 9), (44, 46, 9)], 2.1)
