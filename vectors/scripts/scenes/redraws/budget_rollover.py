from scenes.redraws._kit import badge
from scenes.redraws._sf import coin_stack

DESCRIPTION = "A stack of coins carries an arrow badge as its unspent balance rolls into the next period."


def draw(s):
    top = coin_stack(s, 0, 0, 0, 26, 8)
    badge(s, "arrow", 26, 12, 22, 13)
