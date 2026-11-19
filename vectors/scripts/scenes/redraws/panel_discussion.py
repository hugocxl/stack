from geometry import EDGE
from scenes.redraws._w3 import Surface

DESCRIPTION = "A panel table lines up three empty chairs behind three tabletop microphones."


def draw(s):
    for x in (8, 43, 78):
        s.box(x, 0, 35, 24, 8, 22, 7)
        front = Surface(s, (x, 8, 35))
        front.stroke([(5, 10), (6, 6), (10, 4), (14, 4), (18, 6), (19, 10)])
        s.tube([(x + 6, 6, 25), (x + 6, 6, 36)], 1.1)
        s.tube([(x + 18, 6, 25), (x + 18, 6, 36)], 1.1)
        s.box(x + 2, 8, 23, 20, 16, 5, 2)
    s.box(4, 22, 0, 6, 22, 36, 2)
    s.box(102, 22, 0, 6, 22, 36, 2)
    s.box(0, 19, 35, 111, 31, 5, 3)
    apron = Surface(s, (0, 49, 4))
    apron.plate([(3, 0), (108, 0), (108, 31), (3, 31)], 3)
    apron.rules(11, 7, [89])
    for x in (23, 55, 88):
        s.disk(x, 32, 40, 4.8, 3.3, 2)
        s.tube([(x, 32, 42), (x, 32, 49), (x - 4, 28, 53)], 1.05)
        s.tube([(x - 5, 27, 53), (x - 8, 23, 54)], 1.7)
