from geometry import DETAIL
from scenes.redraws._kit import badge
from scenes.redraws._w5 import folder_with_insert, invoice, invoice_total, rect

DESCRIPTION = "An itemized invoice sits inside a tabbed archive folder with a check badge beside its exposed currency total."


def draw(s):
    def paid_sheet():
        face = invoice(s, in_envelope=True, lift=9)
        invoice_total(s, face)

    face = folder_with_insert(s, paid_sheet, width=78, height=26)
    rect(s, face, 24, 6, 25, 6, 1.2, DETAIL)
    badge(s, "check", 67, 1, 27, 11.5)
