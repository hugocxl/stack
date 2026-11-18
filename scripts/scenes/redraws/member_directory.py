from geometry import EDGE
from scenes.redraws._w3 import manual

DESCRIPTION = "An upright directory binder displays three rows of member badge icons and name lines."


def draw(s):
    face = manual(s, w=87, h=103)
    face.rules(20, 90, [44], ink=EDGE)
    for v, width in ((66, 32), (42, 24), (18, 28)):
        face.rect(20, v - 4, 15, 13, 2, EDGE)
        face.rules(24, v + 5, [7], ink=EDGE)
        face.oval(27.5, v, 2, 2)
        face.rules(44, v + 4, [width], ink=EDGE)
        face.rules(44, v - 3, [width - 7])
    for v in (26, 50, 74):
        face.s.face([face.point(87, v, 6), face.point(103, v, 6),
                     face.point(103, v + 10, 6), face.point(87, v + 10, 6)])
