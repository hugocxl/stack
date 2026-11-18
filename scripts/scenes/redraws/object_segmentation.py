from geometry import BOLD
from scenes.redraws._w2 import chart_line, landscape_frame, pine, woodland

DESCRIPTION = "A fitted dashed selection follows the silhouette of a pine tree inside a photograph."


def draw(s):
    point = landscape_frame(s)
    woodland(s, point)
    pine(s, point, 52, 32)
    selection = [(52, 68), (69, 42), (65, 42), (74, 27), (60, 27), (60, 19),
                 (44, 19), (44, 27), (30, 27), (39, 42), (35, 42), (52, 68)]
    chart_line(s, point, selection, BOLD, dash=(4, 3))
