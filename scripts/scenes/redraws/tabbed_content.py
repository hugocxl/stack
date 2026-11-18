from geometry import BOLD, EDGE, rounded
from scenes.redraws._w4 import front_surface, nav_thumbnail

DESCRIPTION = "Three tabs attach to one content window, and the raised middle tab opens onto a picture and article lines."


def draw(s):
    face = front_surface(s, angle=-24, z=7, lean=.27)
    for u in (5, 76):
        face.slab(rounded(u, 57, 33, 17, 4), 5)
    face.slab([(0, 0), (114, 0), (114, 62), (73, 62), (71, 80),
               (44, 80), (41, 62), (0, 62)], 7)
    face.rows(13, 67, (16,))
    face.rows(84, 67, (16,))
    face.rows(49, 71, (16,), ink=BOLD)
    nav_thumbnail(face, 10, 14, 40, 32)
    face.rows(60, 43, (35,), ink=EDGE)
    face.rows(60, 33, (43, 36, 40, 29), step=-7)
