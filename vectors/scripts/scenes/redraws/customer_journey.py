from math import cos, pi, sin

from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import badge

DESCRIPTION = "A winding route leads from an entry ring past a midpoint marker to a checked final stop."


def draw(s):
    # Concentric turns connect two straight runs without abrupt corners.
    first = [(0, 0, 0), (43, 0, 0)]
    first += [(43 + 18*cos(pi*i/24 - pi/2), 18 + 18*sin(pi*i/24 - pi/2), 0)
              for i in range(1, 25)]
    first.append((18, 36, 0))
    middle = (29, 36, 0)
    last = [(18 + 17*cos(-pi*i/24 - pi/2), 53 + 17*sin(-pi*i/24 - pi/2), 0)
            for i in range(1, 25)]
    route = [*first, *last, (85, 70, 0)]
    s.line(route, BOLD)
    s.disk(0, 0, 0, 7, 7, 3, EDGE)
    s.ellipse(0, 0, 3, 3.7, 3.7, DETAIL)
    s.disk(*middle, 5.5, 5.5, 2, EDGE)
    s.line([(27, 36, 2), (31, 36, 2)], BOLD)
    badge(s, "check", 88, 70, 13, 14)
