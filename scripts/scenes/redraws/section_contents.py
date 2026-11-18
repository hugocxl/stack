from geometry import EDGE
from scenes.redraws._w4 import nav_article

DESCRIPTION = "A bound contents page lines up three section headings with dotted leaders and right-aligned page markers."


def draw(s):
    face = nav_article(s)
    for v, width, marker in ((66, 23, 5), (43, 16, 6), (20, 25, 7)):
        face.rows(15, v, (width,), ink=EDGE)
        for u in range(15 + width + 4, 56, 4):
            face.rows(u, v, (1.2,), ink=EDGE)
        face.frame(69 - marker, v - 2.4, marker, 4.8, 1, EDGE)
        face.rows(15, v - 7, (width*.63,))
