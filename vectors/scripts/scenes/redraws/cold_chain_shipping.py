from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._w1 import insulated_cooler

DESCRIPTION = "A thermometer is mounted on the front wall of an insulated shipping cooler."


def draw(s):
    insulated_cooler(s)
    s.box(-13, 22, 3, 28, 2.5, 31, 2)
    y = 24.5
    bulb = oval(0, 10, 5.4, 5.4, 123.75, 416.25, count=32)
    cap = oval(0, 26, 3, 3, 0, 180, count=12)
    s.line([(x, y, z) for x, z in [*bulb, *cap, bulb[0]]], EDGE)
    s.line([(0, y, 8), (0, y, 22)], BOLD)
    for z in (15, 20, 25):
        s.line([(7, y, z), (12, y, z)], DETAIL)
