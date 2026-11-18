from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w2 import closed_outline, rule, standing_notebook

DESCRIPTION = "A bound template shows three repeating blocks of heading and body placeholders."


def draw(s):
    p = standing_notebook(s, 93, 110)
    for z0 in (73, 42, 11):
        closed_outline(s, p, rounded(10, z0, 73, 24, 2), EDGE)
        rule(s, p, 18, z0 + 17, 31, EDGE)
        rule(s, p, 18, z0 + 10, 56, DETAIL)
        rule(s, p, 18, z0 + 5, 43, DETAIL)
