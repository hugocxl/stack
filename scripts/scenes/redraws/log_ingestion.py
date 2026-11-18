from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._kit import arrow, glyph
from scenes.systems_shapes import bezel

DESCRIPTION = "A row of timestamp symbols lines a log console, and an arrow feeds into the middle entry."


def draw(s):
    s.box(-37, -12, 0, 82, 12, 54, 4)
    bezel(s, -31, 0, 6, 70, 42, EDGE, 2)
    s.line([(-31, 0, 40), (39, 0, 40)], DETAIL)
    s.line([(-21, 0, 44), (-6, 0, 44)], EDGE)

    for z, length in ((32, 28), (22, 32), (12, 22)):
        s.line([(x, 0, v) for x, v in oval(-15, z, 3.4, 3.4, count=22)], EDGE)
        glyph(s, "clock", -15, 0, z, 3.4, EDGE)
        s.line([(-6, 0, z), (-6 + length, 0, z)], EDGE)
    arrow(s, [(-58, 0, 22), (-24, 0, 22)], BOLD, head=8)
