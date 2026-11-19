from geometry import EDGE, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "Two overlapping speech balloons point toward opposite sides of a conversation."


def balloon(s, origin, width, height, *, right=False, depth=5):
    """An extruded speech balloon with a tail integrated into its lower edge."""
    outline = rounded(0, 0, width, height, height * .22)
    tail = [(width * .38, 0), (width * .15, -height * .33), (width * .16, 0)]
    if right:
        tail = [(width - x, v) for x, v in reversed(tail)]
    # The rounded rectangle starts with its lower-right arc and ends with
    # its lower-left arc, so the closing edge runs left to right.
    face = Surface(s, origin)
    face.plate(outline + tail[::-1], depth, EDGE)
    return face


def draw(s):
    balloon(s, (28, -8, 13), 76, 46, right=True)
    front = balloon(s, (0, 0, 41), 76, 46)
    for x in (24, 38, 52):
        front.oval(x, 23, 2.7, 2.7)
