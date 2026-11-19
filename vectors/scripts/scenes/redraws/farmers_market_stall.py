from geometry import DETAIL, EDGE, oval
from scenes.redraws._w5 import apple_mark, printed_stroke

DESCRIPTION = "A striped canopy shades a market counter lined with apples and carrots."


def draw(s):
    for x in (3, 62):
        s.box(x, 1, 0, 3, 3, 77, .8)
    s.box(4, 7, 0, 62, 26, 25, 1.4)
    s.box(0, 3, 24, 70, 35, 4, 2)
    for x, y in ((8, 15), (17, 16), (12, 25), (25, 24)):
        s.solid(oval(x, y, 4.6, 4.6)[:-1], 28, 7,
                oval(x, y, 4.1, 4.1)[:-1], crease=False)
        s.line([(x, y, 35), (x, y, 37), (x + 1.7, y, 38)], EDGE)
    for x, y in ((39, 12), (47, 18), (57, 24)):
        tip, head = (x - 4, y + 8, 29), (x + 5, y - 3, 31)
        s.face([tip, (x + 1, y - 4, 32), head, (x + 6, y, 33)])
        s.line([head, (x + 9, y - 6, 37)], EDGE)
        s.line([head, (x + 11, y - 1, 35)], EDGE)
    for x in (3, 62):
        s.box(x, 32, 28, 3, 3, 32, .8)
    front = lambda x, z: (x, 33.04, z)
    apple_mark(s, front, 34, 11.5, .65)
    roof = lambda x, y: (x, y, 79 - (y + 4) * .32)
    s.face([roof(74, -4), roof(74, 41), (74, 41, 61), (74, -4, 75)])
    s.face([roof(-4, -4), roof(74, -4), roof(74, 41), roof(-4, 41)])
    for x in (9, 22, 35, 48, 61):
        printed_stroke(s, roof, [(x, -4), (x, 41)], DETAIL)
    hem = [(74, 41, 61)]
    for x in (61, 48, 35, 22, 9, -4):
        hem.extend([(x + 9.5, 41, 58.5), (x + 3.5, 41, 58.5), (x, 41, 61)])
    s.face([roof(-4, 41), roof(74, 41), *hem])
