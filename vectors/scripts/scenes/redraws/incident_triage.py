from geometry import DETAIL, EDGE
from scenes.redraws._kit import warning
from scenes.redraws._w5 import rect

DESCRIPTION = "A warning triangle crowns a three-tier incident sorter marked with descending priority bars."


def draw(s):
    for level in range(3):
        z = 17 * level
        if level < 2:
            s.box(0, 0, z, 61, 40, 15, 2.5)
        else:
            s.box(0, 0, z, 61, 40, 3, 2)
            s.face([(0, 0, 37), (61, 0, 37), (61, 0, 54), (0, 0, 54)], EDGE)
            s.face([(0, 0, 37), (0, 40, 37), (0, 40, 49), (0, 0, 54)], EDGE)
            s.face([(7, 22, 38), (33, 22, 38), (33, 13, 56), (7, 13, 56)], EDGE)
            s.line([(11, 14, 53), (29, 14, 53)], DETAIL)
            s.face([(61, 0, 37), (61, 40, 37), (61, 40, 49), (61, 0, 54)], EDGE)
            s.face([(0, 40, 37), (61, 40, 37), (61, 40, 49), (0, 40, 49)], EDGE)
        face = lambda x, h: (x, 40.1, z + h)
        rect(s, face, 7, 5, 18, 5, 1.4, DETAIL)
        for index in range(level + 1):
            x = 32 + index * 6
            s.line([face(x, 5), face(x, 11)], EDGE)
    warning(s, 51, 33, 47, 23)
