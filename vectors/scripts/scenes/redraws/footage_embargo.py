from math import cos, pi, sin

from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import badge

DESCRIPTION = "A film reel with five open spokes carries a padlock badge on its lower rim."


def draw(s):
    s.disk(0, 0, 0, 44, 44, 5)
    s.disk(0, 0, 5, 39, 39, 10, DETAIL)
    holes = [
        [(x, y, 18) for x, y in oval(25*cos(a), 25*sin(a), 9, 9)]
        for a in (i*2*pi/5 for i in range(5))
    ]
    s.face([(x, y, 18) for x, y in oval(0, 0, 44, 44)], EDGE, openings=holes)
    s.ellipse(0, 0, 18, 6, 6, EDGE)
    s.ellipse(0, 0, 18, 3, 3, DETAIL)
    badge(s, "lock", 43, 14, 5, 16)
