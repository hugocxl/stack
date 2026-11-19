from scenes.redraws._kit import badge
from scenes.redraws._w1 import invitation

DESCRIPTION = "An open envelope holds an invitation card and carries a clock badge on its pocket."


def draw(s):
    anchor = invitation(s)
    badge(s, "clock", *anchor, 17)
