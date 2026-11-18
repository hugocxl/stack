from geometry import DETAIL, EDGE
from scenes.redraws._kit import glyph
from scenes.redraws._w1 import clipboard
from scenes.systems_shapes import bezel

DESCRIPTION = "A clipped warehouse transfer order pairs two depot symbols with a right-pointing destination arrow."


def depot(s, x, y, z):
    s.line([(x - 8, y, z), (x - 8, y, z + 10), (x - 5, y, z + 13),
            (x + 5, y, z + 13), (x + 8, y, z + 10),
            (x + 8, y, z), (x - 8, y, z)], EDGE)
    bezel(s, x - 5, y, z, 10, 7, DETAIL, .7)
    s.line([(x - 5, y, z + 4), (x + 5, y, z + 4)], DETAIL)


def draw(s):
    clipboard(s)
    depot(s, -15.5, 0, 22)
    depot(s, 15.5, 0, 22)
    glyph(s, "arrow", 0, 0, 28, 6.5, EDGE)

    for z, w in ((15, 39), (9, 29)):
        s.line([(-20, 0, z), (-20 + w, 0, z)], DETAIL)
