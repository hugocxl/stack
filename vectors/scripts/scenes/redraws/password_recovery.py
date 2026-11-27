from scenes.redraws._kit import badge
from scenes.redraws._sf import padlock

DESCRIPTION = "A padlock with a round shackle carries a refresh badge at its lower right."


def draw(s):
    padlock(s, -30, 0, 0, w=60, h=48, depth=16)
    badge(s, "refresh", 30, 0, 4, 14)
