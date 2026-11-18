from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w2 import chart_marker, rule, standing_notebook

DESCRIPTION = "Two symbol-keyed cohort rows align their values under four shared time columns."


def draw(s):
    p = standing_notebook(s, 137, 83)
    for z in (13, 36, 59):
        rule(s, p, 9, z, 119, EDGE)
    for x in (29, 54, 79, 104):
        s.line([p(x, 13), p(x, 59)], DETAIL)
    for x in (42, 66, 91, 116):
        s.line([p(x, 63), p(x, 68)], EDGE)
    chart_marker(s, p, 18, 48, 5, EDGE)
    s.face([p(18, 30), p(24, 24), p(18, 18), p(12, 24)], EDGE)
    for z, values in ((45, (13, 12, 8, 5)), (21, (10, 8, 7, 6))):
        for x, h in zip((42, 66, 91, 116), values):
            s.line([p(x - 5, z), p(x - 5, z + h*.53),
                    p(x + 5, z + h*.53), p(x + 5, z)], BOLD if h == 13 else EDGE)
