from geometry import DETAIL, EDGE, oval, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface

DESCRIPTION = "Two lanyard cards carry geometric profile emblems, and a status ring lights up the front card."


def draw(s):
    for origin, rise, foreground in (((0, 8, 3), (-.25, .96), False),
                                     ((51, 0, 9), (-.11, .99), True)):
        card = Surface(s, origin, rise=rise, back=(0, -rise[1], rise[0]))
        strap = [(22, 60), (12, 74), (7, 87), (13, 95), (30, 95),
                 (37, 87), (32, 74), (22, 60)]
        s.tube([card.point(x, v, 2) for x, v in strap], 2.1, EDGE)
        card.plate(rounded(0, 0, 44, 65, 4), 4)
        card.rect(15, 55, 14, 4, 2, EDGE)
        if foreground:
            card.stroke([(22, 46), (32, 36), (22, 26), (12, 36)], EDGE, closed=True)
        else:
            card.stroke(oval(22, 36, 9, 9, count=32), EDGE)
        card.rules(10, 17, [24, 17], gap=7, ink=DETAIL)

    cx, cy, cz = card.point(42, 17, -3)
    badge(s, "dot", cx, cy, cz, 12)
