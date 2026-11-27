from scenes.redraws._kit import badge
from scenes.redraws._w1 import software_package

DESCRIPTION = "A sealed software package carries a return badge as the release rolls back."


def draw(s):
    software_package(s, 0, 0, 0, 1.25)
    badge(s, "back", 36, 26, 16, 13)
