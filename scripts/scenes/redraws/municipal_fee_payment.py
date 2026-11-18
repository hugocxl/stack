from geometry import DETAIL, EDGE
from scenes.redraws._w1 import upright_profile
from scenes.redraws.public_facility_booking import civic_emblem

DESCRIPTION = "A civic fee statement shows a municipal building pictogram above a ruled balance and a stack of coins."


def draw(s):
    receipt = [(-27, 6), (-27, 60), (27, 60), (27, 6), (18, 1),
               (9, 6), (0, 1), (-9, 6), (-18, 1)]
    upright_profile(s, receipt, 0, 5)
    civic_emblem(s, 0, 0, 45, 13)
    s.line([(-19, 0, 29), (19, 0, 29)], EDGE)
    for z, length in ((21, 21), (14, 14)):
        s.line([(-18, 0, z), (-18 + length, 0, z)], DETAIL)
    s.disk(23, 10, 0, 11, 11, 4)
    s.disk(23, 10, 4, 11, 11, 4)
    s.ellipse(23, 10, 8, 7.5, 7.5, EDGE)
