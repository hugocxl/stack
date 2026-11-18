from scenes.redraws._kit import badge
from scenes.redraws.payment_methods import chip_card

DESCRIPTION = "A chip payment card carries a clock badge at its upper-right corner."


def draw(s):
    chip_card(s)
    badge(s, "clock", 92, 2, 30, 14)
