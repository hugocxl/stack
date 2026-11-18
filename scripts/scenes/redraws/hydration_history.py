from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w4 import open_book

DESCRIPTION = "An open hydration log shows a water-drop header and three dated intake entries."


def water_drop(page, u, v, r, ink=EDGE):
    shape = [(0, -1), (.24, -.66), (.53, -.29), (.66, .07), (.59, .40),
             (.35, .68), (0, .77), (-.35, .68), (-.59, .40), (-.66, .07),
             (-.53, -.29), (-.24, -.66)]
    page.outline([(u + x*r, v + y*r) for x, y in shape], ink)


def date_mark(page, u, v, scale=1):
    page.frame(u, v, 10*scale, 8*scale, 1, DETAIL)
    page.rows(u, v + 2.6*scale, (10*scale,))
    for x in (u + 2*scale, u + 8*scale):
        page.line([(x, v - 1.3*scale), (x, v + 1.2*scale)], EDGE)


def draw(s):
    left, right = open_book(s)
    water_drop(left, 32, 26, 16, BOLD)
    left.rows(15, 49, (36, 26), step=8, ink=DETAIL)
    for v, amount in ((18, 15), (34, 24), (50, 20)):
        date_mark(right, 72, v - 4)
        right.rows(87, v - 1, (amount,), ink=EDGE)
        right.rows(87, v + 4, (26,), ink=DETAIL)
