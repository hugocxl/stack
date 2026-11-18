from geometry import BOLD, DETAIL
from scenes.redraws._kit import badge
from scenes.redraws._w5 import closed_guide, mountain_mark

DESCRIPTION = "A pocket field guide has a mountain-trail emblem on its cover and a down-arrow badge at its lower corner."


def draw(s):
    face = closed_guide(s)
    mountain_mark(s, face, 28, 42, .98, BOLD)
    s.line([face(13, 23), face(22, 26), face(27, 23), face(37, 29), face(43, 29)], DETAIL)
    badge(s, "down", 50, 0, 15, 12)
