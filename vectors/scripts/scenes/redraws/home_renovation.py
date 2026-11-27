from geometry import DETAIL, EDGE
from scenes.redraws._sf import house

DESCRIPTION = "A gabled house shows exposed studs on one half of its front wall and finished siding on the other."


def draw(s):
    w, h = 76, 40
    front = house(s, -38, -28, 0, w, 52, h, 28)
    for u in range(6, 36, 7):
        s.line([front(u, 1), front(u, h - 2)], DETAIL)
    s.line([front(3, h - 4), front(38, h - 4)], DETAIL)
    s.line([front(38, 0), front(38, h)], EDGE)
    for v in range(5, h - 1, 5):
        s.line([front(38, v), front(w - 2, v)], DETAIL)
    s.face([front(48, 0), front(62, 0), front(62, 24), front(48, 24)], EDGE)
