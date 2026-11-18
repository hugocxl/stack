from geometry import DETAIL, EDGE
from scenes.redraws._w2 import face_magnifier

DESCRIPTION = "A magnifier frames a proposed foundation set among the contours of a raised building plot."


def draw(s):
    site = [(-50, -32), (35, -32), (49, -24), (49, 25),
            (36, 36), (-38, 36), (-50, 24)]
    s.solid(site, 0, 7, crease=False)
    s.face([(*p, 7) for p in site])

    # Both curved ledges meet the same outer edge of the site.
    for x, z in ((0, 14), (-10, 21)):
        edge = [(49, -16 - z/4), (38, -11 + x), (25, -7 + x),
                (13, -7 + x), (0, -14 + x), (-15, -21 + x), (-31, -24 + x/2),
                (-45, -24 + x/2)]
        for a, b in zip(edge, edge[1:]):
            s.face([(*a, z - 7), (*b, z - 7), (*b, z), (*a, z)], DETAIL)
        y = edge[0][1]
        s.face([(49, -24, z - 7), (49, y, z - 7), (49, y, z), (49, -24, z)], EDGE)
        s.face([(-45, -32, z), (35, -32, z), (49, -24, z),
                *[(*p, z) for p in edge]], EDGE)

    base = [(-22, 24), (11, 24), (11, 12), (24, 12), (24, 1), (-22, 1)]
    for a, b in zip(base, base[1:] + base[:1]):
        if b[1] < a[1] or b[0] < a[0]:
            s.face([(*a, 7), (*b, 7), (*b, 10), (*a, 10)], DETAIL)
    s.face([(*p, 10) for p in base], EDGE)
    s.line([(-17, 19, 10), (7, 19, 10), (7, 8, 10), (18, 8, 10)], DETAIL)

    def glass(u, v):
        return -3 + .82*u - .42*v, 14 - .18*u - .72*v, 20 + .46*v

    face_magnifier(s, glass, 0, 0, 23, direction=(.82, -.57))
