from scenes.redraws._kit import badge
from scenes.redraws._w5 import backpack

DESCRIPTION = "A hiking backpack carries a check badge clipped to its front zip pocket."


def draw(s):
    backpack(s)
    badge(s, "check", 38, 35, 19, 13)
