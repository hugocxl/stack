from geometry import EDGE, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "An open mail tray with a scooped front contains only a dashed envelope outline on its floor."


def inbox_tray(s, art=None):
    """Build an open letter tray, then draw its near walls over the floor."""
    s.box(0, 0, 0, 78, 62, 5, 4)
    s.box(3, 3, 5, 72, 4, 19, 1)
    s.face([(3, 7, 5), (3, 58, 5), (3, 58, 15), (3, 7, 24)], EDGE)
    s.face([(3, 7, 24), (3, 58, 15), (7, 58, 15), (7, 7, 24)], EDGE)
    inside = Surface(s, (0, 62, 5), rise=(-1, 0))
    if art is not None:
        art(inside)

    s.face([(75, 7, 5), (75, 58, 5), (75, 58, 15), (75, 7, 24)], EDGE)
    s.face([(71, 7, 24), (71, 58, 15), (75, 58, 15), (75, 7, 24)], EDGE)
    front = Surface(s, (0, 60, 5))
    front.plate([(3, 0), (75, 0), (75, 10), (56, 10), (50, 4),
                 (28, 4), (22, 10), (3, 10)], 3)
    return inside


def envelope_outline(floor):
    floor.stroke(rounded(18, 17, 42, 30, 2), EDGE, closed=True, dashed=True)
    floor.stroke([(19, 45), (39, 29), (59, 45)], EDGE, dashed=True)


def draw(s):
    inbox_tray(s, envelope_outline)
