from geometry import BOLD, EDGE, oval
from scenes.redraws._kit import arrow
from scenes.redraws._w3 import Surface

DESCRIPTION = "A compact keyboard highlights two oversized keycaps for a Command and right-arrow shortcut."


def draw(s):
    s.box(0, 0, 0, 106, 72, 8, 6)
    for x in (10, 56):
        s.box(x, 6, 8, 38, 35, 6, 5)
    crown = Surface(s, (0, 0, 14), rise=(1, 0), back=(0, 0, -1))
    for x, y, start in ((23, 17, 90), (35, 17, 180), (35, 29, 270), (23, 29, 0)):
        crown.stroke(oval(x, y, 3, 3, start, start + 270, 16), BOLD)
    for x in (26, 32):
        crown.stroke([(x, 17), (x, 29)], BOLD)
    for y in (20, 26):
        crown.stroke([(23, y), (35, y)], BOLD)
    arrow(s, [crown.point(65, 23), crown.point(85, 23)], ink=EDGE, head=8)
    for x in (11, 32, 53, 74):
        s.box(x, 48, 8, 17, 15, 4, 3)
