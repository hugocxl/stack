from geometry import EDGE, rounded
from scenes.redraws._w2 import closed_outline, desk_sheet, rule, speech_bubble

DESCRIPTION = "A speech bubble points directly to an outlined passage on a folded-corner document."


def draw(s):
    point = desk_sheet(s, 83, 95)
    rule(s, point, 11, 77, 38, EDGE)
    for z, length in ((63, 51), (54, 45), (30, 57), (20, 43), (11, 47)):
        rule(s, point, 11, z, length)
    closed_outline(s, point, rounded(8, 35, 62, 13, 2), EDGE)
    rule(s, point, 13, 41, 40, EDGE)

    def comment(x, z):
        return point(x + 53, z + 51)

    speech_bubble(s, comment, 59, 31, depth=4, tail=.22)
    rule(s, comment, 9, 20, 37, EDGE)
    rule(s, comment, 9, 11, 28, EDGE)
