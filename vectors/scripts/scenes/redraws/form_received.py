from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import arrow
from scenes.redraws._w5 import panel, rect

DESCRIPTION = "A submitted form has a downward arrow entering an inbox mark at its lower edge."


def draw(s):
    # The layered paper and bent foot give the form a stable freestanding stance.
    face = lambda x, z: (x, 8 - .62*z, z)
    panel(s, [(0, 0), (58, 0), (58, 65), (0, 65)], face, 5.6)
    for z in (30, 41, 52):
        rect(s, face, 8, z - 2.5, 5.5, 5, .7, EDGE)
        s.line([face(18, z), face(47, z)], DETAIL)
    s.line([face(7, 59), face(33, 59)], EDGE)
    s.line([face(15, 17), face(11, 13), face(11, 4), face(47, 4),
            face(47, 13), face(42, 17)], EDGE)
    s.line([face(11, 13), face(23, 13), face(26, 9), face(33, 9),
            face(36, 13), face(47, 13)], EDGE)
    arrow(s, [face(29, 25), face(29, 13)], BOLD, head=5.4)
