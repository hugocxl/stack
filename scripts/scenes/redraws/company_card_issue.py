from scenes.redraws._kit import badge
from scenes.redraws.payment_methods import chip_card

DESCRIPTION = "A company payment card has a visible chip and a plus badge attached to its upper corner."


def draw(s):
    chip_card(s)
    badge(s, "plus", 92, 2, 30, 14)
