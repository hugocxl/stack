from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._sf import shirt

DESCRIPTION = "A T-shirt shows a dashed print area on its chest and carries a plus badge."


def draw(s):
    at = shirt(s, -30, 0, 0, 1.0)
    s.line([at(20, 22), at(40, 22), at(40, 42), at(20, 42), at(20, 22)], DETAIL, dashed=True)
    badge(s, "plus", 22, 0, 6, 11)
