from scenes.redraws._kit import badge
from scenes.redraws._w1 import envelope

DESCRIPTION = "A sealed envelope shows an at sign on its flap and carries a check badge on its corner."


def draw(s):
    envelope(s, -36, 0, 0, 72, 46, addressed=True)
    badge(s, "check", 36, 0, 42, 13)
