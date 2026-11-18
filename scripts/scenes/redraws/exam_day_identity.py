from geometry import EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface

DESCRIPTION = "A slotted exam ID card shows a blank portrait pictogram and a check badge."


def draw(s):
    face = Surface(s, (0, 0, 0))
    face.plate(rounded(0, 0, 88, 65, 5), 5)
    face.rect(33, 55, 22, 5, 2, EDGE)
    face.rect(8, 10, 34, 34, 3, EDGE)
    face.oval(25, 32, 5, 5)
    face.stroke([(13, 15), (14, 20), (18, 24), (25, 26),
                 (32, 24), (36, 20), (37, 15)], EDGE)
    face.rules(49, 40, [27], ink=EDGE)
    face.rules(49, 29, [25, 20, 27], gap=7)
    badge(s, "check", 88, 2, 53, 14)
