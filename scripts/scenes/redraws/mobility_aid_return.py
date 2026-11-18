from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import badge
from scenes.redraws._w4 import Surface, upright

DESCRIPTION = "A wheelchair with large push rims and small front casters carries a return arrow badge."


def draw(s):
    def wheel(x, y, z, radius, thickness, spokes=False):
        upright(s, oval(x, z, radius, radius)[:-1], y, thickness)
        rim = Surface(s, lambda u, v: (u, y, v))
        rim.oval(x, z, radius - 4, radius - 4, EDGE)
        if spokes:
            for u, v in oval(x, z, radius - 6, radius - 6, count=6)[:-1]:
                rim.line([(x, z), (u, v)], DETAIL)
            rim.oval(x, z, 3, 3, EDGE)

    wheel(23, 4, 29, 29, 4, True)
    wheel(65, 5, 8, 8, 4)
    s.tube([(4, 8, 75), (12, 8, 75), (18, 8, 37), (56, 8, 37),
            (64, 8, 16), (64, 8, 9)], 2, EDGE)
    s.box(15, 7, 37, 43, 37, 5, 2)
    s.face([(11, 7, 72), (11, 43, 72), (16, 43, 43), (16, 7, 43)], EDGE)
    s.tube([(4, 43, 75), (12, 43, 75), (18, 43, 37), (56, 43, 37),
            (64, 43, 16), (64, 43, 9)], 2, EDGE)
    s.tube([(25, 44, 47), (25, 44, 55), (51, 44, 55), (55, 44, 40)], 2, EDGE)
    s.box(64, 17, 12, 18, 26, 3, 3)
    wheel(66, 49, 8, 8, 4)
    wheel(23, 49, 29, 29, 5, True)
    badge(s, "back", 70, 4, 60, 16)
