from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w5 import mountain_mark, rect

DESCRIPTION = "A two-post trailhead kiosk shelters a framed map with branching trail lines under a pitched roof."


def draw(s):
    for x in (0, 54):
        s.box(x, 0, 0, 6, 8, 63, 1)
    s.box(0, 0, 16, 60, 8, 39, 1.5)
    face = lambda x, z: (x, 8, z)
    rect(s, face, 4, 20, 52, 31, 1.5)
    mountain_mark(s, face, 19, 43, .68, DETAIL)
    s.line([face(x, z) for x, z in
            ((12, 25), (22, 30), (34, 29), (42, 35), (45, 44), (51, 46))], BOLD)
    s.line([face(x, z) for x, z in ((34, 29), (30, 36), (33, 44))], EDGE, dashed=True)
    s.face([(-5, -8, 59), (-5, 3, 72), (-5, 14, 59)])
    s.face([(-5, -8, 59), (65, -8, 59), (65, 3, 72), (-5, 3, 72)])
    s.face([(-5, 3, 72), (65, 3, 72), (65, 14, 59), (-5, 14, 59)])
    s.face([(65, -8, 59), (65, 3, 72), (65, 14, 59)])
    s.line([(-4, 14, 57.4), (65, 14, 57.4), (65, 14, 59)], DETAIL)
