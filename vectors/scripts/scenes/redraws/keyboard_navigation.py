from geometry import BOLD, rounded
from scenes.redraws._w3 import Surface, printed_glyph

DESCRIPTION = "Four raised arrow keys form a directional cluster on a compact keyboard base."


def draw(s):
    s.box(0, 0, 0, 98, 69, 6, 6)
    for x, y, name in [(35, 8, "up"), (5, 38, "back"),
                       (35, 38, "down"), (65, 38, "arrow")]:
        cap = rounded(x, y, 27, 26, 3)
        top = rounded(x + 2, y + 2, 23, 22, 3)
        s.solid(cap, 6, 9, top)
        face = Surface(s, (x + 2, y + 24, 15), rise=(-1, 0))
        printed_glyph(face, name, 11.5, 11, 9.5, BOLD)
