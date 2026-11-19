from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._w1 import software_package

DESCRIPTION = "A taped parcel rests directly on a platform shipping scale with a large analog weight display."


def draw(s):
    s.box(-38, -30, 0, 76, 61, 15, 3)
    s.box(-36, -28, 15, 72, 56, 4, 2)
    software_package(s, 0, -3, 19, 1.08, show_code=False)
    s.box(-27, 30, 0, 54, 10, 22, 4)
    y = 40
    s.line([(a, y, b) for a, b in oval(0, 6, 21, 12, 0, 180, 32)] +
           [(-21, y, 6), (21, y, 6)], EDGE)
    for x, z in ((-16, 9), (-9, 14), (0, 16), (9, 14), (16, 9)):
        s.line([(x * .79, y, z - 2), (x, y, z)], DETAIL)
    s.line([(0, y, 7), (10, y, 13)], BOLD)
