from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w2 import chart_line, closed_outline, desktop_monitor, recorder_trace, rule

DESCRIPTION = "A source waveform on a desktop mixer forks into three tracks with distinct waveforms."


def draw(s):
    point = desktop_monitor(s, 124, 96)
    recorder_trace(s, point, 13, 68, 3,
                   (0, 6, -8, 15, -11, 9, -14, 6, -5, 0))
    rule(s, point, 42, 68, 10, EDGE)
    chart_line(s, point, [(52, 43), (52, 93)], BOLD)
    tracks = (
        (93, (0, 4, -4, 0, 4, -4, 0, 4, -4, 0, 4, -4, 0)),
        (68, (0, 0, 6, -6, 0, 0, 0, 0, 6, -6, 0, 0, 0)),
        (43, (0, 1, 3, 4, 3, 1, -2, -4, -4, -2, -1, 0, 0)),
    )
    for z, samples in tracks:
        rule(s, point, 52, z, 10, BOLD)
        closed_outline(s, point, rounded(62, z - 8, 52, 16, 2), DETAIL)
        recorder_trace(s, point, 66, z, 3.6, samples, EDGE)
