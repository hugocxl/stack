from geometry import DETAIL, EDGE
from scenes.redraws._w5 import cutlery, printed_stroke, rect, ticket_face

DESCRIPTION = "A perforated staff meal voucher pairs a fork and knife with a boxed value field."


def draw(s):
    face = ticket_face(s)
    cutlery(s, face, 20, 21, 1.6)
    printed_stroke(s, face, [(35, 29), (59, 29)], EDGE)
    printed_stroke(s, face, [(35, 21), (55, 21)], DETAIL)
    printed_stroke(s, face, [(35, 14), (50, 14)], DETAIL)
    rect(s, face, 73, 11, 13, 18, 1.2, EDGE)
    printed_stroke(s, face, [(76, 20), (83, 20)], EDGE)
