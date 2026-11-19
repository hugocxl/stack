from geometry import BOLD, EDGE
from scenes.redraws._w3 import clipboard

DESCRIPTION = "A clipboard form shows a bold label directly above each of two input fields."


def draw(s):
    form = clipboard(s, w=91, h=91)
    for v, label, value in ((58, 19, 25), (29, 29, 32)):
        form.rules(15, v + 8, [label], ink=BOLD)
        form.rect(15, v - 16, 59, 17, 2, EDGE)
        form.rules(21, v - 8, [value])
