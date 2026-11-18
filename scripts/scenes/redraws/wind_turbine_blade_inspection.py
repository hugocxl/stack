from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._w1 import turbine

DESCRIPTION = "An inline magnifier frames the tip of a wind turbine blade."


def draw(s):
    turbine(s, 0, 0, 0, 53)
    x, y, z = 17, 3, 81
    s.tube([(x + 10, y, z - 12), (x + 22, y, z - 26)], 3.1, EDGE)
    for radius, ink in ((16, BOLD), (13, DETAIL)):
        s.line([(a, y, b) for a, b in oval(x, z, radius, radius, count=56)], ink)
