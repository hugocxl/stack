from geometry import EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w2 import audio_deck, chart_marker, closed_outline, recorder_trace, rule

DESCRIPTION = "A check badge is attached to a desktop recorder displaying a saved waveform beside its playback controls."


def draw(s):
    point = audio_deck(s)
    closed_outline(s, point, rounded(14, 15, 77, 33, 3), EDGE)
    recorder_trace(s, point, 20, 31, 4.9,
                   (0, 3, -4, 9, -10, 4, -2, 7, -8, 4, -5, 8, -3, 0))
    chart_marker(s, point, 111, 36, 7, EDGE)
    rule(s, point, 103, 20, 15, EDGE)
    badge(s, "check", *point(132, 57), 14)
