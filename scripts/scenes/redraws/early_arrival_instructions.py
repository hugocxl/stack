from geometry import EDGE
from scenes.redraws._kit import glyph
from scenes.redraws._w3 import ticket

DESCRIPTION = "A perforated admission ticket shows a large analog clock and an inward arrow on its entry stub."


def draw(s):
    face = ticket(s, marks=False)
    face.oval(31, 24, 15, 15, EDGE)
    glyph(s, "clock", 31, 0, 24, 12)
    for x, v, dx, dv in ((31, 37, 0, -2), (44, 24, -2, 0),
                         (31, 11, 0, 2), (18, 24, 2, 0)):
        face.stroke([(x, v), (x + dx, v + dv)], EDGE)
    face.rules(51, 32, [13], ink=EDGE)
    face.rules(51, 23, [12, 10], gap=7)
    glyph(s, "back", 84, 0, 24, 13)
