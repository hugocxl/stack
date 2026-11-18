from geometry import BOLD, DETAIL, EDGE
from scenes.redraws.payment_methods import card_face

DESCRIPTION = "A single gift card bears a printed ribbon and bow across its face."


def draw(s):
    point = card_face(s)
    for y in (25, 33):
        s.line([point(3, y), point(91, y)], DETAIL)
    for x in (43, 51):
        s.line([point(x, 2), point(x, 56)], DETAIL)
    for side in (-1, 1):
        loop = [(47, 29), (47 + side * 13, 12), (47 + side * 23, 12),
                (47 + side * 25, 19), (47 + side * 18, 27), (47, 29)]
        s.face([point(x, y) for x, y in loop], BOLD)
        s.line([point(47, 29), point(47 + side * 12, 44),
                point(47 + side * 20, 45)], EDGE)
