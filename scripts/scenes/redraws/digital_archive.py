from geometry import EDGE
from scenes.redraws._w3 import Surface

DESCRIPTION = "A lidded archival box displays a digital file emblem inside its front label holder."


def draw(s):
    s.box(0, 0, 0, 69, 46, 43, 3)
    s.box(-2, -2, 39, 73, 50, 9, 2)
    side = Surface(s, (0, 48, 0))
    side.rect(23, 42, 23, 3, 1.3, EDGE)
    face = Surface(s, (0, 46.5, 0))
    face.rect(15, 7, 40, 28, 2, EDGE)
    face.stroke([(24, 11), (37, 11), (37, 26), (32, 31), (24, 31)], EDGE, closed=True)
    face.stroke([(32, 31), (32, 26), (37, 26)], EDGE)
    for x, v in ((41, 12), (45, 12), (41, 16), (49, 16), (45, 20)):
        face.rect(x, v, 2.4, 2.4, .2)
