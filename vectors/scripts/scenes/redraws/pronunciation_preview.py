from geometry import EDGE
from scenes.redraws._kit import coin, glyph
from scenes.redraws._w2 import outline, rule
from scenes.systems_shapes import wave

DESCRIPTION = "A desktop pronunciation player pairs a short sample of type with a waveform and a play button."


def draw(s):
    s.box(0, -26, 0, 103, 26, 57, 8)
    outline(s, 8, 0, 10, 56, 38, 4)
    point = lambda x, z: (x, 0, z)
    for x, length in ((15, 10), (29, 7), (40, 12)):
        rule(s, point, x, 39, length, EDGE)
    wave(s, 15, 0, 25, 43, 12, EDGE, mode="pulse")
    coin(s, 82, 1, 28, 13, depth=2)
    glyph(s, "play", 82, 1, 28, 11)
