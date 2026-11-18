from geometry import BOLD, DETAIL, EDGE, oval, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w4 import front_surface

DESCRIPTION = "A freestanding eye chart displays descending rows of broken-ring optotypes with a clock badge at its upper corner."


def draw(s):
    face = front_surface(s, angle=-38, z=6, lean=.18)
    for u in (7, 59):
        x, y, _ = face.at(u, 0)
        s.box(x - 5, y - 8, 0, 10, 16, 6, 2)
    face.slab(rounded(0, 0, 66, 80, 3), 5)
    for v, radius, placements, ink in (
        (62, 11, ((33, 0),), BOLD),
        (41, 6, ((23, 90), (43, 180)), EDGE),
        (25, 4.5, ((17, 270), (33, 0), (49, 90)), EDGE),
        (12, 3.2, ((13, 180), (26, 270), (40, 90), (53, 0)), DETAIL),
    ):
        for u, gap in placements:
            face.line(oval(u, v, radius, radius, gap + 33, gap + 327, 38), ink)
    badge(s, "clock", *face.at(63, 71), 12)
