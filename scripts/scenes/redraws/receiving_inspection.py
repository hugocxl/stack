from geometry import BOLD, DETAIL, EDGE, oval
from scenes.commerce_objects import crushed

DESCRIPTION = "A handheld magnifier frames the torn corner of a shipping carton."


def draw(s):
    crushed(s)
    s.line([(4, 18, 28), (5, 18, 23), (1, 18, 21), (3, 18, 17)], BOLD)
    s.line([(-10, -17, 38), (-9, 12, 38)], DETAIL)
    s.line([(-4, -17, 38), (-3, 12, 38)], DETAIL)

    x, y, z = 11, 26, 31
    s.tube([(x + 11, y, z - 11), (x + 27, y, z - 27)], 3.8, EDGE)
    outer = [(a, y, b) for a, b in oval(x, z, 16.5, 16.5, count=48)[:-1]]
    lens = [(a, y, b) for a, b in oval(x, z, 13.3, 13.3, count=48)[:-1]]
    s.face(outer, EDGE, openings=(lens,))
    s.line([(a, y, b) for a, b in oval(x, z, 10.5, 10.5, 75, 142, count=12)], DETAIL)
