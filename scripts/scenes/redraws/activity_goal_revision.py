from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import badge
from scenes.redraws._w4 import Surface, front_surface

DESCRIPTION = "A pencil rests across a thick fitness target dial with an attached refresh badge."


def draw(s):
    dial = front_surface(s, angle=-29, z=39, lean=.39)
    dial.slab(oval(0, 0, 37, 37)[:-1], 8)
    for r in (29, 20, 10):
        dial.oval(0, 0, r, r, EDGE)
    dial.oval(0, 0, 2, 2, DETAIL)

    pencil = Surface(s, lambda u, v: dial.at(5 + .85*u + .53*v, -2 - .53*u + .85*v))
    pencil.slab([(0, 0), (12, -4.5), (53, -4.5), (57, -3), (57, 3),
                 (53, 4.5), (12, 4.5)], 4)
    pencil.line([(12, -4.5), (12, 4.5)], EDGE)
    pencil.line([(46, -4.5), (46, 4.5)], EDGE)
    pencil.line([(14, 0), (45, 0)], DETAIL)

    badge(s, "refresh", *dial.at(29, 26), 13)
