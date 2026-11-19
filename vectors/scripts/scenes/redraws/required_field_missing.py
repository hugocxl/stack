from geometry import EDGE, rounded
from scenes.redraws._kit import warning
from scenes.redraws._w3 import Surface

DESCRIPTION = "An empty text field with a caret and a short label carries a warning triangle on its upper-right edge."


def draw(s):
    form = Surface(s, (0, 0, 0), rise=(-.37, .93), back=(0, -.93, -.37),
                   across=(.94, -.32))
    form.plate(rounded(0, 0, 86, 48, 5), 7)
    form.rules(9, 36, [24])
    form.rect(8, 8, 69, 20, 3, EDGE)
    form.stroke([(17, 12), (17, 24)], EDGE)
    warning(s, *form.point(91, 32, -4), 35)
