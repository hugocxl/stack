from scenes.redraws._kit import badge
from scenes.redraws._w3 import theater_seat

DESCRIPTION = "An upholstered theater seat has an upward-arrow badge on the corner of its backrest."


def draw(s):
    theater_seat(s)
    badge(s, "up", 42, 2, 53, 11)
