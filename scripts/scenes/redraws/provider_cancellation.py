from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w4 import service_profile

DESCRIPTION = "A provider appointment card has a trade thumbnail, a small calendar, and an attached cancellation X badge."


def draw(s):
    profile = service_profile(s)
    profile.frame(59, 7, 23, 16, 2, EDGE)
    profile.line([(59, 17), (82, 17)], EDGE)
    profile.rows(64, 12, (4,), ink=EDGE)
    profile.rows(73, 12, (4,), ink=EDGE)
    badge(s, "x", *profile.at(99, 11), 14)
