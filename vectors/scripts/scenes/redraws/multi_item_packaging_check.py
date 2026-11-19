from geometry import DETAIL, oval
from scenes.redraws._kit import badge
from scenes.redraws._w1 import open_carton_back, open_carton_front

DESCRIPTION = "An open shipping carton holds a capped bottle and a small box, and a check badge overlaps its front flap."


def draw(s):
    carton = (-33, 33, -24, 24, 29)
    open_carton_back(s, *carton)

    bottle = oval(-15, -4, 12, 12)[:-1]
    neck = oval(-15, -4, 6, 6)[:-1]
    s.solid(bottle, 0, 38, crease=False)
    s.solid(bottle, 38, 9, top=neck, crease=False)
    s.disk(-15, -4, 47, 7, 7, 6)
    s.ellipse(-15, -4, 53, 7, 7, DETAIL)
    for z in (27, 35):
        s.ellipse(-15, -4, z, 12, 12, DETAIL, -45, 135)

    s.box(3, -17, 0, 25, 29, 34, 1)
    s.line([(14, -17, 34), (14, 12, 34), (14, 12, 27)], DETAIL)
    open_carton_front(s, *carton)
    badge(s, "check", 3, 39, 22, 11)
