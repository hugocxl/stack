from geometry import EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws.page_moved import Surface

DESCRIPTION = "A form with two entry fields has a slash badge over its dashed submit button."


def draw(s):
    form = Surface(s, (0, 13, 3), lean=.49)
    form.plate(rounded(0, 0, 83, 82, 6), 5)
    for z in (54, 32):
        form.line([(12, z + 14), (36, z + 14)], EDGE)
        form.frame(12, z, 57, 9, 2, EDGE)
    form.loop(rounded(23, 9, 42, 12, 2), EDGE, dashed=True)
    form.glyph("arrow", 37, 15, 8)
    badge(s, "slash", *form.point(65, 13), 11)
