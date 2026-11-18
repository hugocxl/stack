from geometry import DETAIL, EDGE
from scenes.redraws._w3 import Surface, flat

DESCRIPTION = "Three separate workbenches stand on a workshop floor plan and carry station markers with one, two and three dots."


def bench(s, x, y, count):
    for dx, dy in ((3, 3), (33, 3), (3, 21), (33, 21)):
        s.box(x + dx, y + dy, 2, 4, 4, 15, 1)
    s.box(x, y, 16, 40, 27, 4, 1.8)
    s.box(x + 2, y + 1, 20, 36, 3, 14, 1)
    back = Surface(s, (x, y + 4, 20))
    for i in range(count):
        back.oval(20 + (i - (count - 1) / 2) * 8, 7, 2.1, 2.1, EDGE)
    top = flat(s, x, y + 27, 20)
    top.stroke([(8, 11), (15, 18), (20, 16), (18, 13), (16, 15), (10, 9)], EDGE)


def draw(s):
    floor = flat(s, 0, 107, 2)
    floor.plate([(0, 0), (108, 0), (108, 107), (0, 107)], 2, DETAIL)
    floor.stroke([(50, 6), (50, 97)], DETAIL, dashed=True)
    floor.stroke([(4, 54), (104, 54)], DETAIL, dashed=True)
    for x, y, count in ((7, 9, 1), (61, 8, 2), (29, 74, 3)):
        bench(s, x, y, count)
