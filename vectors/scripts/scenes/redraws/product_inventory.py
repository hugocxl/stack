from geometry import DETAIL, EDGE

DESCRIPTION = "A shelving rack holds labeled stock bins on three shelves, with one empty bay."


def bin_(s, x, y, z, w=22, d=24, h=14):
    s.box(x, y, z, w, d, h, 2)
    s.line([(x + 6, y + d, z + h*.62), (x + w - 6, y + d, z + h*.62)], DETAIL)


def draw(s):
    W, D = 96, 30
    levels = (0, 26, 52)
    for x in (0, W - 3):
        s.box(x, 0, 0, 3, 3, 82, .8)
    for z in levels:
        s.box(0, 0, z + 4, W, D, 3, 1)
        if z == 26:
            bins = (4, 52)
        else:
            bins = (4, 28, 52, 72)
        for x in bins:
            if x + 22 <= W - 2:
                bin_(s, x, 3, z + 7)
    for x in (0, W - 3):
        s.box(x, D - 3, 0, 3, 3, 82, .8)
