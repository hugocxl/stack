from geometry import BOLD, EDGE
from scenes.redraws._w4 import standing_card
from scenes.redraws.provider_profile import portrait

DESCRIPTION = "A raised audience profile card has a bullseye centered on its head-and-shoulders pictogram."


def draw(s):
    card = standing_card(s, 76, 66, angle=-12, lean=.53, depth=7)
    portrait(card, 29, 32, .82, EDGE)
    card.oval(29, 33, 22.5, 22.5, BOLD)
    card.oval(29, 33, 16.5, 16.5, EDGE)
    for a, b in [((29, 5), (29, 14)), ((29, 52), (29, 61)),
                 ((2, 33), (9, 33)), ((49, 33), (57, 33))]:
        card.line([a, b], EDGE)
    card.rows(59, 46, (10, 8, 10), step=-10)
