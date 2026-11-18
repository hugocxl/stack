from scenes.redraws._kit import badge
from scenes.redraws.payment_methods import chip_card

DESCRIPTION = "A chip payment card carries an X badge at its upper-right corner."


def draw(s):
    chip_card(s)
    badge(s, "x", 92, 2, 30, 14)
