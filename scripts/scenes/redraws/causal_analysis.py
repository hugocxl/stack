from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import arrow, coin, glyph
from scenes.redraws._w2 import level_face

DESCRIPTION = "A single directional arrow links a trigger node to a distinct effect node."


def draw(s):
    a, b, c = level_face(17, 52)
    coin(s, a, b, c, 16, depth=6)
    glyph(s, "bolt", a, b, c, 10, BOLD)
    a, b, c = level_face(106, 25)
    coin(s, a, b, c, 16, depth=6)
    coin(s, a, b, c, 8, depth=0, ink=DETAIL)
    coin(s, a, b, c, 3.3, depth=0, ink=EDGE)
    arrow(s, [level_face(33, 48), level_face(88, 30)], BOLD, head=12)
