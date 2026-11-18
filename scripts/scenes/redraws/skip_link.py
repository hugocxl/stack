from geometry import BOLD, EDGE, rounded
from scenes.redraws._kit import arrow
from scenes.redraws._w3 import Surface

DESCRIPTION = "An arrow jumps from the browser toolbar past a navigation row to the start of the main article."


def draw(s):
    browser = Surface(s, (0, 0, 0))
    browser.plate(rounded(0, 0, 105, 80, 6), 11)
    browser.stroke([(0, 65), (105, 65)], EDGE)
    for x in (9, 16, 23):
        browser.oval(x, 72, 1.7, 1.7, EDGE)
    browser.rect(36, 69, 57, 6, 3)
    for x in (39, 59, 79):
        browser.rules(x, 56, [13], ink=EDGE)
    browser.rules(36, 46, [56])
    browser.rules(36, 35, [37], ink=EDGE)
    browser.rules(36, 24, [53, 45, 34], gap=7)
    jump = [(33, 67), (22, 62), (13, 54), (10, 45), (12, 38),
            (18, 34), (29, 34)]
    arrow(s, [browser.point(x, v) for x, v in jump], BOLD, head=7)
