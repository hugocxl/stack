from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "A wide presentation display places a ruled speaker-notes strip directly below its slide."


def draw(s):
    for x in (10, 86):
        s.box(x, -9, 0, 16, 19, 5, 3)
    face = Surface(s, (0, 0, 4), rise=(-.36, .93), back=(0, -.93, -.36))
    face.plate(rounded(0, 0, 112, 74, 4), 9)
    face.rect(6, 6, 100, 62, 2, EDGE)
    face.stroke([(6, 29), (106, 29)], EDGE)
    face.rules(46, 25, [20], ink=DETAIL)

    face.oval(32, 49, 13, 13, BOLD)
    face.stroke([(32, 62), (32, 49), (44, 46)], EDGE)
    face.rules(55, 56, [34, 27, 30], gap=7)
    face.rules(14, 20, [75, 61], gap=6, ink=EDGE)
