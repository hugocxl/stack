from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface, sheet

DESCRIPTION = "A folded-corner file has a prominent extension tab and an X badge at the tab's outer edge."


def draw(s):
    file = sheet(s, 65, 76, rise=(-.29, .96), depth=5)
    file.rules(11, 51, [27], ink=EDGE)
    file.rules(11, 40, [36], ink=DETAIL)
    tab = Surface(s, file.point(-5, 14, -3), rise=file.rise, back=file.back)
    tab.plate(rounded(0, 0, 68, 20, 3), 4, EDGE)
    tab.oval(12, 9, 1.4, 1.4, EDGE)
    tab.rules(21, 10, [24], ink=EDGE)
    badge(s, "x", *tab.point(67, 10, -4), 14)
