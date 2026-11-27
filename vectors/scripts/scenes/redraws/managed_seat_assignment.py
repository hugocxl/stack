from scenes.redraws._kit import badge
from scenes.redraws._w3 import classroom_chair

DESCRIPTION = "Three chairs stand in a row, and the assigned one carries a check badge."


def draw(s):
    for i in range(3):
        classroom_chair(s, -40 + i*30, -i*4, 1.6)
    badge(s, "check", 26, -6, 52, 11)
