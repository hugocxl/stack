from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w2 import axes, chart_line, laptop

DESCRIPTION = "A laptop chart surrounds one estimate line with a lightly outlined band that widens toward the forecast horizon."


def draw(s):
    p = laptop(s, width=130, height=86)
    axes(s, p, x=14, y=16, width=102, height=60)
    lower = [(21, 29), (40, 34), (55, 39), (74, 34), (93, 30), (112, 25)]
    upper = [(21, 32), (40, 39), (55, 48), (74, 51), (93, 62), (112, 74)]
    chart_line(s, p, lower, DETAIL)
    chart_line(s, p, upper, DETAIL)
    chart_line(s, p, [lower[-1], upper[-1]], EDGE)
    for x, low, high in ((74, 34, 51), (93, 30, 62)):
        chart_line(s, p, [(x, low), (x, high)], DETAIL, dash=(2, 3))
    chart_line(s, p, [(21, 30), (40, 37), (55, 43), (74, 43), (93, 47), (112, 50)], BOLD)
