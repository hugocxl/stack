from geometry import EDGE
from scenes.redraws._kit import _screen, badge
from scenes.redraws._sf import screen, smooth

DESCRIPTION = "A telephone handset carries a return badge asking for a call back."


def draw(s):
    at = screen()
    grip = smooth([(-26, 33), (-34, 15), (-26, -9), (-6, -27), (18, -33)], 6)
    s.tube([at(u, v) for u, v in grip], 7, EDGE)
    for a, b in (((-30, 37), (-20, 28)), ((14, -38), (24, -28))):
        s.tube([at(*a), at(*b)], 10, EDGE)
    badge(s, "back", *_screen(0, 0, 0, 26, 22), 14)
