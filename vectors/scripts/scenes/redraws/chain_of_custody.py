from geometry import DETAIL, EDGE
from scenes.redraws._w5 import panel, rect

DESCRIPTION = "A sealed evidence pouch carries an attached label with three connected custody entries."


def draw(s):
    face = lambda x, z: (x, -z * .24, z)
    pouch = [(0, 4), (5, 0), (60, 0), (66, 5), (67, 64), (63, 72),
             (4, 72), (-1, 66)]
    panel(s, pouch, face, 8)
    s.line([face(0, 59), face(67, 59)], EDGE)
    s.line([face(6, 65), face(60, 65)], DETAIL)
    seal = lambda x, z: (x, .7 - z * .24, z)
    panel(s, [(44, 54), (56, 54), (56, 70), (44, 70)], seal, .65)
    s.line([seal(44, 59), seal(56, 59)], DETAIL, dashed=True)
    s.line([face(6, 6), face(59, 6), face(61, 9), face(61, 55)], DETAIL)

    label = lambda x, z: (x, 1.6 - z * .24, z)
    panel(s, [(12, 13), (53, 13), (53, 53), (12, 53)], label, 1)
    s.line([label(18, 45), label(46, 45)], EDGE)
    for z, width in ((36, 22), (28, 17), (20, 20)):
        rect(s, label, 18, z - 1.8, 3.6, 3.6, 1.6, EDGE)
        s.line([label(25, z), label(25 + width, z)], DETAIL)
    for za, zb in ((34.2, 29.8), (26.2, 21.8)):
        s.line([label(19.8, za), label(19.8, zb)], DETAIL)
