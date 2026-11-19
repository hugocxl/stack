from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w2 import clipboard

DESCRIPTION = "A clock badge sits beside the ruled elapsed-time field on a task clipboard."


def draw(s):
    top = clipboard(s)
    for y, width in ((37, 42), (52, 35), (67, 28)):
        s.line([(16, y-4, top), (24, y-4, top), (24, y+4, top),
                (16, y+4, top), (16, y-4, top)], EDGE)
        s.line([(31, y, top), (31 + width, y, top)], DETAIL)
    s.line([(15, 80, top), (69, 80, top)], EDGE)
    for x in (35, 45, 55):
        s.line([(x, 76, top), (x, 80, top)], DETAIL)
    badge(s, "clock", 80, 71, 15, 15)
