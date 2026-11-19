from geometry import BOLD, EDGE
from scenes.redraws._w2 import audio_deck, magnifier, recorder_trace

DESCRIPTION = "A magnifier isolates the low rumble between two taller bursts of speech on a waveform."


def draw(s):
    point = audio_deck(s)
    speech = (0, 4, -8, 12, -16, 10, -7, 4, 0, 1, -2, 2, -1, 3, -2,
              2, -3, 1, 0, 4, -9, 16, -13, 9, -5, 4, 0)
    start, step = 13, 4.15
    recorder_trace(s, point, start, 32, step, speech[:10], EDGE)
    recorder_trace(s, point, start + 9*step, 32, step, speech[9:18], BOLD)
    recorder_trace(s, point, start + 17*step, 32, step, speech[17:], EDGE)
    x, y, z = point(67, 32)
    magnifier(s, x, y + 3, z, 23, direction=(.45, -.89))
