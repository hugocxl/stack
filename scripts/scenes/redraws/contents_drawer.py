from geometry import EDGE, rounded
from scenes.redraws._w4 import attached_panel, nav_thumbnail, nav_window

DESCRIPTION = "A raised table-of-contents drawer slides over the left edge of an open article viewport."


def draw(s):
    face = nav_window(s, width=112, height=86, angle=-25)
    face.rows(53, 61, (43,), ink=EDGE)
    nav_thumbnail(face, 54, 27, 42, 24)
    face.rows(54, 20, (41, 33), step=-7)
    drawer = attached_panel(face, 4)
    drawer.slab(rounded(-7, 4, 53, 62, 3), 5)
    drawer.rows(2, 56, (28,), ink=EDGE)
    for v, width in ((43, 23), (30, 19), (17, 27)):
        drawer.oval(4, v, 1.25, 1.25, EDGE)
        drawer.rows(12, v, (width,), ink=EDGE)
    drawer.line([(39, 27), (39, 40)], EDGE)
