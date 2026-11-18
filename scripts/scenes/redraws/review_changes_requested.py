from geometry import BOLD, DETAIL, rounded
from scenes.redraws._kit import warning
from scenes.redraws._w2 import closed_outline, folded_sheet, rule

DESCRIPTION = "A warning triangle points out a boxed line on a folded review sheet."


def draw(s):
    def point(x, z):
        return .63*x, -.37*x - .20*z, .95*z

    folded_sheet(s, point, 76, 101, fold=15, depth=5)
    rule(s, point, 12, 77, 30)
    rule(s, point, 12, 63, 48)
    closed_outline(s, point, rounded(9, 37, 45, 15, 2), BOLD)
    rule(s, point, 15, 44.5, 32, DETAIL)
    rule(s, point, 12, 24, 47)
    rule(s, point, 12, 13, 28)
    warning(s, *point(74, 38), size=32)
