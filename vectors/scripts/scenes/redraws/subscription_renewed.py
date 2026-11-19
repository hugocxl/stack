from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w5 import printed_stroke, receipt_face, receipt_total, ruled_amounts

DESCRIPTION = "A curled receipt shows itemized charges and a circular renewal arrow beside its total."


def draw(s):
    face = receipt_face(s)
    printed_stroke(s, face, [(8, 57), (32, 57)], EDGE)
    ruled_amounts(s, face, ((47, 18), (38, 23)), 8, 46)
    printed_stroke(s, face, [(8, 31), (45, 31)], EDGE)
    receipt_total(s, face, 23, right=37, ink=EDGE)
    badge(s, "refresh", *face(60, 29), 14)
