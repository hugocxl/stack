from geometry import EDGE, oval
from scenes.redraws._kit import badge
from scenes.redraws._w1 import server_tower

DESCRIPTION = "A server tower has a power button on its front and a pause badge at its upper-right corner."


def draw(s):
    server_tower(s)
    s.line([(x, 0, z) for x, z in oval(0, 43, 10, 10, 120, 420, 32)], EDGE)
    s.line([(0, 0, 55), (0, 0, 43)], EDGE)
    badge(s, "pause", 25, -3, 60, 12)
