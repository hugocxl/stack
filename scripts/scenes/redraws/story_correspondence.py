from geometry import EDGE, rounded
from scenes.redraws._w4 import Surface, paper

DESCRIPTION = "A ruled reader letter unfolds from the mouth of an open envelope."


def draw(s):
    envelope = paper(s, 61, pitch=0, angle=-19, depth=3)
    envelope.slab(rounded(0, 0, 99, 61, 2), 3)

    def flap(u, v):
        x, y, _ = envelope.at(u, v)
        return x, y, 3 - v*.68

    Surface(s, flap).slab([(0, 0), (48, -31), (54, -31), (99, 0)], 1.5)

    def sheet(u, v):
        x, y, _ = envelope.at(u, v)
        z = 24 + (v + 16)*.22 if v < -16 else 24 - (v + 16)*.43
        return x, y, z

    letter = Surface(s, sheet)
    letter.slab([(12, -48), (73, -48), (73, -16), (12, -16)], 1)
    letter.slab([(12, -16), (73, -16), (73, 33), (12, 33)], 1)
    letter.rows(20, -39, (28, 44, 35), step=7)
    letter.rows(20, -8, (43, 40, 31, 27), step=7)
    envelope.slab([(0, 1), (34, 25), (49, 29), (65, 25), (99, 1), (99, 61), (0, 61)], 3)
    envelope.line([(0, 60), (38, 26)], EDGE)
    envelope.line([(99, 60), (60, 26)], EDGE)
