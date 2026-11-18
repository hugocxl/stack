from geometry import EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface, sheet
from scenes.redraws.changes_saved import edit_marks

DESCRIPTION = "A tablet displays a penciled edit on a document and carries a check badge on its case."


def draw(s):
    tablet = Surface(s, (0, 25, 0), rise=(-.65, .76), back=(0, -.76, -.65))
    tablet.plate(rounded(0, 0, 91, 74, 6), 8)
    tablet.rect(5, 5, 78, 64, 3, EDGE)
    tablet.oval(87, 37, 1.5, 1.5)
    page = sheet(s, 57, 54, origin=tablet.point(15, 10, -.6), rise=tablet.rise, depth=.7)
    edit_marks(page, .68)
    badge(s, "check", *tablet.point(87, 10, -4), 15)
