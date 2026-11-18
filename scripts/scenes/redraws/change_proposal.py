from geometry import EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w2 import closed_outline, folded_sheet, rule

DESCRIPTION = "A proposal sheet has a single outlined insertion between its existing lines, with a plus badge at the insertion."


def draw(s):
    def point(x, z):
        return .88*x, -.12*x - .45*z, .89*z

    folded_sheet(s, point, 80, 95, depth=7)
    rule(s, point, 13, 77, 33, EDGE)
    for z, length in ((62, 54), (53, 45), (24, 51), (15, 36)):
        rule(s, point, 13, z, length)
    closed_outline(s, point, rounded(11, 31, 57, 14, 2.5), EDGE)
    rule(s, point, 17, 38, 34, EDGE)
    badge(s, "plus", *point(74, 38), 15)
