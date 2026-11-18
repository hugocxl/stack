from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w4 import Surface, landscape

DESCRIPTION = "An open saddle-stitched zine has two visible staples, a bold masthead, and a two-page image-and-text grid."


def draw(s):
    pages = []
    for u0, u1, rise in ((0, 62, -.12), (62, 124, .12)):
        page = Surface(s, lambda u, v, rise=rise: (u, v*.64, (82 - v)*.39 + 3 + (u - 62)*rise))
        page.slab([(u0, 0), (u1, 0), (u1, 82), (u0, 82)], 3)
        pages.append(page)
    left, right = pages
    left.rows(9, 12, (42,), ink=BOLD)
    left.rows(9, 21, (31,), ink=EDGE)
    landscape(left, 9, 30, 44, 31)
    left.rows(9, 70, (39, 32), step=6)
    right.rows(70, 13, (39,), ink=EDGE)
    for u, widths in ((70, (19, 18, 20, 15, 20, 17)), (95, (20, 17, 20, 16, 19, 13))):
        right.rows(u, 29, widths, step=7)
    right.rows(70, 76, (20,), ink=DETAIL)
    right.line([(62, 1), (62, 81)], EDGE)
    for v in (18, 63):
        right.outline([(60.5, v), (63.5, v), (63.5, v + 6), (60.5, v + 6)], EDGE)
