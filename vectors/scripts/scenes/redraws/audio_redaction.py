from geometry import BOLD, EDGE, rounded
from scenes.redraws._w2 import upright_face
from scenes.systems_shapes import wave

DESCRIPTION = "A waveform on an audio display has one section replaced by a solid redaction bar."


def draw(s):
    def point(x, z):
        return x, 0, z

    upright_face(s, point, rounded(0, 0, 111, 52, 7), 14)
    wave(s, 9, 0, 27, 29, 21, EDGE, mode="rough")
    wave(s, 73, 0, 27, 29, 22, EDGE, mode="rough")
    for step in range(26):
        z = 21 + .48*step
        s.line([point(39, z), point(72, z)], BOLD)
