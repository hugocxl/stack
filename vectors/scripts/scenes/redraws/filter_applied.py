from scenes.redraws._kit import badge
from scenes.redraws._w2 import funnel

DESCRIPTION = "An upright filter funnel carries a check badge on the right side of its taper."


def draw(s):
    funnel(s)
    badge(s, "check", 22, -13, 23, 14)
