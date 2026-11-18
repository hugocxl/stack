from geometry import BOLD, EDGE
from scenes.redraws._kit import arrow
from scenes.redraws._w2 import currency

DESCRIPTION = "A price tag hangs from a bidirectional slider with wide adjustment marks."


def draw(s):
    s.box(0, 0, 0, 105, 22, 10, 5)
    for x in (17, 34, 51, 68, 85):
        s.line([(x, 6, 10), (x, 11, 10)], EDGE)
    s.tube([(18, 15, 10), (87, 15, 10)], 1.6)
    s.box(44, 6, 10, 15, 16, 7, 3)
    for a, b in ((37, 14), (65, 88)):
        arrow(s, [(a, 10, 28), (b, 10, 28)], EDGE, head=7)
    s.tube([(51, 21, 14), (51, 31, 11), (54, 40, 25)], 1.4)
    y = 42
    shape = [(44, 0), (44, 25), (55, 35), (72, 35), (83, 25), (83, 0)]
    s.face([(x, y - 3, z + 2) for x, z in shape])
    s.face([(x, y, z) for x, z in shape])
    s.line([(x, y, z) for x, z in ((51, 25), (54, 28), (58, 25), (54, 22), (51, 25))], EDGE)
    currency(s, lambda x, z: (x, y, z), 64, 15, 1.25, BOLD)
