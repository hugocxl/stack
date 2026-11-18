from geometry import BOLD, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w4 import knee_mark, standing_card

DESCRIPTION = "A standing physiotherapy appointment card displays a knee joint diagram and carries a clock badge."


def draw(s):
    card = standing_card(s, 67, 84, angle=-24, lean=.44, depth=5)
    knee_mark(card, 31, 46, 1.16, BOLD)
    card.line([(9, 17), (57, 17)])
    card.rows(13, 10, (17,), ink=EDGE)
    card.rows(42, 10, (11,), ink=EDGE)
    badge(s, "clock", *card.at(65, 70), 17)
