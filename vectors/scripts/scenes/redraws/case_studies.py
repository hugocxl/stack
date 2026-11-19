from geometry import BOLD, EDGE
from scenes.redraws._w4 import open_book

DESCRIPTION = "An open report pairs a rising bar chart with a short written summary on the facing page."


def draw(s):
    chart, summary = open_book(s)
    chart.rows(11, 12, (34,), ink=EDGE)
    chart.line([(12, 24), (12, 59), (56, 59)], EDGE)
    for u, top in ((18, 47), (29, 38), (40, 26)):
        chart.outline([(u, 58), (u, top), (u + 6, top), (u + 6, 58)], BOLD)
    summary.rows(72, 13, (34,), ink=EDGE)
    summary.rows(72, 24, (43, 36, 42, 31), step=7)
    summary.rows(72, 56, (41, 29), step=7)
