from geometry import BOLD, EDGE, rounded
from scenes.redraws._w3 import Surface, printed_glyph

DESCRIPTION = "Two inward arrows squeeze a list of closely spaced rows toward its center."


def draw(s):
    panel = Surface(s, (0, 0, 0), rise=(-.25, .97), across=(.95, -.3))
    panel.plate(rounded(0, 0, 79, 86, 7), 10)
    for v, width in ((53, 32), (46, 36), (39, 28), (32, 32)):
        panel.oval(12, v, 1.7, 1.7, EDGE)
        panel.rules(20, v, [width], ink=EDGE)
    printed_glyph(panel, "down", 64, 65, 12, BOLD)
    printed_glyph(panel, "up", 64, 21, 12, BOLD)
