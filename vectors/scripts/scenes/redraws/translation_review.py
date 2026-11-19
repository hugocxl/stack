from geometry import BOLD, EDGE, oval
from scenes.redraws._w3 import Surface
from scenes.redraws.line_focus_aid import reading_book

DESCRIPTION = "A magnifying glass reviews a line in the right-aligned translation of an open bilingual proof."


def draw(s):
    left, right = reading_book(s)
    left.rules(7, 58, [22], ink=EDGE)
    left.rules(7, 47, [27, 25, 27, 19, 23], gap=8)
    right.rules(18, 58, [22], ink=EDGE)
    for x, v in ((11, 47), (8, 39), (14, 31), (9, 23), (18, 15)):
        right.rules(x, v, [(37 - x) * .47])
        right.rules(x + (37 - x) * .65, v, [40 - x - (37 - x) * .65])

    lens = Surface(s, right.point(0, 0, -2), rise=right.rise, back=right.back)
    s.tube([lens.point(34, 30), lens.point(46, 13)], 3, EDGE)
    place = lens.viewer_axes(27, 41)
    outer = [lens.point(*place(a, b)) for a, b in oval(0, 0, 13, 13)]
    inner = [lens.point(*place(a, b)) for a, b in oval(0, 0, 10, 10)]
    s.face(outer, BOLD, openings=[inner])
