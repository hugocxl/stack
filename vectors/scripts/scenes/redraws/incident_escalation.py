from geometry import EDGE
from scenes.redraws._kit import arrow, warning

DESCRIPTION = "An upward arrow rises along the edge of a standing incident warning triangle."


def draw(s):
    warning(s, 26, 0, 0, 52)
    arrow(s, [(57, 0, 5), (57, 0, 49)], EDGE, head=10)
