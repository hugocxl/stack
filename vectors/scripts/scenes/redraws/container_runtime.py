from scenes.redraws._kit import glyph
from scenes.redraws._w1 import container_cube

DESCRIPTION = "A play triangle is centered on the emblem plate of a ribbed software container."


def draw(s):
    container_cube(s)
    glyph(s, "play", -1, 24, 25, 21)
