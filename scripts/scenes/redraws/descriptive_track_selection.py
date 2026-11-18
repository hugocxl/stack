from geometry import BOLD, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface, audio_description_art

DESCRIPTION = "A selected channel on an audio receiver pairs an eye and sound waves with a check badge."


def draw(s):
    row = Surface(s, (0, 0, 0))
    row.plate(rounded(0, 0, 110, 49, 5), 23)
    row.rect(8, 10, 83, 30, 3, EDGE)
    audio_description_art(row, 31, 25, 24, BOLD)
    row.rules(53, 29, [24, 16], gap=8)
    badge(s, "check", *row.point(102, 35, -1), 12)
