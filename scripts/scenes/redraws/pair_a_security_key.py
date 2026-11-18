from geometry import DETAIL, EDGE
from scenes.redraws._w1 import chain_links
from scenes.systems_shapes import rectangle

DESCRIPTION = "Two interlocked chain links overlap a USB security key with an exposed plug."


def draw(s):
    chain_links(s, 39, 1, 7, scale=.60)
    s.box(-39, -10, 2, 26, 20, 5, 1)
    for y in (-6, 2):
        rectangle(s, -35, y, 7, 5, 4, EDGE, .4)
    s.box(-16, -15, 0, 47, 30, 10, 6)
    s.ellipse(3, 0, 10, 9, 9, EDGE)
    s.ellipse(3, 0, 10, 5, 5, DETAIL)
