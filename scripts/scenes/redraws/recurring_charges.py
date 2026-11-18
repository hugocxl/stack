from scenes.redraws._kit import badge
from scenes.redraws.payment_methods import chip_card

DESCRIPTION = "A chipped payment card carries a circular renewal-arrow badge at its upper corner."


def draw(s):
    chip_card(s)
    badge(s, "refresh", 92, 2, 30, 14)
