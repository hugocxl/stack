from geometry import DETAIL, EDGE
from scenes.redraws._w2 import chart_marker, folded_sheet, rule

DESCRIPTION = "A folded-corner meeting notes sheet has a short heading and two separated groups of bullets."


def notes_sheet(s):
    def point(x, z):
        return .58*x, -.42*x - .58*z, .79*z

    folded_sheet(s, point, 88, 99, depth=6)
    rule(s, point, 13, 80, 36, EDGE)
    rule(s, point, 13, 73, 52, DETAIL)
    return point


def note_groups(s, point):
    for z, length in ((59, 51), (49, 40), (31, 51), (21, 36)):
        chart_marker(s, point, 16, z, 1.65, EDGE)
        rule(s, point, 23, z, length, EDGE if z in (59, 31) else DETAIL)


def draw(s):
    note_groups(s, notes_sheet(s))
