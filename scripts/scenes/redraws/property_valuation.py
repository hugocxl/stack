from geometry import DETAIL, EDGE, oval
from scenes.commerce_objects import house
from scenes.redraws._w2 import closed_outline, currency, upright_face

DESCRIPTION = "A hanging price tag with a currency symbol is tied to the eave of a gabled house."


def draw(s):
    house(s)
    s.tube([(22, -11, 27.3), (24, -10, 34), (30, -8, 25), (30, -6, 21)], .85, DETAIL)

    def point(x, z):
        return 23 + .65*x, -10 - .35*x, 6 + z

    upright_face(s, point, [(1, 0), (27, 0), (27, 17), (18, 27), (10, 27), (1, 17)], 2.5)
    closed_outline(s, point, oval(14, 21, 1.8, 1.8), DETAIL)
    currency(s, point, 14, 10, .87, EDGE)
