from geometry import EDGE, oval
from scenes.redraws._kit import badge
from scenes.redraws._w4 import service_profile

DESCRIPTION = "A service-provider profile shows linked rings and an attached match check badge."


def draw(s):
    profile = service_profile(s, profile_lines=False)
    profile.line(oval(66, 24, 11, 6, 33, 325, count=30), EDGE)
    profile.oval(79, 24, 11, 6, EDGE)
    badge(s, "check", *profile.at(101, 10), 13.5)
