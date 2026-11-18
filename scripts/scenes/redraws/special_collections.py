from geometry import DETAIL, EDGE
from scenes.redraws._w4 import Surface, upright

DESCRIPTION = "An open archival box holds three staggered tabbed folders above its label holder."


def draw(s):
    w, d, h = 88, 66, 36
    wall = 4
    s.box(0, 0, 0, w, d, wall, 1)
    s.box(0, 0, wall, w, wall, h - wall, 1)
    s.box(0, wall, wall, wall, d - 2*wall, h - wall, 1)

    for face_y, tab_x, top in ((14, 10, 59), (29, 34, 56), (44, 57, 53)):
        upright(s, [(7, 8), (81, 8), (81, top), (tab_x + 20, top),
                    (tab_x + 17, top + 8), (tab_x, top + 8),
                    (tab_x - 2, top), (7, top)], face_y, 2.5)
        s.line([(11, face_y, top - 4), (77, face_y, top - 4)], DETAIL)

    s.box(w - wall, wall, wall, wall, d - wall, h - wall, 1)
    s.box(0, d - wall, wall, w - wall, wall, h - wall, 1)
    label = Surface(s, lambda x, z: (x, d, z))
    label.frame(27, 11, 30, 13, 2, EDGE)
    label.rows(34, 17.5, (16,))
