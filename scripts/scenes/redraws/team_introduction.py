from geometry import EDGE
from scenes.redraws._w4 import credential_mark, standing_card

DESCRIPTION = "An upright team directory displays three staff credentials in a single row."


def draw(s):
    card = standing_card(s, 119, 70, angle=-26, lean=.43, depth=8)
    card.rows(10, 60, (49,), ink=EDGE)
    for u in (9, 46, 83):
        credential_mark(card, u, 12, 27, 37)
    card.oval(22.5, 32.5, 4, 4, EDGE)
    card.outline([(55, 29), (55, 36), (64, 36), (64, 29)], EDGE)
    card.outline([(96.5, 28), (101, 32.5), (96.5, 37), (92, 32.5)], EDGE)
