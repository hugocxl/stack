from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._kit import coin
from scenes.redraws._w5 import printed_stroke

DESCRIPTION = "A closed refrigeration cabinet has two doors and a round thermometer dial on the main door."


def draw(s):
    s.box(2, 1, 0, 44, 33, 7, 2)
    s.box(0, 0, 6, 48, 35, 65, 3)
    s.box(0, 34, 8, 48, 4, 45, 2)
    s.box(0, 34, 55, 48, 4, 16, 2)
    for z, h in ((35, 12), (59, 8)):
        s.tube([(7, 38, z), (7, 40.3, z), (7, 40.3, z + h), (7, 38, z + h)], 1.2)
    s.line([(8, 36, 3.5), (39, 36, 3.5)], DETAIL)
    y = coin(s, 32, 40, 34, 9, depth=2)
    dial = lambda x, z: (x, y + .02, z)
    printed_stroke(s, dial, [(30.5, 32), (30.5, 39), (33.5, 39), (33.5, 32)], EDGE)
    printed_stroke(s, dial, oval(32, 31, 2.4, 2.4, 129, 411, 26), BOLD)
    printed_stroke(s, dial, [(32, 31), (32, 36.5)], BOLD)
