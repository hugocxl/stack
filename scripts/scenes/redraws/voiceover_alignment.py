from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w2 import chart_line, closed_outline, desktop_monitor
from scenes.systems_shapes import wave

DESCRIPTION = "A playhead crosses a cut in the video track at the exact start of the audio track below it."


def draw(s):
    point = desktop_monitor(s, 108, 75)
    for left, width in ((13, 35), (51, 44)):
        closed_outline(s, point, rounded(left, 51, width, 21, 1), EDGE)
        for x in range(left + 5, left + width - 4, 9):
            chart_line(s, point, [(x, 66), (x + 3, 66)], DETAIL)
            chart_line(s, point, [(x, 57), (x + 3, 57)], DETAIL)
    chart_line(s, point, [(13, 41), (51, 41)], DETAIL)
    closed_outline(s, point, rounded(51, 32, 43, 17, 1), EDGE)
    wave(s, 53, 0, 40.5, 40, 9, EDGE, mode="pulse")
    chart_line(s, point, [(51, 77), (51, 30)], BOLD)
    closed_outline(s, point, [(47, 80), (55, 80), (51, 75)], BOLD)
