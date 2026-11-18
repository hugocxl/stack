from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w4 import Surface, sample_vial

DESCRIPTION = "An open return mailer holds one capped specimen vial snugly in its fitted insert."


def draw(s):
    lid = Surface(s, lambda u, v: (u, -.32*v, 18 + .92*v))
    lid.slab([(0, 0), (84, 0), (84, 39), (72, 48), (12, 48), (0, 39)], 4)
    lid.line([(0, 39), (84, 39)], DETAIL)
    lid.frame(27, 10, 31, 22, 2, EDGE)
    lid.rows(33, 18, (19, 13), step=6)

    s.box(0, 0, 0, 84, 46, 17, 2)
    insert = Surface(s, lambda u, v: (u, v, 17.1))
    insert.frame(5, 5, 74, 36, 3)
    insert.frame(11, 10, 62, 26, 11, EDGE)
    sample_vial(s, lambda u, v, h: (16 + h, 23 + .866*u + .5*v, 17 - .5*u + .866*v))
    s.line([(0, 46, 12), (35, 46, 12), (42, 46, 8), (49, 46, 12), (84, 46, 12)], DETAIL)
