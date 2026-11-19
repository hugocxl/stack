from geometry import DETAIL, EDGE, oval
from scenes.redraws._w5 import folded_point, mapped_route

DESCRIPTION = "An accordion-fold map shows a walking route from a hiking-shoe marker to a circled endpoint."


def draw(s):
    mapped_route(s)
    origin = lambda x, z: (x, 4, z)
    s.face([origin(x, z) for x, z in oval(8, 13, 12, 12, count=36)[:-1]])
    shoe = [(-3, 6), (1, 6), (2, 2), (7, -1), (8, -3), (7, -5),
            (-7, -5), (-7, -2), (-5, 1), (-5, 6), (-3, 6)]
    s.line([origin(8 + x, 13 + z) for x, z in shoe], EDGE)
    s.line([origin(2, 11), origin(14, 11)], DETAIL)
    s.face([folded_point(x, z) for x, z in oval(65, 29, 4.3, 4.3, count=24)[:-1]], EDGE)
