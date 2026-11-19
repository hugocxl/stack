from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w5 import currency_mark, printed_stroke

DESCRIPTION = "A ring-bound ledger groups its financial entries in four period columns and carries a check badge at the final column."


def draw(s):
    face = lambda x, z: (x, 16 - .69 * z, z)
    rear = ((0, -31, 0), (90, -31, 0))
    s.face([*rear, face(90, 48), face(0, 48)], EDGE)
    s.face([rear[1], face(90, 0), face(90, 48)], EDGE)
    s.face([face(0, 0), face(90, 0), face(90, 48), face(0, 48)], EDGE)
    for x in (12, 32, 52, 72):
        y = face(x, 48)[1]
        s.tube([(x, y - 4, 45), (x, y - 5, 50), (x, y - 2, 53),
                (x, y + 3, 52), (x, y + 5, 47), (x, y + 5, 42)], 1.4)
    for x in (26, 46, 66):
        printed_stroke(s, face, [(x, 7), (x, 36)], DETAIL)
    printed_stroke(s, face, [(7, 25), (84, 25)], EDGE)
    printed_stroke(s, face, [(7, 12), (84, 12)], DETAIL)
    for x in (16, 36, 56, 76):
        currency_mark(s, face, x, 31, 3.8)
        printed_stroke(s, face, [(x - 5, 19), (x + 5, 19)], DETAIL)
        printed_stroke(s, face, [(x - 5, 7), (x + 5, 7)], EDGE)
    badge(s, "check", *face(88, 9), 11)
