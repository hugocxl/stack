from scenes.redraws._kit import badge
from scenes.redraws._w1 import chain_links, screen_point

DESCRIPTION = "Two interlocked chain links carry a plus badge at the upper end."


def draw(s):
    chain_links(s)
    badge(s, "plus", *screen_point(0, 0, 35, 33, 22), 11.5)
