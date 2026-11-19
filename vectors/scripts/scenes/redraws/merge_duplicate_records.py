from geometry import EDGE, rounded
from scenes.redraws._kit import arrow
from scenes.redraws._w4 import front_surface

DESCRIPTION = "Two overlapping contact cards with matching avatar marks feed into one converging arrow."


def draw(s):
    angle = -24
    for u, v, depth in ((0, 33, 0), (12, 0, 5)):
        card = front_surface(s, angle=angle, y=depth, z=5)
        card.slab(rounded(u, v, 61, 39, 4), 5)
        card.frame(u + 7, v + 8, 20, 23, 2, EDGE)
        card.oval(u + 17, v + 23, 3.6, 3.6, EDGE)
        card.line([(u + 11, v + 12), (u + 13, v + 15),
                   (u + 21, v + 15), (u + 23, v + 12)], EDGE)
        card.rows(u + 34, v + 24, (16, 12), step=-8)

    merge = front_surface(s, angle=angle, y=5, z=5)
    rear_card = front_surface(s, angle=angle, z=5)
    s.line([rear_card.at(61, 53), rear_card.at(76, 53), merge.at(89, 36)], EDGE)
    arrow(s, [merge.at(u, v) for u, v in ((73, 17), (83, 17), (89, 36), (110, 36))],
          EDGE, head=10)
