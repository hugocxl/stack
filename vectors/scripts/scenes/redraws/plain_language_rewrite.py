from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import arrow
from scenes.redraws._w2 import folded_sheet, rule

DESCRIPTION = "A downward rewrite arrow connects a dense paragraph to two short lines on the same document."


def draw(s):
    def p(x, z):
        return .30*x, -.70*x - .39*z, .84*z

    folded_sheet(s, p, 94, 97, fold=15, depth=8)
    for z, length in ((77, 60), (71, 67), (65, 63), (59, 65), (53, 45)):
        rule(s, p, 13, z, length, DETAIL)
    arrow(s, [p(45, 48), p(45, 30)], BOLD, head=5.1)
    rule(s, p, 13, 21, 57, EDGE)
    rule(s, p, 13, 12, 32, EDGE)
