from geometry import BOLD, DETAIL, oval, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w5 import panel, printed_stroke

DESCRIPTION = "A notification card printed with an at-sign carries an alert badge on its upper corner."


def draw(s):
    face = lambda x, z: (x, -.56*z, z)
    panel(s, rounded(0, 0, 57, 49, 5), face, 5)
    for z, end in ((6, 45), (12, 35)):
        printed_stroke(s, face, [(10, z), (end, z)], DETAIL)
    outer = oval(26, 30, 14, 12, -60, -360, 42)
    terminal = [(40, 30), (39, 25), (36, 24), (33, 24), (32, 26), (34, 35)]
    printed_stroke(s, face, outer + terminal[1:], BOLD)
    printed_stroke(s, face, oval(27, 30, 5.7, 5.6, count=32), BOLD)
    badge(s, "exclaim", 53, -19, 39, 11.1)
