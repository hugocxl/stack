from geometry import DETAIL, EDGE
from scenes.redraws._kit import glyph

DESCRIPTION = "An open guidebook shows three checklist rows on its right-hand page."


def draw(s):
    s.box(-50, -27, 0, 100, 56, 4, 3)

    def left(x, y):
        return (x, y, 5 - x * .17 + (26 - y) * .35)

    def right(x, y):
        return (x, y, 5 + x * .17 + (26 - y) * .35)

    for page, start, finish in ((left, -47, 0), (right, 0, 47)):
        corners = [(start, -24), (finish, -24), (finish, 26), (start, 26)]
        s.face([page(x, y) for x, y in corners], EDGE)
        s.face([page(start, 26), page(finish, 26),
                (finish, 26, 4), (start, 26, 4)], EDGE)
    s.face([right(47, -24), right(47, 26), (47, 26, 4), (47, -24, 4)], EDGE)

    for y, width in ((-12, 30), (0, 25), (10, 30), (19, 18)):
        s.line([left(-39, y), left(-39 + width, y)], DETAIL)
    for y, width in ((-12, 22), (2, 17), (16, 21)):
        box = [(6, y - 3.7), (15, y - 3.7), (15, y + 3.7), (6, y + 3.7)]
        s.line([right(x, v) for x, v in [*box, box[0]]], EDGE)
        s.line([right(20, y), right(20 + width, y)], DETAIL)
    x, y, z = right(10, -12)
    glyph(s, "check", x, y, z, 3.6)
