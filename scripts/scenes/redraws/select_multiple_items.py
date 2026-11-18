from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w2 import closed_outline, draft_notebook, printed_glyph, rule

DESCRIPTION = "A spiral-bound item list shows checked boxes on two of its three rows."


def draw(s):
    point = draft_notebook(s)
    for index, z in enumerate((66, 45, 24)):
        closed_outline(s, point, rounded(15, z - 7, 14, 14, 1.5), EDGE)
        rule(s, point, 40, z, (26, 17, 30)[index], EDGE)
        if index != 1:
            printed_glyph(s, point, "check", 22, z, 7, BOLD)
    for z in (55, 34):
        rule(s, point, 13, z, 59, DETAIL)
