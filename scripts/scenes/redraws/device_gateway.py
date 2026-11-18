from geometry import DETAIL, EDGE
from scenes.systems_shapes import bezel, rectangle

DESCRIPTION = "A network gateway has two upright antennas and two cables plugged into its front ports."


def draw(s):
    for x in (-25, 25):
        s.tube([(x, -20, 14), (x, -20, 29), (x * 1.22, -23, 48)], 2.8, EDGE)
    s.box(-32, -24, 0, 64, 48, 21, 4)
    rectangle(s, -22, -13, 21, 44, 24, DETAIL, 3)
    for x in (-14, 14):
        bezel(s, x - 6, 24, 5, 12, 10, EDGE, 1.5)
        s.box(x - 4, 24, 6, 8, 8, 8, 1.2)
        s.tube([(x, 31, 10), (x, 40, 10), (x + 5, 48, 8)], 2.4)
    for x in (-4, 0, 4):
        s.line([(x, 24, 14), (x, 24, 12)], DETAIL)
