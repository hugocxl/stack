from scenes.redraws._kit import badge
from scenes.redraws._sf import headset

DESCRIPTION = "An over-ear headset with a boom microphone carries a plus badge as it pairs."


def draw(s):
    headset(s)
    badge(s, "plus", 44, -8, 23, 12.5)
