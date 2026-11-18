from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w3 import paper, rule, upright

DESCRIPTION = "A reading guide frames one line on a page of short, widely spaced lines."


def draw(s):
    paper(s, 77, 93)

    for z, end in ((76, 49), (64, 60), (33, 44), (21, 59), (9, 37)):
        rule(s, 11, end, z, DETAIL)
    rule(s, 11, 61, 49, EDGE)

    # The guide is a separate strip with a window over the active line.
    outer = rounded(3, 40, 87, 18, 3)
    window = rounded(8, 45, 63, 8, 2)
    s.face(upright(outer, 1), BOLD, openings=[upright(window, 1)])
