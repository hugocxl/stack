from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge

DESCRIPTION = "A stepped office tower with rows of windows carries a star on its upper facade."


def draw(s):
    s.box(0, 0, 0, 53, 34, 84, 2)
    s.box(5, 4, 84, 40, 25, 10, 2)
    s.box(12, 8, 94, 24, 16, 6, 1)
    for floor in (22, 39, 56, 73):
        for x in (8, 22, 36):
            s.face([(x, 34, floor), (x + 8, 34, floor),
                    (x + 8, 34, floor + 9), (x, 34, floor + 9)], DETAIL)
        for y in (7, 20):
            s.face([(53, y, floor), (53, y + 7, floor),
                    (53, y + 7, floor + 9), (53, y, floor + 9)], DETAIL)
    s.line([(18, 34, 1), (18, 34, 13), (34, 34, 13), (34, 34, 1)], EDGE)
    s.line([(26, 34, 1), (26, 34, 13)])
    badge(s, "star", 53, 2, 77, 15)
