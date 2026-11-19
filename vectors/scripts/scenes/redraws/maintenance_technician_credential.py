from geometry import BOLD, EDGE
from scenes.redraws._w4 import wrench_mark
from scenes.redraws.provider_profile import portrait, provider_card

DESCRIPTION = "A technician credential pairs a small portrait pictogram with a large open-jaw wrench emblem."


def draw(s):
    card = provider_card(s)
    card.frame(10, 16, 31, 31, 3)
    portrait(card, 25.5, 31, .8)
    card.rows(11, 10, (28,), ink=EDGE)
    wrench_mark(card, 73, 30, .84, BOLD)
