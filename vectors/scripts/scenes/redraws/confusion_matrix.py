from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w2 import chart_marker, front_bar

DESCRIPTION = "A two-by-two matrix matches circle and triangle labels along a prominently outlined diagonal."


def label(s, p, x, z, triangle, size):
    if triangle:
        s.face([p(x, z + size), p(x + size, z - size*.65),
                p(x - size, z - size*.65)], EDGE)
    else:
        chart_marker(s, p, x, z, size, EDGE)


def draw(s):
    s.box(0, -20, 0, 102, 20, 95, 3)
    p = lambda x, z: (x, 0, z)
    for x, z, triangle in ((42, 84, False), (77, 84, True), (12, 58, False), (12, 25, True)):
        label(s, p, x, z, triangle, 5.2)
    for row, z in enumerate((44, 11)):
        for col, x in enumerate((25, 60)):
            match = row == col
            front_bar(s, p, x, z, 32, 29, BOLD if match else DETAIL)
            if match:
                label(s, p, x + 16, z + 14.5, col == 1, 7.5)
            else:
                s.line([p(x + 13, z + 14.5), p(x + 19, z + 14.5)], DETAIL)
