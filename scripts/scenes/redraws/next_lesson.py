from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w4 import closed_book, media_frame

DESCRIPTION = "A lesson book with a play inset carries a right-arrow badge on its fore edge."


def draw(s):
    cover = closed_book(s, angle=-15)
    cover.rows(15, 21, (39,), ink=EDGE)
    media_frame(cover, 16, 33, 41, 29)
    cover.rows(16, 75, (37, 27), step=7)
    badge(s, "arrow", *cover.at(72, 40), 17)
