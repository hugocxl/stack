from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w2 import chart_line, closed_outline, desk_sheet, magnifier, rule

DESCRIPTION = "A magnifier picks out a short isolated token in a transcript beneath a speech waveform."


def draw(s):
    point = desk_sheet(s, 112, 82, fold=11)
    peaks = [0, 2, -5, 7, -8, 6, -3, 0, 0, 4, -5, 0, 0, 0, 5, -6, 9, -5, 2, 0]
    chart_line(s, point, [(11 + 4.6*i, 62 + peak) for i, peak in enumerate(peaks)], EDGE)
    for z, x, width in ((39, 12, 24), (39, 49, 11), (39, 71, 26), (22, 12, 68)):
        rule(s, point, x, z, width, EDGE if x == 49 else DETAIL)
    closed_outline(s, point, rounded(45, 33, 19, 12, 2), EDGE)
    x, y, z = point(55, 39)
    magnifier(s, x, y + 1, z, 18, direction=(.77, -.64))
