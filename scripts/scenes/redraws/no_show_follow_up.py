from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w4 import front_surface, printed_glyph

DESCRIPTION = "A sealed appointment envelope bears a crossed-out calendar pictogram on its front."


def draw(s):
    envelope = front_surface(s, angle=-23, z=5, lean=.46)
    envelope.slab(rounded(0, 0, 95, 58, 3), 5)
    envelope.line([(1, 55), (32, 37)], EDGE)
    envelope.line([(94, 55), (63, 37)], EDGE)
    envelope.line([(2, 2), (28, 22)], DETAIL)
    envelope.line([(93, 2), (67, 22)], DETAIL)
    envelope.frame(32, 12, 31, 29, 3, EDGE)
    envelope.line([(32, 32), (63, 32)], DETAIL)
    for u in (38, 57):
        envelope.line([(u, 39), (u, 45)], EDGE)
    printed_glyph(envelope, "x", 47.5, 22, 10, BOLD)
