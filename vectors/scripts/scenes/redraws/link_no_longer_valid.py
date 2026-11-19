from scenes.redraws._kit import badge
from scenes.redraws._w1 import chain_links, screen_point

DESCRIPTION = "An X badge overlaps the lower end of two interlocked chain links."


def draw(s):
    chain_links(s)
    badge(s, "x", *screen_point(0, 0, 35, 27, -13), 14)
