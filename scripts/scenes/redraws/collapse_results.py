from geometry import BOLD, EDGE
from scenes.redraws._w4 import standing_card

DESCRIPTION = "A compact results list has three result rows beneath a header with a prominent upward collapse chevron."


def disclosure(face, u, v, *, up, size=8):
    """Print an open disclosure chevron on a control surface."""
    spread = size*.65
    sign = 1 if up else -1
    face.line([(u - size, v - sign*spread/2), (u, v + sign*spread/2),
               (u + size, v - sign*spread/2)], BOLD)


def draw(s):
    list_face = standing_card(s, 84, 69, angle=-2, lean=.17, depth=7)
    list_face.rows(10, 55, (30,), ink=EDGE)
    list_face.rows(0, 44, (84,), ink=EDGE)
    disclosure(list_face, 69, 55, up=True)
    for v, length in ((34, 44), (22, 35), (10, 40)):
        list_face.frame(11, v - 2.5, 5, 5, 1, EDGE)
        list_face.rows(23, v, (length,))
