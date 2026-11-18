from math import cos, pi, sin

from geometry import BOLD, EDGE, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "A large asterisk sits beside the label of a single required form field."


def field(s):
    """The shared labeled field in a thick, sloped control housing."""
    face = Surface(s, (0, 0, 2), rise=(-.62, .78), back=(0, -.78, -.62))
    face.plate(rounded(0, 0, 81, 54, 6), 8)
    face.rect(9, 10, 63, 20, 3, EDGE)
    face.rules(15, 20, [32])
    face.rules(10, 40, [30], ink=EDGE)
    return face


def draw(s):
    face = field(s)
    place = face.viewer_axes(50, 40)
    for angle in (pi / 6, pi / 2, 5 * pi / 6):
        u, v = 6 * cos(angle), 6 * sin(angle)
        face.stroke([place(-u, -v), place(u, v)], BOLD)
