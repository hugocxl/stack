from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w4 import standing_card
from scenes.redraws.provider_profile import portrait

DESCRIPTION = "A vertical visitor pass shows a portrait pictogram with an outward arrow badge at the lower edge."


def draw(s):
    card = standing_card(s, 54, 77, angle=-31, lean=.37, depth=6)
    card.frame(17, 65, 20, 5.5, 2.6, EDGE)
    card.frame(9, 26, 36, 30, 4)
    portrait(card, 27, 40, .88)
    card.rows(12, 19, (26,), ink=EDGE)
    card.rows(12, 12, (18,))
    badge(s, "arrow", *card.at(53, 13), 13)
