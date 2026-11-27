from geometry import DETAIL
from scenes.redraws._kit import badge
from scenes.redraws._sf import left_face

DESCRIPTION = "A flat-roofed building with rows of windows carries a refresh badge for upkeep."


def draw(s):
    s.box(-34, -26, 0, 68, 52, 76, 2)
    s.box(-37, -29, 76, 74, 58, 5, 2)
    front = left_face(-34, 26, 0)
    for v in (16, 34, 52):
        for u in (10, 30, 50):
            s.line([front(u, v), front(u + 9, v), front(u + 9, v + 11), front(u, v + 11), front(u, v)], DETAIL)
    badge(s, "refresh", 34, 26, 12, 13)
