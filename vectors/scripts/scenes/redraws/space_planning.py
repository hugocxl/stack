from geometry import DETAIL, EDGE, oval, rounded

DESCRIPTION = "A low-walled room plan shows a bed and a wardrobe fitted inside the walls with a clear door swing."


def draw(s):
    s.box(-37, -31, 0, 74, 62, 5, 1)
    s.box(-37, -31, 5, 74, 4, 10, .5)
    s.box(-37, -27, 5, 4, 58, 10, .5)

    def footprint(x, y, w, d, radius, ink=EDGE):
        points = [(u, v, 5) for u, v in rounded(x, y, w, d, radius)]
        s.line(points + points[:1], ink)

    footprint(-26, -23, 32, 39, 2)
    for x in (-23, -9):
        footprint(x, -19, 12, 9, 1.7, DETAIL)
    s.line([(-26, -6, 5), (6, -6, 5)], DETAIL)

    footprint(16, -21, 13, 34, 1)
    s.line([(16, -4, 5), (29, -4, 5)], EDGE)
    for y in (-9, -1):
        s.line([(19, y - 1, 5), (19, y + 1, 5)], DETAIL)

    swing = [(x, y, 5) for x, y in oval(33, 27, 22, 22, 180, 238, 24)]
    s.line(swing, DETAIL)
    s.line([(33, 27, 5), swing[-1]], EDGE)
    s.box(33, -27, 5, 4, 58, 7, .5)
    s.box(-33, 27, 5, 44, 4, 7, .5)
