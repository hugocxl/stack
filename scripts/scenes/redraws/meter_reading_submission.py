from geometry import EDGE, oval
from scenes.redraws._kit import badge, glyph
from scenes.redraws._w1 import meter_reader

DESCRIPTION = "A utility meter with three register dials carries an outward submission-arrow badge."


def draw(s):
    meter_reader(s)
    for x, dx, dz in ((-12, -1.7, 2.7), (0, 1.9, 2.5), (12, .1, 3.2)):
        s.line([(a, 17, b) for a, b in oval(x, 44.5, 4.3, 4.3, count=28)], EDGE)
        s.line([(x, 17, 44.5), (x + dx, 17, 44.5 + dz)], EDGE)
    glyph(s, "bolt", 0, 17, 60.5, 4.3, EDGE)
    badge(s, "up", 31, 3, 57, 13)
