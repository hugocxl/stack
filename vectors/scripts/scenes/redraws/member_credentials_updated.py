from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws.expired_member_access import member_emblem, membership_pass

DESCRIPTION = "A membership credential carries an embossed seal and a refresh badge on its upper corner."


def draw(s):
    face = membership_pass(s)
    member_emblem(face, 24, 35, 14)
    face.rules(45, 43, [36], ink=EDGE)
    face.rules(45, 31, [30, 34], gap=8)
    badge(s, "refresh", 95, -13, 44, 15)
