from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface, classroom_desk

DESCRIPTION = "Four separated exam desks sit inside a classroom cutaway with a check badge at its open doorway."


def draw(s):
    s.box(0, 0, 0, 94, 80, 3, 1)
    s.box(0, 0, 3, 94, 4, 53, 1)
    wall = Surface(s, (0, 4, 3))
    wall.rect(24, 29, 43, 19, 1, EDGE)
    wall.rules(29, 35, [32])
    s.box(0, 4, 3, 4, 76, 53, 1)
    window = [(4, y, z) for y, z in ((17, 25), (39, 25), (39, 47), (17, 47))]
    s.face(window, EDGE)
    s.line([(4, 28, 25), (4, 28, 47)], EDGE)
    for y in (13, 44):
        for x in (15, 45):
            classroom_desk(s, x, y, .72)
    s.box(79, 77, 3, 4, 4, 42, 1)
    # The opening is spanned by a lintel, so it has a clear entry threshold.
    s.box(79, 51, 42, 4, 30, 5, 1)
    s.box(79, 50, 3, 4, 4, 42, 1)
    s.box(80, 50, 3, 11, 31, 2, 1)
    badge(s, "check", 99, 55, 12, 12)
