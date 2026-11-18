from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge, glyph
from scenes.redraws._w2 import card, outline


DESCRIPTION = "A plus badge sits in the empty assignee slot of a review checklist."


def draw(s):
    card(s, 102, 58)
    s.line([(12, 0, 45), (50, 0, 45)], EDGE)
    outline(s, 60, 0, 8, 31, 38, 4, EDGE)
    outline(s, 70, 0, 39, 11, 3, 1.5)
    for z in (30, 17):
        outline(s, 12, 0, z - 4, 8, 8, 1.5)
        s.line([(26, 0, z), (45, 0, z)], DETAIL)
    glyph(s, "check", 16, 0, 30, 5, EDGE)
    badge(s, "plus", 78.5, 3, 25, 11)
