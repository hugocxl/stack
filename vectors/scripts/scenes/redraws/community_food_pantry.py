from geometry import DETAIL, EDGE
from scenes.redraws._w5 import printed_stroke, rect


DESCRIPTION = "An open pantry cupboard displays labeled staple-food cans and folded-top cartons on two shelves."


def can(s, x, y, z, radius=6.3):
    s.disk(x, y, z, radius, radius, 17)
    s.ellipse(x, y, z + 17, radius - 1.7, radius - 1.7, DETAIL)
    for height in (4.5, 12):
        s.ellipse(x, y, z + height, radius, radius, DETAIL, start=17, end=74)


def carton(s, x, y, z):
    s.box(x, y, z, 12, 10, 16, .9)
    s.face([(x, y + 10, z + 16), (x + 12, y + 10, z + 16),
            (x + 12, y + 5, z + 22), (x, y + 5, z + 22)])
    s.face([(x + 12, y, z + 16), (x + 12, y + 10, z + 16),
            (x + 12, y + 5, z + 22)], DETAIL)
    s.line([(x, y + 5, z + 22), (x + 12, y + 5, z + 22)], EDGE)
    rect(s, lambda u, v: (u, y + 10, v), x + 3, z + 5, 6, 5, .8, DETAIL)


def draw(s):
    s.box(0, 0, 0, 51, 4, 72, 2)
    s.box(0, 3, 0, 4, 30, 70, 1.2)
    s.box(0, 3, 3, 51, 30, 4, 1)
    s.box(0, 3, 34, 51, 30, 4, 1)
    can(s, 11, 22, 7)
    carton(s, 20, 20, 7)
    can(s, 37, 24, 7, radius=5.1)
    carton(s, 8, 19, 38)
    can(s, 28, 23, 38)
    can(s, 41, 26, 38, radius=4.8)
    s.box(47, 3, 0, 4, 30, 70, 1.2)
    s.box(0, 0, 68, 51, 33, 4, 1.3)
    door = lambda x, z: (-.43 * x, 33 + .9 * x, z)
    outline = [(0, 3), (30, 3), (30, 68), (0, 68)]
    s.face([door(x, z) for x, z in outline], EDGE)
    rect(s, door, 4, 8, 22, 55, 1.8, DETAIL)
    printed_stroke(s, door, [(23, 29), (23, 40)], EDGE)
