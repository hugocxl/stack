from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w2 import chart_marker, section

DESCRIPTION = "A marker on an open magazine’s engagement scale aligns with the last section reached."


def draw(s):
    s.box(-51, -35, 0, 106, 77, 5, 4)
    def left(x, y):
        return x, y, 6 - x*.15

    def right(x, y):
        return x, y, 6 + x*.19

    s.face([left(x,y) for x, y in ((-50,-35), (0,-35), (0,40), (-50,40))], EDGE)
    s.face([right(x,y) for x, y in ((0,-35), (53,-35), (53,40), (0,40))], EDGE)
    section(s, left, -43, 20, (28, 32, 31, 23))
    section(s, right, 13, -13, (25, 20, 24))
    section(s, right, 13, 18, (25, 20, 17))
    s.line([right(44, -26), right(44, 30)], EDGE)
    for y in (-24, -12, 0, 12, 24):
        s.line([right(44, y), right(49, y)], DETAIL)
    chart_marker(s, right, 44, 18, 5.7, BOLD)
