from scenes.redraws._kit import badge
from scenes.redraws._w5 import security_token

DESCRIPTION = "A rounded security token carries a clock badge at the edge of its masked passcode display."


def draw(s):
    face = security_token(s)
    badge(s, "clock", *face(38, 35), 12)
