from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w2 import outline, rule
from scenes.systems_shapes import wave

DESCRIPTION = "A handheld voice-profile device shows a waveform with a check badge beside it."


def draw(s):
    s.box(0, -13, 0, 56, 13, 94, 6)
    outline(s, 5, 0, 19, 46, 61, 4)
    rule(s, lambda x, z: (x, 0, z), 22, 86, 12)
    wave(s, 10, 0, 49, 36, 19, EDGE, mode="pulse")
    outline(s, 23, 0, 7, 10, 6, 3)
    badge(s, "check", 57, 2, 65, 12)
