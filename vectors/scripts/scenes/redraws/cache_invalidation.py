from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.systems_shapes import bezel, rectangle

DESCRIPTION = "An X badge marks the top entry in a staggered stack of cache cartridges."


def draw(s):
    for index, (x, y, z) in enumerate(((-32, -11, 0), (-32, -16, 13), (-32, -23, 26))):
        s.box(x, y, z, 64, 38, 12, 3)
        bezel(s, x + 8, y + 38, z + 3, 17, 5, DETAIL, 1.4)
        for pin in (41, 48, 55):
            s.line([(x + pin, y + 38, z + 4), (x + pin, y + 38, z + 7)], EDGE)
        if index == 2:
            rectangle(s, -20, -11, 38, 33, 14, DETAIL, 2)
    badge(s, "x", 30, 1, 41, 13)
