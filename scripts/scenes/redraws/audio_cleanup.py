from math import pi, sin

from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w2 import audio_deck, chart_line, recorder_trace

DESCRIPTION = "An irregular waveform enters an inline filter and emerges as a clean repeating signal."


def draw(s):
    point = audio_deck(s)
    rough = (0, 9, -10, 2, -4, 13, -12, 6, -6, 4, 11, -13, 0)
    clean = [11*sin(i*pi/9) for i in range(37)]
    recorder_trace(s, point, 13, 31, 3.7, rough, EDGE)
    recorder_trace(s, point, 76, 31, 1.22, clean, BOLD)
    s.face([point(x, z) for x, z in rounded(57, 19, 19, 24, 3)], EDGE)
    chart_line(s, point, [(61, 35), (72, 35), (68, 31), (68, 26), (65, 26), (65, 31),
                          (61, 35)], DETAIL)
