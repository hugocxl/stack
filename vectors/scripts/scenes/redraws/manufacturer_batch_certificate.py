from geometry import DETAIL
from scenes.redraws._w1 import barcode, certificate

DESCRIPTION = "An embossed ribbon seal and a barcoded lot identifier mark a manufacturer's batch certificate."


def draw(s):
    certificate(s, -38, 0, 0, 76, 54)
    barcode(s, -28, 0, 11, 31, 10)
    s.line([(-28, 0, 6), (9, 0, 6)], DETAIL)
