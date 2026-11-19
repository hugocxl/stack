from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w2 import board, closed_outline, rule, sparkle

DESCRIPTION = "A page wireframe with a masthead, a feature panel, and two text columns carries a generation sparkle."


def draw(s):
    p = board(s, 91, 100, run=.26, depth=9)
    closed_outline(s, p, rounded(10, 76, 71, 12, 2), EDGE)
    rule(s, p, 16, 82, 33, EDGE)
    closed_outline(s, p, rounded(10, 38, 71, 30, 2), EDGE)
    for start, end in (((12, 39), (79, 67)), ((12, 67), (79, 39))):
        s.line([p(*start), p(*end)], DETAIL)
    for x in (11, 49):
        rule(s, p, x, 27, 27, EDGE)
        rule(s, p, x, 19, 30)
        rule(s, p, x, 11, 22)
    sparkle(s, p, 86, 92, 17)
