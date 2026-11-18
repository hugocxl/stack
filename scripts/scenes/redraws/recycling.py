from math import cos, radians, sin

from geometry import BOLD, EDGE, rounded

DESCRIPTION = "A lidded collection bin displays a large three-arrow recycling symbol."


def recycling_mark(s, x, y, z, size):
    """Print the three chasing arrows on the front of the bin."""
    arrow = [(-.52, .08), (-.12, .78), (.12, .78), (.42, .26), (.53, .33),
             (.55, -.02), (.24, .16), (.32, .21), (.03, .65), (-.03, .65), (-.4, .01)]
    for rotation in (0, 120, 240):
        c, d = cos(radians(rotation)), sin(radians(rotation))
        s.line([(x + (c * a - d * b) * size, y, z + (d * a + c * b) * size)
                for a, b in arrow + arrow[:1]], BOLD)


def bin_body(s):
    s.solid(rounded(-23, -17, 46, 35, 2), 0, 55, rounded(-27, -20, 54, 41, 3))
    recycling_mark(s, 0, 20, 27, 21)


def draw(s):
    bin_body(s)
    s.box(-29, -22, 55, 58, 45, 5, 3)
    s.tube([(-10, 8, 60), (-10, 8, 65), (10, 8, 65), (10, 8, 60)], 1.4, EDGE)
