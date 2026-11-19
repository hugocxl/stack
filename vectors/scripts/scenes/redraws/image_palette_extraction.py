from geometry import EDGE, rounded
from scenes.redraws._w2 import chart_line, closed_outline, photo_print

DESCRIPTION = "A landscape print has three differently textured palette swatches in a row along its lower edge."


def draw(s):
    p = photo_print(s, footer=29)
    for i, offsets in enumerate(((), (5, 11), (4, 8, 12))):
        x = 17 + 28*i
        closed_outline(s, p, rounded(x, 7, 20, 15, 2), EDGE)
        for shift in offsets:
            chart_line(s, p, [(x + shift, 11), (x + shift + 4, 18)], EDGE)
        if i == 2:
            chart_line(s, p, [(x + 4, 16), (x + 16, 13)], EDGE)
