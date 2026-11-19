from geometry import EDGE, rounded
from scenes.redraws._w2 import closed_outline, currency, folded_sheet, rule, upright_face
from scenes.redraws.homebuyer_closing_packet import house_emblem

DESCRIPTION = "A house-marked property agreement sits behind a payment stub with a large currency symbol."


def draw(s):
    def agreement(x, z):
        return x, -.42*z, .87*z

    folded_sheet(s, agreement, 74, 74, fold=13, depth=5)
    house_emblem(s, agreement, 25, 51, 13)
    for z, width in ((55, 17), (46, 15), (34, 51)):
        rule(s, agreement, 43 if z > 40 else 12, z, width)

    def stub(x, z):
        return 4 + .84*x, 15 - .16*x - .30*z, 2 + .92*z

    upright_face(s, stub, rounded(0, 0, 83, 29, 2), 3.2)
    closed_outline(s, stub, rounded(55, 4, 24, 21, 2), EDGE)
    currency(s, stub, 67, 14.5, 1.05, EDGE)
    rule(s, stub, 8, 19, 28, EDGE)
    rule(s, stub, 8, 10, 38)
