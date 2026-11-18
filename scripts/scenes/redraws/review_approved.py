from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w2 import closed_outline, folded_sheet, rule

DESCRIPTION = "A check badge overlaps a review document with a separate column of annotations."


def review_document(s, kind):
    """Draw a reviewed proof with comments printed along its right margin."""
    def point(x, z):
        return .68*x, -.32*x - .27*z, .92*z

    folded_sheet(s, point, 102, 89, fold=13, depth=8)
    rule(s, point, 11, 73, 32, EDGE)
    s.line([point(60, 12), point(60, 66)], DETAIL)
    for z, width in ((56, 35), (45, 31), (34, 37), (23, 25)):
        rule(s, point, 11, z, width, DETAIL)
    for z in (48, 26):
        closed_outline(s, point, [(64, z + 5), (69, z + 10), (90, z + 10),
                                  (90, z), (69, z), (69, z + 5)], EDGE)
        rule(s, point, 73, z + 5, 12, DETAIL)
    badge(s, kind, *point(100, 75), 15)


def draw(s):
    review_document(s, "check")
