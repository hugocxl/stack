from geometry import EDGE, oval
from scenes.redraws._w1 import envelope, server_unit

DESCRIPTION = "A cable hook carries a sealed envelope toward a server."


def draw(s):
    server_unit(s, 13, -10, width=36, depth=26, height=43)
    s.tube([(15, -20, 43), (-5, -20, 58), (-25, -12, 65),
            (-34, 10, 66), (-34, 10, 57)], 1.9, EDGE)
    hook = [(x, 10, z) for x, z in oval(-34, 49, 8, 9, 90, 350, 30)]
    s.tube(hook, 2.4, EDGE)
    envelope(s, -53, 14, 6, width=44, height=32)
    s.line([(-34, 10, 42), (-31, 14, 38)], EDGE)
