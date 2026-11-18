from geometry import EDGE, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "A freestanding gallery sign shows two clock faces separated by a dash."


def draw(s):
    s.disk(-12, -3, 0, 15, 13, 5)
    s.tube([(-12, -3, 5), (-12, -3, 93), (-10, -3, 97), (-6, -3, 99),
            (92, -3, 99)], 2.8)
    for x in (17, 81):
        s.tube([(x, -3, 98), (x, -3, 82)], 1.6)
    face = Surface(s, (0, 1, 28))
    face.plate(rounded(0, 0, 98, 56, 4), 8)
    face.rules(7, 45, [84])
    for x, tip in ((25, -8), (73, 8)):
        face.oval(x, 23, 14, 14, EDGE)
        face.stroke([(x, 34), (x, 23), (x + tip, 23)], EDGE)
    face.rules(45, 23, [8], ink=EDGE)
