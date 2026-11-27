from scenes.redraws._kit import badge
from scenes.redraws._sf import payment_card

DESCRIPTION = "A standing payment card carries a return badge as the refund comes back to it."


def draw(s):
    payment_card(s)
    badge(s, "back", 43, 0, 52, 12)
