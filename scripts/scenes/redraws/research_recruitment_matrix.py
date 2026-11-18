from geometry import DETAIL, EDGE
from scenes.redraws._kit import glyph
from scenes.redraws._w2 import profile_mark, rule, standing_notebook

DESCRIPTION = "A recruitment notebook lines up three profile headers above a grid of criterion checks."


def draw(s):
    p = standing_notebook(s, 119, 100)
    for z in (12, 29, 46, 63):
        rule(s, p, 9, z, 103, EDGE if z == 63 else DETAIL)
    for x in (39, 62, 85):
        s.line([p(x, 12), p(x, 63)], DETAIL)
    for x in (50, 74, 98):
        profile_mark(s, p, x, 76, 11)
    for z, length, columns in ((54, 21, (50, 98)), (37, 16, (74, 98)), (20, 19, (50,))):
        rule(s, p, 11, z, length, EDGE)
        for x in columns:
            glyph(s, "check", *p(x, z), 7.5, EDGE)
