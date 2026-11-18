from geometry import BOLD, DETAIL, EDGE
from scenes.systems_shapes import rectangle

DESCRIPTION = "A selector lever connects its pivot to the round contact while the square contact remains open."


def draw(s):
    s.box(-46, -25, 0, 92, 50, 9, 5)
    s.disk(-30, 9, 9, 10, 10, 5)
    s.box(20, -19, 9, 18, 18, 5, 1.5)
    rectangle(s, 23, -16, 14, 12, 12, DETAIL, 1)
    s.disk(0, 4, 9, 8, 8, 5)
    s.tube([(0, 4, 17), (-15, 6.5, 17), (-30, 9, 17)], 3, EDGE)
    s.disk(-30, 9, 14, 3.5, 3.5, 12)
    s.disk(-30, 9, 26, 6, 6, 5, BOLD)
