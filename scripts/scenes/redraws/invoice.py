from scenes.redraws._w5 import invoice, invoice_total

DESCRIPTION = "A folded-corner invoice shows three aligned item and amount rows above a ruled currency total."


def draw(s):
    face = invoice(s)
    invoice_total(s, face)
