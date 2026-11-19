from geometry import DETAIL, EDGE

DESCRIPTION = "Three small office buildings connect to one shared hub in a partner network."


def draw(s):
    centers = ((-34, -34), (39, -8), (-8, 38))
    for x, y in centers:
        s.tube([(0, 0, 2), (x, y, 2)], 2, DETAIL)
    s.disk(0, 0, 0, 10, 10, 6)
    s.ellipse(0, 0, 6, 5, 5, DETAIL)
    for x, y in centers:
        s.box(x - 11, y - 9, 0, 22, 18, 31, 1.5)
        for z in (14, 23):
            for u in (-6, 2):
                s.face([(x + u, y + 9, z), (x + u + 4, y + 9, z),
                        (x + u + 4, y + 9, z + 5), (x + u, y + 9, z + 5)], EDGE)
        s.line([(x + 11, y - 5, 20), (x + 11, y + 4, 20)], DETAIL)
        s.line([(x - 2, y + 9, 0), (x - 2, y + 9, 8),
                (x + 3, y + 9, 8), (x + 3, y + 9, 0)])
