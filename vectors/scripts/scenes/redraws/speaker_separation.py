from geometry import BOLD, EDGE
from scenes.redraws._w2 import chart_line, laptop
from scenes.systems_shapes import wave

DESCRIPTION = "A laptop audio editor splits one input waveform into two separate speaker tracks."


def draw(s):
    point = laptop(s, 114, 73)
    wave(s, 12, 0, 43, 28, 15, EDGE, mode="rough")
    chart_line(s, point, [(40, 43), (49, 43), (49, 59), (65, 59)], BOLD)
    chart_line(s, point, [(49, 43), (49, 25), (65, 25)], BOLD)
    wave(s, 65, 0, 59, 37, 16, EDGE, mode="rough")
    wave(s, 65, 0, 25, 37, 18, EDGE, mode="slow")
