from math import cos, radians, sin

from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import arrow
from scenes.redraws._w4 import front_surface, printed_glyph

DESCRIPTION = "Directional arrows connect an input box, a gear, and a checkmark in a three-stage process."


def draw(s):
    diagram = front_surface(s, angle=-26)
    for u in (0, 40, 80):
        diagram.slab(oval(u, 25, 14, 14)[:-1], 4)
    for start in (16, 56):
        arrow(s, [diagram.at(start, 25), diagram.at(start + 8, 25)], EDGE, head=3.5)
    diagram.outline([(-6, 21), (0, 18), (6, 21), (6, 29), (0, 32), (-6, 29)], EDGE)
    diagram.line([(-6, 29), (0, 26), (6, 29)])
    diagram.line([(0, 26), (0, 18)])
    gear = []
    for tooth in range(8):
        for offset, radius in ((0, 5.5), (8, 8), (27, 8), (35, 5.5)):
            a = radians(tooth * 45 + offset)
            gear.append((40 + radius * cos(a), 25 + radius * sin(a)))
    diagram.outline(gear, EDGE)
    diagram.oval(40, 25, 2.6, 2.6, DETAIL)
    printed_glyph(diagram, "check", 80, 25, 9, EDGE)
