from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import badge
from scenes.redraws._w4 import Surface, currency_mark, front_surface, upright

DESCRIPTION = "A curled reservation receipt has a calendar header and a check badge beside the paid amount."


def draw(s):
    face = front_surface(s, angle=0, z=8, lean=.47)
    face.slab([(0, 3), (66, 3), (66, 81), (55, 85), (11, 85), (0, 80)], 3)
    face.frame(9, 56, 19, 16, 2, EDGE)
    face.line([(9, 66), (28, 66)], EDGE)
    for u in (13, 24):
        face.line([(u, 69), (u, 75)], EDGE)
    face.rows(35, 65, (20, 15), step=-7)
    face.rows(9, 46, (43, 35), step=-7)
    face.line([(9, 32), (57, 32)], EDGE, dashed=True)
    currency_mark(face, 17, 20, .78)
    face.rows(31, 20, (17,), ink=EDGE)
    upright(s, oval(-4, 8, 9, 8)[:-1], 66, 66, angle=-90)
    end = Surface(s, lambda u, v: (66, -u, v))
    end.line(oval(-4, 8, 5.2, 4.5, 35, 322, count=26), DETAIL)
    s.line([(0, 9, 14.6), (66, 9, 14.6)], DETAIL)
    badge(s, "check", *face.at(63, 20), 14)
