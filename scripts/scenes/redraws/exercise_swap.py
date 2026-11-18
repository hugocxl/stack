from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w4 import Surface, dumbbell_mark, front_surface
from scenes.redraws.evening_routine import printed_glyph

DESCRIPTION = "A standing workout card shows a dumbbell and two opposing swap arrows on its attached side tab."


def draw(s):
    face = front_surface(s, angle=-33, z=5, lean=.38)
    face.slab(rounded(0, 0, 76, 58, 4), 5)
    face.frame(7, 7, 62, 44, 2, DETAIL)
    dumbbell_mark(face, 35, 36, 19, EDGE)
    face.rows(16, 16, (21, 8), step=-5)
    tab = Surface(s, lambda u, v: (face.at(u, v)[0], face.at(u, v)[1] + 2, face.at(u, v)[2]))
    tab.slab(rounded(63, 9, 26, 29, 5), 4)
    printed_glyph(tab, "arrow", 76, 29, 10, BOLD)
    printed_glyph(tab, "back", 76, 18, 10, EDGE)
