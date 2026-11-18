from geometry import DETAIL, EDGE, oval, rounded
from scenes.redraws._w5 import basket_apple, rect, smooth_loop

DESCRIPTION = "An open refrigerator separates bottled drinks, eggs, and fresh produce into three shelf zones."


def draw(s):
    s.box(0, 0, 0, 48, 4, 86, 1)
    s.box(0, 3, 0, 4, 21, 86, 1)
    for z in (0, 29, 53):
        s.box(3, 4, z, 41, 20, 3, 1)
    door = lambda u, z: (1 - .38*u, 24 + u, z)
    opening = [door(u, v) for u, v in rounded(0, 1, 32, 84, 2)]
    s.face([(x - 3, y, z) for x, y, z in opening])
    s.face(opening)
    rect(s, door, 4, 8, 23, 69, 2, DETAIL)
    for z in (19, 37):
        rect(s, door, 5, z, 21, 6, 1.2)
    for x, base in ((12, 67), (25, 70)):
        s.disk(x, 14, 56, 5.4, 5.4, base - 56)
        s.solid(oval(x, 14, 5.4, 5.4)[:-1], base, 3.6,
                top=oval(x, 14, 2.2, 2.2)[:-1], crease=False)
        s.disk(x, 14, base+3.6, 2.15, 2.15, 4.9)
        s.disk(x, 14, base+8.5, 2.55, 2.55, 1.4)
    s.box(7, 5, 32, 30, 16, 3.5, 2.2)
    for x, y in ((12, 10), (22, 12), (31, 13)):
        egg = [(x - 4, 38), (x - 3, 42), (x, 46), (x + 2.6, 44),
               (x + 4, 40), (x + 3.6, 36), (x, 35), (x - 3, 36)]
        s.face([(u, y, z) for u, z in smooth_loop(egg)])
    s.box(7, 6, 3, 33, 16, 9, 1.6)
    basket_apple(s, 16, 15, 16, 6.4)
    basket_apple(s, 29, 15, 17, 7.3)
    s.face([(7, 22, 3), (40, 22, 3), (40, 22, 12), (7, 22, 12)])
    s.line([(18, 22, 9.5), (28, 22, 9.5)], DETAIL)
    s.box(44, 4, 0, 4, 20, 86, 1)
    s.box(0, 0, 83, 48, 24, 4, 1.3)
