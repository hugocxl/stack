from geometry import BOLD, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w3 import sheet

DESCRIPTION = "A turned-corner file bears a large code symbol and an outward arrow badge."


def draw(s):
    code = sheet(s, 72, 87, rise=(-.34, .94), depth=7)
    code.stroke([(26, 59), (11, 46), (26, 33)], BOLD)
    code.stroke([(45, 59), (60, 46), (45, 33)], BOLD)
    code.stroke([(41, 62), (30, 29)], BOLD)
    code.rules(12, 19, [34], ink=EDGE)
    badge(s, "arrow", *code.point(78, 72, -4), 15)
