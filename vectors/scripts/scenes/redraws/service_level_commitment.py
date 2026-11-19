from scenes.redraws._kit import badge
from scenes.redraws._w5 import agreement

DESCRIPTION = "A signed service agreement has an uptime gauge in its heading and a check badge at its upper corner."


def draw(s):
    face, _ = agreement(s, service=True)
    badge(s, "check", *face(56, 61), 12)
