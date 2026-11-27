from geometry import DETAIL, EDGE, oval
from scenes.redraws._sf import ground, plate, smooth, turned

DESCRIPTION = "A magnifier hovers over a halved avocado, its round pit showing in the cut face."


def draw(s):
    shape = smooth([(0, -38), (19, -28), (23, -8), (15, 12), (8, 30), (0, 35), (-8, 30), (-15, 12), (-23, -8), (-19, -28)], 6, closed=True)
    top = ground(0, 0, 12)
    plate(s, top, shape, 12, (0, 0, -1))
    s.line([top(u*.8, v*.8 - 2) for u, v in shape] + [top(shape[0][0]*.8, shape[0][1]*.8 - 2)], DETAIL)
    turned(s, [(11, 0), (10, 4.5), (6.5, 8.5), (.4, 10)], 0, -12, 12, steps=3)
    ring = [(28 + 22*__import__("math").cos(a/10), -24 + 22*__import__("math").sin(a/10), 44) for a in range(0, 63)]
    s.tube(ring + ring[:1], 2.6, EDGE)
    s.tube([(46, -12, 44), (70, 4, 40)], 3, EDGE)
