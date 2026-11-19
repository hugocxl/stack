from geometry import DETAIL, oval
from scenes.redraws._w5 import rect

DESCRIPTION = "A bottle-filling dispenser has a recessed bay with a visible spout above an uncapped bottle."


def draw(s):
    s.box(0, 0, 0, 49, 33, 8, 2)
    s.box(0, 0, 7, 49, 16, 63, 3)
    s.box(3, 16, 8, 43, 13, 7, 2)
    s.box(1, 14, 14, 5, 15, 51, 2)
    s.box(43, 14, 14, 6, 15, 51, 2)
    s.box(0, 14, 51, 49, 16, 19, 2.5)
    for x in (14, 21, 28, 35):
        s.line([(x, 21, 15), (x, 27, 15)], DETAIL)
    s.tube([(24, 18, 49), (24, 26, 49), (24, 26, 42)], 2)
    s.line([(24, 26, 39), (24, 26, 36)], DETAIL)
    body = oval(24, 26, 6, 5)[:-1]
    neck = oval(24, 26, 3, 2.5)[:-1]
    s.solid(body, 15, 14, crease=False)
    s.solid(body, 29, 3, top=neck, crease=False)
    s.disk(24, 26, 32, 3, 2.5, 2)
    s.ellipse(24, 26, 34, 2, 1.55, DETAIL)
    face = lambda x, z: (x, 30, z)
    rect(s, face, 10, 58, 11, 5, 1.2, DETAIL)
    # A water-drop pictogram identifies the dispenser on its molded fascia.
    s.face([face(37, 67), face(33, 61), face(33, 58), face(35, 56),
            face(39, 56), face(41, 58), face(41, 61)])
