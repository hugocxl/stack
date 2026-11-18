from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w5 import printed_stroke, rect, ruled_amounts
from scenes.redraws.payment_reconciliation_proof import receipt_face, receipt_total

DESCRIPTION = "An itemized expense receipt shows a briefcase emblem and carries a check badge at its top corner."


def draw(s):
    face = receipt_face(s)
    rect(s, face, 8, 51, 16, 9, 1.3)
    printed_stroke(s, face, [(13, 60), (13, 63), (19, 63), (19, 60)], EDGE)
    printed_stroke(s, face, [(8, 56), (24, 56)], DETAIL)
    printed_stroke(s, face, [(29, 55), (42, 55)], EDGE)
    ruled_amounts(s, face, ((43, 15), (34, 22), (25, 12)), 8, 47, width=10)
    printed_stroke(s, face, [(8, 20), (47, 20)], EDGE)
    receipt_total(s, face, 14)
    badge(s, "check", *face(54, 65), 12)
