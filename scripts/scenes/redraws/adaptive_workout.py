from shapely.geometry import MultiPoint

from geometry import DETAIL, EDGE, oval, project, rounded
from scenes.redraws._w4 import Surface

DESCRIPTION = "A sports wheelchair carries a dumbbell in a rack above its seat for an overhead press."


def draw(s):
    # Turn the side of the chair toward the viewer, keeping the two wheels in depth.
    def place(u, y, z):
        return (.86*u + .5*y, -.5*u + .86*y, z)

    def rod(points, radius, ink=EDGE):
        s.tube([place(*point) for point in points], radius, ink)

    def wheel(u, y, z, radius):
        face = Surface(s, lambda x, v: place(x, y, v))
        face.slab(oval(u, z, radius, radius)[:-1], 4)
        face.oval(u, z, radius - 3, radius - 3, EDGE)
        face.oval(u, z, 2.7, 2.7, EDGE)
        for start, end in ((20, 200), (90, 270), (150, 330)):
            face.line([oval(u, z, radius - 4, radius - 4, a, a, 1)[0]
                       for a in (start, end)], DETAIL)

    wheel(7, -19, 23, 23)
    wheel(44, -19, 8, 8)
    rod([(-9, -18, 63), (-9, -18, 28), (24, -18, 28),
         (40, -18, 9)], 2.5)
    back = Surface(s, lambda u, v: place(-8 + .11*(42-v), u, v))
    back.slab(rounded(-20, 36, 39, 27, 4), 4)
    seat = Surface(s, lambda u, y: place(u, y, 37))
    seat.slab(rounded(-8, -19, 37, 38, 4), 5)
    rest = Surface(s, lambda u, y: place(u, y, 11))
    rest.slab(rounded(37, -16, 15, 32, 3), 3)
    rod([(-9, 19, 63), (-9, 19, 28), (24, 19, 28),
         (42, 19, 8)], 2.6)
    wheel(44, 19, 8, 8)
    wheel(7, 21, 24, 24)
    rod([(-9, 17, 60), (-9, 17, 75), (6, 17, 78), (11, 17, 78),
         (11, 17, 83)], 2.4)
    rod([(-11, 17, 84), (35, 17, 84)], 2.2)
    for u in (-14, 33):
        rim = oval(17, 84, 10, 10, 22.5, 382.5, 8)[:-1]
        front = [place(u + 4, y, z) for y, z in rim]
        back = [place(u - 4, y, z) for y, z in rim]
        body = MultiPoint([project(p) for p in front + back]).convex_hull
        s.layers.append((body.boundary, body, EDGE))
        s.line(front + front[:1], DETAIL)
