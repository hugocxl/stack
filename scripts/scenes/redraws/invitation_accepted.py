from scenes.redraws._kit import badge
from scenes.redraws._w1 import invitation

DESCRIPTION = "An open envelope holds an invitation card and carries a check badge on its pocket."


def draw(s):
    anchor = invitation(s)
    badge(s, "check", *anchor, 17)
