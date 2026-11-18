from geometry import BOLD, DETAIL
from scenes.redraws._kit import arrow
from scenes.redraws._w1 import portrait_mark, screen_point

DESCRIPTION = "An inward arrow points into an organization directory with three member portraits."


def draw(s):
    s.box(-27, -10, 0, 54, 10, 69, 3)
    for z, width in ((54, 23), (35, 18), (16, 22)):
        portrait_mark(s, -14, 0, z, 7)
        s.line([(-1, 0, z + 2), (-1 + width, 0, z + 2)], DETAIL)
        s.line([(-1, 0, z - 3), (9, 0, z - 3)], DETAIL)
    origin = (-26, 0, 35)
    arrow(s, [screen_point(*origin, u, 0) for u in (-27, -1)], BOLD, head=10)
