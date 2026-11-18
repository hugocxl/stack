from geometry import DETAIL, EDGE

DESCRIPTION = "A breakfast plate holds a fried egg and two slices of toast beside a cup."


def draw(s):
    s.tube([(33, -15, 13), (39, -15, 13), (42, -15, 10),
            (39, -15, 6), (34, -15, 6)], 1.6)
    s.disk(27, -15, 0, 8, 8, 15)
    s.ellipse(27, -15, 15, 6.5, 6.5, DETAIL)
    s.ellipse(27, -15, 10, 5.9, 5.9, DETAIL, start=194, end=336)
    s.disk(0, 8, 0, 26, 23, 3.6)
    s.ellipse(0, 8, 3.6, 22, 19, DETAIL)
    egg = [(-16, 2), (-15, -2), (-9, -4), (-4, -3), (-1, -5), (3, -4),
           (7, -1), (7, 4), (4, 9), (-1, 11), (-3, 15), (-7, 17), (-12, 13), (-15, 9)]
    s.face([(x - 1.7, y + 1, 5.2) for x, y in egg])
    s.disk(-8, 6, 5.2, 5.1, 4.4, 2.4)
    for x, y, top in ((6, 6, 8.4), (1, 12, 10.8)):
        bread = [(x, y + 13), (x + 17, y + 13), (x + 17, y + 3), (x + 18, y + 1),
                 (x + 16, y - 2), (x + 12, y - 3.5), (x + 5, y - 3.5),
                 (x + 1, y - 2), (x - 1, y + 1), (x, y + 3)]
        s.solid(bread, top - 4.8, 4.8, crease=False)
        s.line([(u, v, top) for u, v in bread + bread[:1]], EDGE)
        s.line([(x + 3, y + 7, top), (x + 3, y + 3, top),
                (x + 1.7, y + .5, top), (x + 5, y - 1, top),
                (x + 11, y - 1, top), (x + 15, y + .5, top)], DETAIL)
