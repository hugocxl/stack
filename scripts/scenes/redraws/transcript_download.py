from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w3 import transcript_folio

DESCRIPTION = "A down-arrow badge overlaps the bottom corner of a bound transcript with a speaker-label column."


def draw(s):
    page = transcript_folio(s)
    page.rules(9, 60, [16], ink=EDGE)
    page.rules(40, 60, [28], ink=EDGE)
    badge(s, "down", *page.point(88, 9, -3), 16)
