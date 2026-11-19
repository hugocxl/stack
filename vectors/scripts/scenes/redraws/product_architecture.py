from geometry import DETAIL, EDGE, oval
from scenes.redraws._w4 import Surface

DESCRIPTION = "An exploded platform stack shows an interface on top, a connected service layer, and storage below."


def draw(s):
    s.box(0, 0, 0, 74, 56, 13, 4)
    storage = Surface(s, lambda u, v: (u, 56, v))
    for u in (24, 50):
        radius = 8
        storage.oval(u, 9, radius, 2, EDGE)
        storage.line([(u - radius, 9), (u - radius, 3)], EDGE)
        storage.line([(u + radius, 9), (u + radius, 3)], EDGE)
        for v, ink in ((6, DETAIL), (3, EDGE)):
            storage.line(oval(u, v, radius, 1.6, 180, 360, 20), ink)

    s.box(0, 0, 29, 74, 56, 12, 4)
    service = Surface(s, lambda u, v: (u, 56, v))
    for u in (11, 33, 55):
        service.frame(u, 32, 8, 6, 1.5, EDGE)
    for u in (19, 41):
        service.rows(u, 35, (14,), ink=EDGE)

    s.box(0, 0, 59, 74, 56, 5, 4)
    interface = Surface(s, lambda u, v: (u, v, 64))
    interface.frame(8, 7, 58, 42, 3, EDGE)
    interface.rows(8, 17, (58,), ink=EDGE)
    for u in (13, 19, 25):
        interface.oval(u, 12, 1.2, 1.2, EDGE)
    interface.frame(13, 22, 18, 21, 2)
    interface.rows(38, 24, (20, 15, 18), step=7)
