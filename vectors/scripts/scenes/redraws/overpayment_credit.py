from scenes.redraws._kit import badge
from scenes.redraws._w5 import billfold, coin_stack

DESCRIPTION = "A billfold holds a currency note behind a stack of coins with a plus badge on its top edge."


def draw(s):
    billfold(s)
    coin_stack(s, 57, 39, 0, 14, 5)
    badge(s, "plus", 67, 37, 23, 11)
