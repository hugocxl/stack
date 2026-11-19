from geometry import EDGE
from scenes.redraws._w2 import target_face

DESCRIPTION = "One dart hits the scoring rings of a freestanding target and another lands outside the rings."


def draw(s):
    p = target_face(s)
    for x, z, length in ((-11, 69, 25), (36, 68, 32)):
        tip = p(x, z)
        tx, ty, tz = tip
        shoulder = tx + .79*length, ty + .28*length, tz + .70*length
        tail = shoulder[0] + 10, shoulder[1] + 3.5, shoulder[2] + 9
        s.tube([tip, shoulder], 1.1)
        s.face([shoulder, (tail[0] - 3, tail[1] - 2, tail[2] + 6), tail,
                (tail[0] + 6, tail[1] + 2, tail[2] - 4)], EDGE)
