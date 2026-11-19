from geometry import BOLD, EDGE, oval, rounded
from scenes.redraws._kit import badge

DESCRIPTION = "A beveled Command keycap carries a check badge on its upper corner."


def draw(s):
    top = rounded(5, 5, 34, 34, 6)
    s.solid(rounded(0, 0, 44, 44, 6), 0, 10, top=top, crease=False)
    s.face([(x, y, 10) for x, y in top], EDGE)
    # One continuous engraved Command legend with four looped corners.
    legend = [(16, 28)]
    for x, y, start in ((32, 32, -90), (32, 12, 180),
                        (12, 12, 90), (12, 32, 0)):
        legend.extend(oval(x, y, 4, 4, start, start + 270, 20))
    s.line([(x, y, 10) for x, y in [*legend, legend[0]]], BOLD)
    badge(s, "check", 35, 0, 15, 11.8)
