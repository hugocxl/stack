from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w4 import dumbbell_mark, standing_card

DESCRIPTION = "A standing training card with a prominent dumbbell pictogram carries a check badge."


def draw(s):
    card = standing_card(s, 91, 61, angle=-32, lean=.35, depth=6)
    card.frame(6, 6, 79, 49, 2)
    dumbbell_mark(card, 45, 32, 25, EDGE)
    badge(s, "check", *card.at(91, 49), 16)
