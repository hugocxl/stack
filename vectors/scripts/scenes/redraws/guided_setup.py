from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._w1 import laptop

DESCRIPTION = "A laptop shows three connected setup steps with the middle step highlighted."


def draw(s):
    y = laptop(s, -38, 0, w=76, h=52, depth=32)
    s.line([(-23, y, 35), (23, y, 35)], EDGE)
    for x in (-23, 0, 23):
        radius = 7.5 if x == 0 else 5
        s.face([(a, y, b) for a, b in oval(x, 35, radius, radius, count=24)[:-1]],
               BOLD if x == 0 else EDGE)
    s.line([(a, y, b) for a, b in oval(0, 35, 3.4, 3.4, count=24)], EDGE)
    for x in (-23, 0, 23):
        s.line([(x - 4.5, y, 20), (x + 4.5, y, 20)], DETAIL)
