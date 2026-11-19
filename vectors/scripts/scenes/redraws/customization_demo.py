from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w4 import Surface

DESCRIPTION = "A control device shows its connectors behind a faceplate snapped into the lower lip of its housing."


def draw(s):
    s.box(0, 0, 0, 69, 27, 57, 5)
    front = Surface(s, lambda u, v: (u, 27, v))
    front.frame(6, 6, 57, 45, 3, EDGE)
    for u, w in ((12, 19), (36, 21)):
        front.frame(u, 36, w, 9, 1.6, EDGE)
        front.rows(u + 3, 40.5, (w - 6,))
    front.line([(10, 12), (59, 12)], EDGE)

    panel = Surface(s, lambda u, v: (u, 28 + v*.92, 8 + v*.25))
    panel.slab(rounded(6, 0, 57, 33, 3), 5)
    panel.frame(12, 5, 31, 22, 2, EDGE)
    panel.rows(17, 18, (21,), ink=DETAIL)
    panel.oval(53, 16, 5, 5, EDGE)
    for u in (12, 55):
        panel.slab(rounded(u, 31, 5, 5, 1), 2, DETAIL)
