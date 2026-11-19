from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w2 import closed_outline, laptop, profile_mark, rule

DESCRIPTION = "A right-arrow badge attaches to the owner field of a workspace window on an open laptop."


def draw(s):
    point = laptop(s, 114, 79)
    rule(s, point, 6, 69, 102, EDGE)
    for x in (12, 19, 26):
        rule(s, point, x, 74, 2, EDGE)
    s.line([point(36, 11), point(36, 69)], DETAIL)
    for z, length in ((59, 14), (48, 12), (37, 15)):
        rule(s, point, 13, z, length)
    rule(s, point, 46, 58, 47, EDGE)
    rule(s, point, 46, 49, 32, DETAIL)
    closed_outline(s, point, rounded(45, 17, 59, 20, 3), EDGE)
    profile_mark(s, point, 55, 27, 7)
    rule(s, point, 66, 27, 25)
    badge(s, "arrow", *point(111, 27), 15)
