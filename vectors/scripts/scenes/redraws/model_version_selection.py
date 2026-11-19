from geometry import EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w2 import board, chart_line, closed_outline, model_layers, rule

DESCRIPTION = "An open model selector shows two layered model revisions with a check badge on the selected row."


def draw(s):
    p = board(s, 104, 88, run=.16, depth=12, level=True)
    closed_outline(s, p, rounded(10, 65, 84, 14, 2), EDGE)
    rule(s, p, 20, 72, 31, EDGE)
    chart_line(s, p, [(77, 74), (82, 69), (87, 74)], EDGE)
    closed_outline(s, p, rounded(10, 9, 84, 49, 2), EDGE)
    rule(s, p, 10, 34, 84)
    for z, layers in ((19, 2), (42, 3)):
        model_layers(s, p, 27, z - 4, layers)
        rule(s, p, 43, z, 22, EDGE)
    badge(s, "check", *p(93, 44), 10)
