from geometry import EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface

DESCRIPTION = "An archive reading-room pass bears an open-book emblem and a plus badge."


def draw(s):
    face = Surface(s, (0, 0, 0), rise=(-.24, 1), back=(0, -1, -.24))
    face.plate(rounded(0, 0, 61, 88, 7), 7)
    face.rect(22, 75, 17, 5, 2.5, EDGE)
    face.stroke([(12, 37), (12, 61), (21, 62), (30, 58), (39, 62),
                 (48, 61), (48, 37), (38, 38), (30, 34), (21, 38)], EDGE, closed=True)
    face.stroke([(30, 58), (30, 34)], EDGE)
    face.rules(15, 23, [30])
    face.rules(20, 15, [20])
    badge(s, "plus", *face.point(63, 81, -3), 14)
