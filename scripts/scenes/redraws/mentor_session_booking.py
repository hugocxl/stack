from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws.mentor_introductory_video import mentor_card

DESCRIPTION = "A mentor profile display carries a clock badge at the upper corner and a name rule beneath the portrait."


def draw(s):
    face = mentor_card(s)
    face.rules(30, 7, [28], ink=EDGE)
    badge(s, "clock", *face.point(85, 57, -3), 13)
