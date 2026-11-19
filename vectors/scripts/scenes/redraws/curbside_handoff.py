from geometry import DETAIL, EDGE
from scenes.redraws._w4 import Surface, side_wheel

DESCRIPTION = "A parcel rests halfway across the cargo sill of a car with its rear hatch raised."


def draw(s):
    x0, x1, width = 0, 111, 52
    near, far = width/2, -width/2
    for x in (25, 85):
        side_wheel(s, x, far + 3, 11, 10)
    s.solid([(x0, -19), (9, far), (102, far), (x1, -20),
             (x1, 20), (102, near), (9, near), (x0, 19)], 12, 19, crease=False)

    roof = [(28, -17, 48), (45, -19, 55), (79, -19, 55), (86, -19, 50),
            (86, 19, 50), (79, 19, 55), (45, 19, 55), (28, 17, 48)]
    s.face(roof)
    s.face([roof[0], roof[-1], (12, near - 3, 31), (12, far + 3, 31)], DETAIL)
    s.face([roof[-1], roof[-2], roof[-3], roof[-4], (98, near - 3, 31),
            (15, near - 3, 31)], EDGE)
    for loop in ([(37, 21, 43), (47, 19.7, 51), (57, 19.7, 51), (57, 22, 35), (28, 22, 35)],
                 [(62, 19.7, 51), (77, 19.7, 51), (90, 22, 35), (62, 22, 35)]):
        s.face(loop, DETAIL)
    s.line([(58, near, 29), (58, near, 15)], DETAIL)
    s.line([(62, near, 26), (69, near, 26)], DETAIL)
    for x in (25, 85):
        side_wheel(s, x, near + 1, 11, 11)

    floor = [(92, -16, 21), (x1, -16, 21), (x1, 16, 21), (92, 16, 21)]
    s.face(floor, DETAIL)
    s.face([(92, -16, 21), (92, 16, 21), (92, 16, 39), (92, -16, 39)], DETAIL)
    mouth = [(x1, -15, 22), (x1, 15, 22), (x1, 15, 33), (x1, -15, 33)]
    s.face([(x1, -20, 14), (x1, 20, 14), (x1, 20, 34), (x1, 16, 40),
            (x1, -16, 40), (x1, -20, 34)], openings=[mouth])
    s.line([(x1, -17, 20), (x1, 17, 20)], EDGE)
    for a, b in ((-19, -13), (13, 19)):
        s.line([(x1, a, 25), (x1, b, 25)], EDGE)

    for y in (-17, 17):
        s.tube([(93, y, 40), (104, y, 64)], 1.05)
    hatch = Surface(s, lambda u, v: (83 + u, v, 54 + .52*u))
    hatch.slab([(0, -20), (30, -22), (33, -19),
                (33, 19), (30, 22), (0, 20)], 2.5)
    hatch.frame(4, -17, 23, 34, 2, DETAIL)
    s.box(99, -11, 20, 22, 21, 20, 1.2)
    s.line([(99, 0, 40), (121, 0, 40), (121, 0, 34)], DETAIL)
