from geometry import BOLD, EDGE
from scenes.redraws._w3 import spiral_notebook

DESCRIPTION = "A wire-bound article outline steps inward through three progressively smaller heading styles."


def draw(s):
    page = spiral_notebook(s, w=83, h=84)
    for x, v, size, length, ink in (
        (15, 66, 13, 40, BOLD), (26, 44, 10, 31, EDGE), (38, 24, 7, 23, EDGE)
    ):
        page.stroke([(x, v - size / 2), (x, v + size / 2)], ink)
        page.stroke([(x + size * .65, v - size / 2),
                     (x + size * .65, v + size / 2)], ink)
        page.rules(x, v, [size * .65], ink=ink)
        page.rules(x + size + 4, v + 2, [length], ink=ink)
        page.rules(x + size + 4, v - 4, [length * .72])
