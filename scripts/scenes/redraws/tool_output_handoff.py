from geometry import BOLD, EDGE
from scenes.redraws._kit import arrow
from scenes.redraws._w2 import folded_sheet, rule

DESCRIPTION = "A folded output document sends a bold arrow outward from its last row."


def draw(s):
    def point(x, z):
        return .79*x, -.21*x - .21*z, z

    folded_sheet(s, point, 67, 88, depth=6)
    for z, length in ((68, 29), (55, 43), (43, 38), (31, 28)):
        rule(s, point, 11, z, length, EDGE)
    start = point(38, 21)
    arrow(s, [start, (start[0] + 29, start[1] - 29, start[2])], BOLD, head=12)
