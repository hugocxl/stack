from geometry import EDGE, oval
from scenes.redraws._kit import glyph
from scenes.systems_shapes import bezel

DESCRIPTION = "A phone receives a wireless signal above a software-update arrow and a progress bar."


def draw(s):
    s.box(-20, -8, 0, 40, 8, 74, 6)
    bezel(s, -16, 0, 5, 32, 63, EDGE, 3)
    s.line([(-3, 0, 71), (3, 0, 71)], EDGE)
    glyph(s, "down", 0, 0, 43, 13)
    bezel(s, -12, 0, 20, 24, 6, EDGE, 2)
    s.line([(2, 0, 20), (2, 0, 26)], EDGE)

    # Airborne wavefronts are parallel to the phone's face.
    for radius in (10, 19, 28):
        s.line([(x, 0, z) for x, z in oval(0, 77, radius, radius, 52, 128, 20)], EDGE)
