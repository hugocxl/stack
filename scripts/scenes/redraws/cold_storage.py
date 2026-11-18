from math import cos, radians, sin

from geometry import BOLD, DETAIL, EDGE
from scenes.systems_shapes import bezel

DESCRIPTION = "A lidded archival box has a snowflake centered on its front label plate."


def draw(s):
    s.box(-34, -26, 0, 68, 52, 38, 3)
    s.box(-36, -28, 35, 72, 56, 8, 2)
    bezel(s, -21, 26, 4, 42, 29, EDGE, 2)
    s.line([(34, -7, 22), (34, 7, 22)], EDGE)
    s.line([(34, -5, 19), (34, 5, 19)], DETAIL)
    for angle in range(0, 360, 60):
        angle = radians(angle)
        u, v = cos(angle), sin(angle)
        s.line([(0, 26, 18), (12 * u, 26, 18 + 12 * v)], BOLD)
        s.line([(7 * u - 2.2 * v, 26, 18 + 7 * v + 2.2 * u),
                (10 * u, 26, 18 + 10 * v),
                (7 * u + 2.2 * v, 26, 18 + 7 * v - 2.2 * u)], BOLD)
