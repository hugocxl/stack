from geometry import BOLD, EDGE, rounded
from scenes.redraws._w3 import Surface, browser_window

DESCRIPTION = "A code-bracket widget sits flush inside a browser page between its headline and text."


def draw(s):
    page = browser_window(s, 111, 86)
    page.rules(11, 62, [55], ink=EDGE)
    page.rect(11, 20, 89, 34, 4, EDGE)
    embed = Surface(s, page.point(16, 24, -1), across=page.across)
    embed.plate(rounded(0, 0, 79, 26, 2), 2)
    embed.stroke([(28, 20), (19, 13), (28, 6)], BOLD)
    embed.stroke([(45, 21), (34, 5)], BOLD)
    embed.stroke([(51, 20), (60, 13), (51, 6)], BOLD)
    page.rules(11, 12, [66])
    page.rules(11, 6, [47])
