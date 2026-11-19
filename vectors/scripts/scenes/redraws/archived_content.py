from geometry import EDGE
from scenes.redraws._w3 import Surface

DESCRIPTION = "A lidded archive box has a recessed pull handle and a folded-corner document label on its front."


def draw(s):
    s.box(0, 0, 0, 77, 52, 38, 2)
    s.box(-2, -2, 33, 81, 56, 11, 2)
    front = Surface(s, (0, 52, 0))
    front.rect(26, 25, 25, 5, 2.5, EDGE)
    front.stroke([(25, 5), (51, 5), (51, 16), (45, 21), (25, 21)], EDGE, closed=True)
    front.stroke([(45, 21), (45, 16), (51, 16)])
    front.rules(29, 14, [12, 17], gap=4)
