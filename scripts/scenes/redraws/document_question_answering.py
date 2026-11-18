from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w2 import closed_outline, folded_sheet, question_mark, rule, speech_bubble

DESCRIPTION = "A question bubble points directly at a marked passage on a folded-corner document."


def draw(s):
    def page(x, z):
        return .78*x, -.22*x - .20*z, z

    folded_sheet(s, page, 83, 100, fold=17, depth=7)
    rule(s, page, 11, 79, 43, EDGE)
    for z, length in ((65, 59), (57, 51), (37, 55), (23, 56), (15, 32)):
        rule(s, page, 11, z, length, DETAIL)
    closed_outline(s, page, rounded(8, 43, 53, 9, 2), EDGE)
    rule(s, page, 12, 47.5, 42, EDGE)
    ox, oy, oz = page(56, 53)

    def bubble(x, z):
        return ox + x*.72, oy - x*.28 + 3, oz + z

    speech_bubble(s, bubble, 45, 43, depth=5)
    question_mark(s, bubble, 22, 20, 15)
