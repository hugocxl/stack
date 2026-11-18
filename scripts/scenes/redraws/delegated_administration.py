from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w5 import avatar_mark, identity_card, key_mark, rect

DESCRIPTION = "An administrator ID has a framed portrait and a key emblem with an outward arrow badge."


def draw(s):
    face = identity_card(s)
    avatar_mark(s, face, 21, 23, 1.52)
    s.line([face(43, 35), face(61, 35)], DETAIL)
    rect(s, face, 39, 11, 24, 17, 2, DETAIL)
    key_mark(s, face, 45.5, 18.5, .59, angle=12, ink=EDGE)
    badge(s, "arrow", *face(68, 18.5), 12)
