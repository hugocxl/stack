from geometry import BOLD
from scenes.redraws._kit import arrow
from scenes.redraws._w5 import billfold, currency_mark

DESCRIPTION = "A currency-marked billfold sends an upward arrow directly out of its open bill slot."


def draw(s):
    face = billfold(s, note=False)
    currency_mark(s, face, 27, 16, 9, ink=BOLD)
    arrow(s, [(30, 13, 34), (30, 13, 42), (30, 13, 64)], BOLD, head=12)
