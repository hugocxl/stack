from geometry import DETAIL, EDGE
from scenes.redraws._kit import warning
from scenes.redraws._w2 import chart_line, open_volume, rule

DESCRIPTION = "An open ledger shows a three-row risk register with a warning triangle on its upper corner."


def draw(s):
    left, right = open_volume(s)
    for z, width in ((57, 30), (43, 36), (33, 31), (23, 35)):
        rule(s, left, 10, z, width, EDGE if z == 57 else DETAIL)

    rule(s, right, 8, 58, 26, EDGE)
    chart_line(s, right, [(34, 12), (34, 48)], DETAIL)
    for z, width in ((48, 18), (36, 15), (24, 18)):
        rule(s, right, 5, z, 45, EDGE)
        rule(s, right, 9, z - 6, width, DETAIL)
        rule(s, right, 39, z - 6, 7, DETAIL)
    rule(s, right, 5, 12, 45, EDGE)
    warning(s, *right(56, 48), size=31)
