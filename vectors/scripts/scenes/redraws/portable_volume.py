from geometry import BOLD
from scenes.redraws._kit import arrow
from scenes.redraws._w1 import hard_drive

DESCRIPTION = "A short outward arrow extends from the front transfer socket of an external drive."


def draw(s):
    hard_drive(s)
    arrow(s, [(-14.5, 29, 7), (-14.5, 55, 7)], BOLD, head=8)
