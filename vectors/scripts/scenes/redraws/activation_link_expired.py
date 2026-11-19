from scenes.redraws._kit import badge
from scenes.redraws._w1 import chain_links, screen_point

DESCRIPTION = "Two interlocked chain links carry a clock badge on the outer link."


def draw(s):
    chain_links(s)
    badge(s, "clock", *screen_point(0, 0, 35, 33, 22), 11.5)
