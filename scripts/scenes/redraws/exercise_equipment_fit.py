from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._w4 import Surface

DESCRIPTION = "A stationary exercise bike shows a graduated telescoping seatpost beneath its padded saddle."


def draw(s):
    def place(u, y, z):
        return (.86*u + .5*y, -.5*u + .86*y, z)

    def rod(points, radius, ink=EDGE):
        s.tube([place(*point) for point in points], radius, ink)

    face = Surface(s, lambda u, z: place(u, 8, z))
    for u in (3, 88):
        rod([(u, -16, 4), (u, 16, 4)], 4)
    rod([(3, 0, 7), (20, 0, 11), (72, 0, 11), (88, 0, 7)], 4.1)
    rod([(26, 0, 15), (13, 0, 51)], 6)
    rod([(13, 0, 49), (7, 0, 72)], 4)
    rod([(61, 0, 14), (77, 0, 67), (78, 0, 80)], 4.4)
    rod([(87, -18, 84), (85, -10, 84), (79, 0, 80),
         (74, 10, 84), (72, 18, 84)], 3.3)

    face.slab(oval(57, 25, 21, 21)[:-1], 9)
    face.oval(57, 25, 15, 15, DETAIL)
    face.slab(oval(34, 21, 10, 10)[:-1], 5)
    face.oval(34, 21, 3, 3, EDGE)
    face.line([(34, 21), (38, 13), (47, 13)], EDGE)
    face.frame(41, 11, 10, 4, 1.4, EDGE)

    saddle = Surface(s, lambda u, v: place(u, v, 72))
    saddle.slab([(-8, -9), (3, -10), (13, -5), (22, -3), (23, 2),
                 (17, 5), (7, 7), (-4, 10), (-8, 7)], 5)
    for z in (52, 57, 62, 67):
        u = 13 - (z - 49)*6/23
        length = 5 if z in (52, 62) else 3
        s.line([place(u - 2, 4, z), place(u - 2 + length, 4, z)], EDGE)
    rod([(14, 5, 48), (14, 8, 48)], 1.8, BOLD)
