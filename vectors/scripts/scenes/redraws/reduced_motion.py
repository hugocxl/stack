from geometry import EDGE, GUIDE, oval
from scenes.redraws._kit import badge

DESCRIPTION = "A pause badge overlaps a spinning top traced by two short motion arcs."


def draw(s):
    s.ellipse(0, 0, 19, 41, 41, GUIDE, start=165, end=227)
    s.ellipse(0, 0, 19, 40, 40, GUIDE, start=319, end=384)
    s.solid(oval(0, 0, 2, 2)[:-1], 0, 24, oval(0, 0, 29, 29)[:-1], crease=False)
    s.disk(0, 0, 24, 29, 29, 6)
    s.ellipse(0, 0, 30, 28, 28, EDGE)
    s.disk(0, 0, 29, 5, 5, 20)
    s.ellipse(0, 0, 49, 5, 5, EDGE)
    badge(s, "pause", 27, -9, 42, 14)
