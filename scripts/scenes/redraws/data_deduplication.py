from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w2 import outline, rule

DESCRIPTION = "Two identical data record cards overlap, and a minus badge marks the front copy for removal."


def record(s, x, y, z):
    s.box(x, y - 5, z, 74, 5, 66, 4)
    p = lambda u, v: (x + u, y, z + v)
    outline(s, x + 8, y, z + 42, 13, 13, 2, EDGE)
    rule(s, p, 29, 52, 31, EDGE)
    rule(s, p, 29, 45, 24, DETAIL)
    for v in (32, 21, 10):
        rule(s, p, 8, v, 53, DETAIL)
        rule(s, p, 32, v + 4, 20, EDGE)


def draw(s):
    record(s, 29, -13, 21)
    record(s, 0, 0, 0)
    badge(s, "minus", 70, 0, 30, 15)
