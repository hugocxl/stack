from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w4 import service_profile

DESCRIPTION = "A service-provider credential has a trade pictogram and an attached verification check over its upper corner."


def draw(s):
    profile = service_profile(s)
    profile.rows(58, 13, (19,), ink=EDGE)
    badge(s, "check", *profile.at(96, 64), 15)
