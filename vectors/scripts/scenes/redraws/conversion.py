from geometry import EDGE
from scenes.redraws._w2 import funnel

DESCRIPTION = "Three input tokens sit over the open mouth of a funnel that tapers into one outlet."


def draw(s):
    funnel(s)
    for x, y, z in ((-17, 5, 92), (2, -2, 97), (18, -10, 101)):
        s.disk(x, y, z, 5.5, 5.5, 3.5, EDGE)
