from geometry import BOLD, oval
from scenes.redraws._kit import arrow
from scenes.redraws._w1 import chain_links, screen_point

DESCRIPTION = "A curved forward arrow sweeps around the outside of a pair of interlocked chain links."


def draw(s):
    chain_links(s)
    sweep = oval(23, 16, 26, 20, 155, 9, 30)
    arrow(s, [screen_point(0, 0, 35, u, v) for u, v in sweep], BOLD, head=8)
