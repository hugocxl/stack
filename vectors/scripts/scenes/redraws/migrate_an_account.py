from geometry import BOLD
from scenes.redraws._kit import arrow
from scenes.redraws._w1 import profile_card, screen_point

DESCRIPTION = "A bold rightward transfer arrow leaves the account card beside its portrait."


def draw(s):
    profile_card(s, -34, 0, 0, rows=((33, 21),))
    origin = (15, .5, 20)
    points = [screen_point(*origin, u, 0) for u in (-11, 25)]
    arrow(s, points, BOLD, head=9)
