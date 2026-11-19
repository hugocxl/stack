from geometry import BOLD, oval
from scenes.redraws._kit import arrow
from scenes.redraws._w1 import screen_point, setup_checklist

DESCRIPTION = "A curved forward arrow bypasses the dashed middle row of a standing checklist."


def draw(s):
    setup_checklist(s, optional=True)
    anchor = (-29, 0, 17.75)
    path = oval(-3.6, 0, 17, 11.5, 91, 272, 28)
    arrow(s, [screen_point(*anchor, u, v) for u, v in path], BOLD, head=7)
