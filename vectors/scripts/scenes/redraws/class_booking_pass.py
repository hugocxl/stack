from geometry import EDGE
from scenes.redraws._w4 import standing_card

DESCRIPTION = "A class admission pass has an open-book emblem, a title line, and an inset date block."


def draw(s):
    card = standing_card(s, 112, 65, angle=-17, lean=.54, depth=5)
    card.frame(41, 52, 25, 5, 2.5, EDGE)
    card.line([(0, 45), (112, 45)], EDGE)
    card.outline([(15, 15), (14, 33), (23, 33), (30, 30), (37, 33),
                  (45, 33), (45, 15), (37, 15), (30, 12), (23, 15)], EDGE)
    card.line([(30, 12), (30, 30)], EDGE)
    card.rows(53, 33, (23,), ink=EDGE)
    card.rows(53, 24, (16,))
    card.frame(82, 12, 21, 24, 2)
    card.line([(82, 28), (103, 28)], EDGE)
    card.frame(89, 17, 7, 6, 1)
