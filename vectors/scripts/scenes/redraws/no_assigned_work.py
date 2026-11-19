from geometry import EDGE, rounded
from scenes.redraws._w3 import clipboard

DESCRIPTION = "An otherwise empty clipboard has one large dashed task row under its heading."


def draw(s):
    page = clipboard(s, 72, 83)
    page.rules(14, 57, [28], ink=EDGE)
    page.stroke(rounded(12, 24, 48, 20, 2), EDGE, closed=True, dashed=True)
    page.stroke(rounded(18, 30, 8, 8, 1), EDGE, closed=True, dashed=True)
    page.stroke([(32, 34), (52, 34)], EDGE, dashed=True)
