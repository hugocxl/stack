from geometry import BOLD, DETAIL, EDGE, oval, rounded
from scenes.redraws._w2 import audio_deck, closed_outline, face_arrow, recorder_trace

DESCRIPTION = "A repeat arrow circles the bounded middle copy of a repeating waveform on an audio editor."


def draw(s):
    point = audio_deck(s, height=70)
    motif = (0, 4, -6, 10, -12, 7, -4, 0)
    for index, start in enumerate((12, 52, 92)):
        recorder_trace(s, point, start, 35, 4.3, motif, EDGE if index == 1 else DETAIL)
    closed_outline(s, point, rounded(49, 19, 36, 32, 3), DETAIL)
    face_arrow(s, point, oval(67, 35, 25, 25, 132, 457, 46), BOLD, head=7)
