from math import cos, radians, sin

from geometry import EDGE, oval, rounded
from scenes.redraws._w3 import Surface, component_art

DESCRIPTION = "Two open ends of a broken chain separate at the corner of a thick component tile."


def draw(s):
    tile = Surface(s, (0, 0, 0), rise=(-.48, .88), back=(0, -.88, -.48),
                   across=(.96, -.28))
    tile.plate(rounded(0, 0, 72, 65, 8), 9)
    component_art(tile, 34, 29, 38, 34, EDGE)

    links = Surface(s, tile.point(64, 58, -5))
    place = links.viewer_axes(0, 0)
    c, q = cos(radians(31)), sin(radians(31))
    # Open capsules face one another across an air gap.
    loop = [(4, 5), *oval(14, 0, 5, 5, 90, -90, 22), (4, -5)]
    for sign in (-1, 1):
        points = [place(sign * (c * u - q * v), sign * (q * u + c * v)) for u, v in loop]
        s.tube([links.point(*p) for p in points], 1.8, EDGE)
