from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import arrow

DESCRIPTION = "A sliding counterweight shifts along the graduated beam of a balance scale."


def draw(s):
    s.box(-21, -15, 0, 42, 31, 7, 5)
    s.tube([(0, 0, 7), (0, 0, 64)], 3)
    s.tube([(-42, 0, 60), (45, 0, 68)], 2.1)
    for x in range(8, 43, 8):
        z = 64 + x * .09
        s.line([(x, 1, z + 4), (x, 1, z + 8)], DETAIL)
    s.box(23, -5, 61, 13, 11, 13, 2, BOLD)
    arrow(s, [(9, 0, 81), (36, 0, 84)], EDGE, head=6)
    s.disk(-36, 0, 23, 16, 14, 3, EDGE)
    s.ellipse(-36, 0, 26, 12, 10, DETAIL)
    for x, y in ((-49, 0), (-34, -11), (-32, 12)):
        s.line([(-37, 0, 60), (x, y, 26)], EDGE)
