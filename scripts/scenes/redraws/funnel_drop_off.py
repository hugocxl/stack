from geometry import BOLD
from scenes.redraws._kit import arrow
from scenes.redraws._w2 import funnel

DESCRIPTION = "An arrow leaves the narrowing side of a conversion funnel before the outlet."


def draw(s):
    funnel(s)
    arrow(s, [(12, -12, 28), (39, -39, 28)], BOLD, head=10)
