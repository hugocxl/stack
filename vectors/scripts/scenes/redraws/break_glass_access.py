from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w5 import key_mark

DESCRIPTION = "A wall-mounted key box holds a large key behind a cracked glass pane."


def draw(s):
    outer = lambda x, z: (x, 0, z)
    inside = lambda x, z: (x, -2, z)
    s.box(3, -15, 2, 46, 15, 62, 2.3)
    window = rounded(9, 9, 34, 48, 1.8)
    frame = rounded(3, 2, 46, 62, 2.3)
    s.face([outer(x, z) for x, z in frame], EDGE,
           openings=[[outer(x, z) for x, z in window]])
    s.line([inside(24, 46), inside(24, 53), inside(28, 53)], DETAIL)
    key_mark(s, inside, 24, 40, 1.1, angle=-79)
    s.line([outer(40, 57), outer(36, 48), outer(39, 43), outer(32, 36),
            outer(36, 29), outer(31, 24), outer(27, 9)], BOLD)
    s.line([outer(39, 43), outer(43, 42)], EDGE)
    s.line([outer(36, 29), outer(43, 26)], EDGE)
