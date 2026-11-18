from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w4 import front_surface

DESCRIPTION = "A stack of three document cards carries a history clock badge on the front card."


def draw(s):
    for u, v, depth in ((0, 12, -13), (7, 6, -6), (14, 0, 1)):
        page = front_surface(s, angle=-30, y=depth, z=5, lean=.23)
        page.slab([(u, v), (u + 67, v), (u + 67, v + 43),
                   (u + 54, v + 56), (u, v + 56)], 4)
    page.line([(68, 56), (68, 43), (81, 43)], EDGE)
    page.rows(25, 43, (28,), ink=EDGE)
    page.rows(25, 29, (38, 28, 32), step=-8)
    badge(s, "clock", *page.at(80, 25), 13)
