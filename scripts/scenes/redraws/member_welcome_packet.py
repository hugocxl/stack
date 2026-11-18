from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._kit import glyph
from scenes.redraws._w3 import Surface

DESCRIPTION = "A membership card with a rosette peeks out of an open welcome envelope."


def draw(s):
    back = Surface(s, (0, 0, 0))
    back.plate([(0, 0), (94, 0), (94, 47), (50, 88), (44, 88), (0, 47)], 4)
    back.stroke([(5, 49), (47, 81), (89, 49)], DETAIL)

    card = Surface(s, (0, 3, 0))
    card.plate(rounded(14, 20, 66, 48, 4), 2)
    card.oval(30, 55, 9, 9, EDGE)
    glyph(s, "star", 30, 3, 55, 8, BOLD)
    card.rules(44, 57, [26, 20], gap=8)

    front = Surface(s, (0, 9, 0))
    s.face([front.point(x, v) for x, v in
            ((0, 48), (47, 24), (94, 48), (94, 4), (90, 0), (4, 0), (0, 4))])
    front.stroke([(5, 4), (34, 29)], DETAIL)
    front.stroke([(89, 4), (60, 29)], DETAIL)
