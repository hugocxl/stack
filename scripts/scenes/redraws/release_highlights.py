from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w4 import front_surface

DESCRIPTION = "A thick release-notes sheet has one outlined feature row with a star badge on its upper-right corner."


def draw(s):
    sheet = front_surface(s, angle=9, z=7, lean=.42)
    sheet.slab([(0, 0), (69, 0), (69, 71), (54, 87), (0, 87)], 6)
    sheet.line([(54, 87), (54, 71), (69, 71)], EDGE)
    sheet.rows(10, 72, (32,), ink=EDGE)
    sheet.rows(10, 65, (23,))
    sheet.frame(8, 40, 51, 17, 3, EDGE)
    sheet.outline(rounded(13, 44, 9, 9, 2), EDGE)
    sheet.rows(28, 51, (24,), ink=EDGE)
    sheet.rows(28, 45, (19,), ink=DETAIL)
    sheet.rows(10, 29, (38, 29, 37), step=-8)
    badge(s, "star", *sheet.at(66, 58), 13)
