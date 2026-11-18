from geometry import EDGE
from scenes.redraws._kit import warning
from scenes.redraws._w3 import clipboard

DESCRIPTION = "An exclamation triangle is anchored to the right edge of the invalid field on a clipboard form."


def draw(s):
    form = clipboard(s, 85, 90)
    form.rules(13, 65, [28], ink=EDGE)
    for v in (40, 13):
        form.rules(14, v + 17, [17], ink=EDGE)
        form.rect(13, v, 54, 12, 2, EDGE)
        form.rules(20, v + 6, [26])
    warning(s, *form.point(78, 13, -5), size=36)
