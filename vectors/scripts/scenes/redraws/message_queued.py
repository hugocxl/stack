from scenes.redraws._kit import badge
from scenes.redraws.message_delivered import message

DESCRIPTION = "A rounded message bubble carries a clock badge on its lower-right corner."


def draw(s):
    badge(s, "clock", *message(s), 12)
