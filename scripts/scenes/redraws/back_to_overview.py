from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import glyph
from scenes.redraws._w4 import upright

DESCRIPTION = "An overview card shows three list rows beneath a back arrow in its top bar."


def draw(s):
    upright(s, rounded(0, 0, 86, 70, 4), 0, 5)
    s.line([(0, 0, 48), (86, 0, 48)], DETAIL)
    glyph(s, "back", 18, 0, 59, 16)

    for z, width in ((36, 51), (24, 42), (12, 46)):
        bullet = [(x, 0, k) for x, k in rounded(11, z - 2.5, 5, 5, 1)]
        s.line([*bullet, bullet[0]], EDGE)
        s.line([(23, 0, z), (23 + width, 0, z)], EDGE)
