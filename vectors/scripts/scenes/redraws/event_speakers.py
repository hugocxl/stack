from geometry import EDGE
from scenes.redraws._w3 import Surface

DESCRIPTION = "A paneled conference lectern holds a gooseneck microphone aimed toward the speaker position."


def draw(s):
    s.box(3, 7, 0, 67, 45, 6, 3)
    s.box(12, 11, 5, 49, 33, 59, 3)
    front = Surface(s, (12, 44, 5))
    front.rect(6, 7, 37, 43, 3, EDGE)
    top = Surface(s, (2, 52, 61), rise=(-.97, .24), back=(0, 0, -1))
    top.plate([(0, 0), (69, 0), (69, 49), (0, 49)], 6)
    lug = top.point(55, 11)
    s.disk(*lug, 4, 4, 3)
    s.tube([lug, (57, 41, 80), (54, 39, 88), (44, 38, 94), (33, 36, 94)], 1.7)
    s.tube([(34, 36, 94), (24, 34, 94)], 3.4)
    s.line([(27, 35, 92), (24, 34, 92)], EDGE)
