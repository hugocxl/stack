from geometry import BOLD, EDGE, rounded
from scenes.redraws._kit import arrow
from scenes.redraws._w4 import Surface, landscape

DESCRIPTION = "Two branches from a source article point to smaller copies of its layout."


def draw(s):
    plane = Surface(s, lambda u, v: (u*.95, -u*.45 + v*.28, 75 - v*.82))
    for u, v, w, h in ((0, 15, 63, 76), (113, -9, 44, 49), (113, 59, 44, 49)):
        plane.slab(rounded(u, v, w, h, 2), 4)
        plane.rows(u + w*.13, v + h*.15, (w*.55,), ink=BOLD if u == 0 else EDGE)
        landscape(plane, u + w*.13, v + h*.25, w*.74, h*.40)
        plane.rows(u + w*.13, v + h*.77, (w*.62, w*.46), step=h*.10)
    plane.line([(63, 53), (81, 53), (81, 15), (81, 84)], EDGE)
    for v in (15, 84):
        arrow(s, [plane.at(81, v), plane.at(109, v)], EDGE, head=6)
