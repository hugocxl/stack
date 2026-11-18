from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w2 import outline, profile_mark, rule

DESCRIPTION = "A standing customer ID card pairs a group pictogram with three trait bars."


def draw(s):
    s.box(0, -20, 0, 98, 34, 11, 4)
    s.box(7, -5, 9, 84, 5, 70, 5)
    outline(s, 35, 0, 66, 28, 6, 2, DETAIL)
    p = lambda x, z: (x, 0, z)
    profile_mark(s, p, 20, 45, 12)
    profile_mark(s, p, 35, 45, 12)
    profile_mark(s, p, 27.5, 30, 13, EDGE)
    s.line([p(49, 19), p(49, 55)], DETAIL)
    for z, length in ((49, 29), (38, 17), (27, 23)):
        rule(s, p, 56, z, length, BOLD if length == 29 else EDGE)
        rule(s, p, 56, z - 2, length, DETAIL)
