from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w2 import closed_outline, folded_sheet, rule

DESCRIPTION = "An attached check badge marks the selected outcome on a workshop decision sheet."


def draw(s):
    def point(x, z):
        return .71*x, -.29*x - .48*z, .82*z

    folded_sheet(s, point, 102, 90, fold=13, depth=7)
    rule(s, point, 12, 73, 43, EDGE)
    for z, width in ((53, 56), (34, 43), (15, 51)):
        rule_ink = EDGE if z == 34 else DETAIL
        closed_outline(s, point, rounded(11, z - 7, 64, 14, 2), rule_ink)
        rule(s, point, 15, z, width - 8, rule_ink)
    badge(s, "check", *point(79, 35), 15)
