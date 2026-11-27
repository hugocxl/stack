from scenes.redraws._kit import badge
from scenes.redraws._w3 import classroom_chair, classroom_desk

DESCRIPTION = "Two school desks with chairs carry a refresh badge as the seating changes."


def draw(s):
    for x, y in ((-70, -10), (10, -40)):
        classroom_desk(s, x, y, 1.6)
        classroom_chair(s, x + 12, y + 40, 1.4)
    badge(s, "refresh", 76, -30, 58, 12)
