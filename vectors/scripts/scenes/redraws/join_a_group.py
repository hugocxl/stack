from geometry import BOLD
from scenes.redraws._kit import arrow
from scenes.redraws._w3 import theater_seat

DESCRIPTION = "A single incoming arrow points toward a close group of three chairs."


def draw(s):
    theater_seat(s, 0, -18)
    theater_seat(s, -38, 10)
    theater_seat(s, 42, 10)
    arrow(s, [(108, 69, 6), (84, 73, 7), (47, 62, 10)], BOLD, head=11)
