from geometry import BOLD, EDGE, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "A thick tag pairs a brace-enclosed color variable with a beveled swatch."


def draw(s):
    tag = Surface(s, (0, 0, 0), rise=(-.45, .89), back=(0, -.89, -.45),
                  across=(.92, -.39))
    tag.plate([(0, 15), (15, 0), (105, 0), (109, 4), (109, 53),
               (105, 57), (15, 57), (0, 42)], 8)
    tag.oval(11, 28.5, 4, 4, EDGE)

    brace = [(9, 13), (5, 13), (3, 10), (3, 4), (0, 0),
             (3, -4), (3, -10), (5, -13), (9, -13)]
    for x, direction in ((22, 1), (66, -1)):
        tag.stroke([(x + direction * u, 28 + v) for u, v in brace], BOLD)
    tag.rules(35, 28, [18], ink=EDGE)
    swatch = Surface(s, tag.point(74, 15, -4), rise=tag.rise, back=tag.back, across=tag.across)
    swatch.plate(rounded(0, 0, 26, 27, 5), 4)
    swatch.rect(4, 4, 18, 19, 3, EDGE)
