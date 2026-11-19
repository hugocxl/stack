from geometry import DETAIL, EDGE
from scenes.redraws._w2 import chart_line, folded_sheet, rule

DESCRIPTION = "A prompt sheet has two dashed editable fields inset among fixed text rules."


def draw(s):
    def point(x, z):
        return .54*x, -.46*x - .34*z, z

    folded_sheet(s, point, 81, 89, fold=13, depth=7)
    rule(s, point, 11, 73, 35, EDGE)
    for z, start, width in ((48, 31, 37), (23, 11, 41)):
        chart_line(s, point, [(start, z), (start + width, z),
                              (start + width, z + 13), (start, z + 13), (start, z)],
                   EDGE, dash=(4, 2.6))
    rule(s, point, 11, 54, 14, EDGE)
    rule(s, point, 58, 29, 11, EDGE)
    rule(s, point, 11, 41, 54, DETAIL)
    rule(s, point, 11, 14, 31, DETAIL)
