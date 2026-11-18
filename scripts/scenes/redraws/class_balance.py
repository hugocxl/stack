from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w2 import level_face

DESCRIPTION = "A level balance scale holds a round weight and a square weight at equal heights."


def draw(s):
    s.disk(0, 0, 0, 19, 17, 6)
    s.disk(0, 0, 6, 4, 4, 72)
    s.tube([level_face(-53, 72), level_face(53, 72)], 2.6, BOLD)
    s.disk(0, 0, 77, 6, 6, 4, EDGE)
    for x, cornered in ((-48, False), (48, True)):
        u, v, _ = level_face(x, 0)
        s.disk(u, v, 23, 17, 15, 4, EDGE)
        if cornered:
            s.box(u - 6, v - 6, 27, 12, 12, 15, 1)
        else:
            s.disk(u, v, 27, 8, 8, 15, EDGE)
        s.line([level_face(x - 18, 28), level_face(x, 70),
                level_face(x + 18, 28)], DETAIL)
