from geometry import DETAIL, EDGE
from scenes.redraws._kit import coin
from scenes.redraws._w1 import lightning

DESCRIPTION = "A sealed software build package bears a code mark and a lightning-bolt badge."


def draw(s):
    s.face([(-29, -21, 36), (29, -21, 36), (29, 21, 36), (-29, 21, 36)], EDGE)
    s.face([(29, -21, 0), (29, 21, 0), (29, 21, 36), (29, -21, 36)], EDGE)
    s.face([(-29, 21, 0), (29, 21, 0), (29, 21, 36), (-29, 21, 36)], EDGE)
    for x in (-5, 5):
        s.line([(x, -21, 36), (x, 21, 36), (x, 21, 30)], DETAIL)

    # The angle brackets and slash identify the carton as a software package.
    s.line([(-13, 21, 22), (-22, 21, 15), (-13, 21, 8)], EDGE)
    s.line([(-4, 21, 7), (4, 21, 23)], EDGE)
    s.line([(13, 21, 22), (22, 21, 15), (13, 21, 8)], EDGE)

    face = coin(s, 32, 7, 52, 13)
    lightning(s, 32, face + .01, 52, 9)
