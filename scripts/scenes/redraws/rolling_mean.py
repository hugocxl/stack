from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w2 import axes, chart_line, laptop

DESCRIPTION = "A laptop chart shows a strong smooth curve following a faint jagged time series."


def draw(s):
    p = laptop(s, 123, 74)
    axes(s, p, x=12, y=16, width=97, height=47)
    raw = [(14, 26), (20, 33), (27, 25), (32, 43), (39, 37), (45, 53),
           (51, 42), (59, 58), (66, 43), (72, 49), (78, 31), (84, 42),
           (91, 27), (98, 42), (109, 37)]
    smooth = [(14, 29), (21, 30), (28, 32), (35, 36), (42, 41), (49, 46),
              (55, 49), (61, 50), (67, 48), (73, 44), (79, 40),
              (85, 36), (91, 35), (97, 35.5), (103, 37), (109, 40)]
    chart_line(s, p, raw, DETAIL)
    chart_line(s, p, smooth, BOLD)
