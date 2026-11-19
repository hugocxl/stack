from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w5 import avatar_mark, panel, rect

DESCRIPTION = "An upright guest pass has a lanyard slot, a contact pictogram, and a clock badge on its validity band."


def draw(s):
    face = lambda x, z: (x, -.16 * z, z)
    panel(s, rounded(0, 0, 47, 66, 5), face, 5.5)
    rect(s, face, 15, 57, 17, 4, 2, EDGE)
    avatar_mark(s, face, 23.5, 40, 1.68)
    rect(s, face, 6, 9, 35, 12, 2, DETAIL)
    s.line([face(11, 15), face(26, 15)], EDGE)
    badge(s, "clock", *face(41, 15), 11)
