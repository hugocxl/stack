from geometry import EDGE
from scenes.redraws._w3 import eye, transcript_folio

DESCRIPTION = "An eye marks the heading of a transcript’s separate speaker-label column."


def draw(s):
    page = transcript_folio(s)
    eye(page, 19, 60, 10)
    page.rules(41, 60, [29], ink=EDGE)
