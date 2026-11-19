from geometry import BOLD
from scenes.redraws._kit import arrow
from scenes.redraws._w5 import billfold

DESCRIPTION = "A billfold holds a visible currency note, and a bold arrow carries the payment out to the right."


def draw(s):
    billfold(s)
    arrow(s, [(38, 15, 35), (51, 13, 38), (64, 9, 42),
                      (78, 3, 48)], BOLD, head=11)
