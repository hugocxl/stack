from geometry import BOLD, oval
from scenes.redraws._w3 import Surface, flat, keycap, printed_glyph

DESCRIPTION = "A plus sign connects a Command keycap and a left-arrow keycap in a keyboard chord."


def draw(s):
    keycap(s, 0, 60, 42)
    keycap(s, 60, 0, 42)
    crowns = flat(s, 0, 102, 8)
    # Four loops and the intersecting stems of the Command symbol.
    for x, v, start in ((16, 16, 0), (26, 16, 90), (26, 26, 180), (16, 26, 270)):
        crowns.stroke(oval(x, v, 3, 3, start, start + 270, 20), BOLD)
    for x in (19, 23):
        crowns.stroke([(x, 16), (x, 26)], BOLD)
    for v in (19, 23):
        crowns.rules(16, v, [10], ink=BOLD)
    printed_glyph(crowns, "back", 81, 81, 15)
    # The plus is on a viewer-facing plane in the gap between the caps.
    sign = Surface(s, (51, 51, 8), across=(.707, -.707))
    printed_glyph(sign, "plus", 0, 0, 10)
