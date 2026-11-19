from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._w5 import rect

DESCRIPTION = "A visitor information counter has a large information symbol, a desk bell, and a chair tucked behind it."


def draw(s):
    s.disk(42, -13, 0, 10, 8, 3)
    s.tube([(42, -13, 3), (42, -13, 21)], 1.45)
    s.box(32, -21, 20, 20, 17, 4, 3)
    s.box(32, -25, 24, 20, 5, 24, 3)
    s.box(0, 0, 0, 56, 24, 29, 4)
    s.box(-3, -3, 29, 62, 30, 5, 3)
    face = lambda x, z: (x, 24, z)
    rect(s, face, 12, 5, 33, 20, 3, DETAIL)
    s.line([face(x, z) for x, z in oval(28, 15, 8.1, 8.1, count=32)], EDGE)
    s.line([face(28, 15.8), face(28, 10)], BOLD)
    s.line([face(28, 19), face(28, 20.3)], BOLD)
    s.disk(11, 8, 34, 6.5, 5.7, 1.9)
    s.solid(oval(11, 8, 5.9, 5.2)[:-1], 35.9, 4.5,
            oval(11, 8, 2.5, 2.2)[:-1], crease=False)
    s.disk(11, 8, 40.4, 1.4, 1.3, 1.7)
