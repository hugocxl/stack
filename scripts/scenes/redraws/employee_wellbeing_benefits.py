from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import glyph
from scenes.redraws._w4 import Surface, upright

DESCRIPTION = "A clipped employee benefits card displays a heart outline crossed by a pulse trace."


def draw(s):
    s.box(32, 2, 62, 25, 14, 21, 4, EDGE)
    upright(s, rounded(0, 0, 88, 69, 6), 16, 7)
    front = Surface(s, lambda u, v: (u, 16, 69 - v))
    front.frame(36, 6, 16, 4.5, 2)
    glyph(s, "heart", 29, 16, 29, 26, EDGE)
    front.line([(11, 38), (21, 38), (26, 32), (30, 45), (35, 36), (48, 36)], EDGE)
    front.rows(56, 29, (22, 16, 22), step=8, ink=DETAIL)
