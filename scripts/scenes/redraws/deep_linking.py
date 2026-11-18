from geometry import EDGE
from scenes.redraws._w4 import link_emblem, nav_thumbnail, nav_window

DESCRIPTION = "A chain link sits at the endpoint of a dashed route from a browser address to a specific article heading."


def draw(s):
    face = nav_window(s, width=116, height=88, angle=-23)
    face.rows(38, 80, (41,), ink=EDGE)
    face.line([(94, 79), (94, 46), (86, 46)], EDGE, dashed=True)
    nav_thumbnail(face, 13, 40, 35, 24)
    face.rows(13, 28, (63,), ink=EDGE)
    face.rows(13, 17, (85, 72), step=-7)
    face.rows(54, 47, (12,), ink=EDGE)
    face.rows(54, 42, (10,))
    link_emblem(face, 77, 46, 12)
