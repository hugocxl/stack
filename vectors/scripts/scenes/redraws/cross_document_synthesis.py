from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w2 import chart_line, folded_sheet, rule

DESCRIPTION = "Two offset source pages sit behind a summary sheet whose two streams of text converge into one."


def draw(s):
    def left(x, z):
        return x*.64 - z*.17 - 12, -x*.36 - 8, z + 4

    def right(x, z):
        return x*.64 + z*.19 + 11, -x*.36 - 6, z + 3

    def front(x, z):
        return x*.7, -x*.3 - z*.11, z

    for page in (left, right):
        folded_sheet(s, page, 78, 86, fold=10, depth=2)
        for z in (62, 53, 44):
            rule(s, page, 7, z, 62)
    folded_sheet(s, front, 84, 83, depth=5)
    for x in (11, 48):
        rule(s, front, x, 59, 24, EDGE)
        rule(s, front, x, 51, 19, DETAIL)
    chart_line(s, front, [(21, 44), (21, 37), (42, 30), (42, 24)], EDGE)
    chart_line(s, front, [(61, 44), (61, 37), (42, 30)], EDGE)
    rule(s, front, 18, 16, 47, BOLD)
    rule(s, front, 18, 9, 34, DETAIL)
