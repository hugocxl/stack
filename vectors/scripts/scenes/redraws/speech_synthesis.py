from geometry import BOLD, EDGE, oval
from scenes.redraws._w2 import chart_line, folded_sheet, rule

DESCRIPTION = "A folded text page carries a speaker emblem with two sound waves at its lower corner."


def draw(s):
    def page(x, z):
        return .83*x, -.17*x - .24*z, z

    folded_sheet(s, page, 74, 96, depth=5)
    for z, length in ((77, 37), (64, 48), (52, 42), (40, 29)):
        rule(s, page, 11, z, length, EDGE)
    # The speaker and its waves are one emblem across the bottom of the text.
    chart_line(s, page, [(25, 25), (33, 25), (43, 32), (43, 10),
                         (33, 17), (25, 17), (25, 25)])
    for radius in (9, 16):
        chart_line(s, page, oval(48, 21, radius, radius, -53, 53, 16), BOLD)
