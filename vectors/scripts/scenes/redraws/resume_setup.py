from geometry import BOLD
from scenes.redraws._kit import arrow
from scenes.redraws._w1 import screen_point, setup_checklist

DESCRIPTION = "A forward arrow points to the first open row on a standing checklist."


def draw(s):
    setup_checklist(s)
    anchor = (-29, 0, 17.75)
    arrow(s, [screen_point(*anchor, u, 0) for u in (-26, -2.8)], BOLD, head=8)
