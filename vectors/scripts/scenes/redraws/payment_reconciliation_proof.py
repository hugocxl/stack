from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w5 import printed_stroke, receipt_face, receipt_total, ruled_amounts

DESCRIPTION = "A curled receipt shows itemized amounts and carries a check badge beside its ruled total."


def draw(s):
    face = receipt_face(s)
    printed_stroke(s, face, [(8, 57), (32, 57)], EDGE)
    ruled_amounts(s, face, ((46, 15), (37, 21), (28, 13)), 8, 47)
    printed_stroke(s, face, [(8, 23), (46, 23)], EDGE)
    printed_stroke(s, face, [(25, 21), (46, 21)], DETAIL)
    receipt_total(s, face, 15, right=43)
    badge(s, "check", *face(57, 20), 12)
