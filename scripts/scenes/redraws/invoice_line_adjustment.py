from geometry import DETAIL, EDGE
from scenes.redraws._w5 import invoice, invoice_total, printed_stroke, rect

DESCRIPTION = "A pencil point touches a boxed line item on the face of an itemized invoice."


def draw(s):
    face = invoice(s)
    invoice_total(s, face, ink=EDGE)
    rect(s, face, 5, 31, 42, 10.5, 1.2, EDGE)

    def pencil(u, v):
        return 40 + .94 * u + .1 * v, -15 - .23 * u - .35 * v, 36 + .62 * u - .75 * v

    tip = pencil(0, 0)
    s.face([tip, pencil(11, -3.4), pencil(11, 3.4)], EDGE)
    body = [(11, -3.4), (37, -3.4), (40, -2), (40, 2), (37, 3.4), (11, 3.4)]
    s.face([pencil(u, v) for u, v in body], EDGE)
    printed_stroke(s, pencil, [(7, -2.1), (7, 2.1)], DETAIL)
    printed_stroke(s, pencil, [(33, -3.4), (33, 3.4)], EDGE)
    printed_stroke(s, pencil, [(11, -.9), (33, -.9)], DETAIL)
