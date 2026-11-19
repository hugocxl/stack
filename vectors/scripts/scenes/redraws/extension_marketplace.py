from geometry import BOLD, EDGE, oval, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "A storefront with a scalloped awning displays three interlocking puzzle-piece shapes as software add-ons."


def draw(s):
    wall = Surface(s, (0, 0, 0))
    wall.plate(rounded(0, 0, 113, 73, 3), 15)
    wall.rect(7, 8, 99, 44, 3, EDGE)
    for x in (40, 73):
        wall.stroke([(x, 8), (x, 52)])
    for x, raised in ((23, 0), (56, 3), (89, 0)):
        v = 28 + raised
        outline = [(x - 8, v - 9), (x + 8, v - 9), (x + 8, v - 4)]
        outline += oval(x + 8, v, 5, 4, -90, 90, 14)
        outline += [(x + 8, v + 9), (x + 3, v + 9)]
        outline += oval(x, v + 9, 3, 5, 0, 180, 14)
        outline += [(x - 8, v + 9), (x - 8, v + 4)]
        outline += oval(x - 8, v, 4, 4, 90, -90, 14)
        wall.stroke(outline, BOLD, closed=True)

    awning = Surface(s, (-3, 13, 56), rise=(-.62, .78), back=(0, -.78, -.62))
    lower_edge = [(0, 5)]
    for center in (8.5, 25.5, 42.5, 59.5, 76.5, 93.5, 110.5):
        lower_edge.extend(oval(center, 5, 8.5, 4, 180, 360, 12)[1:])
    awning.plate([*lower_edge, (119, 24), (0, 24)], 3)
    for x in (17, 34, 51, 68, 85, 102):
        awning.stroke([(x, 6), (x, 23)])
