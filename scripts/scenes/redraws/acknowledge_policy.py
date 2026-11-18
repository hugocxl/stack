from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge

DESCRIPTION = "An open policy booklet has two ruled pages and a check badge at the bottom of the right page."


def draw(s):
    s.box(-37, -27, 0, 74, 54, 4, 2)
    for side in (-1, 1):
        profile = [(0, 5), (8, 11), (24, 12), (34, 9)]
        s.face([(side * x, y, z) for y, run in ((-24, profile), (24, reversed(profile)))
                for x, z in run], EDGE)
        s.face([(0, 24, 4), (side * 34, 24, 4),
                *[(side * x, 24, z) for x, z in reversed(profile)]], EDGE)
        for y, end in ((-15, 27), (-6, 29), (3, 25), (12, 21)):
            s.line([(side * 10, y, 11.125), (side * min(end, 24), y, 12)], DETAIL)
            if end > 24:
                s.line([(side * 24, y, 12), (side * end, y, 12 - .3 * (end - 24))], DETAIL)
    badge(s, "check", 31, 23, 11, 12)
