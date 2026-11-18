from math import sqrt

from geometry import BOLD, GUIDE, rounded
from scenes.redraws._kit import _strokes
from scenes.redraws._w3 import Surface, selection_handle

DESCRIPTION = "A content card sits inside a dashed bounding frame whose lower corner extends along a diagonal resize arrow."


def draw(s):
    card = Surface(s, (0, 0, 0), rise=(-.53, .85), back=(0, -.85, -.53),
                   across=(.98, -.2))
    card.plate(rounded(0, 0, 80, 57, 6), 7)
    card.rules(12, 42, [40], ink=BOLD)
    card.rules(12, 29, [52, 42, 49], gap=8)
    card.stroke([(0, 0), (99, 0), (99, 69), (0, 69), (0, 0)], GUIDE, dashed=True)
    # The diagonal uses the kit's arrow, rotated in the viewer's plane.
    place = card.viewer_axes(88, 8)
    for stroke in _strokes("arrow", 17):
        card.stroke([place((u + v) / sqrt(2), (v - u) / sqrt(2)) for u, v in stroke], BOLD)
    selection_handle(card, 0, 69, 5)
