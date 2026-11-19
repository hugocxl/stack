from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w2 import chart_line, rule, standing_notebook

DESCRIPTION = "A citation list shows three bracketed source entries with a clock beside the waiting rows."


def draw(s):
    point = standing_notebook(s, 83, 96)
    for z, length in ((69, 41), (48, 32), (27, 36)):
        chart_line(s, point, [(14, z + 4), (11, z + 4), (11, z - 5), (14, z - 5)], EDGE)
        rule(s, point, 16, z, 3, EDGE)
        chart_line(s, point, [(21, z + 4), (24, z + 4), (24, z - 5), (21, z - 5)], EDGE)
        rule(s, point, 30, z, length, EDGE)
        rule(s, point, 30, z - 7, length*.7, DETAIL)
    badge(s, "clock", *point(82, 43), 12)
