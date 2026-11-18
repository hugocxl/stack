from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w4 import currency_mark, front_surface, wrench_mark

DESCRIPTION = "An estimate in an open bid folder has a clock badge on its boxed due-date row."


def draw(s):
    back = front_surface(s, angle=-22, z=6, lean=.4)
    back.slab([(0, 0), (95, 0), (95, 66), (41, 66), (35, 75),
               (3, 75), (0, 70)], 6)
    page = front_surface(s, angle=-22, y=5, z=4, lean=.36)
    page.slab([(8, 4), (83, 4), (83, 88), (8, 88)], 3)
    wrench_mark(page, 27, 72, .31)
    currency_mark(page, 48, 72, .62)
    page.rows(58, 70, (15,), ink=EDGE)
    page.rows(18, 56, (53,))
    page.frame(17, 35, 55, 14, 2, EDGE)
    page.rows(23, 42, (24,), ink=EDGE)
    flap = front_surface(s, angle=-22, y=10, z=5, lean=.32)
    flap.slab([(0, 0), (95, 0), (95, 29), (43, 29), (34, 24), (0, 24)], 4)
    badge(s, "clock", *page.at(80, 41), 14)
